---
title: 概要
type: overview
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2017-11-26-firstbloodstats-gold-efficiency]]"
  - "[[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency]]"
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
- 173件すべてに `wiki/entities/champions/` 配下の個別エンティティページがあり、指定CDNから取得・検証した128×128ピクセルのPNG画像を表示する。
- 173件すべての個別ページに、日本語のパッシブ1件とQ/W/E/Rの4スキル説明を掲載している。チャンピオンのtooltip数値、スキン、TFT等は未展開である。
- 173件すべてのチャンピオンページに、基礎ステータス・能力の蓄積成長・明示的なアイテム連動を根拠としたパワースパイク（序盤・中盤・終盤）を記録している。役割タグは判定に使わない。これは実戦の強さを断定しない再現可能な分類である。
- アイテム868件、ルーン62件、サモナースペル34件を、それぞれ `wiki/entities/items/`、`wiki/entities/runes/`、`wiki/entities/spells/` に原典のID単位で個別ページ化している。名称空欄のアイテム4件やモード別スペルも、推測で統合せず保持している。
- アイテム868件には、レッド＆ふぉー記事の単価表を適用したゴールド効率、理論価格、算定対象外の効果を個別に記録している。行動妨害耐性、割合物理防御貫通、割合・固定魔法防御貫通、ライフスティール、割合移動速度などを算定し、固定通常攻撃時追加ダメージだけはFirstBloodStats記事の補助単価を使う。記事に単価のないステータスや条件付き効果は対象外である。
- アイテム868件には、効果・ステータスから相性のよいチャンピオン系統を推定した `champion-synergy-*` タグを付与している。複数タグを許し、`marksman`、`fighter`、`assassin`、`mage`、`tank`、`support`、`jungler`、`utility` の検索で絞り込める。これはData Dragon原典からの候補分類であり、個別チャンピオンの最適ビルドや勝率を断定しない。
- チャンピオン173件、アイテム868件、ルーン62件、サモナースペル34件の全個別ページに、Data Dragon由来であることを示す共通タグ `data-dragon` を付与している。
- サモナーズリフトで購入できるアイテムの高低10例を比較し、消耗品・視界・ジャングル用品・時間限定効果の0%を「弱い」と結論付けられないことを整理した。
- 個別ページの説明ではHTML風の表示タグを除去しているが、サモナースペル等のツールチップ内プレースホルダーは追加仕様なしに数値化していない。

## ナビゲーション

- [[wiki/index|Wiki 索引]]
- [[wiki/index#エンティティ|個別エンティティ一覧]]
- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|チャンピオンデータセット v16.18.1]]
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]]
- [[wiki/sources/src-2017-11-26-firstbloodstats-gold-efficiency|アイテムのゴールド効率について改めてまとめた]]
- [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency|アイテムの金銭効率ランキング：ファイター編【LoL】]]
- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/concepts/game-data-catalog|ゲームデータ個別ページのカタログ]]
- [[wiki/syntheses/gold-efficiency-stat-values|アイテム金銭効率の基準単価]]
- [[wiki/syntheses/gold-efficiency-high-low-examples|アイテム金銭効率の高低例と総合評価]]
- [[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテムのチャンピオン相性タグ分類 v16.18.1]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]
- [[wiki/syntheses/champion-power-spikes-v16-18-1|チャンピオンのパワースパイク分類 v16.18.1]]
- [[wiki/log|Wiki ログ]]

## 未解決の問い

- データの正式な配布元とフィールド定義は何か。
- tooltipの数値プレースホルダーを検証できる仕様資料は何か。
- `item-modifiers.json`、他ロケール、TFT等の周辺データをどの粒度で取り込むか。

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|チャンピオンデータセット v16.18.1]]
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]]
- [[wiki/sources/src-2017-11-26-firstbloodstats-gold-efficiency|アイテムのゴールド効率について改めてまとめた]]
