# Page Types

Each page type should represent one main durable object.

## Metadata contract

The goal is not schema-heavy rigidity. The goal is enough consistency that different agents or operators can maintain the same wiki without losing provenance.

### Common recommended fields

| Field | Applies to | Required | Purpose |
|---|---|---:|---|
| `type` | all page types | yes | declares the canonical page class |
| `created` | all non-generated pages | yes | first creation date |
| `updated` | all non-generated pages | yes | latest meaningful update date |
| `status` | all page types | yes | lightweight lifecycle marker |
| `tags` | all page types | recommended | lightweight grouping only |
| `source_path` | `sources/` | yes | exact vault-relative origin |
| `source_title` | `sources/` | yes | original source note title |
| `source_canonical` | `sources/` | optional | stable URL / DOI / video ID / paper ID |
| `ingested_on` | `sources/` | yes | ingest date |

### Required-vs-optional principle

- Require fields that preserve provenance and chronology.
- Keep other metadata optional unless it clearly improves maintenance.
- Do not turn page frontmatter into a large taxonomy system.

## `sources/`
Use for compiled single-source pages.

Create when:
- a raw source note is worth preserving in compiled form

Do not skip this page type when ingesting durable source material.

Minimum metadata:
- `type: source`
- `source_path`
- `source_title`
- `ingested_on`
- `created`
- `updated`
- `status`

## `concepts/`
Use for recurring ideas, methods, frameworks, distinctions.

Create when:
- the concept is likely to recur
- multiple sources point toward the same durable abstraction
- an existing concept page needs canonical enrichment

Do not create when:
- the phrase is one-off
- the idea has no likely reuse value

## `entities/`
Use for durable people, orgs, projects, products, protocols, or artifacts.

Create when:
- the entity materially matters to multiple future notes or questions

## `questions/`
Use for durable, revisitable questions.

Create when:
- the question is likely to recur
- the answer evolves across multiple sources

## `syntheses/`
Use for multi-source merged views.

Create when:
- a durable thesis requires more than one source
- a stage view or integrated interpretation will save future work

## `comparisons/`
Use for structured side-by-side distinctions.

Create when:
- the decision becomes clearer in a comparison format than in isolated notes

## General rules

- Prefer updating canonical pages over creating duplicates.
- Do not create empty pages “for completeness.”
- A smaller, more stable wiki beats a larger, noisier one.

## Promotion thresholds

Use these as practical gates:

- **Stay source-only** when the material is low-density, unstable, or not yet worth abstraction.
- **Promote to `concepts/`** when the idea is likely to recur across multiple future notes.
- **Promote to `entities/`** when the person/org/project/product is becoming a durable reference point.
- **Promote to `questions/`** when the question is likely to be asked again or evolve over time.
- **Promote to `syntheses/`** when a single-source page is no longer enough to hold the durable answer.
- **Promote to `comparisons/`** when the user benefits more from side-by-side structure than from isolated notes.

When unsure, prefer a stronger `sources/` page first and defer abstraction.

## Naming conventions

Keep naming predictable and boring.

- Prefer human-readable filenames over dense IDs.
- For `sources/`, date prefixes are often useful: `YYYY-MM-DD-title.md`.
- For canonical pages, favor stable titles over clever short names.
- Keep display titles and filenames aligned unless language policy requires otherwise.
- Preserve the original source title in metadata even when the compiled filename is normalized.
