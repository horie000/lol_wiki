---
title: "生命の泉"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - rune
  - league-of-legends
  - resolve
  - data-dragon
---

# 生命の泉

## 概要

「生命の泉」は、不滅（Resolve）系統に属するルーン選択肢である。原典の `slots` 配列ではスロット2（第1列）に配置されている。

## 識別情報

- ルーンID: `8463`
- ルーンキー: `FontOfLife`
- 系統ID: `8400`
- 系統キー: `Resolve`
- 系統名: 不滅
- 系統アイコンパス: `perk-images/Styles/7204_Resolve.png`
- スロット番号: `2`
- スロット種別: 第1列
- アイコンパス: `perk-images/Styles/Resolve/FontOfLife/FontOfLife.png`

## 効果（短い説明）

敵チャンピオンに行動妨害効果を付与すると、近くにいる味方チャンピオンの体力が回復する。

## 効果（詳細）

敵チャンピオンに行動妨害効果を付与すると、自身と近くにいる体力が最も低い味方チャンピオンの体力を@BaseHeal@回復する。

遠隔攻撃チャンピオンは効果が70%になる。

クールダウン: 20秒

## 収録範囲と整理上の注意

- 名称、ID、キー、系統、アイコンパス、短い説明、詳細説明は、Data Dragon v16.18.1 の `ja_JP` ルーン原典に記載された値である。
- 「スロット種別」は原典に独立したラベルがないため、`slots` 配列の順序から整理した表示である。スロット1をキーストーン、スロット2〜4を各マイナー選択肢の列として扱っている。
- 効果説明のHTML表示タグは可読性のため除去した。タグ除去後の本文は原典の日本語説明を保持している。
- 本ページでは個別選択肢を扱い、系統全体のページは作成していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]] — `16.18.1/data/ja_JP/runesReforged.json` の 不滅 / 生命の泉 レコード。
- 原典アーカイブ: [[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
