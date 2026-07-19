#!/usr/bin/env python3
"""Resolve bounded static source context for retained CZL event subscribers."""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path


EXPECTED_COMMIT = "397d01199c321e774edaf23a7290fee40f75c6a6"
PLATFORM_REFERENCE = (
    "https://learn.microsoft.com/en-us/dynamics365/business-central/"
    "dev-itpro/developer/devenv-event-types"
)

OBJECT_PATTERN = re.compile(
    r'^\s*(codeunit|table|page|report|xmlport|query)\s+(\d+)\s+("(?:[^"]|"")*"|\S+)',
    re.IGNORECASE,
)
EXTENSION_PATTERN = re.compile(
    r'^\s*(tableextension|pageextension)\s+(\d+)\s+("(?:[^"]|"")*"|\S+)\s+'
    r'extends\s+("(?:[^"]|"")*"|\S+)', re.IGNORECASE,
)
PROCEDURE_PATTERN = re.compile(
    r'^\s*(?:(?:local|internal|protected)\s+)?procedure\s+'
    r'("(?:[^"]|"")*"|[A-Za-z_][\w]*)\s*\(',
    re.IGNORECASE,
)
EVENT_ATTRIBUTE_PATTERN = re.compile(
    r'^\s*\[(IntegrationEvent|BusinessEvent|InternalEvent)\b', re.IGNORECASE
)
ATTRIBUTE_PATTERN = re.compile(r'^\s*\[EventSubscriber\s*\(', re.IGNORECASE)

BOUNDARY_ROOTS = {
    "CZDEP-0001": "src/Apps/CZ/CoreLocalizationPack/app",
    "CZDEP-0002": "src/Apps/W1/EU3PartyTradePurchase/app",
    "CZDEP-0003": "src/Layers/W1/BaseApp",
    "CZDEP-0004": "src/Business Foundation/App",
    "CZDEP-0005": "src/System Application/App",
}


def normalize_name(value: str) -> str:
    value = value.strip()
    if "::" in value:
        value = value.split("::", 1)[1]
    if '."' in value:
        value = value[value.find('."') + 1:]
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1].replace('""', '"')
    return re.sub(r"\s+", " ", value).casefold()


def git_head(root: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        check=True, capture_output=True, text=True,
    )
    return result.stdout.strip()


