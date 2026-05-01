# Ingest Rules

## Default ingest sequence

1. read the raw source note fully
2. identify exact `source_path`
3. check whether a compiled source page already exists
4. create or update one `_wiki/sources/...` page
5. decide whether downstream pages need updates
6. update only what is justified
7. update `index.md`
8. append to `log.md`
9. re-read changed pages

## Non-negotiable rules

- Start durable ingest with a `sources/` page.
- Preserve provenance and traceability.
- Prefer canonical updates over duplicate page creation.
- Separate source-grounded facts from synthesis and open questions.
- Keep downstream updates selective.

## Source-only ingest is valid

Stop at `sources/` when:
- the source is low-density
- the topic is unstable
- more sources are needed before abstraction
- the right canonical downstream home does not yet exist

If you stop at `sources/` only, explicitly record:
- candidate concepts
- candidate entities
- open questions
- why source-only was sufficient for now

## Anti-patterns

- copying raw notes directly into `_wiki/`
- creating many pages from a single weak source
- skipping `index.md` or `log.md`
- mixing unsupported inference into source facts
- creating a second source page for the same note when `source_path` already matches
