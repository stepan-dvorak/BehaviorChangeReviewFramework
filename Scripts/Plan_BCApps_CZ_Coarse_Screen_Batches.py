#!/usr/bin/env python3
"""Create a deterministic execution manifest for the CZL coarse screen."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


EXPECTED_WORKSHEET_SHA256 = "0a60f6a24466195fd2cd94d98fd3d4f1518ac24f2bc84f00c7435059d0219729"
EXPECTED_RECORDS = 448
BATCH_SIZE = 16


def canonical_sha256(path: Path) -> str:
    content = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def plan(records: list[dict]) -> dict:
    batches = []
    for offset in range(0, len(records), BATCH_SIZE):
        members = records[offset:offset + BATCH_SIZE]
        batch_number = offset // BATCH_SIZE + 1
        batches.append({
            "batch_id": f"CZCS-B{batch_number:02d}",
            "first_inventory_id": members[0]["inventory_id"],
            "last_inventory_id": members[-1]["inventory_id"],
            "record_count": len(members),
            "inventory_ids": [record["inventory_id"] for record in members],
            "execution_status": "Planned",
            "checkpoint_after_batch": batch_number == 1,
        })
    return {
        "manifest_version": "1.0.0",
        "worksheet_sha256_lf": EXPECTED_WORKSHEET_SHA256,
        "execution_order": "Lexical inventory_id order",
        "batch_size": BATCH_SIZE,
        "record_count": len(records),
        "batch_count": len(batches),
        "batches": batches,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--worksheet", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    if canonical_sha256(args.worksheet) != EXPECTED_WORKSHEET_SHA256:
        parser.error("worksheet canonical SHA-256 does not match the fixed initial state")
    records = read_jsonl(args.worksheet)
    expected_ids = [f"CZPOP-{number:04d}" for number in range(1, EXPECTED_RECORDS + 1)]
    if [record.get("inventory_id") for record in records] != expected_ids:
        parser.error("worksheet must contain CZPOP-0001 through CZPOP-0448 in order")
    if any(record.get("screening_status") != "Not Screened" for record in records):
        parser.error("batch planning requires the pristine Not Screened worksheet")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(plan(records), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print("records=448")
    print("batches=28")
    print("first_batch=CZPOP-0001..CZPOP-0016")
    return 0


if __name__ == "__main__":
    sys.exit(main())
