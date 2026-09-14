---
title: "ジャーヴァンⅣ"
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
champion_id: "JarvanIV"
champion_key: "59"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/JarvanIV.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/JarvanIV.png"
---

# ジャーヴァンⅣ

![[raw/assets/champions/JarvanIV.png|128]]

## 基本情報

- **英字ID：** `JarvanIV`
- **キー：** `59`
- **称号：** デマーシアの儀範
- **データversion：** `16.18.1`

## 紹介

ライトシールド王家の後継ぎであるジャーヴァン王子はデマーシアの王位継承者だ。母国の最大の美徳の鑑となるように育てられた彼は、寄せられる大きな期待に応えるために、最前線で戦いたいという自身の欲望を抑える必要がある。ジャーヴァンは恐れ知らずな勇敢さと自己を省みない強い決意で部隊を鼓舞し、王家の名誉にかけて未来の指導者たるべき力を示している。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 8 |
| `magic` | 3 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 104 |
| `mp` | 300 |
| `mpperlevel` | 55 |
| `movespeed` | 340 |
| `armor` | 36 |
| `armorperlevel` | 4.6 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 6.5 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 武魂の律動：** 最初の通常攻撃が命中する際、対象の現在体力に応じた追加物理ダメージを与えるが、同一の敵に対しては数秒間に一度しか発動できない。

- **Q — ドラゴンストライク：** 槍を伸ばして貫通した敵ユニットに物理ダメージを与え、物理防御を低下させる。さらに「デマーシアの旗印」にこのスキルが命中した場合、自身をそこまで引き寄せ、通り道にいた敵をノックアップさせる。
- **W — ゴールデンイージス：** デマーシアの歴代王の力を借りて、ダメージを防ぐシールドを発生させ、周囲の敵にスロウを与える。
- **E — デマーシアの旗印：** デマーシアの誇りを胸に抱き、自動効果で攻撃速度が増加するようになる。発動すると指定地点にデマーシア軍の旗を投げ、地面に突き刺さると同時に魔法ダメージを与える。この旗は味方を鼓舞し、自身を含む味方チャンピオンの攻撃速度が、自動効果と同じ分だけ増加する。
- **R — 決戦場：** ジャーヴァンⅣが対象に向かって雄々しく跳躍して、物理ダメージを与える。着地と同時に猛烈な力で地面を踏みつけ、周囲の地形を変化させて対象を囲い込む。周囲の敵も着地時にダメージを受ける。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.JarvanIV` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/JarvanIV.png)
