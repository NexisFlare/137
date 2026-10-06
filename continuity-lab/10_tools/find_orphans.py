#!/usr/bin/env python3
"""Report files, sources, claims, and anchors with no current registry path.

This is an index reachability audit, not a test of anyone's lived memory.
"""
import argparse
import json
from pathlib import Path


def rows(path):
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def inventory(lab, repo, repo_inventory=None):
    source_rows = rows(lab / "00_manifest/sources.jsonl")
    claim_rows = rows(lab / "02_evidence/claims.jsonl")
    anchors = rows(lab / "04_memory/anchors.jsonl")
    index = json.loads((lab / "09_machine/index.json").read_text(encoding="utf-8"))

    listed_files = set(index.get("lab_files", []))
    actual_lab = {str(p.relative_to(lab)) for p in lab.rglob("*") if p.is_file() and "__pycache__" not in p.parts}
    actual_lab.discard("SHA256SUMS.txt")
    lab_orphans = sorted(actual_lab - listed_files)
    bad_lab_refs = sorted(listed_files - actual_lab)

    source_ids = {x["source_id"] for x in source_rows}
    referenced_sources = set(index.get("source_ids", []))
    for c in claim_rows:
        referenced_sources.update(c.get("supporting_sources", []))
        referenced_sources.update(c.get("contradicting_sources", []))
        if c.get("first_known_source"):
            referenced_sources.add(c["first_known_source"])
    orphan_sources = sorted(source_ids - referenced_sources)
    bad_sources = sorted(referenced_sources - source_ids)

    claim_ids = {x["claim_id"] for x in claim_rows}
    orphan_claims = sorted(claim_ids - set(index.get("claim_ids", [])))
    bad_claims = sorted(set(index.get("claim_ids", [])) - claim_ids)

    anchor_ids = {x["anchor_id"] for x in anchors}
    orphan_anchors = sorted(anchor_ids - set(index.get("anchor_ids", [])))
    bad_anchors = sorted(set(index.get("anchor_ids", [])) - anchor_ids)

    repo_orphans = []
    bad_repo_refs = []
    if repo or repo_inventory:
        referenced_paths = {x["repo_path"] for x in source_rows if x.get("repo_path")}
        if repo_inventory:
            remote = json.loads(repo_inventory.read_text(encoding="utf-8"))
            files = set(remote["paths"])
        else:
            repo = repo.resolve()
            if not repo.is_dir():
                raise ValueError("Repository root must be an existing directory")
            files = {
                str(p.relative_to(repo))
                for p in repo.rglob("*")
                if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts
                and not p.is_relative_to(lab.resolve())
            }
        repo_orphans = sorted(files - referenced_paths)
        bad_repo_refs = sorted(referenced_paths - files)
    return {
        "lab_files_unindexed": lab_orphans,
        "index_paths_missing": bad_lab_refs,
        "sources_unreferenced": orphan_sources,
        "source_refs_missing": bad_sources,
        "claims_unindexed": orphan_claims,
        "claim_refs_missing": bad_claims,
        "anchors_unindexed": orphan_anchors,
        "anchor_refs_missing": bad_anchors,
        "historical_repo_files_unmapped": repo_orphans,
        "repo_paths_missing": bad_repo_refs,
    }


def render(data, repo):
    lines = [
        "# ORPHAN REPORT",
        "",
        "This is an index coverage report. A candidate does not prove that an agent",
        "forgot a memory, or that an unindexed historical file should be loaded.",
        "No content was deleted or rewritten.",
        "",
    ]
    for key, values in data.items():
        lines += ["## " + key + " (" + str(len(values)) + ")", ""]
        lines += ["- " + x for x in values] or ["- None"]
        lines += [""]
    if repo is None:
        lines += ["Repository scan omitted: pass --repo-inventory or --repo-root.", ""]
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--lab", type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument("--repo-root", type=Path)
    p.add_argument("--repo-inventory", type=Path)
    p.add_argument("--out", type=Path)
    a = p.parse_args()
    data = inventory(a.lab.resolve(), a.repo_root, a.repo_inventory)
    result = render(data, a.repo_root or a.repo_inventory)
    if a.out:
        a.out.write_text(result, encoding="utf-8")
    else:
        print(result)


if __name__ == "__main__":
    main()
