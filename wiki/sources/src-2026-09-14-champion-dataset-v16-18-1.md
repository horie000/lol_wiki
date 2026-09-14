---
title: チャンピオンデータセット v16.18.1
type: source
status: active
source_path: raw/sources/champion.json.md
ingested: 2026-09-14
created: 2026-09-14
updated: 2026-09-14
tags:
  - champion
  - game-data
  - dataset
---

# チャンピオンデータセット v16.18.1

## 要約

version `16.18.1` のチャンピオン情報を収録したJSONデータである。`data` オブジェクト内に173件のレコードがあり、各レコードには識別子、日本語の名前・称号・紹介文、役割タグ、リソース種別、画像参照、4種類の評価値、20種類の数値ステータスが格納されている。

全レコードの `version` はトップレベルと同じ `16.18.1` で、必須フィールドの欠落や `id`・`key`・`name` の重複は検出されなかった。一方で、一部の値は欠損または一律値になっており、分析時にはデータ品質上の制約として扱う必要がある。

## 主要な内容

- トップレベルのフィールドは `type`、`format`、`version`、`data` である。値はそれぞれ `champion`、`standAloneComplex`、`16.18.1`、173件のレコードを持つオブジェクトである。
- 各レコードは `id`、`key`、`name`、`title`、`blurb`、`info`、`image`、`tags`、`partype`、`stats`、`version` の共通フィールドを持つ。
- 日本語の `name`、`title`、`blurb` と、英語の `id` および役割タグが併存している。
- 役割タグは複数付与される場合がある。所属件数は `Mage` 75件、`Fighter` 60件、`Assassin` 46件、`Tank` 46件、`Support` 43件、`Marksman` 33件である。
- `partype` は「マナ」が145件で最も多く、残りは「なし」「気」や各チャンピオン固有の名称などに分かれる。

## データ品質と制約

> [!warning] 分析上の注意
> `attackdamageperlevel`、`crit`、`critperlevel` は173件すべてで `0` である。このデータだけでは、実際に変化がないのか、値が未収録なのかを判定できない。

- アクシャン、レル、セラフィーン、ヴェックスは、`info` 内の `attack`、`defense`、`magic`、`difficulty` がすべて `0` である。
- ベル＝ヴェスは `partype` が空文字列である。
- 173件すべてに一意な `image.full` のファイル名があり、対応する画像を指定CDNから `raw/assets/champions/` に保存している。
- `source_url`、公開日、各フィールドの正式な定義は原典内にない。そのため、フィールド名から推測した意味を確定事項として扱ってはならない。
- `mp` にはヴィエゴの `10000` など大きな値があり、単純平均は代表値として注意が必要である。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]] — トップレベル、レコード、数値フィールドの構造。
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]] — 役割、リソース、主要数値の分布と品質上の注意。
- [[wiki/index#エンティティ|個別チャンピオン一覧]] — 173件の個別ページへの索引。

## 未解決の問い

- このデータの正式な配布元と、各フィールドの定義は何か。
- 一律 `0` のステータス値は仕様上の値か、未収録値か。

## 出典

- 原典：[[raw/sources/champion.json.md|champion.json.md]]
