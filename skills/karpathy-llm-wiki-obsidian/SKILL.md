---
name: karpathy-llm-wiki-obsidian
description: Set up or document a Karpathy-style LLM wiki workflow in Obsidian when raw material should live in Inbox and compiled knowledge should live in a dedicated wiki root.
version: 1.0.0
author: Hermes contributors
license: MIT
metadata:
  tags: [obsidian, llm-wiki, karpathy, knowledge-base, methodology]
  related_skills: [obsidian-inbox-to-wiki-ingest, obsidian-wiki-lint-triage]
---

# Karpathy LLM Wiki in Obsidian

## Overview

Use this skill when the goal is to define or operationalize a persistent compiled wiki workflow in Obsidian.

Core pattern:
- `INBOX_ROOT` (default `Inbox/`) = raw/source space
- `WIKI_ROOT` (default `_wiki/`) = compiled/maintained knowledge layer

The goal is not to build a generic RAG system. The goal is to define a maintenance workflow that turns raw material into a durable wiki.

## When to Use

Use when:
- the user wants Karpathy-style LLM wiki methodology operationalized
- the user wants clear raw-vs-compiled separation
- the workflow rules should be documented before heavy automation
- the host should maintain a persistent wiki instead of only generating one-off answers

Do not use when:
- the task is only to ingest one note
- the task is only to lint an existing compiled wiki
- the source/compiled roots are still undefined and require a broader system design first

## Required mental model

Keep three layers distinct:
1. source space
2. compiled wiki
3. schema/workflow rules

Do not collapse raw notes and compiled pages into the same folder or page type.

## Recommended process

1. Confirm `INBOX_ROOT`, `WIKI_ROOT`, and optional `DESIGN_NOTES_ROOT`.
2. Inspect the existing vault structure.
3. Write the methodology/design note before heavy scaffolding.
4. Define page-type templates and workflow checklists.
5. Only then scaffold the minimal compiled wiki structure.

## Minimal wiki structure

```text
_wiki/
  index.md
  log.md
  overview.md
  sources/
  concepts/
  entities/
  questions/
  syntheses/
  comparisons/
```

## Operational rules implied by this methodology

- use one page for one main durable object
- start durable source ingestion in `sources/`
- answer wiki-first
- write back selectively
- prefer updating canonical pages over creating duplicates
- keep `index.md` curated and `log.md` append-only

## Pitfalls

- writing methodology docs directly into the compiled wiki too early
- treating the compiled wiki as an archive dump
- starting with embeddings/automation before the structure is stable
- confusing chat answers with durable pages

## Verification

Before claiming success, confirm:
- source and compiled roots are explicit
- the methodology clearly states the raw/compiled split
- the minimal page types are defined
- routing to ingest and lint workflows is explicit
