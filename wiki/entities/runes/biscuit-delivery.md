---
title: "ビスケットデリバリー"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - rune
  - league-of-legends
  - inspiration
  - data-dragon
---

# ビスケットデリバリー

## 概要

「ビスケットデリバリー」は、天啓（Inspiration）系統に属するルーン選択肢である。原典の `slots` 配列ではスロット3（第2列）に配置されている。

## 識別情報

- ルーンID: `8345`
- ルーンキー: `BiscuitDelivery`
- 系統ID: `8300`
- 系統キー: `Inspiration`
- 系統名: 天啓
- 系統アイコンパス: `perk-images/Styles/7203_Whimsy.png`
- スロット番号: `3`
- スロット種別: 第2列
- アイコンパス: `perk-images/Styles/Inspiration/BiscuitDelivery/BiscuitDelivery.png`

## 効果（短い説明）

6分経過するまで2分毎にビスケットを獲得する。消費するか売却すると最大体力が増加し、体力が回復する。

## 効果（詳細）

ビスケットデリバリー: 6分間、2分ごとに英気満点ビスケットを獲得する。

ビスケットは最大体力の20 + 2%を回復する。効果は自身の減少体力に応じて最大100%まで増加する。ビスケットを消費するか売却すると、恒久的に最大体力が30増加する。

## 収録範囲と整理上の注意

- 名称、ID、キー、系統、アイコンパス、短い説明、詳細説明は、Data Dragon v16.18.1 の `ja_JP` ルーン原典に記載された値である。
- 「スロット種別」は原典に独立したラベルがないため、`slots` 配列の順序から整理した表示である。スロット1をキーストーン、スロット2〜4を各マイナー選択肢の列として扱っている。
- 効果説明のHTML表示タグは可読性のため除去した。タグ除去後の本文は原典の日本語説明を保持している。
- 本ページでは個別選択肢を扱い、系統全体のページは作成していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]] — `16.18.1/data/ja_JP/runesReforged.json` の 天啓 / ビスケットデリバリー レコード。
- 原典アーカイブ: [[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
