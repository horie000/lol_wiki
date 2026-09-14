---
title: "ルル"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-support
  - role-mage
  - data-dragon
champion_id: "Lulu"
champion_key: "117"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Lulu.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lulu.png"
---

# ルル

![[raw/assets/champions/Lulu.png|128]]

## 基本情報

- **英字ID：** `Lulu`
- **キー：** `117`
- **称号：** 森の妖精使い
- **データversion：** `16.18.1`

## 紹介

ルルは魔法で夢のような幻想や空想の生き物を作り出すことで知られるヨードルのメイジで、ピックスという妖精の相棒と一緒にルーンテラを放浪している。ルルはこの平凡な物質世界を制約だと感じており、気まぐれに世界の法則を捻じ曲げては物体を作り出している。周囲の者は彼女の魔法を異常で危険なものだと感じているが、彼女はみんなには魔法が足りないと感じている。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 5 |
| `magic` | 7 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 565 |
| `hpperlevel` | 92 |
| `mp` | 350 |
| `mpperlevel` | 55 |
| `movespeed` | 330 |
| `armor` | 26 |
| `armorperlevel` | 4.6 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 11 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 47 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.25 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 仲良し妖精ピックス：** ピックスがくっついているチャンピオンが敵ユニットを攻撃するたびに、ピックスも魔法のビームで援護する。このビームは対象に追従するが、射線に別のユニットが割り込むと、そのユニットに遮られる。

- **Q — ぴかぴかビーム：** ピックスとルルが同時に魔法のビームを発射し、命中したすべての敵にダメージと重度のスロウ効果を付与する。
- **W — イタズラ：** 味方に使用した場合、短時間攻撃速度と移動速度を増加させる。敵に使用した場合、かわいらしい動物に変身させ、通常攻撃とスキルの使用を封じる。
- **E — ピックス、おねがい！：** 味方に使用した場合、ピックスをそばに送り込んでダメージを防ぐシールドを付与する。その後ピックスは対象にくっついて移動し、通常攻撃時に魔法のビームで援護する。敵に使用した場合、対象のもとへピックスが飛んでいきダメージを与える。その後ピックスは対象にくっついて移動し、可視状態にする。
- **R — おおきくなぁれ！：** 味方1体を巨大化させ、周囲にいる敵をノックアップさせる。巨大化した味方は体力が大幅に増加し、体の周囲に数秒間光の輪が発生する。輪の中に入った敵はスロウ状態になる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 中盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 本分類で採用した序盤の基礎ステータス上位15%と、終盤の能力の蓄積成長・明示的なステータス連動のいずれにも当たらないため、中盤を暫定指定する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Lulu` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lulu.png)
