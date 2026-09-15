---
title: "フィオラ"
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
  - role-fighter
  - role-assassin
  - data-dragon
champion_id: "Fiora"
champion_key: "114"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Fiora.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Fiora.png"
---

# フィオラ

![[raw/assets/champions/Fiora.png|128]]

## 基本情報

- **英字ID：** `Fiora`
- **キー：** `114`
- **称号：** 高潔なるデュエリスト
- **データversion：** `16.18.1`

## 紹介

ヴァロランでもっとも恐れられる決闘士フィオラは、冷ややかで狡猾、そして目にも止まらぬ速さで強靭な両刃の剣レイピアを振るう。フィオラはデマーシア王国の名家であるローラン家に生まれた。ある時、一族を貶める事件が起こり、その結果フィオラは父親から一家の実権を奪うことになった。この事件によってローラン家の評判は地に落ちたが、フィオラは一族の名誉を回復してデマーシアの貴族として再起させるべく力を尽くしている。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 10 |
| `defense` | 4 |
| `magic` | 2 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 99 |
| `mp` | 300 |
| `mpperlevel` | 60 |
| `movespeed` | 345 |
| `armor` | 33 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 66 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.2 |
| `attackspeed` | 0.69 |

## アビリティ

- **パッシブ — デュエリスト・ダンス：** このチャンピオンの「急所」を特定している。「急所」を攻撃すると、自身は体力が回復して、移動速度が増加する。

- **Q — ファント：** 指定地点に向かってダッシュし、移動した地点から一番近くにいる敵ユニットをレイピアで突いて、物理ダメージと通常攻撃時効果を与える。
- **W — リポスト：** 短時間自身への全ての攻撃を受け流し、指定方向に鋭い突きを行う。反撃が命中した最初の敵チャンピオンにスロウ効果を付与する。このスキルで移動妨害効果を無効化した場合、スロウ効果のかわりにスタン効果を付与する。
- **E — ブレードワーク：** 次の2回の攻撃速度が増加し、追加効果が付与される。最初の攻撃は対象にスロウ効果を付与し、次の攻撃はクリティカルとなる。
- **R — グランドチャレンジ：** 敵チャンピオンの「急所」を4カ所特定して、その近くにいる間は移動速度が増加する。4カ所の「急所」をすべて攻撃するか、敵チャンピオンが倒れるまでに「急所」を1 カ所以上攻撃していると、その後数秒間、自身と味方の体力を回復するフィールドが展開される。

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
- **対象試合：** 78試合、全体勝率 60.3%
- **時間帯別勝率：** 〜20分 73.3%（n=15）、20〜25分 55.6%（n=9）、25〜30分 57.7%（n=26）、30〜35分 57.1%（n=14）、35分〜 57.1%（n=14）
- **最高帯：** 〜20分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Fiora` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Fiora.png)
