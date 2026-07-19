#!/usr/bin/env python3
"""Prepare deterministic, not-screened CZL coarse-screen worksheet records."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


EXPECTED_CONTEXT_SHA256 = "2cbeb7a45b46f937f5749e73caad6167c5604ffa100ca4f084ca77ac5a2df4eb"
PROTOCOL_VERSION = "0.1.0"

INDICATOR_ORDER = [
    "Integration Event", "Database Trigger Event", "Page Trigger Event",
    "Subject Publisher", "Dependency Publisher", "Platform Trigger",
    "Static Subscriber", "Manual Subscriber", "Mutable Parameter Read",
    "Mutable Parameter Write", "Transaction Marker", "Error or Exit Marker",
    "Same-Target CZL Peers", "No Same-Target CZL Peer",
    "Linked Test Context", "No Linked Test Context",
]


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def indicators(context: dict) -> list[str]:
    found = {context["target_event_class"]}
    publisher_status = context["publisher_resolution_status"]
    if publisher_status == "Publisher in Subject Application":
        found.add("Subject Publisher")
    elif publisher_status == "Resolved Source Publisher":
        found.add("Dependency Publisher")
    elif publisher_status == "Resolved Platform or Trigger Event":
        found.add("Platform Trigger")

    if context["subscriber_instance"] == "Manual":
        found.add("Manual Subscriber")
    else:
        found.add("Static Subscriber")
    if context["control_parameter_reads"]:
        found.add("Mutable Parameter Read")
    if context["control_parameter_writes"]:
        found.add("Mutable Parameter Write")
    if context["transaction_markers"]:
        found.add("Transaction Marker")
    if context["error_markers"]:
        found.add("Error or Exit Marker")
    found.add(
        "Same-Target CZL Peers" if context["composition_subscriber_ids"]
        else "No Same-Target CZL Peer"
    )
    found.add("Linked Test Context" if context["test_context_paths"] else "No Linked Test Context")
    return [item for item in INDICATOR_ORDER if item in found]


def prepare_record(context: dict) -> dict:
    manual = context["subscriber_instance"] == "Manual"
    questions = [
        "Identify and cite the bounded established activity surrounding the resolved raise site or platform trigger."
    ]
    if manual and not context["binding_context_paths"]:
        questions.append(
            "Locate bounded binding or activation evidence for this manual subscriber, or record that the fixed boundary is exhausted."
        )
    observations = [
        f"Context resolution status: {context['context_resolution_status']}.",
        f"Publisher resolution status: {context['publisher_resolution_status']}.",
        f"Subscriber body: {context['subscriber_path']}:{context['subscriber_body_start_line']}-{context['subscriber_body_end_line']}.",
    ]
    return {
        "inventory_id": context["inventory_id"],
        "context_dataset_sha256": EXPECTED_CONTEXT_SHA256,
        "screening_protocol_version": PROTOCOL_VERSION,
        "screening_status": "Not Screened",
        "evidence_availability": {
            "subscriber_identity": "Available",
            "subscriber_body": "Available",
            "publisher_or_platform": "Available",
            "raise_or_trigger": "Available",
            "established_flow": "Targeted Search Required",
            "runtime_participation": (
                "Binding Evidence Available" if manual and context["binding_context_paths"]
                else "Targeted Search Required" if manual
                else "Static Automatic"
            ),
            "composition_scope": (
                "CZL Peers Recorded" if context["composition_subscriber_ids"]
                else "No CZL Peer Recorded"
            ),
            "test_context": (
                "Linked Evidence Available" if context["test_context_paths"]
                else "No Linked Evidence"
            ),
        },
        "stratum_indicators": indicators(context),
        "targeted_search_questions": questions,
        "screening_observations": observations,
        "unavailability_reason": None,
        "screened_by": None,
        "screened_on": None,
        "prior_known": "Unknown",
        "selection_status": "Unselected",
        "trigger_status": "Not Evaluated",
        "checklist_status": "Not Evaluated",
    }


def validation_selection(contexts: list[dict], records: list[dict]) -> list[dict]:
    pairs = list(zip(contexts, records, strict=True))
    selected: dict[str, dict] = {}

    def first(key: str, predicate) -> None:
        match = next(((context, record) for context, record in pairs if predicate(context, record)), None)
        if match:
            selected.setdefault(key, match[1])

    for event_class in sorted({context["target_event_class"] for context in contexts}):
        first(f"class:{event_class}", lambda context, _record, value=event_class: context["target_event_class"] == value)
    first("static", lambda context, _record: context["subscriber_instance"] != "Manual")
    first("manual", lambda context, _record: context["subscriber_instance"] == "Manual")
    first("manual-binding", lambda context, _record: context["subscriber_instance"] == "Manual" and bool(context["binding_context_paths"]))
    first("manual-no-binding", lambda context, _record: context["subscriber_instance"] == "Manual" and not context["binding_context_paths"])
    first("composition", lambda context, _record: bool(context["composition_subscriber_ids"]))
    first("no-composition", lambda context, _record: not context["composition_subscriber_ids"])
    for status in sorted({record["screening_status"] for record in records if record["screening_status"] != "Ready for Prior-Knowledge Labeling"}):
        first(f"status:{status}", lambda _context, record, value=status: record["screening_status"] == value)
    return sorted({record["inventory_id"]: record for record in selected.values()}.values(), key=lambda item: item["inventory_id"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--context", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--mode", choices=("validation", "full-template"), default="validation")
    args = parser.parse_args()

    actual_hash = file_sha256(args.context)
    if actual_hash != EXPECTED_CONTEXT_SHA256:
        parser.error(f"context SHA-256 is {actual_hash}; expected {EXPECTED_CONTEXT_SHA256}")
    contexts = read_jsonl(args.context)
    if len(contexts) != 448 or len({item["inventory_id"] for item in contexts}) != 448:
        parser.error("context input must contain 448 unique retained inventory IDs")
    if any(item["context_resolution_status"] != "Resolved" for item in contexts):
        parser.error("context input contains a non-resolved record")

    records = [prepare_record(context) for context in contexts]
    output = records if args.mode == "full-template" else validation_selection(contexts, records)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="\n") as handle:
        for record in output:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")
    print(f"context_records={len(contexts)}")
    print(f"output_records={len(output)}")
    print("screening_status[Not Screened]=" + str(len(output)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
