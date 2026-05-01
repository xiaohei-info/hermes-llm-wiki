# Generic Agent Integration

You do not need Hermes specifically to use this methodology.

## Minimal requirements

A host agent should ideally support:
- reading/writing Markdown files
- a reusable instruction/skill surface
- optional scheduling for recurring prompts
- a place for compact runtime guidance

## Mapping strategy

### If you have a prompt/profile system
- place the compressed principles from `SOUL.md` there

### If you have reusable task recipes
- convert `skills/` into your host's recipe/skill format

### If you have durable memory
- enforce the boundaries from `MEMORY.md`

### If you have scheduling
- wire only advisory prompts first

## Important caution

Do not force host-specific taxonomy back into the core methodology. Keep the central rules portable and move host details to the edge.
