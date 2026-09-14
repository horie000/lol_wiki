---
title: "キンドレッド"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-marksman
champion_id: "Kindred"
champion_key: "203"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Kindred.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kindred.png"
---

# キンドレッド

![[raw/assets/champions/Kindred.png|128]]

## 基本情報

- **英字ID：** `Kindred`
- **キー：** `203`
- **称号：** 永遠なる狩人
- **データversion：** `16.18.1`

## 紹介

別々の存在なれど、決して離れることはない──キンドレッドは死の本質を対で指し示す。子羊の放つ矢は、己の運命を受け入れた者を速やかにこの世から解放する。狼は死から逃れようとする者を追い詰め、強靭な顎で噛み砕き、惨たらしい最期を遂げさせる。キンドレッドの真髄についてはルーンテラ全域で諸説囁かれるが、いずれにせよ、生ける者は全て、死の本質を選ぶ必要に迫られる。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 2 |
| `magic` | 2 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 595 |
| `hpperlevel` | 104 |
| `mp` | 300 |
| `mpperlevel` | 35 |
| `movespeed` | 325 |
| `armor` | 29 |
| `armorperlevel` | 4.7 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 500 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — キンドレッドの刻印：** 獲物とする対象に印を付ける。印をつけた獲物を狩ることで、通常スキルを恒常的に強化する。獲物を4体狩るごとに、通常攻撃の射程も強化される。

- **Q — 矢の輪舞：** 素早く移動し、周囲の対象に最大3本の矢を放つ。
- **W — 狼の激昂：** 狼が猛り、周囲の敵に攻撃を繰り出す。子羊は自動効果により移動と通常攻撃でスタックを獲得する。チャージが完了すると子羊の次の攻撃で体力が回復する。
- **E — 忍び寄る恐怖：** 子羊が対象に狙いを定めて攻撃し、スロウ効果を与える。子羊が同じ対象をさらに2回攻撃すると、その次の攻撃で狼が代わりに襲撃して大ダメージを与える。
- **R — 羊の執行猶予：** 子羊が展開した効果範囲内にいるすべての生命は死から免れる。効果時間中は誰も倒されることはない。効果時間終了時に全ユニットの体力が一定数回復する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kindred` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kindred.png)
