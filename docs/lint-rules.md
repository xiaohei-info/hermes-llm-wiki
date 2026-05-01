# Lint Rules

Lint should optimize for knowledge health, not surface prettiness.

## Default mode

Default to **audit-only**.

Audit-only lint should:
- inspect `_wiki/`
- inspect relevant `Inbox/` backlog candidates
- report findings and priorities
- avoid mutating wiki pages unless repair mode was explicitly requested

## Main checks

1. navigation health
2. duplicate/synonym pages
3. orphan or weakly linked pages
4. stale or contradicted core pages
5. missing high-value canonical pages
6. Inbox backlog worthy of compilation
7. split-root coexistence with a legacy `Wiki/`

## Priority levels

### P1
- broken navigation
- duplicate sprawl harming retrieval
- stale core pages
- high-value compiled knowledge not findable

### P2
- orphan pages
- missing important links
- stale question/synthesis pages

### P3
- naming cleanup
- possible new pages
- cosmetic structure improvements

## Output expectations

A good lint report should include:
- one-line healthy summary
- grouped findings
- explicit P1 actions
- short backlog recommendations
- whether any writeback was intentionally skipped

## Anti-patterns

- large refactors during lint
- silent repairs during audit-only mode
- focusing on formatting while ignoring knowledge drift
- promoting every backlog item just because it exists
