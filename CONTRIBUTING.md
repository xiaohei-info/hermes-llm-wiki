# Contributing

Thanks for your interest in `hermes-llm-wiki`.

## Contribution principles

- Keep the package light.
- Prefer portable methodology over host-specific assumptions.
- Prefer updating existing docs/skills over adding parallel surfaces.
- Do not turn this repo into a general-purpose RAG or automation framework.
- Preserve the distinction between:
  - doctrine
  - runtime guidance
  - skills
  - memory boundaries
  - recurring prompt templates

## Good contributions

- improving clarity of skill trigger conditions
- strengthening provenance rules
- tightening ingest/lint anti-patterns
- adding portable examples
- improving host-neutral adoption guidance
- fixing accidental local/private assumptions

## Changes that need extra care

Please be conservative with changes that:
- introduce runtime dependencies
- imply automatic mass writeback
- add plugin-specific or vendor-specific assumptions to core docs
- duplicate the same rule across multiple files
- expand the public surface without a clear adoption need

## Suggested workflow

1. Open an issue or draft note for non-trivial scope changes.
2. Keep PRs focused.
3. Explain which surface you are changing:
   - README
   - docs
   - skills
   - templates
   - examples
4. State how the change improves adoptability or execution quality.

## Validation checklist

Before submitting, verify:
- README still reads like an OSS landing page, not a system prompt.
- `AGENTS.md` stays thin.
- `SOUL.md` stays compressed.
- `MEMORY.md` only defines durable-memory boundaries.
- skills remain reusable and not session-specific.
- templates stay generic and portable.
