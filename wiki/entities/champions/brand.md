---
title: "ブランド"
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
  - role-support
  - data-dragon
champion_id: "Brand"
champion_key: "63"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Brand.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Brand.png"
---

# ブランド

![[raw/assets/champions/Brand.png|128]]

## 基本情報

- **英字ID：** `Brand`
- **キー：** `63`
- **称号：** 復讐の炎
- **データversion：** `16.18.1`

## 紹介

ブランドとして知られる生命体は、かつてキーガン・ローデという名の凍てつくフレヨルドの部族の一員だったが、今では偉大な力への誘惑に溺れることへの教訓としてその存在を知られるようになった。伝説のワールドルーンのひとつを求めて、キーガンは仲間を裏切り、それを自らの手で奪った──その瞬間、彼は人間ではなくなった。魂は燃え去り、肉体は生きた炎の器となった。ブランドとなったその男は、いくつの命があっても足りない苦痛を味わわされることへの復讐を誓いながら、他のルーンを求めてヴァロランをさまよっている。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 2 |
| `magic` | 9 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 570 |
| `hpperlevel` | 105 |
| `mp` | 469 |
| `mpperlevel` | 21 |
| `movespeed` | 340 |
| `armor` | 24 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 11 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 57 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.681 |

## アビリティ

- **パッシブ — 炎上：** スキルで攻撃するたびに対象が炎上し、4秒かけて魔法ダメージを与える。この効果は3回までスタックする。炎上中の敵ユニットを倒すとマナを回復する。チャンピオンまたは大型モンスターに付与されたスタックが最大になると臨界点に達して2秒後に爆発し、周囲の敵にスキル命中時効果を付与して大ダメージを与える。

- **Q — 焦炎：** 指定方向に火の玉を放ち、最初に命中した敵ユニットに魔法ダメージを与える。炎上中の対象は、このスキルが命中するとスタン状態になる。
- **W — 烈火の柱：** 発動から一瞬遅れて指定地点に火柱を発生させ、範囲内の敵ユニットに魔法ダメージを与える。炎上中の対象は、火柱から受けるダメージが25%増加する。
- **E — 焼灼：** 強力な爆風で対象を攻撃し、周囲の敵も巻き込んで魔法ダメージを与える。炎上中の対象に爆風が命中すると、効果範囲が2倍になる。
- **R — 業火：** 指定した対象に最大5回まで跳ね返る強力な火炎弾を放つ。この火炎弾は自身と付近にいる敵の間で跳ね返り、敵に命中するたびに魔法ダメージを与える。この跳ね返りは、優先的に敵チャンピオンの「炎上」スタックを最大にしようとする。炎上中の対象に命中すると、短い間その対象にスロウを与える。

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

- **観測分類：** 中盤寄り
- **対象試合：** 270試合、全体勝率 51.9%
- **時間帯別勝率：** 〜20分 35.6%（n=45）、20〜25分 64.5%（n=31）、25〜30分 64.3%（n=56）、30〜35分 50.0%（n=64）、35分〜 48.6%（n=74）
- **最高帯：** 20〜25分（判定差 15.9ポイント）
- **判定根拠：** 中間帯が最高、端点との差 15.9%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Brand` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Brand.png)
