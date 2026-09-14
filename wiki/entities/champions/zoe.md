---
title: "ゾーイ"
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
champion_id: "Zoe"
champion_key: "142"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Zoe.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zoe.png"
---

# ゾーイ

![[raw/assets/champions/Zoe.png|128]]

## 基本情報

- **英字ID：** `Zoe`
- **キー：** `142`
- **称号：** 超常の遊び
- **データversion：** `16.18.1`

## 紹介

いたずら、想像、変化を具現化する存在であるゾーイは、時空を駆け抜けて霊峰ターゴンのメッセージ──世界の再編を招く出来事の到来──を告げる。彼女の存在は、現実を支配する聖なる数学に歪みを生み出し、時に激変を引き起こす。意識的にではないし、悪意もない。だからこそゾーイはたっぷりと時間をかけて遊びに集中し、定命の者をからかい、あるいはただ楽しいからという理由で、平然とその義務を果たせるのだろう。ゾーイに出会うと気分が高揚して前向きな気持ちになるが、実際にはそれは常に危険と隣り合わせだ。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 7 |
| `magic` | 8 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 106 |
| `mp` | 425 |
| `mpperlevel` | 25 |
| `movespeed` | 340 |
| `armor` | 21 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.65 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — スパークル！：** スキル使用後、次に行う通常攻撃が追加魔法ダメージを与える。

- **Q — パドルスター：** 途中で進行方向を変えられる星を飛ばす。真っすぐ飛んだ距離の長さに応じてダメージが増加する。
- **W — スペルシーフ：** 敵のサモナースペルと発動効果アイテムのかけらを拾って1回使用できる。サモナースペルを使用するごとに最大3つの魔法の弾を最も近くにいる対象に向かって飛ばす。
- **E — スリープバブル：** 対象に眠気を与えてから眠らせる。眠っている間は、対象の魔法防御が低下する。眠りを覚ます攻撃は2倍のダメージを与える(上限あり)。
- **R — ポータルジャンプ：** 近くの指定した位置に1秒間ブリンクして、もとの位置に戻る。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Zoe` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zoe.png)
