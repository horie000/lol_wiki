---
title: ゲームデータ個別ページのカタログ
type: concept
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
tags:
  - game-data
  - data-catalog
  - league-of-legends
---

# ゲームデータ個別ページのカタログ

## 概要

Data Dragon version `16.18.1` の日本語データを、原典レコード単位で検索できる個別ページへ整理したカタログである。チャンピオン、アイテム、ルーン、サモナースペルをそれぞれ専用ディレクトリへ分け、IDやキーを保持したまま日本語の説明を参照できるようにしている。

## 収録範囲

| 種別 | 原典 | 個別ページ数 | ページ配置 |
| --- | --- | ---: | --- |
| チャンピオン | `data/ja_JP/champion/*.json` | 173 | [[wiki/entities/champions/aatrox\|チャンピオンページ]] |
| アイテム | `data/ja_JP/item.json` | 868 | [[wiki/entities/items/item-1001\|アイテムページ]] |
| ルーン | `data/ja_JP/runesReforged.json` | 62 | [[wiki/entities/runes/absolute-focus\|ルーンページ]] |
| サモナースペル | `data/ja_JP/summoner.json` | 34 | [[wiki/entities/spells/summoner-barrier\|スペルページ]] |

アイテムは名称が空欄の4レコードを含め、IDをタイトルにしたページを作成している。ルーンは5系統・20スロットの個別選択肢、サモナースペルは通常レコードとモード別レコードを含む原典34件をID単位で保持する。

## ページ化の方針

- 原典レコードのID、英語キー、versionをメタデータとして残し、ページタイトルや表示名は日本語の原典値を使う。
- HTML風の装飾タグを含む短い説明は、可読性のためタグを除去して表示する。原文の完全なツールチップが必要な場合は原典アーカイブを確認する。
- チャンピオン、アイテム、ルーン、サモナースペルのページは、それぞれ `wiki/entities/champions/`、`wiki/entities/items/`、`wiki/entities/runes/`、`wiki/entities/spells/` に配置する。
- アイテムの合成関係、利用可能マップ、価格、ステータス、ルーンの系統・スロット、スペルの利用モードや基本パラメータなど、各データ種別に固有のフィールドを個別ページへ整理する。
- アイテム個別ページのフロントマターには、効果・ステータスから推定した `champion-synergy-*` タグを付け、相性のよいチャンピオン系統やジャングル・汎用用途で絞り込めるようにする。分類の規則と限界は [[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテムのチャンピオン相性タグ分類]] に記録する。
- 個別ページのタグは原典由来の候補分類として保持する。実試合のチャンピオン・ロール・個別アイテム相関、Data Dragon `stats` の同一ステータス群、完成アイテム中核は `scripts/riot_champion_item_synergy.py` と [[wiki/syntheses/item-champion-synergy-tags-v16-18-1|相性タグ分類の実試合再評価]] で別に確認し、最終所持状態の勝率差やステータス仮説だけで個別タグを書き換えない。
- チャンピオン情報の入口は `wiki/entities/champions/` とする。各entityには実測候補と理論仮説を分けた短い生成ブロックだけを置き、全候補・負の差・詳細表は同一スナップショットの `reports/riot-champion-item-synergy/` へ直接リンクする。同期は `scripts/riot_champion_build_wiki_sync.py` で明示的に実行する。
- チャンピオン、アイテム、ルーン、サモナースペルの全個別ページには、共通の出典検索用タグ `data-dragon` を付ける。ページ内の `sources` と同じく、個別データの大元が Data Dragon 配布アーカイブであることを示す。
- データに存在しない名称や意味は推測しない。名称空欄やマップ名不明などはページ上で未解決として明記する。

## 制約と未展開情報

> [!warning] 原典フィールドの解釈
> Data Dragonの説明文やツールチップには表示タグ、実行時に置換される変数、内部用配列が含まれる。個別ページは検索・閲覧用の整理であり、ゲーム内の実際の数値や挙動を独立に再計算する仕様書ではない。

- アイテム名が空欄のレコードは、名称を補完せずIDベースで表示している。
- サモナースペルの `datavalues`、`effect`、`effectBurn`、`vars` は、内部計算用のため個別ページでは表形式に展開していない。
- `item-modifiers.json`、他ロケールの説明、アイテム・ルーン・スペル画像のローカルコピー、TFT等の周辺データは、この取り込みでは個別ページ化していない。

## 関連ページ

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]] — 個別ページの原典と配布物全体。
- [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]] — entityへ同期した短い分析の入力範囲と限界。
- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]] — チャンピオンの集約・詳細レコード。
- [[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテムのチャンピオン相性タグ分類]] — アイテムの相性候補タグ、付与規則、分類上の限界。
- [[wiki/overview|概要]] — Wiki全体の収録範囲。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]] — `ja_JP` のアイテム、ルーン、サモナースペル原典。
- [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]] — チャンピオンentityの実試合ビルド分析ブロック。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
