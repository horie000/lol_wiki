---
title: "魂の収穫"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - rune
  - league-of-legends
  - domination
  - data-dragon
---

# 魂の収穫

## 概要

「魂の収穫」は、覇道（Domination）系統に属するルーン選択肢である。原典の `slots` 配列ではスロット1（キーストーン）に配置されている。

## 識別情報

- ルーンID: `8128`
- ルーンキー: `DarkHarvest`
- 系統ID: `8100`
- 系統キー: `Domination`
- 系統名: 覇道
- 系統アイコンパス: `perk-images/Styles/7200_Domination.png`
- スロット番号: `1`
- スロット種別: キーストーン
- アイコンパス: `perk-images/Styles/Domination/DarkHarvest/DarkHarvest.png`

## 効果（短い説明）

体力の低下したチャンピオンにダメージを与えるとアダプティブダメージを与えて、犠牲者から魂を1つ収穫する。

## 効果（詳細）

体力が50%以下のチャンピオンにダメージを与えるとアダプティブダメージを与えて、その魂を収穫し、「魂の収穫」のダメージが恒久的に11増加する。

「魂の収穫」のダメージ: 30(+魂の数x11)(+増加攻撃力x0.1)(+魔力x0.05)
クールダウン: 35秒(キルまたはアシストで1.0秒にリセット)

## 収録範囲と整理上の注意

- 名称、ID、キー、系統、アイコンパス、短い説明、詳細説明は、Data Dragon v16.18.1 の `ja_JP` ルーン原典に記載された値である。
- 「スロット種別」は原典に独立したラベルがないため、`slots` 配列の順序から整理した表示である。スロット1をキーストーン、スロット2〜4を各マイナー選択肢の列として扱っている。
- 効果説明のHTML表示タグは可読性のため除去した。タグ除去後の本文は原典の日本語説明を保持している。
- 本ページでは個別選択肢を扱い、系統全体のページは作成していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]] — `16.18.1/data/ja_JP/runesReforged.json` の 覇道 / 魂の収穫 レコード。
- 原典アーカイブ: [[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
