---
title: Wiki Log
type: log
---

# Wiki Log

This file is append-only. Newest entries are appended at the end.

## [2026-09-14] maintenance | Initial wiki scaffold

- Inputs: Karpathy's LLM Wiki pattern and the local Obsidian vault.
- Changes: Created the raw-source layer, generated-wiki layer, project schema, and repository-scoped Codex skill.
- Unresolved: No domain or source collection has been added yet.

## [2026-09-14] ingest | チャンピオンデータセット v16.18.1

- 入力：`raw/sources/champion.json.md`
- 変更：[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|原典要約]]、[[wiki/concepts/champion-dataset-schema|データスキーマ]]、[[wiki/syntheses/champion-roster-profile-v16-18-1|全体概況]]、[[wiki/overview|概要]]、[[wiki/index|索引]]
- 未解決：正式な配布元とフィールド定義、一律 `0` の値の意味、個別チャンピオンページを展開する粒度、参照画像の不足。

## [2026-09-14] maintenance | 個別チャンピオンページと画像を追加

- 入力：`raw/sources/champion.json.md`、Data Dragon CDNのversion `16.18.1` チャンピオン画像。
- 変更：`wiki/entities/` に173件の個別ページを作成し、[[wiki/index#エンティティ|索引]]へ登録した。`raw/assets/champions/` に173件のPNG画像を保存し、各ページへ埋め込んだ。[[wiki/overview|概要]]、[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|原典要約]]、[[wiki/syntheses/champion-roster-profile-v16-18-1|全体概況]]を更新した。
- 未解決：正式な配布元とフィールド定義、一律 `0` の値の意味。

## [2026-09-14] ingest | Data Dragon 配布アーカイブ v16.18.1

- 入力：`raw/sources/dragontail-16.18.1.tgz`
- 変更：[[wiki/sources/src-2026-09-14-dragontail-16-18-1|原典要約]]を作成し、[[wiki/concepts/champion-dataset-schema|データスキーマ]]、[[wiki/syntheses/champion-roster-profile-v16-18-1|全体概況]]、[[wiki/overview|概要]]、[[wiki/index|索引]]を更新した。173件の個別チャンピオンページへ、日本語のパッシブ1件とQ/W/E/Rの4スキル説明を統合した。
- 未解決：正式な配布元URLと公開日時、tooltipの数値プレースホルダーの仕様、アイテム・ルーン・TFT等の非チャンピオンデータを展開する粒度。

## [2026-09-14] ingest | アイテム・ルーン・サモナースペル個別ページ

- 入力：`raw/sources/dragontail-16.18.1.tgz` の `data/ja_JP/item.json`、`runesReforged.json`、`summoner.json`
- 変更：[[wiki/concepts/game-data-catalog|ゲームデータ個別ページのカタログ]]を作成し、アイテム868件、ルーン62件、サモナースペル34件を `wiki/entities/items/`、`wiki/entities/runes/`、`wiki/entities/spells/` に分担して作成した。[[wiki/sources/src-2026-09-14-dragontail-16-18-1|原典要約]]、[[wiki/overview|概要]]、[[wiki/index|索引]]を更新した。
- 未解決：`item-modifiers.json`、他ロケール、TFT等の周辺データを展開する粒度、ツールチップ内プレースホルダーの仕様。
