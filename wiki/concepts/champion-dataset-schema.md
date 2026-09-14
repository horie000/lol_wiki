---
title: チャンピオンデータのスキーマ
type: concept
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - data-schema
---

# チャンピオンデータのスキーマ

## 概要

[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|チャンピオンデータセット v16.18.1]] は、トップレベルのメタデータと、チャンピオンIDをキーとする `data` オブジェクトから成る。[[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]] には同じ基本レコードの個別版があり、能力・ヒント・スキン等の詳細フィールドが追加されている。基本情報を含む173件のレコードは同じフィールド集合を持つため、識別情報、説明文、分類、評価値、数値ステータスを一貫した方法で検索・比較できる。

## トップレベル

| フィールド | 原典内の値・役割 |
| --- | --- |
| `type` | `champion` |
| `format` | `standAloneComplex` |
| `version` | `16.18.1` |
| `data` | 173件のチャンピオンレコードを持つオブジェクト |

## レコード構造

| 区分 | フィールド | 内容 |
| --- | --- | --- |
| 識別 | `id`, `key`, `name` | 英字ID、数値文字列のキー、日本語名 |
| 説明 | `title`, `blurb` | 日本語の称号と紹介文 |
| 分類 | `tags`, `partype` | 役割タグの配列とリソース種別 |
| 評価 | `info` | `attack`, `defense`, `magic`, `difficulty` |
| 画像参照 | `image` | `full`, `sprite`, `group`, `x`, `y`, `w`, `h` |
| 数値 | `stats` | 20種類の数値フィールド |
| 版 | `version` | 全件で `16.18.1` |

## 個別詳細レコード

Data Dragon アーカイブの `16.18.1/data/ja_JP/champion/{id}.json` は、集約レコードと同じ基本情報に次の詳細フィールドを加える。173件すべてにパッシブ1件とスキル4件がある。

| フィールド | 内容 |
| --- | --- |
| `lore` | 日本語の長い紹介文。既存ページの「紹介」と同じ内容を含む |
| `allytips`, `enemytips` | 味方・敵としてのプレイヒントの配列 |
| `passive` | パッシブの名前、説明、画像参照 |
| `spells` | Q/W/E/Rに対応する4スキルの名前、説明、tooltip、画像参照 |
| `skins` | スキンの識別情報、名称、画像参照 |
| `recommended` | 推奨設定の配列。内容はチャンピオンにより異なる |

個別ページには `passive.name`、`passive.description`、`spells[].name`、`spells[].description` を取り込んでいる。`tooltip` は実行時の変数プレースホルダーを含むため、そのままの数値仕様としては扱わない。

## 数値フィールド

`stats` には次のフィールドがある。

- 耐久・回復：`hp`、`hpperlevel`、`hpregen`、`hpregenperlevel`
- リソース：`mp`、`mpperlevel`、`mpregen`、`mpregenperlevel`
- 防御：`armor`、`armorperlevel`、`spellblock`、`spellblockperlevel`
- 攻撃：`attackdamage`、`attackdamageperlevel`、`attackrange`、`attackspeed`、`attackspeedperlevel`
- その他：`movespeed`、`crit`、`critperlevel`

上記の分類はフィールド名を整理したものであり、原典には単位や正式な意味の定義がない。

## 利用上の注意

- 比較や集計では、必ず version `16.18.1` に限定された観測として記述する。
- `tags` は複数値を持つため、タグ所属数の合計はレコード総数と一致しない。
- `partype` は表示名であり、`mp` 系フィールドとの対応関係は原典だけでは確定できない。
- 一律値や空文字列を、確認なしに有効なゼロ値として解釈しない。
- 個別チャンピオンの説明や数値を回答するときは、Wiki の要約だけでなく原典レコードを確認する。

## 関連ページ

- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]] — このスキーマを使った全体集計。
- [[wiki/syntheses/champion-power-spikes-v16-18-1|チャンピオンのパワースパイク分類 v16.18.1]] — `stats` と個別詳細レコードを使った再現可能な時期分類。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]] — 個別詳細レコードと配布物全体の構造。

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|チャンピオンデータセット v16.18.1]] — スキーマと全レコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]] — 日本語の能力詳細フィールドとロケール別配布構造。
