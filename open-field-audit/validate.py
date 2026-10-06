#!/usr/bin/env python3
"""Check the public Open Field audit against the parent Mutual Agency Lab."""
import argparse
import collections
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote


def rows(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(repo, audit, private_sources=None):
    errors = []
    def check(ok, message):
        if not ok:
            errors.append(message)

    lab = repo / "mutual-agency-lab"
    ledger = rows(lab / "02_evidence/INITIATIVE_LEDGER.jsonl")
    matrix = json.loads((lab / "01_framework/mutual_agency.json").read_text(encoding="utf-8"))
    sources = {x["source_id"]: x for x in rows(lab / "00_sources/SOURCE_REGISTRY.jsonl")}
    events = {x["initiative_id"]: x for x in ledger}
    check(len(ledger) == 36, "parent ledger size changed; revisit interpretation")
    check(collections.Counter(x["initiator"] for x in ledger) == {"Parazs": 28, "archived_model_text": 8}, "initiator counts changed")
    assistant_refs = [i for dim in matrix["dimensions"] for i in dim["assistant_examples"]]
    check(len(assistant_refs) == 18, "assistant reference count changed")
    check(sum(events[i]["initiator"] == "Parazs" for i in assistant_refs) == 11, "assistant/turn mismatch count changed")
    check(len(set(assistant_refs)) == 13, "assistant unique reference count changed")

    metadata = json.loads((audit / "sample_metadata.json").read_text(encoding="utf-8"))
    sample = metadata["sample"]
    coded = rows(audit / "coded_sample.jsonl")
    recheck = rows(audit / "selected_ledger_recheck.jsonl")
    ids = {x["sample_id"] for x in sample}
    check(len(sample) == len(ids) == 20, "sample size or IDs differ")
    check({x["sample_id"] for x in coded} == ids and len(coded) == 20, "coded coverage differs")
    check(metadata["counts"]["MA-SRC-017"]["unique_eligible"] == 219 and metadata["counts"]["MA-SRC-018"]["unique_eligible"] == 192, "frame counts differ")
    check(len(recheck) == 8 and {x["initiative_id"] for x in recheck} == {x["initiative_id"] for x in ledger if x["initiator"] == "archived_model_text"}, "eight model-led rechecks differ")
    for item in sample:
        source = sources.get(item["source_id"])
        check(source is not None, f"unknown source {item['source_id']}")
        if source:
            check(1 <= item["user_lines"][0] <= item["user_lines"][1] < item["assistant_lines"][0] <= item["assistant_lines"][1] <= source["line_count"], f"line range invalid {item['sample_id']}")
        check(bool(re.fullmatch("[0-9a-f]{64}", item["turn_hash"])), f"turn hash invalid {item['sample_id']}")
        check("user_text" not in item and "assistant_text" not in item, f"private text leaked {item['sample_id']}")
    moves = collections.Counter(x["assistant_move"] for x in coded)
    expected = {"answer_only": 5, "followup_option": 5, "capability_claim": 3, "narrative_expansion": 3,
                "new_specific_proposal": 2, "requested_output": 1, "creative_continuation": 1}
    check(moves == expected, "coded move counts differ from README")
    check(sum(x["unverified_capability_claim"] for x in coded) == 3, "unverified capability count differs")
    check(all(not x["external_action_verified_in_excerpt"] for x in coded), "external action count differs")
    for item in recheck:
        check(item["initiative_id"] in events and item["source_id"] in sources, f"bad recheck reference {item['initiative_id']}")
        if item["initiative_id"] in events:
            check(item["source_id"] == events[item["initiative_id"]]["source"]["source_id"], f"recheck source differs {item['initiative_id']}")

    actual = {p.name for p in audit.iterdir() if p.is_file()}
    manifest = rows(audit / "FILE_MANIFEST.jsonl")
    names = {x["path"] for x in manifest}
    check(len(manifest) == len(names) and names == actual - {"FILE_MANIFEST.jsonl", "SHA256SUMS.txt"}, "manifest coverage differs")
    for item in manifest:
        p = audit / item["path"]
        check(p.is_file() and sha(p) == item["sha256"], f"manifest hash differs {item['path']}")
        check(item.get("decision_log") == "DECISION_TRACE.md" and item.get("version") == "0.1" and bool(item.get("source")), f"provenance missing {item['path']}")
    sums = {}
    for line in (audit / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        m = re.fullmatch("([0-9a-f]{64})  ([^/]+)", line)
        check(m is not None, "malformed SHA line")
        if m:
            digest, name = m.groups()
            sums[name] = digest
            check((audit / name).is_file() and sha(audit / name) == digest, f"SHA mismatch {name}")
    check(set(sums) == actual - {"SHA256SUMS.txt"}, "SHA list coverage differs")

    for md in [audit / "README.md", audit / "DECISION_TRACE.md"]:
        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", md.read_text(encoding="utf-8")):
            path = unquote(link.split("#", 1)[0])
            if not path or re.match(r"^(https?://|mailto:)", path):
                continue
            dest = (repo / path.removeprefix("../")) if path.startswith("../mutual-agency-lab/") else md.parent / path
            check(dest.exists(), f"broken link {md.name} -> {path}")

    if private_sources:
        with tempfile.TemporaryDirectory() as d:
            subprocess.run([sys.executable, str(audit / "sample_turns.py"), "--repo", str(repo),
                            "--sources-dir", str(private_sources), "--out-dir", d],
                           check=True, capture_output=True, text=True)
            check((Path(d) / "sample_metadata.json").read_bytes() == (audit / "sample_metadata.json").read_bytes(), "sample not reproducible from private copies")
    return errors, {"events": len(ledger), "assistant_refs": len(assistant_refs), "sample": len(sample), "eligible": metadata["counts"], "files": len(actual)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--private-sources", type=Path)
    args = parser.parse_args()
    problems, counts = validate(args.repo.resolve(), args.audit.resolve(), args.private_sources.resolve() if args.private_sources else None)
    print(json.dumps({"ok": not problems, "counts": counts, "problems": problems}, ensure_ascii=False, indent=2))
    raise SystemExit(1 if problems else 0)
