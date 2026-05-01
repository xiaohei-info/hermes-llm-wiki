# MEMORY.md

This repository distinguishes durable memory from doctrine, procedures, and transient task state.

## What belongs in memory

Only stable facts that help future execution without re-reading the whole repo, for example:
- vault root chosen by the adopter
- whether `Inbox/` and `_wiki/` roots are customized
- chosen output language mode
- whether a legacy `Wiki/` tree coexists with `_wiki/`
- stable naming conventions adopted by the workspace

## What does NOT belong in memory

Do not store these as durable memory:
- the full operating doctrine
- long procedural instructions from skills/docs
- one-off ingest results
- temporary backlog items
- full wiki page contents
- transient maintenance findings
- current-task TODO state

## Where other things belong instead

- Long-form rationale -> `docs/`
- Repeatable procedures -> `skills/`
- Recurring prompts -> `templates/cron/`
- Runtime principles -> `SOUL.md`
- Session work logs -> host session history / local notes

## Why this matters

If doctrine leaks into memory, memory becomes noisy and starts behaving like a second prompt layer. Keep memory factual and compact.
