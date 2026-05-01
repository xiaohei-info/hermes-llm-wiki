---
name: obsidian-inbox-to-wiki-ingest
description: Compile one or more raw Obsidian Inbox notes into a compiled wiki root using controlled source pages, selective downstream updates, and mandatory navigation maintenance.
version: 1.0.0
author: Hermes contributors
license: MIT
metadata:
  tags: [obsidian, llm-wiki, ingest, inbox, knowledge-base]
  related_skills: [karpathy-llm-wiki-obsidian, obsidian-wiki-lint-triage]
---

# Obsidian Inbox to Wiki Ingest

## Overview

Use this skill when raw material already exists in `INBOX_ROOT` and should be compiled into `WIKI_ROOT`.

This is an execution skill, not a methodology skill.

## When to Use

Use when:
- a note, article, transcript, or memo in `INBOX_ROOT` deserves durable compilation
- the host should create or update a source page
- the host should selectively update concepts, entities, questions, syntheses, or comparisons

Do not use when:
- the task is only to explain the methodology
- the task is only to lint the compiled wiki
- the source has not actually been read

## Preflight

Before writing anything:
1. confirm `VAULT_ROOT`, `INBOX_ROOT`, and `WIKI_ROOT`
2. locate the raw source note
3. inspect related compiled pages
4. decide whether the source is worth compiling now

## Dedup discipline

Before creating a new `sources/` page:
1. capture exact vault-relative `source_path`
2. search existing `WIKI_ROOT/sources/` pages for that `source_path`
3. search canonical identifiers when available
4. update an existing page instead of duplicating it

## What to extract

Extract at least:
- facts
- claims
- concepts
- entities
- tensions or contradictions
- open questions

## Output rules

### Always start with a source page
Each durable source ingest should create or update one canonical `sources/` page.

### Then decide downstream impact
Update downstream pages only when justified:
- `concepts/`
- `entities/`
- `questions/`
- `syntheses/`
- `comparisons/`

### Maintain navigation and chronology
A valid ingest also updates:
- `index.md`
- `log.md`

## Preferred behavior

- prefer updating canonical pages over creating new ones
- separate source-grounded content from synthesis and unresolved questions
- preserve provenance
- keep compiled output selective and navigable

## Verification

Before claiming completion, confirm:
- the raw note was actually read
- dedup checks were performed
- the source page exists or was updated
- downstream changes were selective and justified
- `index.md` and `log.md` were maintained
- changed pages were re-read
