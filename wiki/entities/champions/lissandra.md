---
title: "リサンドラ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-mage
  - data-dragon
champion_id: "Lissandra"
champion_key: "127"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Lissandra.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lissandra.png"
---

# リサンドラ

![[raw/assets/champions/Lissandra.png|128]]

## 基本情報

- **英字ID：** `Lissandra`
- **キー：** `127`
- **称号：** 氷の魔女
- **データversion：** `16.18.1`

## 紹介

リサンドラの魔力は清らかな氷さえも闇で汚し、暗く恐ろしいモノへとねじ曲げる。彼女が操る黒き氷はただ物を凍らせるだけにとどまらず、彼女に従わぬ者を刺し貫き、押しつぶす武器となる。北部の民からは“氷の魔女”と呼ばれ恐れられるリサンドラだが、その実体は遥かに邪悪だ。彼女は世界に氷河期をもたらさんとたくらむ、自然の破壊者なのだ。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 5 |
| `magic` | 8 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 110 |
| `mp` | 475 |
| `mpperlevel` | 30 |
| `movespeed` | 325 |
| `armor` | 22 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.5 |
| `attackspeed` | 0.656 |

## アビリティ

- **パッシブ — アイスボーンへの服従：** リサンドラの近くで倒された敵チャンピオンは「氷の奴隷」になる。「氷の奴隷」は周囲の敵にスロウ効果を与え、少ししてから極度の寒さに砕け散り、周囲の対象に魔法ダメージを与える。

- **Q — アイスシャード：** 氷の槍を放ち、最初に命中した敵に魔法ダメージとスロウ効果を与える。槍は対象に当たると破片になって、背後にいる敵に同量の魔法ダメージを与える。
- **W — リング・オブ・フロスト：** 周囲にいる敵ユニットを氷漬けにして魔法ダメージを与え、スネア効果を付与する。
- **E — グラシアルパス：** 前進する氷の爪を召喚し、触れた敵ユニットに魔法ダメージを与える。効果時間内に再度発動すると、爪の位置へワープする。
- **R — フローズングレイブ：** 敵チャンピオンに使用した場合、対象は凍結してスタン状態になる。自身に使用すると、体が闇の氷で覆われ体力を回復するとともに、対象指定されず無敵になる。発動後対象の足元から闇の氷が広がり、触れた敵ユニットに魔法ダメージとスロウ効果を付与する。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Lissandra` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lissandra.png)
