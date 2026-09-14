---
title: "モルデカイザー"
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
  - role-mage
  - data-dragon
champion_id: "Mordekaiser"
champion_key: "82"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Mage"
resource_type: "シールド"
image_path: "raw/assets/champions/Mordekaiser.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Mordekaiser.png"
---

# モルデカイザー

![[raw/assets/champions/Mordekaiser.png|128]]

## 基本情報

- **英字ID：** `Mordekaiser`
- **キー：** `82`
- **称号：** 鋼の魂奪者
- **データversion：** `16.18.1`

## 紹介

二度殺され、三度生まれたモルデカイザーは死霊術によって人の魂を拘束し、彼らを永遠の奴隷に変えてしまう、古の時代の残忍な武闘王である。彼の過去の覇業を覚えている者や、真の力を知る者はほとんど残っていないが、モルデカイザーを知るわずかな者たちは、彼が再び現れて生ける者も死せる者も支配してしまう日が来ることを恐れている。

## 分類

- **役割タグ：** `Fighter`、`Mage`
- **リソース種別：** シールド

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 6 |
| `magic` | 7 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 645 |
| `hpperlevel` | 104 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 335 |
| `armor` | 37 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 無窮の闇：** チャンピオンまたはモンスターに通常攻撃かスキルを3回命中させると、ダメージを与える強力なオーラを発生させ、移動速度が増加する。

- **Q — 滅魂の一撃：** 地面にメイスを叩きつけ、命中したすべての敵にダメージを与える。対象が1体のみだった場合はダメージが上昇する。
- **W — 不滅の鎧：** 与えたダメージや受けたダメージを蓄え、シールドを作り出す。シールドを消費して体力を回復することも可能。
- **E — 死の呪縛：** 範囲内にいるすべての敵を引き寄せる。
- **R — 死の国：** 獲物を別の次元へと引きずり込み、ステータスの一部を奪い取る。対象を倒した場合は、その対象が復活するまで奪ったステータスが維持される。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Mordekaiser` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Mordekaiser.png)
