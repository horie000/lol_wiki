---
title: "マオカイ"
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
  - role-tank
  - role-support
  - data-dragon
champion_id: "Maokai"
champion_key: "57"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Maokai.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Maokai.png"
---

# マオカイ

![[raw/assets/champions/Maokai.png|128]]

## 基本情報

- **英字ID：** `Maokai`
- **キー：** `57`
- **称号：** 歪みし樹人
- **データversion：** `16.18.1`

## 紹介

荒々しい巨大な樹人、マオカイは、シャドウアイルで自然界にあってはならない怨念に立ち向かう。大異変が起こり、故郷が破滅するのを目の当たりにした彼は、否応なく報復に生きる運命を背負わされた。幹の中心に浸透していた生命の水の力で、マオカイはこの災禍を生き延びた。かつて穏やかな自然界の精霊だった彼は、今や不死の亡霊という厄災をシャドウアイルから追放し、かつて美しかった故郷を取り戻すために猛然と戦っている。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 8 |
| `magic` | 6 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 665 |
| `hpperlevel` | 109 |
| `mp` | 375 |
| `mpperlevel` | 43 |
| `movespeed` | 335 |
| `armor` | 35 |
| `armorperlevel` | 5.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.125 |
| `attackspeed` | 0.8 |

## アビリティ

- **パッシブ — 魔樹液：** 通常攻撃が自身の体力を回復し、追加ダメージを与える。この効果にはある程度のクールダウンはあるが、スキルを使用するか、敵のスキルが自身に命中すると、このクールダウンが短縮される。

- **Q — 茨打ち：** 衝撃波で周囲の敵ユニットをノックバックして魔法ダメージとスロウ効果を与える。
- **W — 樹人の進撃：** 巨大な根の塊になって対象指定されなくなり、指定した対象に向かってダッシュする。対象に到達するとスネア効果を与える。
- **E — 苗木投げ：** 指定地点に苗木を投げて見張らせる。茂みの中ならより効果的になる。
- **R — 大地の捕縛：** 大量の茨や棘で出来た巨大な壁を召喚する。壁はゆっくりと前進しながら、通り道にいる敵ユニットにダメージとスネア効果を与える。

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

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 215試合、全体勝率 46.5%
- **時間帯別勝率：** 〜20分 44.4%（n=36）、20〜25分 45.0%（n=20）、25〜30分 48.9%（n=47）、30〜35分 47.3%（n=55）、35分〜 45.6%（n=57）
- **最高帯：** 25〜30分（判定差 4.5ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Maokai` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Maokai.png)
