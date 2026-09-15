---
title: "オーロラ"
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
  - role-assassin
  - data-dragon
champion_id: "Aurora"
champion_key: "893"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Aurora.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Aurora.png"
---

# オーロラ

![[raw/assets/champions/Aurora.png|128]]

## 基本情報

- **英字ID：** `Aurora`
- **キー：** `893`
- **称号：** 世界の狭間の魔女
- **データversion：** `16.18.1`

## 紹介

生まれたときから、オーロラは精霊界と物質世界の間を行き来する独自の能力で人生を歩んでいた。精霊界の住民たちに関する知識を手に入れようと、故郷を離れて研究を進めていたとき、彼女は時とともに心が捻じれて自我を失い、はぐれた半神に遭遇した。彼の絶望を目撃し、オーロラはこの暴れる仲間が忘れてしまった自我を取り戻す方法を見つける覚悟を決めた──その旅のなかで、彼女はフレヨルドの辺境の地を訪ねてまわることとなった。

## 分類

- **役割タグ：** `Mage`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 4 |
| `magic` | 8 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 607 |
| `hpperlevel` | 110 |
| `mp` | 475 |
| `mpperlevel` | 30 |
| `movespeed` | 335 |
| `armor` | 23 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 53 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.668 |

## アビリティ

- **パッシブ — 精霊の解放：** スキルおよび通常攻撃で敵にダメージを与えると、その敵を祓い、精霊を解放する。解放された精霊はオーロラの背後に付いてまわり、オーロラの体力を回復する。

- **Q — 折れ重なる魔法：** 呪いの塊を放ち、それが触れたすべての敵に呪いをかける。スキルを再発動すると呪いを自身のもとへ呼び戻し、その際に触れた敵にダメージを与える。
- **W — ベールを越えて：** 指定方向に飛び跳ね、着地時に精霊界に入って、少しの間、インビジブル状態になり、移動速度が増加する。
- **E — ウィアーディング：** 二つの領域を融合し、激しくほとばしる精霊魔法を放つ。敵に魔法ダメージとスロウ効果を与え、自身は安全を確保するために後方に飛び跳ねる。
- **R — 世界の狭間：** 指定方向に飛び跳ね、波動を放ち、それが触れたすべての敵にダメージとスロウ効果を与える。その後、敵にスロウ効果を与えるエリアを作り出し、自身はそのエリアの端から別の端にテレポートできるようになる。

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
- **対象試合：** 186試合、全体勝率 51.6%
- **時間帯別勝率：** 〜20分 55.9%（n=34）、20〜25分 52.2%（n=23）、25〜30分 41.3%（n=46）、30〜35分 50.0%（n=44）、35分〜 61.5%（n=39）
- **最高帯：** 35分〜（判定差 20.2ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Aurora` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Aurora.png)
