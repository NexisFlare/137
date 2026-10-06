#!/usr/bin/env python3
"""Offline structural and integrity checks for Continuity Lab."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

from find_orphans import inventory, rows

NODE_TYPES = {"Human", "Model", "Session", "Document", "Memory",
              "Repository commit", "Public post", "Video", "Claim", "Correction", "Test"}
RELATIONS = {"created", "quoted", "copied_from", "influenced", "corrected",
             "contradicted", "archived_as", "retrieved_by", "used_in_context", "published_as"}
STATUSES = {"supported", "partially_supported", "open", "contradicted", "unverifiable"}
HASH = re.compile(r"^[0-9a-f]{64}$")


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def validate(lab, phase_b=None):
    errors = []
    sources = rows(lab / "00_manifest/sources.jsonl")
    claims = rows(lab / "02_evidence/claims.jsonl")
    crosswalk = rows(lab / "02_evidence/legacy_crosswalk.jsonl")
    anchors = rows(lab / "04_memory/anchors.jsonl")
    graph = json.loads((lab / "02_evidence/provenance_graph.json").read_text(encoding="utf-8"))
    source_ids = [s.get("source_id") for s in sources]
    claim_ids = [c.get("claim_id") for c in claims]
    anchor_ids = [a.get("anchor_id") for a in anchors]
    require(len(source_ids) == len(set(source_ids)), "duplicate source_id", errors)
    require(len(claim_ids) == len(set(claim_ids)), "duplicate claim_id", errors)
    require(len(anchor_ids) == len(set(anchor_ids)), "duplicate anchor_id", errors)
    for s in sources:
        sid = s.get("source_id", "?")
        for field in ("title", "platform", "mime_type", "model_label_confidence",
                      "verification_level", "copy_status"):
            require(field in s, sid + ": missing " + field, errors)
        require(bool(re.fullmatch(r"NF-SRC-\d{6}", sid)), sid + ": bad ID", errors)
        if s.get("sha256") is not None:
            require(bool(HASH.fullmatch(s["sha256"])), sid + ": invalid sha256", errors)
        if s.get("source_locator") and not s["source_locator"].startswith("private:"):
            require(s["source_locator"].startswith("https://"), sid + ": bad locator", errors)
        if s.get("parent_source"):
            require(s["parent_source"] in source_ids, sid + ": unknown parent", errors)
        for ref in s.get("related_sources", []):
            require(ref in source_ids, sid + ": unknown related source " + ref, errors)
    for c in claims:
        cid = c.get("claim_id", "?")
        require(bool(re.fullmatch(r"NF-CLM-\d{6}", cid)), cid + ": bad ID", errors)
        require(c.get("current_status") in STATUSES, cid + ": invalid status", errors)
        for sid in c.get("supporting_sources", []) + c.get("contradicting_sources", []):
            require(sid in source_ids, cid + ": missing source " + sid, errors)
        if c.get("first_known_source"):
            require(c["first_known_source"] in source_ids, cid + ": unknown first source", errors)
        require(c.get("confidence") in {"high", "medium", "low", "undetermined"},
                cid + ": invalid confidence", errors)
    require(len(crosswalk) == 26, "legacy crosswalk must retain E01–E26 IDs", errors)
    require({x.get("legacy_id") for x in crosswalk} ==
            {"E" + str(i).zfill(2) for i in range(1, 27)},
            "legacy crosswalk has missing or duplicate IDs", errors)
    for item in crosswalk:
        for sid in item.get("source_ids", []):
            require(sid in source_ids, item.get("legacy_id", "?") + ": bad crosswalk source", errors)
    for a in anchors:
        for sid in a.get("source_ids", []):
            require(sid in source_ids, a.get("anchor_id", "?") + ": unknown source", errors)

    for doc in lab.rglob("*.md"):
        body = doc.read_text(encoding="utf-8")
        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
            if link.startswith(("https://", "http://", "#", "mailto:")):
                continue
            local = (doc.parent / unquote(link.split("#", 1)[0])).resolve()
            require(local.is_relative_to(lab.resolve()) and local.exists(),
                    "broken internal link " + str(doc.relative_to(lab)) + ": " + link, errors)

    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    ids = [n.get("id") for n in nodes]
    require(len(ids) == len(set(ids)), "duplicate graph node", errors)
    for n in nodes:
        require(n.get("type") in NODE_TYPES, str(n.get("id")) + ": invalid node type", errors)
    for e in edges:
        require(e.get("from") in ids and e.get("to") in ids, "dangling graph edge: " + str(e), errors)
        require(e.get("relation") in RELATIONS, "unknown graph relation: " + str(e), errors)
        require(e.get("evidence_source") in source_ids, "edge without known evidence: " + str(e), errors)

    try:
        orphan = inventory(lab, None)
        for name in ("index_paths_missing", "source_refs_missing", "claim_refs_missing", "anchor_refs_missing"):
            require(not orphan[name], name + ": " + ", ".join(orphan[name]), errors)
    except Exception as exc:
        errors.append("orphan inventory: " + str(exc))

    sums = lab / "SHA256SUMS.txt"
    if sums.exists():
        for line in sums.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            expected, sep, relative = line.partition("  ")
            require(bool(sep) and bool(HASH.fullmatch(expected)), "bad hash line: " + line, errors)
            target = (lab / relative).resolve()
            require(target.is_relative_to(lab.resolve()) and target.is_file(), "missing hash target: " + relative, errors)
            if target.is_file():
                actual = hashlib.sha256(target.read_bytes()).hexdigest()
                require(expected == actual, "hash mismatch: " + relative, errors)

    locked = lab / "06_tests/phase_b/SHA256SUMS.txt"
    if phase_b and locked.exists():
        for line in locked.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            expected, sep, name = line.partition("  ")
            require(bool(sep), "bad Phase B line: " + line, errors)
            path = phase_b / name
            require(path.is_file(), "Phase B file missing: " + name, errors)
            if path.is_file():
                require(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                        "Phase B hash mismatch: " + name, errors)
    return errors, {"sources": len(sources), "claims": len(claims), "anchors": len(anchors),
                    "nodes": len(nodes), "edges": len(edges)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--lab", type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument("--phase-b-path", type=Path)
    a = p.parse_args()
    errors, counts = validate(a.lab.resolve(), a.phase_b_path)
    print(json.dumps({"status": "OK" if not errors else "FAIL", **counts, "errors": errors},
                     ensure_ascii=False, indent=2))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
