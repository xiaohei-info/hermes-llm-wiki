# AGENTS.md

This repository is a methodology and skill kit, not an application runtime.

## Read order

1. `README.md`
2. `SOUL.md`
3. `MEMORY.md`
4. `docs/implementation-guide.md`
5. `skills/README.md`

## Surface map

- `README.md` — public OSS landing page
- `SOUL.md` — compressed runtime principles
- `MEMORY.md` — durable-memory boundaries
- `docs/` — doctrine, methodology, rules, adoption guidance
- `skills/` — reusable operational skill files
- `templates/` — `_wiki` skeleton, page templates, cron prompts
- `examples/` — worked examples and expected artifacts

## Routing guidance

Use:
- `skills/karpathy-llm-wiki-obsidian/SKILL.md` for methodology/setup work
- `skills/obsidian-inbox-to-wiki-ingest/SKILL.md` for compilation work
- `skills/obsidian-wiki-lint-triage/SKILL.md` for audit/maintenance work

## Important boundaries

- Do not assume any machine-specific vault path.
- Do not treat raw `Inbox/` notes as compiled `_wiki/` pages.
- Do not mass-create pages for completeness.
- Do not silently repair `_wiki/` during audit-only lint.
- Prefer linking to canonical docs instead of duplicating instructions here.
