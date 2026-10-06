#!/usr/bin/env python3
"""Validate public Mutual Agency Lab records and optional restricted source copies."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def validate(lab, private_sources=None):
    problems = []
    def check(condition, message):
        if not condition:
            problems.append(message)

    sources = jsonl(lab / "00_sources/SOURCE_REGISTRY.jsonl")
    ledger = jsonl(lab / "02_evidence/INITIATIVE_LEDGER.jsonl")
    receipts = jsonl(lab / "05_my_contribution/capability_receipts.jsonl")
    graph = json.loads((lab / "02_evidence/INFLUENCE_GRAPH.json").read_text(encoding="utf-8"))
    matrix = json.loads((lab / "01_framework/mutual_agency.json").read_text(encoding="utf-8"))
    source_by_id = {x["source_id"]: x for x in sources}
    ledger_by_id = {x["initiative_id"]: x for x in ledger}
    check(len(sources) == len(source_by_id) == 25, "source IDs: duplicate or unexpected count")
    check(len(ledger) == len(ledger_by_id) and len(ledger) >= 30, "initiative IDs: duplicate or fewer than 30")
    check(len({x["episode_group"] for x in ledger}) >= 20, "episode diversity below reported threshold")

    for event in ledger:
        check(event.get("confidence") in {"low", "medium", "high"}, f"{event['initiative_id']}: invalid confidence")
        check(bool(event.get("alternative_explanation")), f"{event['initiative_id']}: missing rival explanation")
        for ref in event.get("source_refs", []):
            src = source_by_id.get(ref["source_id"])
            check(src is not None, f"{event['initiative_id']}: unknown source {ref['source_id']}")
            if src:
                check(1 <= ref["line_start"] <= ref["line_end"] <= src["line_count"], f"{event['initiative_id']}: source line range outside copy")
        check(event.get("source") in event.get("source_refs", []), f"{event['initiative_id']}: primary source missing from refs")

    node_ids = {x["id"] for x in graph["nodes"]}
    check(len(node_ids) == len(graph["nodes"]), "duplicate graph node")
    edge_ids = [x["id"] for x in graph["edges"]]
    check(len(set(edge_ids)) == len(edge_ids), "duplicate graph edge")
    directions = set()
    for edge in graph["edges"]:
        check(edge["from"] in node_ids and edge["to"] in node_ids, f"{edge['id']}: missing node")
        check(edge["direction"] in {"Human_to_AI", "AI_to_Human"}, f"{edge['id']}: invalid direction")
        check(bool(edge.get("alternative")), f"{edge['id']}: rival explanation missing")
        directions.add(edge["direction"])
        for ref in edge["evidence"]:
            check(ref in ledger_by_id, f"{edge['id']}: unknown initiative {ref}")
    check(directions == {"Human_to_AI", "AI_to_Human"}, "two-way graph absent")

    for dim in matrix["dimensions"]:
        for ref in dim["human_examples"] + dim["assistant_examples"]:
            check(ref in ledger_by_id, f"matrix {dim['dimension']}: unknown initiative {ref}")
    check(len({x["dimension"] for x in matrix["dimensions"]}) == len(matrix["dimensions"]), "duplicate matrix dimension")
    for receipt in receipts:
        for ref in receipt["evidence"]:
            check(ref in ledger_by_id, f"{receipt['receipt_id']}: unknown initiative {ref}")

    if private_sources is not None:
        root = private_sources.resolve()
        for src in sources:
            p = (root / src["private_local_filename"]).resolve()
            if not p.is_relative_to(root) or not p.is_file():
                problems.append(f"{src['source_id']}: restricted copy missing or unsafe path")
                continue
            check(p.stat().st_size == src["byte_count"], f"{src['source_id']}: byte count differs")
            check(sha256(p) == src["sha256_exact_uploaded_copy"], f"{src['source_id']}: SHA-256 differs")
            with p.open("rb") as fh:
                # splitlines matches the original registry's counting rule, including CRLF.
                line_count = sum(1 for _ in fh)
            check(line_count == src["line_count"], f"{src['source_id']}: line count differs")

    actual_files = {str(p.relative_to(lab)) for p in lab.rglob("*") if p.is_file() and "__pycache__" not in p.parts}
    checksums = lab / "SHA256SUMS.txt"
    if checksums.exists():
        listed = {}
        for line in checksums.read_text(encoding="utf-8").splitlines():
            match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
            if not match:
                problems.append("malformed SHA256SUMS line")
                continue
            digest, name = match.groups()
            check(name not in listed, f"duplicate SHA entry: {name}")
            listed[name] = digest
            target = (lab / name).resolve()
            if target.is_relative_to(lab.resolve()) and target.is_file():
                check(sha256(target) == digest, f"hash mismatch: {name}")
            else:
                problems.append(f"missing or unsafe SHA target: {name}")
        check(set(listed) == actual_files - {"SHA256SUMS.txt"}, "SHA256SUMS coverage differs from file tree")
    else:
        problems.append("SHA256SUMS.txt missing")

    manifest_path = lab / "docs/FILE_MANIFEST.jsonl"
    if manifest_path.exists():
        manifest = jsonl(manifest_path)
        mapped = {}
        for row in manifest:
            name = row["path"]
            check(name not in mapped, f"duplicate manifest path: {name}")
            mapped[name] = row
            p = (lab / name).resolve()
            check(p.is_relative_to(lab.resolve()) and p.is_file(), f"manifest path missing: {name}")
            if p.is_file():
                check(sha256(p) == row["sha256"], f"manifest hash mismatch: {name}")
            check(row.get("version") == "0.1" and bool(row.get("source")) and row.get("worklog") == "docs/WORKLOG.md", f"manifest provenance missing: {name}")
        check(set(mapped) == actual_files - {"docs/FILE_MANIFEST.jsonl", "SHA256SUMS.txt"}, "manifest coverage differs from file tree")
    else:
        problems.append("FILE_MANIFEST.jsonl missing")

    for md in lab.rglob("*.md"):
        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", md.read_text(encoding="utf-8")):
            path = unquote(link.split("#", 1)[0])
            if not path or re.match(r"^(https?://|mailto:)", path):
                continue
            if "continuity-lab" in Path(path).parts and path.startswith("../"):
                # This directory is provided by the branch parent, not the standalone lab package.
                continue
            target = (md.parent / path).resolve()
            check(target.is_relative_to(lab.resolve()) and target.exists(), f"broken local link {md.relative_to(lab)} -> {link}")

    return problems, {"sources": len(sources), "initiatives": len(ledger), "episode_groups": len({x['episode_group'] for x in ledger}), "graph_edges": len(graph["edges"]), "files": len(actual_files)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lab", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--private-sources", type=Path)
    args = ap.parse_args()
    problems, counts = validate(args.lab.resolve(), args.private_sources)
    print(json.dumps({"ok": not problems, "counts": counts, "problems": problems}, ensure_ascii=False, indent=2))
    raise SystemExit(1 if problems else 0)


if __name__ == "__main__":
    main()
