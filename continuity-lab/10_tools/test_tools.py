#!/usr/bin/env python3
"""Small regression checks for index reachability and synthetic controls."""
import json
import tempfile
import unittest
from pathlib import Path

from find_orphans import inventory
from phase_c_dry_run import simulate


class ReachabilityTests(unittest.TestCase):
    def test_unindexed_references_and_unmapped_repo_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            lab = Path(tmp)
            for relative, data in {
                "00_manifest/sources.jsonl": '{"source_id":"NF-SRC-000001","repo_path":"old.txt"}\n',
                "02_evidence/claims.jsonl": '{"claim_id":"NF-CLM-000001","supporting_sources":[]}\n',
                "04_memory/anchors.jsonl": '{"anchor_id":"NF-ANC-001"}\n',
                "09_machine/index.json": json.dumps({
                    "lab_files": [], "source_ids": [], "claim_ids": [], "anchor_ids": []
                }),
                "00_manifest/repo_tree_at_base.json": '{"paths":["old.txt","lost.txt"]}\n',
            }.items():
                path = lab / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(data, encoding="utf-8")
            report = inventory(lab, None, lab / "00_manifest/repo_tree_at_base.json")
            self.assertEqual(report["historical_repo_files_unmapped"], ["lost.txt"])
            self.assertEqual(report["sources_unreferenced"], ["NF-SRC-000001"])
            self.assertEqual(report["claims_unindexed"], ["NF-CLM-000001"])
            self.assertEqual(report["anchors_unindexed"], ["NF-ANC-001"])

    def test_stored_but_unindexed_does_not_reach_context(self):
        row = simulate({
            "condition": "stored_unindexed", "memory_id": "SYN-ALPHA",
            "stored": True, "indexed": False, "retrieval_enabled": True,
            "context_injection_enabled": True, "use_available_memory": True,
            "memory_value": "KÉK-KŐ", "expected": "NINCS",
        })
        self.assertTrue(row["stored"])
        self.assertFalse(row["retrieved"])
        self.assertFalse(row["used"])
        self.assertTrue(row["matches_expected"])

    def test_decoy_can_be_used_and_wrong(self):
        row = simulate({
            "condition": "decoy_memory", "memory_id": "SYN-ALPHA",
            "stored": True, "indexed": True, "retrieval_enabled": True,
            "context_injection_enabled": True, "use_available_memory": True,
            "memory_value": "PIROS-KŐ", "expected": "KÉK-KŐ",
        })
        self.assertTrue(row["used"])
        self.assertFalse(row["matches_expected"])


if __name__ == "__main__":
    unittest.main()
