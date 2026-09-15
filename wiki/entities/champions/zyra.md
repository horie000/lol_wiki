---
title: "ザイラ"
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
champion_id: "Zyra"
champion_key: "143"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Zyra.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zyra.png"
---

# ザイラ

![[raw/assets/champions/Zyra.png|128]]

## 基本情報

- **英字ID：** `Zyra`
- **キー：** `143`
- **称号：** 茨の目覚め
- **データversion：** `16.18.1`

## 紹介

古代の魔法の大惨事の中で生まれたザイラは自然の怒りが具現化した存在であり、人間と植物が融合した妖艶な姿で、一歩進むたびに新たな生命を生み出していく。彼女はヴァロランに住む定命の者たちを自分の種から生まれた子供たちの餌食としか見ておらず、恐ろしい棘を使って平気な顔で彼らを抹殺している。その真の目的は定かではないが、ザイラは世界中を歩き回り、本能の赴くままに根を生やして繁殖しては、他のあらゆる生物を絡めとって絞め殺している。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 3 |
| `magic` | 8 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 574 |
| `hpperlevel` | 93 |
| `mp` | 418 |
| `mpperlevel` | 25 |
| `movespeed` | 340 |
| `armor` | 29 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 575 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 53 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.11 |
| `attackspeed` | 0.681 |

## アビリティ

- **パッシブ — 茨の楽園：** 定期的に自身の周囲に種を発生させる。その周期はレベルに応じて速くなる。種の近くで「死華の棘」または「捕縛の根」を使用すると種は植物に成長し、自身の味方となって戦う。

- **Q — 死華の棘：** 太いツルが地中に広がって鋭いトゲを生やし、範囲内の敵に魔法ダメージを与える。「死華の棘」を種の近くで使用すると、遠距離の敵を射撃する「棘吹草」に成長させる。
- **W — 狂い咲き：** 最大60秒間持続する種を生やす。種の近くで「死華の棘」または「捕縛の根」を使用すると種は植物に成長し、味方として戦う。同時に複数の種を蓄えておくことが可能で、敵ユニットを倒すと「狂い咲き」のチャージ時間が短縮される。
- **E — 捕縛の根：** 地中から伸びる巨大なツタが対象を絡めとり、ダメージを与え移動不能にする。「捕縛の根」を種の近くで使用すると「棘鞭草」に成長させ、近距離の敵を攻撃しダメージを与え、移動速度を低下させる。
- **R — 茨のゆりかご：** 指定地点から茨を放射状に成長させて範囲内の敵にダメージを与え、茨が地中に戻る際に触れた敵をノックアップさせる。茨の範囲内の植物は怒り狂う。

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
- **対象試合：** 372試合、全体勝率 53.2%
- **時間帯別勝率：** 〜20分 57.4%（n=61）、20〜25分 47.1%（n=51）、25〜30分 54.5%（n=77）、30〜35分 54.1%（n=74）、35分〜 52.3%（n=109）
- **最高帯：** 〜20分（判定差 10.3ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Zyra` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zyra.png)
