---
title: "イラオイ"
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
  - role-tank
  - data-dragon
champion_id: "Illaoi"
champion_key: "420"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Illaoi.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Illaoi.png"
---

# イラオイ

![[raw/assets/champions/Illaoi.png|128]]

## 基本情報

- **英字ID：** `Illaoi`
- **キー：** `420`
- **称号：** 海の女司祭
- **データversion：** `16.18.1`

## 紹介

イラオイは頑強な巨体の持ち主だが、その不屈の信仰心はそれ以上に大きい。「大いなるクラーケン」の預言者である彼女は、巨大な黄金の偶像を使って敵の魂を肉体から引き剥がし、現実の知覚を打ち砕く。「ナーガケイボロスの真実の担い手」に挑むものは、すぐさまイラオイは一人で戦っているのではないということを思い知るだろう。そう──サーペントアイルの名状しがたい神が彼女とともにあり、戦うのだということを。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 6 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 656 |
| `hpperlevel` | 115 |
| `mp` | 350 |
| `mpperlevel` | 50 |
| `movespeed` | 350 |
| `armor` | 35 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9.5 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 旧神の預言者：** イラオイと、イラオイに「器」にされた者は、周囲の地形に一定時間ごとに触手を発生させる。触手は魂、「器」、イラオイの「過酷なる教訓」をくらった者を攻撃する。触手は命中すると敵に物理ダメージを与え、敵チャンピオンにダメージを与えた場合はイラオイを回復する。

- **Q — 触手の鉄槌：** 触手の与ダメージが増加する。発動すると、触手を叩きつけて物理ダメージを与える。
- **W — 過酷なる教訓：** 次の通常攻撃で対象に飛びかかって偶像で殴りつけ、物理ダメージを与える。周囲の触手にも対象を攻撃させる。
- **E — 魂の試練：** 偶像から触手を伸ばし、敵の肉体から魂を引きずり出して、自身の前に立たせる。魂は受けたダメージから一定の割合を、本体に反映させる。魂がキルされるか本体が遠く離れた場合、対象は「器」となり、その周囲に触手が発生するようになる。
- **R — 信仰震：** 偶像を地面に叩きつけて衝撃波を生み出し、周囲の敵に物理ダメージを与える。命中した敵チャンピオン1体ごとに、触手が1本発生する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中9位（上位15%）。体力656、物理防御35、攻撃力65、移動速度350。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 324試合、全体勝率 53.7%
- **時間帯別勝率：** 〜20分 59.3%（n=54）、20〜25分 50.0%（n=46）、25〜30分 66.2%（n=74）、30〜35分 44.7%（n=76）、35分〜 48.6%（n=74）
- **最高帯：** 25〜30分（判定差 21.5ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Illaoi` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Illaoi.png)
