# Page formats

Use these as starting shapes. Keep only sections that carry real information, and add domain-specific sections when they improve the page.

## Source summary

```markdown
---
title: Source title
type: source
status: active
source_path: raw/sources/original-file.ext
source_url: https://example.com/original
source_date: YYYY-MM-DD
ingested: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - stable-topic
---

# Source title

## Summary

An evidence-grounded account of the source's thesis and scope.

## Key claims

- Claim, with relevant qualification or evidence.

## Evidence and limitations

- Evidence used by the source and limits on what it establishes.

## Connections

- [[wiki/concepts/example|Example]] — why this source matters to the page.

## Open questions

- Unresolved question raised by the source.

## Source

- Original: [[raw/sources/original-file.ext|original-file.ext]]
```

Omit `source_url` or `source_date` when unknown. Never invent them.

## Entity or concept

```markdown
---
title: Page title
type: concept
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - "[[wiki/sources/src-yyyy-mm-dd-example]]"
tags:
  - stable-topic
---

# Page title

## Summary

Current evidence-grounded understanding.

## Key points

- A sourced point with a source-summary Wikilink.

## Relationships

- [[wiki/entities/related-page|Related page]] — the relationship and why it matters.

## Contradictions and uncertainty

Document meaningful disputes, confidence limits, and superseded claims.

## Open questions

- A question that would materially improve the page.

## Sources

- [[wiki/sources/src-yyyy-mm-dd-example|Source title]] — what it supports.
```

Set `type: entity` for an entity page.

## Synthesis

```markdown
---
title: Synthesis title
type: synthesis
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - "[[wiki/sources/src-yyyy-mm-dd-first]]"
  - "[[wiki/sources/src-yyyy-mm-dd-second]]"
tags:
  - stable-topic
---

# Synthesis title

## Question

The question or comparison this page addresses.

## Synthesis

The answer, separating source-backed findings from interpretation.

## Evidence

| Finding | Support | Limits |
| --- | --- | --- |
| Finding | [[wiki/sources/src-yyyy-mm-dd-first|First source]] | Qualification |

## Contradictions and uncertainty

Preserve competing claims and explain what remains unresolved.

## Implications

Clearly label deductions that go beyond explicit source claims.

## Open questions

- A high-value next question or missing source.

## Sources

- [[wiki/sources/src-yyyy-mm-dd-first|First source]]
- [[wiki/sources/src-yyyy-mm-dd-second|Second source]]
```

## Index entry

Place every generated content page exactly once under its type in `wiki/index.md`:

```markdown
- [[wiki/concepts/page-name|Page title]] — One sentence describing the page's scope.
```

## Log entry

Append entries at the bottom of `wiki/log.md`:

```markdown
## [YYYY-MM-DD] ingest | Source title

- Inputs: `raw/sources/original-file.ext`
- Changes: [[wiki/sources/src-yyyy-mm-dd-example|Source title]], [[wiki/concepts/example|Example]]
- Unresolved: None, or a concise list of contradictions and evidence gaps.
```
