---
title: 概要
type: overview
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - overview
---

# 概要

この Vault は、原典を `raw/sources/` に保存し、そこから得た知識を継続的に統合する LLM 管理型 Wiki である。

## 現在の対象範囲

現在は、version `16.18.1` のチャンピオンデータセットとData Dragon配布アーカイブを収録している。基本原典には173件のレコードがあり、日本語の名前・称号・紹介文、役割タグ、リソース種別、画像参照、評価値、数値ステータスが含まれる。配布アーカイブの日本語個別レコードから、各チャンピオンのパッシブと4スキルの説明、868件のアイテム、62件のルーン、34件のサモナースペルを個別ページへ展開している。

## 現在の知見

- レコードのフィールド集合と version は統一され、主要な識別子に重複はない。
- 役割タグでは `Mage` と `Fighter` の所属件数が多い。
- 複数の一律 `0` フィールドと一部の空値があり、性能比較では欠損の可能性を考慮する必要がある。
- 173件すべてに個別のエンティティページがあり、指定CDNから取得・検証した128×128ピクセルのPNG画像を表示する。
- 173件すべての個別ページに、日本語のパッシブ1件とQ/W/E/Rの4スキル説明を掲載している。チャンピオンのtooltip数値、スキン、TFT等は未展開である。
- アイテム868件、ルーン62件、サモナースペル34件を、原典のID単位で個別ページ化している。名称空欄のアイテム4件やモード別スペルも、推測で統合せず保持している。
- 個別ページの説明ではHTML風の表示タグを除去しているが、サモナースペル等のツールチップ内プレースホルダーは追加仕様なしに数値化していない。

## ナビゲーション

- [[wiki/index|Wiki 索引]]
- [[wiki/index#エンティティ|個別エンティティ一覧]]
- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|チャンピオンデータセット v16.18.1]]
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]]
- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/concepts/game-data-catalog|ゲームデータ個別ページのカタログ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]
- [[wiki/log|Wiki ログ]]

## 未解決の問い

- データの正式な配布元とフィールド定義は何か。
- tooltipの数値プレースホルダーを検証できる仕様資料は何か。
- `item-modifiers.json`、他ロケール、TFT等の周辺データをどの粒度で取り込むか。

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|チャンピオンデータセット v16.18.1]]
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]]
