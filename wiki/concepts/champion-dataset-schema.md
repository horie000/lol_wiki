---
title: チャンピオンデータのスキーマ
type: concept
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
tags:
  - champion
  - data-schema
---

# チャンピオンデータのスキーマ

## 概要

[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|チャンピオンデータセット v16.18.1]] は、トップレベルのメタデータと、チャンピオンIDをキーとする `data` オブジェクトから成る。173件のレコードは同じフィールド集合を持つため、識別情報、説明文、分類、評価値、数値ステータスを一貫した方法で検索・比較できる。

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

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|チャンピオンデータセット v16.18.1]] — スキーマと全レコード。
