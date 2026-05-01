# Methodology

## Core workflow

The operating loop is:

1. **Ingest** raw source material from `Inbox/`
2. **Compile** it into `_wiki/sources/`
3. **Promote selectively** into concepts/entities/questions/syntheses/comparisons
4. **Maintain navigation** with `index.md`
5. **Maintain chronology** with `log.md`
6. **Query wiki-first**
7. **Lint periodically** for structural health

## Key idea: compilation, not dumping

The goal is not to copy raw notes into `_wiki/`.

A good compiled page should:
- reduce future reading burden
- preserve provenance
- link to the right canonical objects
- be durable enough to support future answers

## Query posture

When answering a question:
1. inspect `_wiki/index.md`
2. read the most relevant compiled pages
3. answer from `_wiki/` first
4. revisit raw `Inbox/` material only if the compiled layer lacks evidence or detail
5. write back only if the answer is likely to matter again

## Writeback gate

Write back a result when it:
- resolves a recurring question
- materially improves a canonical concept/entity page
- creates a durable synthesis from multiple sources
- prevents likely future repeated work

Do not write back one-off answers just to make the wiki larger.
