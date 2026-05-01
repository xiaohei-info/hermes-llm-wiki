# Example source-only ingest

Use source-only ingest when the material is worth preserving, but not yet strong enough to justify stable abstraction.

## Input
- a useful but narrow memo
- a source with only one durable claim
- a topic likely to evolve after more evidence arrives

## Expected output
- create or update exactly one `_wiki/sources/...` page
- record candidate concepts/entities/questions inside that source page
- update `index.md`
- append to `log.md`
- do **not** create concept/entity/synthesis pages yet

## Example log line

```md
2026-05-01 — ingested [[sources/2026-05-01-narrow-memo|Narrow memo]] from Inbox/narrow-memo.md; updated none beyond sources/
```

## Why this is valid

Source-only ingest prevents premature ontology growth while still preserving the material in compiled form.
