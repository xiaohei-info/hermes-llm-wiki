# Implementation Guide

This guide explains how to land `hermes-llm-wiki` into a host agent stack.

## 1. Package layers

### Public landing
- `README.md`

### Agent routing
- `AGENTS.md`

### Runtime principles
- `SOUL.md`

### Memory boundaries
- `MEMORY.md`

### Full doctrine and rules
- `docs/`

### Reusable skills
- `skills/`

### Reusable scaffolds and prompts
- `templates/`

### Worked examples
- `examples/`

## 2. Rollout order

Keep rollout order separate from package structure.

### Phase 1 — Minimum adoption
- choose `INBOX_ROOT`
- choose `WIKI_ROOT`
- scaffold `_wiki/`
- adopt one manual ingest workflow

### Phase 2 — Standard adoption
- load all three skills
- use page templates as references
- introduce audit-only lint

### Phase 3 — Full adoption
- add recurring prompt templates to your scheduler
- monitor backlog, duplication, and stale-page drift
- refine language/output conventions

## 3. Adoption profiles

### Minimum
Use if you want the methodology without scheduler integration.

Install:
- docs
- `_wiki` skeleton templates
- one manual ingest flow

### Standard
Use if you want repeatable curation.

Install:
- docs
- `_wiki` templates
- page templates
- all three skills
- audit-only lint flow

### Full
Use if your host agent supports scheduling and reusable skill loading.

Install:
- everything in Standard
- triage/lint/digest recurring prompts
- host-specific routing in your scheduler/profile system

## 4. Capability-based landing algorithm

### If the host supports skill loading
- load the `skills/` surfaces directly
- link runtime/profile docs to `SOUL.md` and `MEMORY.md`

### If the host supports only prompt files
- translate `SOUL.md` into the runtime prompt layer
- keep `MEMORY.md` as policy, not repeated prompt text
- copy the skill procedures into your host's reusable instruction system

### If the host supports scheduling
- start with advisory prompts only
- do not enable mass-write jobs by default

### If the host has no scheduler
- run triage/lint prompts manually as periodic maintenance

## 5. Host-neutral install sequence

1. Configure roots and language policy.
2. Create `_wiki/` skeleton.
3. Load the methodology skill.
4. Test one manual ingest.
5. Verify index/log discipline.
6. Run one audit-only lint pass.
7. Add recurring prompts only after the manual workflow feels stable.

## 6. Smoke test

A successful adoption should be able to do all of these:

1. read one raw note from `Inbox/`
2. create/update exactly one `_wiki/sources/...` page
3. selectively update a downstream page only if justified
4. add a curated entry to `index.md`
5. append a dated line to `log.md`
6. run an audit-only lint pass without silent rewrites
7. produce a concise backlog recommendation

## 7. Common failure modes

- treating `Inbox/` as if it were already a wiki
- creating too many pages too early
- skipping provenance fields
- forgetting `index.md` and `log.md`
- writing audit tools that silently mutate the compiled layer
- overfitting the workflow to one local machine or one vault layout
