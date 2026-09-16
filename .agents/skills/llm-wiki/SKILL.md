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
- `scripts/riot_ranked_match_analyzer.py` — aggregate champion, item, rune, champion-by-rune selection, complete champion rune-set selection, summoner-spell, performance, duration, and optional matchup reports. Champion-by-rune and complete-set rates use the same champion/role participant denominator and remain descriptive rather than causal.
- `scripts/riot_champion_rune_wiki_sync.py` — syncs the three most frequently observed complete rune sets (with selection-time win rates) for the dominant observed role into champion entity pages from one explicitly selected ranked-match `analysis.json`. Run `--dry-run` before `--write` and finish with `--check`; the generated ranking is descriptive, not a recommendation.
- `scripts/riot_champion_query.py` — champion-specific ally-pair and opponent queries. The default minimum sample is 15 games; opponent results are same-role by default.
- `scripts/riot_champion_item_synergy.py` — reusable participant-level champion/role/item co-occurrence analysis, held-vs-not-held win-rate comparison, Data Dragon item-stat group analysis (including critical chance), completed-item core builds, and per-champion reports with observed candidates separated from metadata-only hypotheses. It supports patch filtering, utility-item exclusion, `--status-groups`, and `--build-sizes`. The default minimum sample is 15 games; the result is descriptive rather than causal.
- `scripts/riot_champion_build_wiki_sync.py` — syncs a mechanically ranked compact block from one explicitly selected item/build `analysis.json` into champion entity pages while retaining full detail under `reports/`. Its rankings are report candidates, not qualitative curation; do not invoke it as automatic lint promotion. When explicitly using it, run `--dry-run` first, use `--write` only for the intended snapshot, and finish with `--check`; do not edit generated blocks by hand.
- `scripts/riot_champion_matchup_wiki_sync.py` — aggregates ally-combo and same-role opponent candidates, and can sync up to three high-win-rate combos and three low-target-win-rate counter-pick examples per role from an existing `analysis.json` with `--analysis`. Its results are descriptive; use `--dry-run` before `--write` and do not treat the generated block as causal curation.
- `scripts/riot_ranked_tier_analyzer.py` — compares observed-rank-tier samples using the shared loader, with tier, role, champion, keystone, and spell-pair outputs. `observed_tier` is the collection-time discovery tier, not every participant's match-time rank; results are descriptive and cross-tier duplicate matches are retained in quality metadata.
- `scripts/riot_match_timeline_collector.py` — retrieves Timeline data for existing Match-v5 records, deduplicates match IDs, reuses a sanitized local cache, and writes analysis-ready JSONL without PUUIDs or other participant identifiers. It writes under `reports/` and supports `--dry-run`, filters, `--limit`, and `--refresh`.

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

1. Inventory generated pages and compare them with `wiki/index.md`. Also inventory in-scope report families from the filesystem under `reports/`. Treat a run as complete only when its manifest and declared outputs exist, then compare complete runs with existing synthesis pages and prior log entries to find material findings that have not been curated into the wiki.
2. Check broken or ambiguous Wikilinks, orphan pages, duplicate concepts, missing reciprocal links, invalid frontmatter, missing source traceability, stale claims, and unresolved contradictions.
3. Review candidate report findings against the report's manifest, quality information, machine-readable result, and underlying raw source. Promote a finding only when its method, conditions, denominator, quality, limitations, and raw-source provenance are verifiable; it is non-duplicative and reusable; and it adds more than a newer snapshot, extreme or favorable value, or metadata-only hypothesis.
4. Integrate eligible findings into the closest existing page in `wiki/syntheses/`, creating a synthesis only when no suitable page exists. Separate observation from interpretation and retain material null results, counterevidence, contradictions, and limitations. Put only a compact summary and synthesis link on an entity page when that improves navigation.
5. Treat `reports/` as derived artifacts, not sources. Record the selected run path and filters where useful, but cite the corresponding source-summary page backed by `raw/`. If source summaries, reproducibility details, or quality evidence are missing, leave the finding unpromoted and record the gap.
6. Fix safe structural and consistency issues in `wiki/`. Do not change `raw/`. Reconcile `wiki/index.md` and `wiki/overview.md` when report curation changes them.
7. Append a lint entry to `wiki/log.md` listing checks, fixes, reports reviewed, findings promoted, important candidates declined with reasons, and unresolved gaps.
8. Report the wiki's health and recommend the highest-value next sources or questions.

Running `scripts/lint.py` alone does not complete report curation; qualitative selection and evidence review are part of the agent's lint workflow. Rankings or generated blocks from report and sync scripts do not count as curated findings by themselves.

For a targeted lint request, limit edits and reporting to the requested scope.
