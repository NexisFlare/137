# Tools

All scripts use only the Python standard library and do not call external services.

    python3 10_tools/validate_lab.py --lab .
    python3 10_tools/find_orphans.py --lab . --repo-inventory 00_manifest/repo_tree_at_base.json
    python3 10_tools/phase_c_dry_run.py --lab .

find_orphans.py can instead use --repo-root with a fresh local checkout. It checks current index reachability, not subjective memory. Unmapped historical files in v0.1 are coverage work, not evidence of actual retrieval failure. ORPHAN_REPORT.md is a snapshot against the base commit's 98 blobs and may become stale after future commits. To update the report, first refresh the repository inventory and record its new commit SHA.

For the original private Phase B directory only:

    python3 10_tools/validate_lab.py --lab . --phase-b-path /path/to/phase_b_test_pack

The Phase C script is a deterministic fixture. It makes zero model calls.
