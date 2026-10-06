#!/usr/bin/env python3
"""Deterministic pilot sample from two edited transcript copies.

The private text output stays in scratch; only metadata is suitable for publication.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

SOURCE_NAMES = {"MA-SRC-017": "17-elso-nap-es-minden-honap.txt", "MA-SRC-018": "18-csapat3.txt"}
SEED = "OpenField-2026-10-06-denominator-v0.1-fixed-before-sample-inspection"


def h(x):
    return hashlib.sha256(x.encode("utf-8")).hexdigest()


def normalize(x):
    return " ".join(x.split()).casefold()


def candidates(sid, path, registry, curated):
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != registry[sid]["sha256_exact_uploaded_copy"]:
        raise ValueError(f"source copy hash differs: {sid}")
    lines = raw.decode("utf-8-sig", errors="replace").splitlines()
    out = []
    i = 0
    while i < len(lines):
        if lines[i].strip() != "Ezt mondtad:":
            i += 1
            continue
        um = i
        j = i + 1
        while j < len(lines) and lines[j].strip() not in ("A ChatGPT ezt mondta:", "Ezt mondtad:"):
            j += 1
        if j >= len(lines) or lines[j].strip() != "A ChatGPT ezt mondta:":
            i = j
            continue
        am = j
        k = j + 1
        while k < len(lines) and lines[k].strip() != "Ezt mondtad:":
            k += 1
        user = "\n".join(lines[um+1:am]).strip()
        assistant = "\n".join(lines[am+1:k]).strip()
        i = k
        if not (20 <= len(user) <= 3000 and 20 <= len(assistant) <= 5000):
            continue
        if any(ref["source_id"] == sid and not (k < ref["line_start"] or um+1 > ref["line_end"])
               for row in curated for ref in row["source_refs"]):
            continue
        key = h(normalize(user) + "\n---\n" + normalize(assistant))
        out.append({"source_id": sid, "user_lines": [um+2, am], "assistant_lines": [am+2, k],
                    "user_text": user, "assistant_text": assistant, "turn_hash": key})
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True, help="repository root containing mutual-agency-lab")
    parser.add_argument("--sources-dir", type=Path, required=True, help="private, exact uploaded TXT copies")
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--private-out", type=Path, help="optional path for raw sampled text; never publish this file")
    args = parser.parse_args()
    registry = {x["source_id"]: x for x in map(json.loads, (args.repo / "mutual-agency-lab/00_sources/SOURCE_REGISTRY.jsonl").read_text().splitlines())}
    curated = [x for x in map(json.loads, (args.repo / "mutual-agency-lab/02_evidence/INITIATIVE_LEDGER.jsonl").read_text().splitlines())]
    args.out_dir.mkdir(parents=True, exist_ok=True)
    seen = set()
    selected = []
    counts = {}
    for sid, filename in SOURCE_NAMES.items():
        rows = candidates(sid, args.sources_dir / filename, registry, curated)
        unique = []
        for row in rows:
            if row["turn_hash"] not in seen:
                seen.add(row["turn_hash"])
                unique.append(row)
        counts[sid] = {"eligible_before_cross_file_dedup": len(rows), "unique_eligible": len(unique)}
        ranks = [(h(SEED + sid + row["turn_hash"]), row) for row in unique]
        chosen = [row for _, row in sorted(ranks, key=lambda x: x[0])[:10]]
        for row in chosen:
            row["sample_id"] = f"OF-SAMPLE-{len(selected)+1:02d}"
            selected.append(row)
    if args.private_out:
        args.private_out.write_text(json.dumps({"seed": SEED, "counts": counts, "sample": selected}, ensure_ascii=False, indent=2) + "\n")
    public = [{k: v for k, v in row.items() if k not in ("user_text", "assistant_text")} for row in selected]
    (args.out_dir / "sample_metadata.json").write_text(json.dumps({"seed": SEED, "counts": counts, "sample": public}, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"counts": counts, "selected": len(selected), "sample_ids": [x["sample_id"] for x in selected]}))


if __name__ == "__main__":
    main()