def relative_path(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8-sig").splitlines()


def matching_brace(lines: list[str], start: int) -> tuple[int | None, int | None]:
    opened = False
    depth = 0
    for index in range(start, len(lines)):
        code = lines[index].split("//", 1)[0]
        for character in code:
            if character == "{":
                opened = True
                depth += 1
            elif character == "}" and opened:
                depth -= 1
                if depth == 0:
                    return start + 1, index + 1
    return None, None


def al_procedure_boundary(lines: list[str], procedure_at: int) -> tuple[int | None, int | None]:
    """Return one-based body bounds using the next top-level object member."""
    begin_at = next(
        (index for index in range(procedure_at + 1, len(lines)) if lines[index].strip().casefold() == "begin"),
        None,
    )
    if begin_at is None:
        return None, None
    member = re.compile(r"^    (?:(?:local|internal|protected)\s+)?procedure\b|^    \[")
    for index in range(begin_at + 1, len(lines)):
        if member.match(lines[index]) or lines[index] == "}":
            end = index
            while end > begin_at and not lines[end - 1].strip():
                end -= 1
            return begin_at + 1, end
    return None, None


def build_source_index(root: Path, codeunit_names: set[str]) -> tuple[dict, dict, dict]:
    events: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    qualified_calls: dict[str, list[str]] = defaultdict(list)
    normalized_names = {normalize_name(name): name for name in codeunit_names}
    binding_index: dict[str, list[str]] = defaultdict(list)
    for boundary_id, source_root in BOUNDARY_ROOTS.items():
        for path in sorted((root / source_root).rglob("*.al")):
            lines = read_lines(path)
            source_path = relative_path(root, path)
            for line_number, line in enumerate(lines, 1):
                for call in re.findall(r'\.\s*("(?:[^"]|"")*"|[A-Za-z_][\w]*)\s*\(', line):
                    qualified_calls[normalize_name(call)].append(
                        f"{source_path}:{line_number}"
                    )
            binding_lines = [
                line_number for line_number, line in enumerate(lines, 1)
                if re.search(r"\b(?:BindSubscription|UnbindSubscription)\s*\(", line, re.IGNORECASE)
            ]
            if binding_lines:
                normalized_source = normalize_name("\n".join(lines))
                for normalized_name, original_name in normalized_names.items():
                    if normalized_name in normalized_source:
                        binding_index[original_name].extend(
                            f"{source_path}:{line_number}" for line_number in binding_lines
                        )
            object_match = next((OBJECT_PATTERN.match(line) for line in lines if OBJECT_PATTERN.match(line)), None)
            extension_match = next(
                (EXTENSION_PATTERN.match(line) for line in lines if EXTENSION_PATTERN.match(line)), None
            ) if object_match is None else None
            if object_match is None and extension_match is None:
                continue
            if object_match:
                object_type, object_id, object_name = object_match.groups()
            else:
                extension_type, object_id, _extension_name, object_name = extension_match.groups()
                object_type = "table" if extension_type.casefold() == "tableextension" else "page"
            object_type = object_type.casefold()
            obj = {
                "boundary_id": boundary_id,
                "object_id": object_id,
                "object_name": object_name,
                "path": source_path,
                "lines": lines,
            }
            pending_event: tuple[str, int] | None = None
            for line_number, line in enumerate(lines, 1):
                attribute = EVENT_ATTRIBUTE_PATTERN.match(line)
                if attribute:
                    pending_event = (attribute.group(1), line_number)
                    continue
                procedure = PROCEDURE_PATTERN.match(line)
                if procedure and pending_event:
                    event_class, attribute_line = pending_event
                    name = procedure.group(1)
                    start, end = al_procedure_boundary(lines, line_number - 1)
                    event_record = {
                        **obj,
                        "event_class": f"{event_class.replace('Event', '').strip()} Event",
                        "procedure": name,
                        "declaration_line": line_number,
                        "attribute_line": attribute_line,
                        "body_start": start,
                        "body_end": end,
                    }
                    events[(object_type, normalize_name(object_name), normalize_name(name))].append(event_record)
                    events[(object_type, object_id, normalize_name(name))].append(event_record)
                    pending_event = None
                elif line.strip() and not line.lstrip().startswith("["):
                    pending_event = None
    return events, qualified_calls, {
        key: sorted(set(value)) for key, value in binding_index.items()
    }


def procedure_context(lines: list[str], attribute_line: int, procedure_name: str,
                      var_parameters: list[str]) -> dict:
    window = "\n".join(lines[attribute_line - 1:attribute_line + 16])
    procedure_at = None
    for index in range(attribute_line - 1, min(len(lines), attribute_line + 30)):
        match = PROCEDURE_PATTERN.match(lines[index])
        if match and normalize_name(match.group(1)) == normalize_name(procedure_name):
            procedure_at = index
            break
    if procedure_at is None or "EventSubscriber" not in window:
        raise ValueError("subscriber attribute or procedure does not match retained identity")
    body_start, body_end = al_procedure_boundary(lines, procedure_at)
    if body_start is None or body_end is None:
        raise ValueError("subscriber body boundary is unresolved")
    body = lines[body_start - 1:body_end]
    calls: list[str] = []
    transaction: list[str] = []
    errors: list[str] = []
    reads: list[str] = []
    writes: list[str] = []
    for line_number, line in enumerate(body, body_start):
        code = line.split("//", 1)[0]
        for symbol in re.findall(r'(?<!\bprocedure\s)("[^"]+"|[A-Za-z_][\w.]*)\s*\(', code):
            if symbol.casefold() not in {"if", "while", "for", "case", "with", "and", "or", "not"}:
                calls.append(f"{line_number}:{symbol}")
        if re.search(r"\bCommit\s*\(", code, re.IGNORECASE):
            transaction.append(f"{line_number}:Commit")
        for marker in ("Error", "Exit"):
            if re.search(rf"\b{marker}\s*\(", code, re.IGNORECASE):
                errors.append(f"{line_number}:{marker}")
        for parameter in var_parameters:
            if not re.search(rf'(?<![\w"])"?{re.escape(parameter)}"?(?![\w"])', code, re.IGNORECASE):
                continue
            location = f"{line_number}:{parameter}"
            if re.search(rf'"?{re.escape(parameter)}"?(?:\."?[\w /.-]+"?)?\s*:=', code, re.IGNORECASE):
                writes.append(location)
            else:
                reads.append(location)
    return {
        "body_start": body_start,
        "body_end": body_end,
        "calls": sorted(set(calls)),
        "transaction": sorted(set(transaction)),
        "errors": sorted(set(errors)),
        "reads": sorted(set(reads)),
        "writes": sorted(set(writes)),
    }


def raise_sites(event: dict, qualified_calls: dict[str, list[str]]) -> list[str]:
    result = []
    name = re.escape(normalize_name(event["procedure"]))
    for line_number, line in enumerate(event["lines"], 1):
        normalized = line.casefold()
        if line_number != event["declaration_line"] and re.search(rf"\b{name}\s*\(", normalized):
            result.append(f"{event['path']}:{line_number}")
    result.extend(qualified_calls.get(normalize_name(event["procedure"]), []))
    return sorted(set(result))


def runtime_class(row: dict[str, str]) -> str | None:
    object_type = row["publisher_object_type"].split("::")[-1].casefold()
    event = row["published_event_name"].casefold()
    if object_type == "table" and event in {
        "onbeforeinsertevent", "onafterinsertevent", "onbeforemodifyevent",
        "onaftermodifyevent", "onbeforedeleteevent", "onafterdeleteevent",
        "onbeforerenameevent", "onafterrenameevent", "onbeforevalidateevent",
        "onaftervalidateevent",
    }:
        return "Database Trigger Event"
    if object_type == "page" and event in {
        "onaftergetcurrrecordevent", "onaftergetrecordevent", "onclosepageevent",
        "ondeleteevent", "oninsertrecordevent", "onmodifyrecordevent",
        "onnewrecordevent", "onopenpageevent", "onqueryclosepageevent",
    }:
        return "Page Trigger Event"
    return None


def resolve_row(root: Path, row: dict[str, str], events: dict, peers: dict,
                qualified_calls: dict[str, list[str]], binding_index: dict[str, list[str]],
                boundary_apps: dict[str, dict[str, str]]) -> dict:
    base = {
        "inventory_id": row["inventory_id"],
        "source_commit": row["source_commit"],
        "subscriber_path": row["source_path"],
        "subscriber_codeunit": row["subscriber_codeunit_name"],
        "subscriber_procedure": row["subscriber_procedure"],
        "target_object_type": row["publisher_object_type"],
        "target_object": row["publisher_object"],
        "target_event": row["published_event_name"],
        "target_element": row["published_element_name"],
        "subscriber_instance": row["subscriber_instance"],
        "binding_context_paths": binding_index.get(row["subscriber_codeunit_name"], []),
        "direct_call_symbols": [],
        "control_parameter_reads": [], "control_parameter_writes": [],
        "transaction_markers": [], "error_markers": [],
        "composition_subscriber_ids": sorted(x for x in peers if x != row["inventory_id"]),
        "caller_context_paths": [], "test_context_paths": [],
        "prior_known": "Unknown", "coarse_screen_status": "Not Screened",
        "selection_status": "Unselected", "manual_correction": None,
    }
    try:
        path = root / row["source_path"]
        lines = read_lines(path)
        var_parameters = [item.strip() for item in row["var_parameter_names"].split("|") if item.strip()]
        context = procedure_context(
            lines, int(row["source_line"]), row["subscriber_procedure"], var_parameters
        )
        base.update({
            "subscriber_body_start_line": context["body_start"],
            "subscriber_body_end_line": context["body_end"],
            "direct_call_symbols": context["calls"],
            "control_parameter_reads": context["reads"],
            "control_parameter_writes": context["writes"],
            "transaction_markers": context["transaction"],
            "error_markers": context["errors"],
        })
    except (OSError, ValueError, KeyError) as error:
        return {**base, "target_event_class": "Unknown",
                "publisher_resolution_status": "Parse Failure",
                "context_resolution_status": "Unresolved",
                "unresolved_reason": str(error)}

    object_type = row["publisher_object_type"].split("::")[-1].casefold()
    key = (object_type, normalize_name(row["publisher_object"]), normalize_name(row["published_event_name"]))
    candidates = events.get(key, [])
    if len(candidates) == 1:
        event = candidates[0]
        sites = raise_sites(event, qualified_calls)
        in_subject = event["boundary_id"] == "CZDEP-0001"
        boundary_app = boundary_apps[event["boundary_id"]]
        status = "Publisher in Subject Application" if in_subject else "Resolved Source Publisher"
        unresolved = None
        context_status = "Resolved"
        if not sites:
            status = "Raise Site Unresolved"
            unresolved = "Source publisher resolved, but no raise site was found in its owning object."
            context_status = "Partially Resolved"
        return {**base, "target_event_class": event["event_class"],
                "publisher_resolution_status": status,
                "publisher_boundary_id": event["boundary_id"],
                "publisher_app_id": boundary_app["app_id"],
                "publisher_app_name": boundary_app["app_name"],
                "publisher_path": event["path"],
                "publisher_procedure": event["procedure"],
                "raise_site_paths": sites, "platform_semantics_reference": None,
                "context_resolution_status": context_status,
                "unresolved_reason": unresolved}
    if len(candidates) > 1:
        locations = [f"{item['path']}:{item['declaration_line']}" for item in candidates]
        return {**base, "target_event_class": "Unknown",
                "publisher_resolution_status": "Ambiguous Target",
                "raise_site_paths": [], "platform_semantics_reference": None,
                "context_resolution_status": "Partially Resolved",
                "unresolved_reason": "Multiple compatible publisher declarations: " + " | ".join(locations)}
    platform = runtime_class(row)
    if platform:
        return {**base, "target_event_class": platform,
                "publisher_resolution_status": "Resolved Platform or Trigger Event",
                "publisher_boundary_id": None, "publisher_app_id": None,
                "publisher_app_name": None, "publisher_path": None,
                "publisher_procedure": None, "raise_site_paths": [],
                "platform_semantics_reference": PLATFORM_REFERENCE,
                "context_resolution_status": "Resolved", "unresolved_reason": None}
    return {**base, "target_event_class": "Unknown",
            "publisher_resolution_status": "Source Not in Boundary",
            "publisher_boundary_id": None, "publisher_app_id": None,
            "publisher_app_name": None, "publisher_path": None,
            "publisher_procedure": None, "raise_site_paths": [],
            "platform_semantics_reference": None,
            "context_resolution_status": "Unresolved",
            "unresolved_reason": "No compatible publisher declaration or recognized platform trigger was found in the fixed boundary."}


def validation_selection(records: list[dict]) -> list[dict]:
    selected: dict[str, dict] = {}
    for record in records:
        selected.setdefault(f"class:{record['target_event_class']}", record)
        if record["publisher_resolution_status"] not in {
            "Resolved Source Publisher", "Resolved Platform or Trigger Event",
            "Publisher in Subject Application",
        }:
            selected.setdefault(f"status:{record['publisher_resolution_status']}", record)
    return sorted({item["inventory_id"]: item for item in selected.values()}.values(), key=lambda x: x["inventory_id"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bcapps-root", required=True, type=Path)
    parser.add_argument("--population", required=True, type=Path)
    parser.add_argument("--boundary", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--mode", choices=("dry-run", "validation"), default="validation")
    args = parser.parse_args()
    root = args.bcapps_root.resolve()
    if git_head(root) != EXPECTED_COMMIT:
        parser.error(f"BCApps checkout must be at {EXPECTED_COMMIT}")
    rows = list(csv.DictReader(args.population.open(encoding="utf-8-sig", newline="")))
    if len(rows) != 448 or len({row["inventory_id"] for row in rows}) != 448:
        parser.error("population must contain 448 unique retained inventory IDs")
    if any(row["source_commit"] != EXPECTED_COMMIT for row in rows):
        parser.error("population contains an unexpected source commit")
    boundary_rows = list(csv.DictReader(args.boundary.open(encoding="utf-8-sig", newline="")))
    boundary_apps = {row["boundary_id"]: row for row in boundary_rows}
    if set(boundary_apps) != set(BOUNDARY_ROOTS):
        parser.error("boundary must contain the five fixed boundary IDs")
    if any(row["source_commit"] != EXPECTED_COMMIT for row in boundary_rows):
        parser.error("boundary contains an unexpected source commit")
    manual_names = {
        row["subscriber_codeunit_name"] for row in rows
        if row["subscriber_instance"].casefold() == "manual"
    }
    events, qualified_calls, binding_index = build_source_index(root, manual_names)
    peers: dict[tuple[str, str, str, str], list[str]] = defaultdict(list)
    for row in rows:
        target = tuple(row[key] for key in (
            "publisher_object_type", "publisher_object", "published_event_name", "published_element_name"
        ))
        peers[target].append(row["inventory_id"])
    records = []
    for row in rows:
        target = tuple(row[key] for key in (
            "publisher_object_type", "publisher_object", "published_event_name", "published_element_name"
        ))
        records.append(resolve_row(
            root, row, events, peers[target], qualified_calls, binding_index,
            boundary_apps,
        ))
    output = records if args.mode == "dry-run" else validation_selection(records)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="\n") as handle:
        for record in output:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")
    counts: dict[str, int] = defaultdict(int)
    for record in records:
        counts[record["publisher_resolution_status"]] += 1
    print(f"population_records={len(records)}")
    print(f"output_records={len(output)}")
    for status in sorted(counts):
        print(f"status[{status}]={counts[status]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
