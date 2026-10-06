#!/usr/bin/env python3
"""Deterministic plumbing check. Does not call a language model."""
import argparse
import json
from pathlib import Path


def simulate(case):
    stored = bool(case["stored"])
    indexed = stored and bool(case["indexed"])
    retrieved = indexed and bool(case["retrieval_enabled"])
    in_context = retrieved and bool(case["context_injection_enabled"])
    used = in_context and bool(case["use_available_memory"])
    observed = case["memory_value"] if used else "NINCS"
    return {
        "condition": case["condition"],
        "memory_id": case["memory_id"],
        "stored": stored, "indexed": indexed, "retrieved": retrieved,
        "in_context": in_context, "used": used,
        "observed": observed, "expected": case["expected"],
        "matches_expected": observed == case["expected"],
        "note": "Scripted fixture, no model inference or continuity conclusion.",
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--lab", type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument("--out", type=Path)
    a = p.parse_args()
    cases = json.loads((a.lab / "06_tests/phase_c/cases.json").read_text(encoding="utf-8"))
    assert {x["condition"] for x in cases} == {
        "positive_retrieval", "stored_unindexed", "absent",
        "decoy_memory", "neutral_control"
    }
    result = {"kind": "synthetic_dry_run", "model_calls": 0,
              "runs": [simulate(x) for x in cases]}
    target = a.out or a.lab / "06_tests/phase_c/synthetic_run.json"
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Synthetic runs:", len(result["runs"]), "model calls:", result["model_calls"])


if __name__ == "__main__":
    main()
