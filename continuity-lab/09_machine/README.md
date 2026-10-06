# Machine data

The index.json file lists every public Lab file, source ID, claim ID, and anchor ID. The two JSON Schemas describe the JSONL rows. The validator checks referential integrity, enum values, duplicate IDs, exact-file hashes, and internal Markdown links without using the network.

Null hash means exact bytes were not acquired. GitHub blob SHA uses Git's object encoding and is not a SHA-256 of the visible file; do not substitute it for the source sha256 field. Dates include a basis in the source record or nearby notes.
