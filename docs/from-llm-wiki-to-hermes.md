# From Karpathy's LLM Wiki to a Hermes Workflow

Chinese mirror: [from-llm-wiki-to-hermes.zh-CN.md](from-llm-wiki-to-hermes.zh-CN.md)

This document explains the distinctive translation layer in `hermes-llm-wiki`:

- the original idea comes from Andrej Karpathy's **LLM Wiki** gist
- this repository turns that idea into an explicit Hermes/Obsidian operating model
- the value is not just the concept, but the operational discipline required to make it usable in practice

## Original source

Karpathy's original gist:

- Gist: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Raw: <https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw>

The original pattern has three layers:

1. raw sources
2. an LLM-maintained wiki
3. a schema/rules layer that keeps the wiki maintainer disciplined

And three core operations:

- ingest
- query
- lint

That is the conceptual starting point.

## What this repository adds

`hermes-llm-wiki` is not just a summary of the original gist. It answers a more practical question:

> If you actually want a Hermes-style agent to run this pattern inside an Obsidian vault, what should the folder boundaries, operator rules, page types, and maintenance loops look like?

This repository's answer is a constrained operating model.

## 1. Mapping the three-layer pattern into Hermes + Obsidian

### Karpathy layer -> Hermes mapping

| Original pattern | Hermes/Obsidian translation |
|---|---|
| Raw sources | `Inbox/` as low-friction intake space |
| LLM-maintained wiki | `_wiki/` as compiled knowledge layer |
| Schema/rules | `skills/`, `docs/`, `templates/`, `AGENTS.md`, `SOUL.md`, `MEMORY.md` |

This mapping is one of the main features of the repo.

### Why `Inbox/` matters

The raw side needs a place that tolerates mess:

- clipped articles
- temporary notes
- research fragments
- unresolved questions
- draft analysis
- design notes

So the model here is:

- `Inbox/` optimizes for **capture and preservation**
- `_wiki/` optimizes for **structure, reuse, and maintenance**

That boundary is deliberate. It prevents premature structuring and keeps the compiled layer from becoming a raw archive.

## 2. Turning "the wiki" into a concrete compiled layer

The original gist describes a persistent wiki. This repo makes that operational by giving the compiled layer a minimal but opinionated structure:

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

This is important for two reasons:

1. it gives the agent stable places to file knowledge
2. it keeps the wiki legible without requiring a heavy retrieval stack

### Why `index.md` and `log.md` are first-class

This repo takes `index.md` and `log.md` seriously as operating surfaces, not decorative files.

- `index.md` is the navigation map the agent should read first
- `log.md` is the append-only chronology of ingest, lint, and maintenance

That decision comes directly from trying to make the pattern maintainable in real vaults.

## 3. Making ingest concrete instead of vague

In many casual discussions of LLM wikis, ingest sounds like "read a thing and summarize it."

This repo makes a stronger claim:

> A valid ingest is a compilation action, not a summary action.

A real ingest should usually do all of these:

1. read the raw note
2. create or update a `sources/` page
3. decide whether downstream canonical pages must change
4. update `index.md`
5. append to `log.md`
6. expose tensions, gaps, and next questions

One source may legitimately touch multiple pages.

This is one of the most distinctive practical translations from the original idea into an executable workflow.

## 4. Explicit page-type gates

The original gist leaves plenty of freedom about page layout. This repo intentionally narrows that freedom.

It distinguishes:

- `sources/` for single-source compiled pages
- `concepts/` for recurring abstractions
- `entities/` for durable people/orgs/projects/products/protocols
- `questions/` for reusable, recurring questions
- `syntheses/` for multi-source integrated views
- `comparisons/` for structured side-by-side reasoning

The point is not taxonomy for its own sake.

The point is to stop the wiki from collapsing into:

- raw dumps
- duplicate pages
- ungrounded syntheses
- arbitrary page creation driven by momentary chat context

## 5. Wiki-first query posture

Another distinctive design choice is that this repo does **not** treat raw sources as the default answer surface.

Instead:

1. start at `index.md`
2. read the most relevant compiled pages
3. answer from `_wiki/` first
4. only revisit raw `Inbox/` material when the compiled layer lacks enough evidence or detail

This matters because it turns the wiki into a compounding artifact instead of a decorative cache.

## 6. Selective writeback instead of summary spam

The original gist strongly suggests that good answers should be filed back into the wiki.

This repo keeps that spirit, but adds a stricter gate:

Only write back when the result is likely to have future reuse value.

Typical writeback targets:

- a recurring question
- a durable synthesis
- a material update to a canonical concept/entity page
- a structured comparison that will matter again

This keeps the system from turning chat history into noisy wiki growth.

## 7. Lint as knowledge-health maintenance

This repository interprets lint as:

- duplicate detection
- orphan detection
- stale-page detection
- missing high-value page detection
- backlog surfacing from `Inbox/`
- navigation health review

Importantly, lint defaults to **audit-only**.

That is another practical translation choice. It reflects the idea that maintenance should be active and regular, but not silently destructive.

## 8. Human/Hermes split

The original LLM Wiki pattern implies division of labor. This repo makes it explicit.

### Human responsibilities

- decide what matters
- choose research direction
- decide which questions deserve priority
- make final calls on key conclusions

### Hermes responsibilities

- read material
- extract structure
- update multiple pages coherently
- maintain navigation and chronology
- expose contradictions, gaps, and backlog
- convert durable answers into reusable pages

This split is a core feature of the repo because it prevents both over-automation and under-use of the agent.

## 9. Structure before automation

The repo also takes a strong implementation stance:

> First define boundaries and operating rules. Then trial the workflow on a small batch. Only later add stronger automation.

So the recommended sequence is:

1. define roots and page types
2. test small-scale ingest
3. establish wiki-first query and audit-only lint
4. only later add scheduled prompts or stronger tooling

This is why the repo ships prompt templates and validation, but does not start by pretending to be a full automation product.

## 10. Why this design is distinctive

Many people can repeat the phrase "LLM Wiki."

The distinctive contribution here is making it operational in a way that is:

- light enough for real note workflows
- explicit enough for another agent to adopt
- structured enough to compound over time
- constrained enough to resist wiki sprawl

In short:

> Karpathy supplied the original conceptual pattern. `hermes-llm-wiki` packages one disciplined way to actually run that pattern inside a Hermes-style agent workflow with Obsidian as the working surface.
