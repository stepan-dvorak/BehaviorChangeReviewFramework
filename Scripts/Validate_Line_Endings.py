#!/usr/bin/env python3
"""Validate the repository's Git-index line-ending invariant."""

from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

EOL_LINE = re.compile(
    r"^i/(?P<index>\S+)\s+w/(?P<worktree>\S+)\s+attr/(?P<attrs>.*?)\t(?P<path>.*)$"
)


@dataclass(frozen=True)
class EolRecord:
    path: str
    index: str
    worktree: str
    attrs: str

    @property
    def binary(self) -> bool:
        return self.index == "-text" or "-text" in self.attrs.split()

    @property
    def configured_worktree_eol(self) -> str:
        return "crlf" if "eol=crlf" in self.attrs.split() else "lf"


def run_git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout


def parse_eol_line(line: str) -> EolRecord:
    match = EOL_LINE.match(line)
    if not match:
        raise ValueError(f"unrecognized git ls-files --eol output: {line!r}")
    return EolRecord(
        path=match.group("path"),
        index=match.group("index"),
        worktree=match.group("worktree"),
        attrs=match.group("attrs").strip(),
    )


def collect_records(root: Path) -> list[EolRecord]:
    output = run_git(root, "ls-files", "--eol")
    return [parse_eol_line(line) for line in output.splitlines() if line.strip()]


def validate_records(records: list[EolRecord]) -> list[str]:
    errors: list[str] = []
    for record in records:
        if record.binary:
            continue

        # The Git index is the canonical cross-platform representation. Empty
        # files and text files without a terminator are reported as i/none and
        # contain no CRLF sequence to normalize.
        if record.index not in {"lf", "none"}:
            errors.append(
                f"{record.path}: Git index EOL is {record.index}; expected LF-normalized text"
            )
    return errors


def validate_policy_files(root: Path) -> list[str]:
    attributes = root / ".gitattributes"
    if not attributes.is_file():
        return [".gitattributes is missing"]

    lines = attributes.read_text(encoding="utf-8").splitlines()
    required = {
        "* text=auto eol=lf": "default LF policy",
        "*.bat text eol=crlf": "BAT working-tree exception",
        "*.cmd text eol=crlf": "CMD working-tree exception",
    }
    return [
        f".gitattributes: missing {description}: {rule}"
        for rule, description in required.items()
        if rule not in lines
    ]


def validate(root: Path) -> tuple[list[str], list[EolRecord]]:
    errors = validate_policy_files(root)
    try:
        records = collect_records(root)
    except (RuntimeError, ValueError) as exc:
        return errors + [str(exc)], []
    errors.extend(validate_records(records))
    return errors, records


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate LF-normalized tracked text in the canonical Git index."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root; defaults to the parent of Scripts/.",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    errors, records = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Line-ending validation failed: {len(errors)} error(s).")
        return 1

    text_records = [record for record in records if not record.binary]
    crlf_paths = [
        record.path
        for record in text_records
        if record.configured_worktree_eol == "crlf"
    ]
    print(
        "Line-ending validation: OK\n"
        f"- tracked text records: {len(text_records)}\n"
        "- canonical Git-index text EOL: LF\n"
        f"- configured CRLF working-tree exceptions: {len(crlf_paths)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
