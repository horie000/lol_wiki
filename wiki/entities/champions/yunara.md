---
title: "ユナラ"
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
  - role-marksman
  - data-dragon
champion_id: "Yunara"
champion_key: "804"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Yunara.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yunara.png"
---

# ユナラ

![[raw/assets/champions/Yunara.png|128]]

## 基本情報

- **英字ID：** `Yunara`
- **キー：** `804`
- **称号：** 揺るがぬ誓い
- **データversion：** `16.18.1`

## 紹介

アイオニアへの揺るぎない忠誠心を胸にユナラは精霊界に身を隠し、均衡の守人に代々受け継がれる遺物「アイオン・エルナ」で修行を重ねた。あらゆるものを犠牲にしてなお、調和を乱すものを排し、争いを絶つという誓いは揺るがず、その信仰もまた決して失われていない。だが、彼女を待ち受ける世界と、再び蘇った古の脅威の影は、ユナラの決意のすべてを試すことになる。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 2 |
| `magic` | 0 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 590 |
| `hpperlevel` | 110 |
| `mp` | 275 |
| `mpperlevel` | 45 |
| `movespeed` | 325 |
| `armor` | 25 |
| `armorperlevel` | 4.4 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 575 |
| `hpregen` | 4 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.65 |

## アビリティ

- **パッシブ — 始まりの地への誓い：** クリティカル攻撃が追加魔法ダメージを与える。

- **Q — 精神修養：** 攻撃速度が増加し、通常攻撃時効果で追加ダメージを与え、通常攻撃が周囲の敵に拡散する。
- **W — 裁きの弧/滅びの弧：** 回転する珠を撃ち出し、敵にダメージとスロウ効果を与える。超越状態では、レーザー状に精霊魔法を発射して、敵にダメージとスロウ効果を与える。
- **E — カンメイの歩み/触れ得ぬ影：** 移動速度が増加し、ゴースト化する。超越状態では、代わりに指定方向にダッシュする。
- **R — 自己超越：** 超越状態になり、通常スキルがアップグレードされる。

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
- **対象試合：** 496試合、全体勝率 50.4%
- **時間帯別勝率：** 〜20分 52.3%（n=86）、20〜25分 48.6%（n=74）、25〜30分 50.5%（n=107）、30〜35分 54.0%（n=126）、35分〜 45.6%（n=103）
- **最高帯：** 30〜35分（判定差 8.3ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Yunara` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yunara.png)
