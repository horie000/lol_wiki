---
title: "秘儀の彗星"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - rune
  - league-of-legends
  - sorcery
  - data-dragon
---

# 秘儀の彗星

## 概要

「秘儀の彗星」は、魔道（Sorcery）系統に属するルーン選択肢である。原典の `slots` 配列ではスロット1（キーストーン）に配置されている。

## 識別情報

- ルーンID: `8229`
- ルーンキー: `ArcaneComet`
- 系統ID: `8200`
- 系統キー: `Sorcery`
- 系統名: 魔道
- 系統アイコンパス: `perk-images/Styles/7202_Sorcery.png`
- スロット番号: `1`
- スロット種別: キーストーン
- アイコンパス: `perk-images/Styles/Sorcery/ArcaneComet/ArcaneComet.png`

## 効果（短い説明）

スキルでダメージを与えた敵チャンピオンの位置に彗星を飛ばす。

## 効果（詳細）

スキルでチャンピオンにダメージを与えると、その位置に向かって彗星を飛ばし、距離に応じて増加するダメージを与える。

アダプティブダメージ: 15 - 100(レベルに応じて)(+魔力0.05および+増加攻撃力0.1)
クールダウン: 20 - 8秒

ダメージ増幅率は距離750で最大100%まで増加する。

## 収録範囲と整理上の注意

- 名称、ID、キー、系統、アイコンパス、短い説明、詳細説明は、Data Dragon v16.18.1 の `ja_JP` ルーン原典に記載された値である。
- 「スロット種別」は原典に独立したラベルがないため、`slots` 配列の順序から整理した表示である。スロット1をキーストーン、スロット2〜4を各マイナー選択肢の列として扱っている。
- 効果説明のHTML表示タグは可読性のため除去した。タグ除去後の本文は原典の日本語説明を保持している。
- 本ページでは個別選択肢を扱い、系統全体のページは作成していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]] — `16.18.1/data/ja_JP/runesReforged.json` の 魔道 / 秘儀の彗星 レコード。
- 原典アーカイブ: [[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
