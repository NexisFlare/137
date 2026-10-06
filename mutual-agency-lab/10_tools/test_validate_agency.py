#!/usr/bin/env python3
"""Three focused regression checks for provenance and package integrity."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from validate_agency import validate

ROOT = Path(__file__).resolve().parents[1]


class AgencyValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.lab = Path(self.tmp.name) / "mutual-agency-lab"
        shutil.copytree(ROOT, self.lab, ignore=shutil.ignore_patterns("__pycache__"))

    def tearDown(self):
        self.tmp.cleanup()

    def test_original_package(self):
        problems, counts = validate(self.lab)
        self.assertEqual(problems, [])
        self.assertGreaterEqual(counts["initiatives"], 30)

    def test_unknown_source_is_rejected(self):
        p = self.lab / "02_evidence/INITIATIVE_LEDGER.jsonl"
        lines = p.read_text(encoding="utf-8").splitlines()
        event = json.loads(lines[0])
        event["source_refs"][0]["source_id"] = "MA-SRC-999"
        lines[0] = json.dumps(event, ensure_ascii=False)
        p.write_text("\n".join(lines) + "\n", encoding="utf-8")
        problems, _ = validate(self.lab)
        self.assertTrue(any("unknown source" in x for x in problems), problems)

    def test_tampered_file_is_rejected(self):
        p = self.lab / "04_public/PRINCIPLES.md"
        p.write_text(p.read_text(encoding="utf-8") + "\nchanged after manifest\n", encoding="utf-8")
        problems, _ = validate(self.lab)
        self.assertTrue(any("hash mismatch: 04_public/PRINCIPLES.md" in x for x in problems), problems)


if __name__ == "__main__":
    unittest.main()
