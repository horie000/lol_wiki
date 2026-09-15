---
title: "ニーラ"
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
champion_id: "Nilah"
champion_key: "895"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Nilah.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nilah.png"
---

# ニーラ

![[raw/assets/champions/Nilah.png|128]]

## 基本情報

- **英字ID：** `Nilah`
- **キー：** `895`
- **称号：** 放たれし喜び
- **データversion：** `16.18.1`

## 紹介

ニーラは遠く離れた土地で苦行を続けていた戦士で、世界で最も恐ろしく、最も巨大な敵を見つけ、それに挑戦して倒すことを求めている。彼女は長く閉じ込められていた歓喜の悪魔と出会ったことで力を手に入れたため、常に絶え間ない歓喜の感情に満たされているが、彼女が手に入れた強大な力と比べれば大した代償ではない。ニーラは流体である悪魔を比類なき力を持つ刃に変え、遠い昔に忘れられていた古代の脅威に堂々と立ち向かう。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 4 |
| `magic` | 4 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 570 |
| `hpperlevel` | 101 |
| `mp` | 350 |
| `mpperlevel` | 35 |
| `movespeed` | 340 |
| `armor` | 27 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 225 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 8.2 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.25 |
| `attackspeed` | 0.697 |

## アビリティ

- **パッシブ — 終わりなき喜び：** ラストヒットしたミニオンから得る経験値が増加する。また、周囲の味方の体力回復およびシールド効果を強化し、その味方と共有する。

- **Q — 形なき刃：** 鞭の刃を指定した方向に打ちつけ、直線上にいるすべての敵にダメージを与える。この攻撃が命中すると、少しの間だけ射程距離が増加する。
- **W — 歓喜のヴェール：** 霧に身を包み、移動速度が増加して、あらゆる通常攻撃を軽やかに回避する。また、霧の効果時間中に接触したすべての味方が、この効果を獲得する。
- **E — 流撃：** 対象に向かって勢いよくダッシュし、その際に接触したすべての敵にダメージを与える。
- **R — アポテオシス：** あふれ出る喜びの中で鞭の刃を振り回し、周囲の敵にダメージを与えてから、自身の方向に引き寄せる。

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
- **対象試合：** 32試合、全体勝率 50.0%
- **時間帯別勝率：** 〜20分 71.4%（n=7）、20〜25分 50.0%（n=4）、25〜30分 33.3%（n=6）、30〜35分 55.6%（n=9）、35分〜 33.3%（n=6）
- **最高帯：** 〜20分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Nilah` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nilah.png)
