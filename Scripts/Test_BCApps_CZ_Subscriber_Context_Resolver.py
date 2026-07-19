#!/usr/bin/env python3
"""Focused regression tests for the bounded CZL subscriber-context resolver."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("Resolve_BCApps_CZ_Subscriber_Context.py")
SPEC = importlib.util.spec_from_file_location("context_resolver", SCRIPT)
assert SPEC and SPEC.loader
RESOLVER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RESOLVER)
BOUNDARY = {
    "CZDEP-0001": {"app_id": "subject", "app_name": "Subject"},
    "CZDEP-0003": {"app_id": "base", "app_name": "Base Application"},
}


def retained_row(path: str) -> dict[str, str]:
    return {
        "inventory_id": "CZPOP-0001",
        "source_commit": RESOLVER.EXPECTED_COMMIT,
        "source_path": path,
        "source_line": "2",
        "subscriber_codeunit_name": "Fixture Subscriber",
        "subscriber_instance": "StaticAutomatic (default)",
        "subscriber_procedure": "HandleFixture",
        "publisher_object_type": "ObjectType::Codeunit",
        "publisher_object": "Codeunit::FixturePublisher",
        "published_event_name": "OnFixture",
        "published_element_name": "",
        "var_parameter_names": "Value",
    }


class ResolverFailureStatusTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.relative = "FixtureSubscriber.Codeunit.al"
        (self.root / self.relative).write_text(
            "codeunit 1 FixtureSubscriber\n"
            "    [EventSubscriber(ObjectType::Codeunit, Codeunit::FixturePublisher, 'OnFixture', '', false, false)]\n"
            "    local procedure HandleFixture(var Value: Boolean)\n"
            "    begin\n"
            "        Value := true;\n"
            "    end;\n"
            "}\n",
            encoding="utf-8",
        )
        self.row = retained_row(self.relative)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_missing_source_remains_explicit(self) -> None:
        result = RESOLVER.resolve_row(
            self.root, self.row, {}, ["CZPOP-0001"], {}, {}, BOUNDARY
        )
        self.assertEqual("Source Not in Boundary", result["publisher_resolution_status"])
        self.assertEqual("Unresolved", result["context_resolution_status"])
        self.assertEqual("Not Screened", result["coarse_screen_status"])
        self.assertEqual(["5:Value"], result["control_parameter_writes"])

    def test_ambiguous_source_remains_explicit(self) -> None:
        key = ("codeunit", "fixturepublisher", "onfixture")
        candidate = {
            "path": "Publisher.Codeunit.al", "declaration_line": 8,
            "event_class": "Integration Event",
        }
        result = RESOLVER.resolve_row(
            self.root, self.row, {key: [candidate, {**candidate, "declaration_line": 18}]},
            ["CZPOP-0001"], {}, {}, BOUNDARY,
        )
        self.assertEqual("Ambiguous Target", result["publisher_resolution_status"])
        self.assertEqual("Partially Resolved", result["context_resolution_status"])
        self.assertIn("Publisher.Codeunit.al:8", result["unresolved_reason"])

    def test_validation_selection_is_deterministic(self) -> None:
        records = [
            {"inventory_id": "CZPOP-0002", "target_event_class": "Integration Event",
             "publisher_resolution_status": "Resolved Source Publisher"},
            {"inventory_id": "CZPOP-0001", "target_event_class": "Integration Event",
             "publisher_resolution_status": "Source Not in Boundary"},
        ]
        selected = RESOLVER.validation_selection(sorted(records, key=lambda x: x["inventory_id"]))
        self.assertEqual(["CZPOP-0001"], [item["inventory_id"] for item in selected])


if __name__ == "__main__":
    unittest.main()
