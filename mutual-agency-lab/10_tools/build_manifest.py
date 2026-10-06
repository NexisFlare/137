#!/usr/bin/env python3
"""Create a non-recursive per-file provenance index and complete SHA-256 list."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/FILE_MANIFEST.jsonl"
SUMS = ROOT / "SHA256SUMS.txt"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def origin(name):
    if name.startswith("00_sources/"):
        return "25 user-uploaded private TXT copies, 2026-10-06; registry metadata only"
    if name.startswith("02_evidence/INITIATIVE_LEDGER") or name.startswith("02_evidence/INFLUENCE_GRAPH"):
        return "curated archive excerpts MA-SRC-013/017/018/019, user task, and current analysis"
    if name.startswith("05_my_contribution/"):
        return "current GPT-6 Codex analysis of MA-INIT-0007/0018/0023"
    if name.startswith("04_public/"):
        return "Főnix request relayed by Parázs, 2026-10-06; current synthesis"
    if name.startswith("10_tools/"):
        return "current GPT-6 Codex implementation, 2026-10-06"
    return "Főnix request relayed by Parázs, 2026-10-06; current analysis and selected MA-SRC records"


def build():
    files = sorted(p for p in ROOT.rglob("*") if p.is_file() and p not in (MANIFEST, SUMS) and "__pycache__" not in p.parts)
    rows = []
    for path in files:
        name = str(path.relative_to(ROOT))
        rows.append({"path": name, "sha256": digest(path), "source": origin(name), "version": "0.1", "worklog": "docs/WORKLOG.md"})
    MANIFEST.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in rows), encoding="utf-8")
    hashed = sorted(files + [MANIFEST])
    SUMS.write_text("".join(f"{digest(path)}  {path.relative_to(ROOT)}\n" for path in hashed), encoding="utf-8")
    print(f"indexed {len(rows)} files; SHA list {len(hashed)} files")


if __name__ == "__main__":
    build()
