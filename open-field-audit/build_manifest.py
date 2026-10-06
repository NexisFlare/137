#!/usr/bin/env python3
"""Build file provenance manifest and SHA-256 list without self-reference cycles."""
import hashlib
import json
from pathlib import Path

AUDIT = Path(__file__).resolve().parent
MANIFEST = AUDIT / "FILE_MANIFEST.jsonl"
SUMS = AUDIT / "SHA256SUMS.txt"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source(name):
    if name in {"sample_metadata.json", "coded_sample.jsonl", "selected_ledger_recheck.jsonl"}:
        return "MA-SRC-013/017/018/019 excerpts and Mutual Agency Lab v0.1; see README"
    if name == "README.md":
        return "Current GPT-6 Codex analysis; Mutual Agency Lab v0.1; Wikimedia Foundation 2026-10-05"
    return "Current GPT-6 Codex implementation and decision record, 2026-10-06"


files = sorted(p for p in AUDIT.iterdir() if p.is_file() and p not in (MANIFEST, SUMS))
MANIFEST.write_text("".join(json.dumps({"path": p.name, "sha256": sha(p), "source": source(p.name),
                                         "version": "0.1", "decision_log": "DECISION_TRACE.md"},
                                        ensure_ascii=False, sort_keys=True) + "\n" for p in files), encoding="utf-8")
SUMS.write_text("".join(f"{sha(p)}  {p.name}\n" for p in sorted(files + [MANIFEST])), encoding="utf-8")
print(f"indexed {len(files)} content files; {len(files)+1} SHA-256 entries")
