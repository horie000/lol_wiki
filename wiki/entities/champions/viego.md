---
title: "ヴィエゴ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-fighter
  - role-assassin
  - data-dragon
champion_id: "Viego"
champion_key: "234"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "なし"
image_path: "raw/assets/champions/Viego.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Viego.png"
---

# ヴィエゴ

![[raw/assets/champions/Viego.png|128]]

## 基本情報

- **英字ID：** `Viego`
- **キー：** `234`
- **称号：** 滅びの王
- **データversion：** `16.18.1`

## 紹介

遠い昔に滅びた王国の支配者であったヴィエゴは、千年以上前に亡き妻を甦らせようと試みたことで「破滅」と呼ばれる魔力の大災厄を引き起こし、自らも命を落とした。遥か昔に喪った王妃への執着と愛に苛まれ、強力な不死の霊と化したヴィエゴは「滅びの王」として君臨し、王妃を甦らせる術を求め、「暗黒の刻」を操ってこの世界を調べ回っている。その行く手を阻むものは、空虚で冷酷なる胸からとめどなく流れ出でる「黒き霧」によってことごとく滅ぼされるだろう。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** なし

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 4 |
| `magic` | 2 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 109 |
| `mp` | 10000 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 34 |
| `armorperlevel` | 4.6 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 200 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 57 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.75 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 王の支配：** ヴィエゴの周囲で倒された敵は亡霊になる。ヴィエゴは亡霊に通常攻撃を行うことで、その倒された敵の死体を一時的に操れるようになり、対象の最大体力の一定割合にあたる体力を回復し、対象の通常スキルとアイテムを使用できる。対象のアルティメットスキルは自身のものと入れ替わり、自由に1回発動できるようになる。

- **Q — 滅びの王剣：** 自動効果により、霊体の刃が通常攻撃時効果で現在体力に応じた追加ダメージを与える。直前にスキルで攻撃した敵には2回攻撃を行い、体力を奪う。 このスキルを発動すると、剣で前方に突きを放ち、自身の前にいる敵を貫く。
- **W — 亡霊の嘆き：** チャージしてから前方にダッシュし、凝縮した「黒き霧」を発射して最初に当たった敵をスタンさせる。
- **E — 彷徨える苦悶：** 「黒き霧」を出現させて、地形の周囲を覆う。自身は「霧」の中では亡霊となって隠れることができ、カモフラージュ状態となり、移動速度と攻撃速度が増加する。
- **R — ハートブレイカー：** 近くの地点に瞬間移動し、到着時に敵チャンピオンを斬りつけ、対象の心臓を貫いて衝撃を発生させ、周囲の敵をノックバックさせる。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Viego` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Viego.png)
