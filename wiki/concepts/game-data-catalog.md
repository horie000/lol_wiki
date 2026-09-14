---
title: ゲームデータ個別ページのカタログ
type: concept
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - game-data
  - data-catalog
  - league-of-legends
---

# ゲームデータ個別ページのカタログ

## 概要

Data Dragon version `16.18.1` の日本語データを、原典レコード単位で検索できる個別ページへ整理したカタログである。チャンピオンの個別ページに加えて、アイテム、ルーン、サモナースペルをそれぞれ専用ディレクトリへ分け、IDやキーを保持したまま日本語の説明を参照できるようにしている。

## 収録範囲

| 種別 | 原典 | 個別ページ数 | ページ配置 |
| --- | --- | ---: | --- |
| チャンピオン | `data/ja_JP/champion/*.json` | 173 | [[wiki/index#エンティティ|チャンピオン一覧]] |
| アイテム | `data/ja_JP/item.json` | 868 | [[wiki/entities/items/item-1001|アイテムページ]] |
| ルーン | `data/ja_JP/runesReforged.json` | 62 | [[wiki/entities/runes/absolute-focus|ルーンページ]] |
| サモナースペル | `data/ja_JP/summoner.json` | 34 | [[wiki/entities/spells/summoner-barrier|スペルページ]] |

アイテムは名称が空欄の4レコードを含め、IDをタイトルにしたページを作成している。ルーンは5系統・20スロットの個別選択肢、サモナースペルは通常レコードとモード別レコードを含む原典34件をID単位で保持する。

## ページ化の方針

- 原典レコードのID、英語キー、versionをメタデータとして残し、ページタイトルや表示名は日本語の原典値を使う。
- HTML風の装飾タグを含む短い説明は、可読性のためタグを除去して表示する。原文の完全なツールチップが必要な場合は原典アーカイブを確認する。
- アイテムの合成関係、利用可能マップ、価格、ステータス、ルーンの系統・スロット、スペルの利用モードや基本パラメータなど、各データ種別に固有のフィールドを個別ページへ整理する。
- データに存在しない名称や意味は推測しない。名称空欄やマップ名不明などはページ上で未解決として明記する。

## 制約と未展開情報

> [!warning] 原典フィールドの解釈
> Data Dragonの説明文やツールチップには表示タグ、実行時に置換される変数、内部用配列が含まれる。個別ページは検索・閲覧用の整理であり、ゲーム内の実際の数値や挙動を独立に再計算する仕様書ではない。

- アイテム名が空欄のレコードは、名称を補完せずIDベースで表示している。
- サモナースペルの `datavalues`、`effect`、`effectBurn`、`vars` は、内部計算用のため個別ページでは表形式に展開していない。
- `item-modifiers.json`、他ロケールの説明、アイテム・ルーン・スペル画像のローカルコピー、TFT等の周辺データは、この取り込みでは個別ページ化していない。

## 関連ページ

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]] — 個別ページの原典と配布物全体。
- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]] — チャンピオンの集約・詳細レコード。
- [[wiki/overview|概要]] — Wiki全体の収録範囲。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]] — `ja_JP` のアイテム、ルーン、サモナースペル原典。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
