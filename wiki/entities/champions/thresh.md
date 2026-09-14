---
title: "スレッシュ"
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
  - role-tank
  - data-dragon
champion_id: "Thresh"
champion_key: "412"
data_version: "16.18.1"
roles:
  - "Support"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Thresh.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Thresh.png"
---

# スレッシュ

![[raw/assets/champions/Thresh.png|128]]

## 基本情報

- **英字ID：** `Thresh`
- **キー：** `412`
- **称号：** 縛鎖の看守
- **データversion：** `16.18.1`

## 紹介

残虐で狡猾なスレッシュは、シャドウアイルを彷徨う貪欲なる亡霊だ。かつては膨大な量の古の魔法の秘密を管理する立場にあったが、生死を超える力によって亡霊となった彼は、他者を拷問し、じわじわと嬲り殺すことに生き甲斐を見出すようになった。犠牲者の魂はスレッシュの持つ邪悪なランタンの中に囚われ、尽きることのない激しい苦痛に満ちた拷問を受けながら永劫を送ることになる。

## 分類

- **役割タグ：** `Support`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 6 |
| `magic` | 6 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 120 |
| `mp` | 274 |
| `mpperlevel` | 44 |
| `movespeed` | 330 |
| `armor` | 33 |
| `armorperlevel` | 0 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.55 |
| `attackrange` | 450 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 56 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 魂の束縛：** 近くで倒れた敵の魂を集め、物理防御と魔力を永続的に獲得する。

- **Q — 死の宣告：** 敵に鎖を投げ、命中した対象をそばに引き寄せる。もう一度発動すると、つないだ鎖をたぐって対象まで移動する。
- **W — 嘆きの魂灯：** ランタンを投げて、その周囲にいる味方チャンピオンにシールドを付与する。ランタンをクリックした味方チャンピオンは、スレッシュの元に素早く移動できる。
- **E — 絶望の鎖：** 前回の通常攻撃から経過した時間に応じて次の通常攻撃が強化される。発動すると鎖を投げ、範囲内の敵ユニットを鎖が投げられた方向へ弾き飛ばす。
- **R — 魂の牢獄：** 牢獄の壁を出現させる。壁を壊した者にダメージを与えスロウ効果を付与する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 近くで倒れた敵の魂から物理防御と魔力を永続的に獲得する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Thresh` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Thresh.png)
