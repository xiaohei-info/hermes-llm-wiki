# Hermes Integration

This repo was designed with Hermes-style reusable skills in mind, but the methodology is portable.

## Recommended mapping

- runtime/profile surface -> `SOUL.md`
- durable memory policy -> `MEMORY.md`
- reusable task procedures -> `skills/`
- longer rationale -> `docs/`
- recurring review prompts -> `templates/cron/`

## Suggested usage pattern

1. Load `karpathy-llm-wiki-obsidian` when designing or setting up the workflow.
2. Load `obsidian-inbox-to-wiki-ingest` for real curation work.
3. Load `obsidian-wiki-lint-triage` for periodic structural health review.
4. Keep cron jobs advisory-first.

## Hermes-specific advice

- Use file tools for vault reads/writes.
- Keep scheduler prompts concise.
- Prefer model-efficient triage/lint jobs over heavy autonomous writeback.
- Do not treat durable memory as a place to dump doctrine text.
