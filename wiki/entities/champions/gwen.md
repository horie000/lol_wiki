---
title: "グウェン"
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
  - data-dragon
champion_id: "Gwen"
champion_key: "887"
data_version: "16.18.1"
roles:
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Gwen.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gwen.png"
---

# グウェン

![[raw/assets/champions/Gwen.png|128]]

## 基本情報

- **英字ID：** `Gwen`
- **キー：** `887`
- **称号：** 聖なるお針子
- **データversion：** `16.18.1`

## 紹介

魔法によって人間となり、命を与えられた元人形のグウェンは、かつて自分を生み出したまさにその道具を携えている。一歩ごとに作り手の愛の重みを感じながら、あらゆることに感謝を忘れない。グウェンが意のままに操る「聖なる霧」は、古代の防護魔法であり、自身が手にしたハサミ、針、そして縫い糸もその祝福を授かっている。目新しいものに囲まれながらも、グウェンは壊れた世界に生き残っている善意を守るため、大いなる喜びをもって戦い続けようと固く誓っている。

## 分類

- **役割タグ：** `Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 4 |
| `magic` | 5 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 115 |
| `mp` | 330 |
| `mpperlevel` | 40 |
| `movespeed` | 340 |
| `armor` | 39 |
| `armorperlevel` | 4.9 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.25 |
| `attackspeed` | 0.69 |

## アビリティ

- **パッシブ — 裁断：** 通常攻撃が対象の体力に応じて追加魔法ダメージを与える。この効果でチャンピオンに与えたダメージの一定割合を体力として回復する。

- **Q — チョキチョキッ！：** ハサミで扇状の範囲を最大6回切りつけて魔法ダメージを与える。範囲の中心にいるユニットには確定ダメージを与え、切るたびに固有スキルの効果を適用する。
- **W — 聖なる霧：** 霧を召喚して、霧の外にいる敵から身を守る。霧の中にいる敵からしか対象指定されない。
- **E — スキップスラッシュ：** 短い距離をダッシュして数秒間、攻撃速度と射程が増加し、通常攻撃時効果で魔法ダメージを与える。効果時間中に通常攻撃を命中させた場合、このスキルのクールダウンが一定割合解消される。
- **R — 針仕事：** 針を投げ、命中した敵にスロウ効果と魔法ダメージを与えて、チャンピオンに命中した場合は「裁断」を適用する。 このスキルは最大2回まで再発動可能で、再発動するたびに投げる針の本数とダメージが増加する。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Gwen` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gwen.png)
