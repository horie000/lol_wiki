---
title: 概要
type: overview
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
tags:
  - overview
---

# 概要

この Vault は、原典を `raw/sources/` に保存し、そこから得た知識を継続的に統合する LLM 管理型 Wiki である。

## 現在の対象範囲

現在は、version `16.18.1` のチャンピオンデータセットを収録している。原典には173件のレコードがあり、日本語の名前・称号・紹介文、役割タグ、リソース種別、画像参照、評価値、数値ステータスが含まれる。

## 現在の知見

- レコードのフィールド集合と version は統一され、主要な識別子に重複はない。
- 役割タグでは `Mage` と `Fighter` の所属件数が多い。
- 複数の一律 `0` フィールドと一部の空値があり、性能比較では欠損の可能性を考慮する必要がある。
- 173件すべてに個別のエンティティページがあり、指定CDNから取得・検証した128×128ピクセルのPNG画像を表示する。

## ナビゲーション

- [[wiki/index|Wiki 索引]]
- [[wiki/index#エンティティ|個別チャンピオン一覧]]
- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|チャンピオンデータセット v16.18.1]]
- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]
- [[wiki/log|Wiki ログ]]

## 未解決の問い

- データの正式な配布元とフィールド定義は何か。
- 次に取り込むversionまたは補足資料は何か。

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|チャンピオンデータセット v16.18.1]]
