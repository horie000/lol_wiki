---
title: "カシオペア"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
tags:
  - champion
  - role-mage
  - data-dragon
champion_id: "Cassiopeia"
champion_key: "69"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Cassiopeia.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Cassiopeia.png"
---

# カシオペア

![[raw/assets/champions/Cassiopeia.png|128]]

## 基本情報

- **英字ID：** `Cassiopeia`
- **キー：** `69`
- **称号：** 毒蛇の抱擁
- **データversion：** `16.18.1`

## 紹介

カシオペアは相手を意のままに操って死に陥れる、恐ろしい妖女だ。彼女はノクサスの名門貴族であるデュ・クートウ家の美しい末娘だったが、古代の力を求めてシュリーマの地下墓地に足を踏み入れた時におぞましい墓守りに噛まれ、その毒が彼女を蛇のような捕食者へと変えてしまった。狡猾で機敏な姿となった彼女は夜の闇の中を這いずり回りながら、その邪悪な一瞥で敵を石化する。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 3 |
| `magic` | 9 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 98 |
| `mp` | 480 |
| `mpperlevel` | 40 |
| `movespeed` | 335 |
| `armor` | 18 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 53 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.5 |
| `attackspeed` | 0.647 |

## アビリティ

- **パッシブ — 妖艶な蛇行：** カシオペアは獲得するあらゆる移動速度ボーナスの効果が増加する。

- **Q — ノクサスブラスト：** 発動から一瞬遅れて指定地点に強力な毒を噴出させる。このスキルがチャンピオンに命中すると、自身の移動速度が増加する。
- **W — ミアズマ：** 多数の毒霧を発生させ、その範囲に足を踏み入れた敵にスロウ効果と釘付け効果に加え、軽度のダメージを与える。釘付け効果を受けた敵は、移動スキルを使用することができない。
- **E — ツインファング：** 毒に侵された対象に対してダメージが増加する攻撃を繰り出す。与えたダメージの一定割合分、自身の体力を回復する。また、このスキルで対象を倒すと自身のマナを回復する。
- **R — 石化の魔眼：** 石化の魔眼を開放し、扇形範囲内で自身のほうを向いている敵にスタン効果を付与する。 自身に背を向けている敵にはスロウ効果を付与する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 中盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 本分類で採用した序盤の基礎ステータス上位15%と、終盤の能力の蓄積成長・明示的なステータス連動のいずれにも当たらないため、中盤を暫定指定する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 判定保留（分母不足）
- **対象試合：** 74試合、全体勝率 35.1%
- **時間帯別勝率：** 〜20分 37.5%（n=8）、20〜25分 10.0%（n=10）、25〜30分 36.8%（n=19）、30〜35分 38.1%（n=21）、35分〜 43.8%（n=16）
- **最高帯：** 35分〜（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Cassiopeia` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Cassiopeia.png)
