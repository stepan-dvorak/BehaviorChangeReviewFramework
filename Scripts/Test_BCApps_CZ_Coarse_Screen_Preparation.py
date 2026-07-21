#!/usr/bin/env python3
"""Focused regression tests for coarse-screen worksheet preparation."""

from __future__ import annotations

import importlib.util
import hashlib
import json
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("Prepare_BCApps_CZ_Coarse_Screen.py")
SPEC = importlib.util.spec_from_file_location("coarse_screen", SCRIPT)
assert SPEC and SPEC.loader
SCREEN = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SCREEN)


def context(**overrides) -> dict:
    value = {
        "inventory_id": "CZPOP-0001", "target_event_class": "Integration Event",
        "publisher_resolution_status": "Resolved Source Publisher",
        "subscriber_instance": "StaticAutomatic (default)",
        "control_parameter_reads": [], "control_parameter_writes": [],
        "transaction_markers": [], "error_markers": [],
        "composition_subscriber_ids": [], "test_context_paths": [],
        "binding_context_paths": [], "context_resolution_status": "Resolved",
        "subscriber_path": "Subscriber.Codeunit.al", "subscriber_body_start_line": 10,
        "subscriber_body_end_line": 20,
    }
    value.update(overrides)
    return value


class PreparationTests(unittest.TestCase):
    def test_static_prefill_preserves_workflow_boundary(self) -> None:
        record = SCREEN.prepare_record(context())
        self.assertEqual("Not Screened", record["screening_status"])
        self.assertEqual("Static Automatic", record["evidence_availability"]["runtime_participation"])
        self.assertEqual("Unknown", record["prior_known"])
        self.assertEqual("Unselected", record["selection_status"])
        self.assertEqual("Not Evaluated", record["trigger_status"])

    def test_manual_without_binding_requires_targeted_question(self) -> None:
        record = SCREEN.prepare_record(context(subscriber_instance="Manual"))
        self.assertEqual("Targeted Search Required", record["evidence_availability"]["runtime_participation"])
        self.assertEqual(2, len(record["targeted_search_questions"]))
        self.assertIn("Manual Subscriber", record["stratum_indicators"])

    def test_indicators_are_mechanical_and_ordered(self) -> None:
        record = SCREEN.prepare_record(context(
            control_parameter_writes=["12:Value"], composition_subscriber_ids=["CZPOP-0002"]
        ))
        self.assertEqual(
            ["Integration Event", "Dependency Publisher", "Static Subscriber",
             "Mutable Parameter Write", "Same-Target CZL Peers", "No Linked Test Context"],
            record["stratum_indicators"],
        )

    def test_validation_selection_deduplicates_and_orders(self) -> None:
        contexts = [
            context(inventory_id="CZPOP-0002", subscriber_instance="Manual"),
            context(inventory_id="CZPOP-0001"),
        ]
        records = [SCREEN.prepare_record(item) for item in contexts]
        selected = SCREEN.validation_selection(contexts, records)
        self.assertEqual(["CZPOP-0001", "CZPOP-0002"], [item["inventory_id"] for item in selected])

    def test_retained_full_template_is_pristine_and_reproducible(self) -> None:
        root = SCRIPT.parent.parent
        retained = root / "Empirical/Data/BCApps_CZ_Coarse_Screen.jsonl"
        context_path = root / "Empirical/Data/BCApps_CZ_Subscriber_Context.jsonl"
        records = [json.loads(line) for line in retained.read_text(encoding="utf-8").splitlines()]
        contexts = SCREEN.read_jsonl(context_path)
        expected = [SCREEN.prepare_record(item) for item in contexts]

        self.assertEqual(448, len(records))
        self.assertEqual(expected, records)
        self.assertEqual(
            [item["inventory_id"] for item in contexts],
            [item["inventory_id"] for item in records],
        )
        self.assertTrue(all(item["screening_status"] == "Not Screened" for item in records))
        self.assertTrue(all(item["screened_by"] is None for item in records))
        self.assertTrue(all(item["screened_on"] is None for item in records))
        self.assertTrue(all(item["prior_known"] == "Unknown" for item in records))
        self.assertTrue(all(item["selection_status"] == "Unselected" for item in records))
        self.assertTrue(all(item["trigger_status"] == "Not Evaluated" for item in records))
        self.assertTrue(all(item["checklist_status"] == "Not Evaluated" for item in records))
        canonical_retained_bytes = (
            "\n".join(retained.read_text(encoding="utf-8").splitlines()) + "\n"
        ).encode("utf-8")
        self.assertEqual(
            "0a60f6a24466195fd2cd94d98fd3d4f1518ac24f2bc84f00c7435059d0219729",
            hashlib.sha256(canonical_retained_bytes).hexdigest(),
        )


if __name__ == "__main__":
    unittest.main()
