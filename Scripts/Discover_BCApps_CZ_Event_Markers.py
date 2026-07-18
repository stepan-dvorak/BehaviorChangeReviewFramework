#!/usr/bin/env python3
"""Generate fixed BCApps Czech event publisher and discovery-marker inventories."""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

from Discover_BCApps_CZ_Event_Population import (
    EXPECTED_COMMIT,
    SOURCE_PATH,
    balanced_end,
    clean_symbol,
    compilation_context,
    mask_comments,
    parameter_names,
    split_top_level,
)


PUBLISHER = re.compile(r"\[(IntegrationEvent|BusinessEvent|InternalEvent)\s*\(", re.IGNORECASE)
PROCEDURE = re.compile(
    r"\b(?:local\s+|internal\s+|protected\s+)?procedure\s+"
    r"(\"(?:\"\"|[^\"])+\"|[A-Za-z_][A-Za-z0-9_]*)\s*\(", re.IGNORECASE,
)
CONTAINER = re.compile(
    r"\b(codeunit|table|tableextension|page|pageextension|report|reportextension|"
    r"xmlport|query|interface|enum|enumextension|permissionset|permissionsetextension)\s+"
    r"(\d+)\s+(\"(?:\"\"|[^\"])+\"|[^\s{]+)", re.IGNORECASE,
)
MARKERS = {
    "EventSubscriberInstance": re.compile(r"\bEventSubscriberInstance\s*=\s*([^;]+);", re.IGNORECASE),
    "BindSubscriptionCall": re.compile(r"\bBindSubscription\s*\(", re.IGNORECASE),
    "UnbindSubscriptionCall": re.compile(r"\bUnbindSubscription\s*\(", re.IGNORECASE),
    "TryFunctionAttribute": re.compile(r"\[TryFunction\b", re.IGNORECASE),
    "CommitBehaviorAttribute": re.compile(r"\[CommitBehavior\s*\(", re.IGNORECASE),
    "CommitCall": re.compile(r"(?<![A-Za-z0-9_])Commit\s*\(", re.IGNORECASE),
    "ObsoleteAttribute": re.compile(r"\[Obsolete\s*\(", re.IGNORECASE),
}

PUBLISHER_FIELDS = [
    "publisher_id", "source_commit", "source_path", "source_line", "event_type",
    "container_type", "container_id", "container_name", "procedure_name",
    "procedure_signature", "parameter_names", "var_parameter_names", "include_sender",
    "global_var_access", "isolated_argument", "has_ishandled_parameter",
    "has_handled_parameter", "has_skip_parameter", "conditional_compilation_context",
]
MARKER_FIELDS = [
    "marker_id", "source_commit", "source_path", "source_line", "marker_type",
    "lexical_value", "containing_procedure", "conditional_compilation_context",
    "interpretation_status",
]
TARGET_FIELDS = [
    "target_id", "source_commit", "publisher_object_type", "publisher_object",
    "published_event_name", "published_element_name", "subscriber_count",
    "subscriber_inventory_ids", "composition_status",
]


def commit(root: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"], check=True,
        capture_output=True, text=True,
    )
    return result.stdout.strip()


def line_number(text: str, offset: int) -> str:
    return str(text.count("\n", 0, offset) + 1)


def nearest_container(masked: str, offset: int) -> tuple[str, str, str]:
    matches = list(CONTAINER.finditer(masked, 0, offset))
    if not matches:
        return "Unknown", "", ""
    match = matches[-1]
    return match.group(1), match.group(2), clean_symbol(match.group(3))


def containing_procedure(masked: str, offset: int) -> str:
    matches = list(PROCEDURE.finditer(masked, 0, offset))
    return clean_symbol(matches[-1].group(1)) if matches else ""


def extract_publishers(path: Path, root: Path, source_commit: str) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig")
    masked = mask_comments(text)
    rows: list[dict[str, str]] = []
    for match in PUBLISHER.finditer(masked):
        open_paren = masked.find("(", match.start())
        close_paren = balanced_end(masked, open_paren, "(", ")")
        arguments = split_top_level(text[open_paren + 1:close_paren], ",")
        procedure = PROCEDURE.search(masked, close_paren)
        if not procedure:
            raise ValueError(f"{path}:{line_number(text, match.start())}: publisher has no following procedure")
        proc_open = masked.find("(", procedure.start())
        proc_close = balanced_end(masked, proc_open, "(", ")")
        signature = " ".join(text[proc_open + 1:proc_close].split())
        names, var_names = parameter_names(signature)
        lowered = {name.casefold() for name in names}
        container_type, container_id, container_name = nearest_container(masked, match.start())
        rows.append({
            "source_commit": source_commit,
            "source_path": path.relative_to(root).as_posix(),
            "source_line": line_number(text, match.start()),
            "event_type": match.group(1),
            "container_type": container_type,
            "container_id": container_id,
            "container_name": container_name,
            "procedure_name": clean_symbol(procedure.group(1)),
            "procedure_signature": signature,
            "parameter_names": " | ".join(names),
            "var_parameter_names": " | ".join(var_names),
            "include_sender": clean_symbol(arguments[0]) if arguments else "",
            "global_var_access": clean_symbol(arguments[1]) if len(arguments) > 1 else "",
            "isolated_argument": " | ".join(" ".join(arg.split()) for arg in arguments[2:]),
            "has_ishandled_parameter": "Yes" if "ishandled" in lowered else "No",
            "has_handled_parameter": "Yes" if "handled" in lowered else "No",
            "has_skip_parameter": "Yes" if "skip" in lowered else "No",
            "conditional_compilation_context": compilation_context(text, match.start()),
        })
    return rows


