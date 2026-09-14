---
title: "ワーウィック"
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
  - role-tank
  - data-dragon
champion_id: "Warwick"
champion_key: "19"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Warwick.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Warwick.png"
---

# ワーウィック

![[raw/assets/champions/Warwick.png|128]]

## 基本情報

- **英字ID：** `Warwick`
- **キー：** `19`
- **称号：** 解き放たれたゾウンの激憤
- **データversion：** `16.18.1`

## 紹介

ワーウィックはゾウンの灰色の路地を徘徊する怪物だ。苦痛を伴う実験によって変性した彼の肉体に融合された、ポンプやシリンダーで構成された複雑なシステムが、錬金術的に合成された憤怒を彼の血流に送り込んでいる。物陰から飛び出しては、都市の深部を脅かしている犯罪者を餌食とするのだ。ワーウィックは血に引き寄せられ、その匂いは彼の正気を失わせる。血を流す者は、決して彼から逃れることはできない。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 99 |
| `mp` | 280 |
| `mpperlevel` | 35 |
| `movespeed` | 335 |
| `armor` | 33 |
| `armorperlevel` | 4.4 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 4 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7.45 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.638 |

## アビリティ

- **パッシブ — 永遠の渇き：** 通常攻撃が追加魔法ダメージを与える。自身の体力が50%未満の場合、追加魔法ダメージと同量の体力を回復する。自身の体力が25%未満の場合、この回復効果は3倍になる。

- **Q — 野獣の牙：** 前方にダッシュして対象に噛みつき、対象の最大体力に応じたダメージを与え、与えたダメージに応じて自身の体力を回復する。
- **W — 血の追跡：** 体力が50%未満の敵ユニットを感知して、その敵ユニットに向かう際に移動速度と攻撃速度が増加する。その敵ユニットの体力が25%未満に低下した場合は、ワーウィックが狂乱状態になってこれらの効果が3倍になる。
- **E — 怒りの咆哮：** 2.5秒間、受けるダメージが減少する。効果の終了時、またはスキルを再発動すると、咆哮をあげて周囲の敵ユニットを1秒間逃走させる。
- **R — 絶狼牙連撃：** 指定方向にジャンプして、最初に接触した敵チャンピオンに1.5秒間サプレッション効果を与える(増加した移動速度に応じて射程が拡大)。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Warwick` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Warwick.png)
