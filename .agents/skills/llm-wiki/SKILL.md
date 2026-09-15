---
name: llm-wiki
description: Maintain this Obsidian knowledge base by ingesting raw sources, answering evidence-grounded questions, filing durable syntheses, analyzing collected Riot match data, or linting wiki health. Use for work on the LLM wiki; do not use for unrelated Markdown editing.
---

# LLM Wiki

Operate the current vault as a persistent, cumulative wiki. Follow the ownership, structure, citation, naming, index, and log rules in the repository-root `AGENTS.md`.

Before creating or substantially updating a content page, read [references/page-formats.md](references/page-formats.md).

## Route the request

- **Ingest** when the user asks to add, process, summarize, or integrate material in `raw/`.
- **Query** when the user asks a question whose answer should come from this knowledge base.
- **File a synthesis** when the user requests a durable analysis, comparison, or connection page.
- **Lint** when the user asks to audit, clean, reconcile, or health-check the wiki.
- **Match analysis** when the user asks to aggregate or compare collected Riot ranked-match results.

## Match analysis resources

For Riot ranked-match analysis, read [the analysis specification](../../../docs/riot-ranked-match-analysis-spec.md) before changing the scripts. Reuse the checked-in tools instead of rewriting the normalization logic:

- `scripts/riot_match_analysis.py` — shared Match-v5/cache loader, deduplication, tier handling, participant normalization, and local Data Dragon name resolution.
- `scripts/riot_ranked_match_analyzer.py` — aggregate champion, item, rune, summoner-spell, performance, duration, and optional matchup reports.
- `scripts/riot_champion_query.py` — champion-specific ally-pair and opponent queries. The default minimum sample is 15 games; opponent results are same-role by default.

Run `--dry-run` first when checking a new input set. Keep `raw/` read-only and write reports to `reports/` or another non-raw output directory. Do not expose PUUIDs, summoner IDs, summoner names, or Riot IDs in generated reports.

## Ingest

1. Identify the requested raw source. If none is named, compare `raw/sources/` with `source_path` values under `wiki/sources/` and select the unprocessed source. Never alter the raw file.
2. Read `wiki/index.md`, then search `wiki/` with `rg` for related entities, concepts, claims, and source summaries.
3. Read the source completely enough to preserve its thesis, evidence, limitations, and context. Inspect locally referenced images when they affect meaning.
4. Create one source-summary page. Update or create all materially affected entity, concept, and synthesis pages; prefer integrating into an existing page over creating a synonym or duplicate.
5. Make every important claim traceable. Mark inference, uncertainty, and contradictions explicitly. Preserve competing claims until the evidence resolves them.
6. Reconcile cross-links, update `wiki/overview.md` when the high-level picture changes, update `wiki/index.md`, and append an ingest entry to `wiki/log.md`.
7. Report the files changed, the main additions, contradictions, and remaining questions.

Process one source at a time by default. Batch only when the user requests it or the inputs are a single coherent set.

## Query and synthesis

1. Read `wiki/index.md` first and select the smallest relevant page set.
2. Search and read relevant wiki pages. Check raw sources when a claim needs verification, the wiki lacks detail, or pages conflict.
3. Answer with links to the wiki pages and underlying source summaries used. Separate sourced conclusions from inference and state evidence gaps.
4. File the answer in `wiki/syntheses/` when the user requests a page or the requested work is explicitly a durable wiki update. Then update the index and append a query entry to the log.

Do not silently add remembered or web-derived facts. If outside research would help, propose the missing source; ingest it only when the user places or authorizes it as a raw source.

## Lint

1. Inventory generated pages and compare them with `wiki/index.md`.
2. Check broken or ambiguous Wikilinks, orphan pages, duplicate concepts, missing reciprocal links, invalid frontmatter, missing source traceability, stale claims, and unresolved contradictions.
3. Fix safe structural and consistency issues in `wiki/`. Do not change `raw/`.
4. Append a lint entry to `wiki/log.md` listing checks, fixes, and unresolved gaps.
5. Report the wiki's health and recommend the highest-value next sources or questions.

For a targeted lint request, limit edits and reporting to the requested scope.