def lexical_value(text: str, masked: str, marker_type: str, match: re.Match[str]) -> str:
    if marker_type == "EventSubscriberInstance":
        return clean_symbol(match.group(1))
    if marker_type in {"BindSubscriptionCall", "UnbindSubscriptionCall", "CommitBehaviorAttribute", "ObsoleteAttribute"}:
        open_paren = masked.find("(", match.start())
        close_paren = balanced_end(masked, open_paren, "(", ")")
        return " ".join(text[match.start():close_paren + 1].split())
    return " ".join(text[match.start():match.end()].split())


def extract_markers(path: Path, root: Path, source_commit: str) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig")
    masked = mask_comments(text)
    rows: list[dict[str, str]] = []
    for marker_type, pattern in MARKERS.items():
        for match in pattern.finditer(masked):
            rows.append({
                "source_commit": source_commit,
                "source_path": path.relative_to(root).as_posix(),
                "source_line": line_number(text, match.start()),
                "marker_type": marker_type,
                "lexical_value": lexical_value(text, masked, marker_type, match),
                "containing_procedure": containing_procedure(masked, match.start()),
                "conditional_compilation_context": compilation_context(text, match.start()),
                "interpretation_status": "Not Evaluated",
            })
    for procedure in PROCEDURE.finditer(masked):
        proc_open = masked.find("(", procedure.start())
        proc_close = balanced_end(masked, proc_open, "(", ")")
        signature = " ".join(text[proc_open + 1:proc_close].split())
        _, var_names = parameter_names(signature)
        for name in var_names:
            if name.casefold() not in {"ishandled", "handled", "skip"}:
                continue
            rows.append({
                "source_commit": source_commit,
                "source_path": path.relative_to(root).as_posix(),
                "source_line": line_number(text, procedure.start()),
                "marker_type": "MutableControlParameter",
                "lexical_value": name,
                "containing_procedure": clean_symbol(procedure.group(1)),
                "conditional_compilation_context": compilation_context(text, procedure.start()),
                "interpretation_status": "Not Evaluated",
            })
    return rows


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def target_rows(population_path: Path, source_commit: str) -> list[dict[str, str]]:
    with population_path.open(encoding="utf-8", newline="") as handle:
        population = list(csv.DictReader(handle))
    groups: dict[tuple[str, str, str, str], list[str]] = {}
    for row in population:
        key = (
            row["publisher_object_type"], row["publisher_object"],
            row["published_event_name"], row["published_element_name"],
        )
        groups.setdefault(key, []).append(row["inventory_id"])
    rows: list[dict[str, str]] = []
    for key, ids in sorted(groups.items()):
        if len(ids) < 2:
            continue
        rows.append({
            "source_commit": source_commit,
            "publisher_object_type": key[0], "publisher_object": key[1],
            "published_event_name": key[2], "published_element_name": key[3],
            "subscriber_count": str(len(ids)),
            "subscriber_inventory_ids": " | ".join(ids),
            "composition_status": "Syntactic Multiplicity Only",
        })
    for number, row in enumerate(rows, 1):
        row["target_id"] = f"CZTGT-{number:04d}"
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bcapps-root", type=Path, required=True)
    parser.add_argument("--population", type=Path, required=True)
    parser.add_argument("--publishers-output", type=Path, required=True)
    parser.add_argument("--markers-output", type=Path, required=True)
    parser.add_argument("--targets-output", type=Path, required=True)
    args = parser.parse_args()
    root = args.bcapps_root.resolve()
    source_commit = commit(root)
    if source_commit != EXPECTED_COMMIT:
        parser.error(f"BCApps HEAD is {source_commit}; expected {EXPECTED_COMMIT}")
    source = root / SOURCE_PATH
    if not source.is_dir():
        parser.error(f"production source boundary does not exist: {source}")
    files = sorted(source.rglob("*.al"), key=lambda item: item.relative_to(root).as_posix())
    publishers = [row for path in files for row in extract_publishers(path, root, source_commit)]
    publishers.sort(key=lambda row: (row["source_path"], int(row["source_line"]), row["event_type"]))
    for number, row in enumerate(publishers, 1):
        row["publisher_id"] = f"CZPUB-{number:04d}"
    markers = [row for path in files for row in extract_markers(path, root, source_commit)]
    markers.sort(key=lambda row: (row["source_path"], int(row["source_line"]), row["marker_type"], row["lexical_value"]))
    for number, row in enumerate(markers, 1):
        row["marker_id"] = f"CZMRK-{number:04d}"
    targets = target_rows(args.population, source_commit)
    write_csv(args.publishers_output, PUBLISHER_FIELDS, publishers)
    write_csv(args.markers_output, MARKER_FIELDS, markers)
    write_csv(args.targets_output, TARGET_FIELDS, targets)
    counts = Counter(row["event_type"] for row in publishers)
    marker_counts = Counter(row["marker_type"] for row in markers)
    print(f"commit={source_commit}")
    print(f"publishers={len(publishers)} {dict(sorted(counts.items()))}")
    print(f"markers={len(markers)} {dict(sorted(marker_counts.items()))}")
    print(f"multi_subscriber_targets={len(targets)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
