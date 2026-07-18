#!/usr/bin/env python3
"""Generate the fixed BCApps Czech event-subscriber population inventory."""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path


EXPECTED_COMMIT = "397d01199c321e774edaf23a7290fee40f75c6a6"
SOURCE_PATH = Path("src/Apps/CZ/CoreLocalizationPack/app/Src")
APP_ID = "267b59d3-7302-44c5-ba77-c87000380514"
APP_NAME = "Core Localization Pack for Czech"
APP_VERSION = "29.0.0.0"
ATTRIBUTE = re.compile(r"\[EventSubscriber\s*\(", re.IGNORECASE)
CODEUNIT = re.compile(r"\bcodeunit\s+(\d+)\s+(\"(?:\"\"|[^\"])+\"|[^\s{]+)", re.IGNORECASE)
INSTANCE = re.compile(r"\bEventSubscriberInstance\s*=\s*([^;]+);", re.IGNORECASE)
PROCEDURE = re.compile(
    r"\b(?:local\s+|internal\s+|protected\s+)?procedure\s+"
    r"(\"(?:\"\"|[^\"])+\"|[A-Za-z_][A-Za-z0-9_]*)\s*\(",
    re.IGNORECASE,
)

FIELDS = [
    "inventory_id", "source_commit", "application_id", "application_name",
    "application_version", "source_path", "source_line", "subscriber_codeunit_id",
    "subscriber_codeunit_name", "subscriber_instance", "subscriber_procedure",
    "publisher_object_type", "publisher_object", "published_event_name",
    "published_element_name", "skip_on_missing_license", "skip_on_missing_permission",
    "procedure_signature", "parameter_names", "var_parameter_names",
    "has_ishandled_parameter", "has_handled_parameter", "has_skip_parameter",
    "conditional_compilation_context", "prior_known", "coarse_screen_status",
    "selection_status",
]


def git_commit(root: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        check=True, capture_output=True, text=True,
    )
    return result.stdout.strip()


def mask_comments(text: str) -> str:
    """Replace AL comments with spaces while preserving offsets and newlines."""
    out = list(text)
    i = 0
    quote: str | None = None
    while i < len(text):
        if quote:
            if text[i] == quote:
                if i + 1 < len(text) and text[i + 1] == quote:
                    i += 2
                    continue
                quote = None
            i += 1
            continue
        if text[i] in "'\"":
            quote = text[i]
            i += 1
        elif text.startswith("//", i):
            end = text.find("\n", i)
            end = len(text) if end < 0 else end
            out[i:end] = " " * (end - i)
            i = end
        elif text.startswith("/*", i):
            end = text.find("*/", i + 2)
            end = len(text) - 2 if end < 0 else end
            for pos in range(i, min(end + 2, len(text))):
                if out[pos] != "\n":
                    out[pos] = " "
            i = end + 2
        else:
            i += 1
    return "".join(out)


def balanced_end(text: str, start: int, opening: str, closing: str) -> int:
    depth = 0
    quote: str | None = None
    for i in range(start, len(text)):
        char = text[i]
        if quote:
            if char == quote:
                if i + 1 < len(text) and text[i + 1] == quote:
                    continue
                quote = None
            continue
        if char in "'\"":
            quote = char
        elif char == opening:
            depth += 1
        elif char == closing:
            depth -= 1
            if depth == 0:
                return i
    raise ValueError(f"Unbalanced {opening}{closing} expression at offset {start}")


def split_top_level(value: str, delimiter: str) -> list[str]:
    parts: list[str] = []
    start = 0
    depth = 0
    quote: str | None = None
    i = 0
    while i < len(value):
        char = value[i]
        if quote:
            if char == quote:
                if i + 1 < len(value) and value[i + 1] == quote:
                    i += 2
                    continue
                quote = None
        elif char in "'\"":
            quote = char
        elif char in "([{":
            depth += 1
        elif char in ")]}":
            depth -= 1
        elif char == delimiter and depth == 0:
            parts.append(value[start:i].strip())
            start = i + 1
        i += 1
    parts.append(value[start:].strip())
    return parts


def clean_symbol(value: str) -> str:
    value = " ".join(value.split())
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        return value[1:-1].replace(value[0] * 2, value[0])
    return value


def parameter_names(signature: str) -> tuple[list[str], list[str]]:
    names: list[str] = []
    var_names: list[str] = []
    for declaration in split_top_level(signature, ";"):
        if ":" not in declaration:
            continue
        left = declaration.split(":", 1)[0].strip()
        is_var = bool(re.match(r"^var\s+", left, re.IGNORECASE))
        left = re.sub(r"^var\s+", "", left, flags=re.IGNORECASE)
        for name in split_top_level(left, ","):
            cleaned = clean_symbol(name)
            if cleaned:
                names.append(cleaned)
                if is_var:
                    var_names.append(cleaned)
    return names, var_names


