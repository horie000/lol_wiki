---
title: "アイバーン"
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
  - role-support
  - role-mage
  - data-dragon
champion_id: "Ivern"
champion_key: "427"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Ivern.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ivern.png"
---

# アイバーン

![[raw/assets/champions/Ivern.png|128]]

## 基本情報

- **英字ID：** `Ivern`
- **キー：** `427`
- **称号：** 豊緑の神秘
- **データversion：** `16.18.1`

## 紹介

「豊緑の神秘」の名で広く知られるアイバーン・ブランブルフットは、ルーンテラの森を渡り歩きながら行く先々で生命の種を蒔く、奇妙な半人半樹である。彼は自然界の秘密に精通しており、ありとあらゆる草木、花鳥、昆虫たちと深い友情を結んでいる。アイバーンは荒野をさすらい、出会うもの皆に奇妙な知恵を授け、森に滋養を与え、時には口の軽いチョウチョを信用して秘密を教えてしまう。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 5 |
| `magic` | 7 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 99 |
| `mp` | 450 |
| `mpperlevel` | 60 |
| `movespeed` | 330 |
| `armor` | 27 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 475 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.85 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 50 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.4 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — モリノトモダチ：** アイバーンはエピック以外のモンスターに対して、攻撃することも攻撃されることもない。ジャングルキャンプに時間が経つことで成長する小さな魔法の森を作ることができる。小さな森が完全に成長すると、モンスターを逃がしてゴールドと経験値を獲得できる。

- **Q — ネッコナゲ：** 魔法の根を飛ばし、命中した敵ユニットにダメージを与えてスネア状態にする。味方はスネア状態になった敵に向かってダッシュできる。
- **W — シゲミヅクリ：** 茂みの中にいると、自身および周囲の味方の通常攻撃が追加魔法ダメージを与える。このスキルを発動すると茂みを作り出せる。
- **E — タネバクダン：** 味方にシールドを付与する。少しすると爆発して、周囲の敵にスロウ効果とダメージを与える。敵に命中しなかった場合は、シールドがリフレッシュされる。
- **R — デイジー！：** 守護者である友達のデイジーを召喚して、一緒に戦わせる。再発動するとデイジーに攻撃または移動を指示できる。

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
- **対象試合：** 34試合、全体勝率 47.1%
- **時間帯別勝率：** 〜20分 16.7%（n=6）、20〜25分 33.3%（n=6）、25〜30分 40.0%（n=5）、30〜35分 70.0%（n=10）、35分〜 57.1%（n=7）
- **最高帯：** 30〜35分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Ivern` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ivern.png)
