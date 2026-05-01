---
name: obsidian-wiki-lint-triage
description: Review the health of a compiled wiki root, surface priority fixes, and triage backlog candidates without defaulting to silent writeback.
version: 1.0.0
author: Hermes contributors
license: MIT
metadata:
  tags: [obsidian, llm-wiki, lint, maintenance, triage, knowledge-base]
  related_skills: [karpathy-llm-wiki-obsidian, obsidian-inbox-to-wiki-ingest]
---

# Obsidian Wiki Lint Triage

## Overview

Use this skill when `WIKI_ROOT` exists and the host should inspect structural health, report problems, and suggest repair priorities.

This is an execution skill, not a methodology skill.

## Default mode

Default to **audit-only**.

Read scope:
- all of `WIKI_ROOT`
- relevant raw candidates under `INBOX_ROOT`

Default write scope:
- none

Unless repair mode was explicitly requested, lint should report rather than rewrite.

## What lint should check

1. navigation health
2. duplicates or synonyms
3. orphans or weakly linked pages
4. stale or contradicted pages
5. missing high-value canonical pages
6. backlog candidates still stuck in `INBOX_ROOT`
7. split-root coexistence with an optional legacy wiki root

## Priority levels

- **P1** — broken navigation, stale core pages, duplicate sprawl harming retrieval
- **P2** — orphans, missing important links, stale questions/syntheses
- **P3** — naming cleanup and possible future pages

## Output structure

A good lint pass should produce:
1. healthy summary
2. grouped findings
3. explicit P1 recommendations
4. backlog candidates
5. optional next-ingest recommendation

## Anti-patterns

- silently repairing pages during audit-only mode
- focusing on formatting while ignoring knowledge quality
- generating huge raw dumps instead of a concise triage report

## Verification

Before claiming lint is complete, confirm:
- `index.md` was inspected
- duplicates/orphans were judged from content, not filenames alone
- stale pages were checked against newer evidence
- backlog candidates are grounded in real source inspection
- no files were mutated unless repair mode was explicitly requested
