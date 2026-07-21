#!/usr/bin/env python3
"""Regression tests for the CZL coarse-screen batch plan."""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "Scripts" / "Plan_BCApps_CZ_Coarse_Screen_Batches.py"
SPEC = importlib.util.spec_from_file_location("batch_plan", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class BatchPlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.worksheet = ROOT / "Empirical" / "Data" / "BCApps_CZ_Coarse_Screen.jsonl"
        cls.manifest_path = ROOT / "Empirical" / "Data" / "BCApps_CZ_Coarse_Screen_Batches.json"
        cls.records = MODULE.read_jsonl(cls.worksheet)
        cls.manifest = json.loads(cls.manifest_path.read_text(encoding="utf-8"))

    def test_manifest_is_exact_generator_output(self) -> None:
        self.assertEqual(MODULE.plan(self.records), self.manifest)

    def test_every_record_appears_once_in_lexical_order(self) -> None:
        actual = [item for batch in self.manifest["batches"] for item in batch["inventory_ids"]]
        expected = [f"CZPOP-{number:04d}" for number in range(1, 449)]
        self.assertEqual(expected, actual)
        self.assertEqual(len(actual), len(set(actual)))

    def test_batches_are_fixed_and_unexecuted(self) -> None:
        self.assertEqual(28, self.manifest["batch_count"])
        self.assertTrue(all(batch["record_count"] == 16 for batch in self.manifest["batches"]))
        self.assertTrue(all(batch["execution_status"] == "Planned" for batch in self.manifest["batches"]))

    def test_only_first_batch_requires_initial_checkpoint(self) -> None:
        checkpoints = [batch["batch_id"] for batch in self.manifest["batches"] if batch["checkpoint_after_batch"]]
        self.assertEqual(["CZCS-B01"], checkpoints)

    def test_source_worksheet_is_pristine(self) -> None:
        self.assertEqual(MODULE.EXPECTED_WORKSHEET_SHA256, MODULE.canonical_sha256(self.worksheet))
        for record in self.records:
            self.assertEqual("Not Screened", record["screening_status"])
            self.assertIsNone(record["screened_by"])
            self.assertIsNone(record["screened_on"])
            self.assertEqual("Unknown", record["prior_known"])
            self.assertEqual("Unselected", record["selection_status"])
            self.assertEqual("Not Evaluated", record["trigger_status"])
            self.assertEqual("Not Evaluated", record["checklist_status"])


if __name__ == "__main__":
    unittest.main()
