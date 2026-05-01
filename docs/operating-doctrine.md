# Operating Doctrine

## Thesis

A useful knowledge agent should not merely answer questions from raw material. It should help maintain a durable, source-grounded compiled layer that gets better over time.

`hermes-llm-wiki` treats an LLM agent as a wiki curator and compiler. The purpose is not to maximize automatic output volume. The purpose is to maximize reusable knowledge per unit of agent effort.

## The two-layer model

### Source space
`Inbox/` contains raw material:
- clippings
- research notes
- transcripts
- drafts
- design notes
- temporary analysis

This layer is allowed to be messy.

### Compiled layer
`_wiki/` contains durable knowledge:
- canonical source pages
- concepts
- entities
- questions
- syntheses
- comparisons
- navigational pages

This layer should be selective, maintained, and readable.

## Human vs agent responsibilities

### Human
- choose what matters
- decide research direction
- set priorities
- make final judgment on high-level conclusions

### Agent
- read source material fully
- extract facts/claims/concepts/entities/questions
- update canonical pages
- maintain navigation and chronology
- surface gaps, conflicts, and backlog

## Economic model

The system should spend agent effort on:
- selective compilation
- durable writeback
- navigation maintenance
- backlog triage
- structural health checks

It should avoid spending agent effort on:
- repeated re-summarization of the same raw inputs
- speculative page creation
- low-value formatting churn
- unbounded background automation

## Completion standard

A result is not complete when it merely “looks useful.”

A compiled change is complete only when:
- the material is placed in the right page type
- provenance is preserved
- duplicates are avoided
- index/log are updated when appropriate
- the final pages are re-read for coherence

## Default caution

Automation should start narrow:
- manual ingest first
- audit-only lint second
- recurring advisory prompts third
- only later consider more aggressive automation

## What success looks like

A healthy compiled wiki should feel like:
- fewer repeated explanations
- more stable canonical pages
- better retrieval from maintained summaries
- lower friction when returning to a topic weeks later
- gradual compounding rather than growth by page count alone
