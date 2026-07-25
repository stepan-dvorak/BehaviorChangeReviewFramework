#!/usr/bin/env python3
"""Regression tests for the retained CZL coarse-screen calibration batch."""

from __future__ import annotations

import hashlib
import json
import subprocess
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
WORKSHEET = ROOT / "Empirical" / "Data" / "BCApps_CZ_Coarse_Screen.jsonl"
SCHEMA = ROOT / "Schemas" / "BCApps_CZ_Coarse_Screen.schema.json"
BASE_COMMIT = "aea85c8627b78dcd88e8eb7e8c17d27e4adadcf5"
WORKSHEET_PATH = "Empirical/Data/BCApps_CZ_Coarse_Screen.jsonl"
EXPECTED_SCREENED_SHA256 = "5dac8a307299bec68d859d6bfd40e33a1551310c110a18d4eaa2196dd25db0d5"
ALLOWED_SCREENING_FIELDS = {
    "screening_status", "evidence_availability", "targeted_search_questions",
    "screening_observations", "unavailability_reason", "screened_by", "screened_on",
}


def read_jsonl_text(text: str) -> list[dict]:
    return [json.loads(line) for line in text.splitlines()]


class BatchExecutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = WORKSHEET.read_text(encoding="utf-8")
        cls.records = read_jsonl_text(cls.text)
        cls.baseline = read_jsonl_text(subprocess.check_output(
            ["git", "show", f"{BASE_COMMIT}:{WORKSHEET_PATH}"],
            cwd=ROOT, text=True,
        ))
        cls.schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    def test_complete_worksheet_is_schema_valid(self) -> None:
        validator = Draft202012Validator(self.schema, format_checker=FormatChecker())
        errors = [
            f"record {number}: {error.message}"
            for number, record in enumerate(self.records, 1)
            for error in validator.iter_errors(record)
        ]
        self.assertEqual([], errors)

    def test_calibration_batch_only_is_screened(self) -> None:
        self.assertEqual(448, len(self.records))
        self.assertEqual(
            [f"CZPOP-{number:04d}" for number in range(1, 449)],
            [record["inventory_id"] for record in self.records],
        )
        for index, record in enumerate(self.records):
            if index < 16:
                self.assertEqual("Ready for Prior-Knowledge Labeling", record["screening_status"])
                self.assertEqual("Available", record["evidence_availability"]["established_flow"])
                self.assertEqual([], record["targeted_search_questions"])
                self.assertEqual("OpenAI Codex", record["screened_by"])
                self.assertEqual("2026-07-21", record["screened_on"])
            else:
                self.assertEqual(self.baseline[index], record)

    def test_non_screening_and_downstream_fields_are_protected(self) -> None:
        for number, (before, after) in enumerate(zip(self.baseline, self.records), 1):
            changed = {key for key in before if before[key] != after[key]}
            if number <= 16:
                self.assertLessEqual(changed, ALLOWED_SCREENING_FIELDS)
            else:
                self.assertEqual(set(), changed)
            self.assertEqual("Unknown", after["prior_known"])
            self.assertEqual("Unselected", after["selection_status"])
            self.assertEqual("Not Evaluated", after["trigger_status"])
            self.assertEqual("Not Evaluated", after["checklist_status"])

    def test_screened_worksheet_is_deterministic(self) -> None:
        canonical = "\n".join(self.text.splitlines()) + "\n"
        self.assertEqual(EXPECTED_SCREENED_SHA256, hashlib.sha256(canonical.encode()).hexdigest())


if __name__ == "__main__":
    unittest.main()