def compilation_context(text: str, offset: int) -> str:
    stack: list[str] = []
    for line in text[:offset].splitlines():
        directive = re.match(r"\s*#(if|elif|else|endif)\b\s*(.*)", line, re.IGNORECASE)
        if not directive:
            continue
        kind, condition = directive.group(1).lower(), directive.group(2).strip()
        if kind == "if":
            stack.append(condition)
        elif kind in {"elif", "else"} and stack:
            stack[-1] = f"{kind} {condition}".strip()
        elif kind == "endif" and stack:
            stack.pop()
    return " | ".join(stack)


def extract_file(path: Path, root: Path, commit: str) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig")
    masked = mask_comments(text)
    codeunit_match = CODEUNIT.search(masked)
    if not codeunit_match:
        return []
    instance_match = INSTANCE.search(masked)
    instance = clean_symbol(instance_match.group(1)) if instance_match else "StaticAutomatic (default)"
    rows: list[dict[str, str]] = []
    for match in ATTRIBUTE.finditer(masked):
        open_paren = masked.find("(", match.start())
        close_paren = balanced_end(masked, open_paren, "(", ")")
        arguments = split_top_level(text[open_paren + 1:close_paren], ",")
        if len(arguments) != 6:
            raise ValueError(f"{path}:{text.count(chr(10), 0, match.start()) + 1}: expected 6 event arguments")
        procedure_match = PROCEDURE.search(masked, close_paren)
        if not procedure_match:
            raise ValueError(f"{path}: subscriber at offset {match.start()} has no following procedure")
        proc_open = masked.find("(", procedure_match.start())
        proc_close = balanced_end(masked, proc_open, "(", ")")
        signature = " ".join(text[proc_open + 1:proc_close].split())
        names, var_names = parameter_names(signature)
        lowered = {name.casefold() for name in names}
        relative = path.relative_to(root).as_posix()
        rows.append({
            "source_commit": commit,
            "application_id": APP_ID,
            "application_name": APP_NAME,
            "application_version": APP_VERSION,
            "source_path": relative,
            "source_line": str(text.count("\n", 0, match.start()) + 1),
            "subscriber_codeunit_id": codeunit_match.group(1),
            "subscriber_codeunit_name": clean_symbol(codeunit_match.group(2)),
            "subscriber_instance": instance,
            "subscriber_procedure": clean_symbol(procedure_match.group(1)),
            "publisher_object_type": clean_symbol(arguments[0]),
            "publisher_object": " ".join(arguments[1].split()),
            "published_event_name": clean_symbol(arguments[2]),
            "published_element_name": clean_symbol(arguments[3]),
            "skip_on_missing_license": clean_symbol(arguments[4]),
            "skip_on_missing_permission": clean_symbol(arguments[5]),
            "procedure_signature": signature,
            "parameter_names": " | ".join(names),
            "var_parameter_names": " | ".join(var_names),
            "has_ishandled_parameter": "Yes" if "ishandled" in lowered else "No",
            "has_handled_parameter": "Yes" if "handled" in lowered else "No",
            "has_skip_parameter": "Yes" if "skip" in lowered else "No",
            "conditional_compilation_context": compilation_context(text, match.start()),
            "prior_known": "Unknown",
            "coarse_screen_status": "Not Screened",
            "selection_status": "Unselected",
        })
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bcapps-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--files-output", type=Path, required=True)
    args = parser.parse_args()
    root = args.bcapps_root.resolve()
    commit = git_commit(root)
    if commit != EXPECTED_COMMIT:
        parser.error(f"BCApps HEAD is {commit}; expected {EXPECTED_COMMIT}")
    source = root / SOURCE_PATH
    if not source.is_dir():
        parser.error(f"production source boundary does not exist: {source}")
    files = sorted(source.rglob("*.al"), key=lambda item: item.relative_to(root).as_posix())
    rows = [row for path in files for row in extract_file(path, root, commit)]
    rows.sort(key=lambda row: (row["source_path"], int(row["source_line"]), row["subscriber_procedure"]))
    for number, row in enumerate(rows, 1):
        row["inventory_id"] = f"CZPOP-{number:04d}"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    subscriber_counts: dict[str, int] = {}
    for row in rows:
        subscriber_counts[row["source_path"]] = subscriber_counts.get(row["source_path"], 0) + 1
    args.files_output.parent.mkdir(parents=True, exist_ok=True)
    with args.files_output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["file_id", "source_commit", "source_path", "event_subscriber_attributes"],
            lineterminator="\n",
        )
        writer.writeheader()
        for number, path in enumerate(files, 1):
            relative = path.relative_to(root).as_posix()
            writer.writerow({
                "file_id": f"CZFILE-{number:04d}",
                "source_commit": commit,
                "source_path": relative,
                "event_subscriber_attributes": subscriber_counts.get(relative, 0),
            })
    subscriber_files = len({row["source_path"] for row in rows})
    print(f"commit={commit}")
    print(f"al_files={len(files)}")
    print(f"subscriber_attributes={len(rows)}")
    print(f"subscriber_files={subscriber_files}")
    print(f"output={args.output}")
    print(f"files_output={args.files_output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
