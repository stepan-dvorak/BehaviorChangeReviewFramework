#!/usr/bin/env python3
"""Unit tests for the repository line-ending validator."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("Validate_Line_Endings.py")
SPEC = importlib.util.spec_from_file_location("validate_line_endings", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

EolRecord = MODULE.EolRecord
parse_eol_line = MODULE.parse_eol_line
validate_records = MODULE.validate_records


class LineEndingValidatorTests(unittest.TestCase):
    def test_parse_lf_record(self) -> None:
        record = parse_eol_line("i/lf    w/lf    attr/text=auto eol=lf\tREADME.md")
        self.assertEqual(record.path, "README.md")
        self.assertEqual(record.index, "lf")
        self.assertEqual(record.worktree, "lf")
        self.assertEqual(record.configured_worktree_eol, "lf")

    def test_crlf_in_index_fails(self) -> None:
        errors = validate_records(
            [EolRecord("legacy.txt", "crlf", "crlf", "text=auto eol=lf")]
        )
        self.assertEqual(len(errors), 1)
        self.assertIn("Git index EOL is crlf", errors[0])

    def test_bat_crlf_worktree_is_allowed_with_lf_index(self) -> None:
        errors = validate_records(
            [EolRecord("run.bat", "lf", "crlf", "text eol=crlf")]
        )
        self.assertEqual(errors, [])

    def test_existing_bat_lf_worktree_does_not_break_index_gate(self) -> None:
        record = EolRecord("run.bat", "lf", "lf", "text eol=crlf")
        self.assertEqual(validate_records([record]), [])
        self.assertEqual(record.configured_worktree_eol, "crlf")

    def test_binary_is_ignored(self) -> None:
        errors = validate_records(
            [EolRecord("image.png", "-text", "-text", "-text -diff -merge")]
        )
        self.assertEqual(errors, [])

    def test_none_is_allowed_for_empty_text_file(self) -> None:
        errors = validate_records(
            [EolRecord("empty.txt", "none", "none", "text=auto eol=lf")]
        )
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
