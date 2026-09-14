---
title: "アッシュ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-marksman
  - role-support
  - data-dragon
champion_id: "Ashe"
champion_key: "22"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Ashe.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ashe.png"
---

# アッシュ

![[raw/assets/champions/Ashe.png|128]]

## 基本情報

- **英字ID：** `Ashe`
- **キー：** `22`
- **称号：** 氷の射手
- **データversion：** `16.18.1`

## 紹介

アッシュはアヴァローサンのアイスボーンの戦母であり、北部でもっとも数の多い部隊を率いている。先祖から受け継いだ魔力を手に入れて真なる氷の弓で戦う彼女は、ストイックで知的な理想家だが、リーダーとしての自らの役割には戸惑いがある。部族の人間が彼女は生まれ変わったアヴァローサの伝説の英雄だと信じる中、アッシュは古代から続く部族の土地を取り戻して、もう一度フレヨルドを統一しようと望んでいる。

## 分類

- **役割タグ：** `Marksman`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 3 |
| `magic` | 2 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 101 |
| `mp` | 280 |
| `mpperlevel` | 35 |
| `movespeed` | 325 |
| `armor` | 26 |
| `armorperlevel` | 4.6 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 600 |
| `hpregen` | 3.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.65 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — フロストショット：** 通常攻撃が命中した対象にスロウ効果を付与する。さらにその対象に通常攻撃をすると、ダメージが増加する。 アッシュのクリティカルは追加ダメージを一切与えない代わりに、対象により強力なスロウ効果を付与する。

- **Q — レンジャーフォーカス：** 通常攻撃によって「フォーカス」のスタックがたまるようになり、スタックが最大になるとすべて消費して「レンジャーフォーカス」を使用できる。効果時間中は攻撃速度が増加し、通常攻撃が強力な「疾風の矢」に変化する。
- **W — ボレー：** 矢を扇状に発射し、命中した敵にダメージを与える。同時に、命中した相手に「フロストショット」のレベルに応じたスロウ効果を付与する。
- **E — スカウトホーク：** マップ上の指定した地点へ「ホークスピリット」を放ち、視界を確保することができる。
- **R — クリスタルアロー：** アッシュが一直線に飛翔する氷の矢を放つ。最初に命中した敵チャンピオンにダメージを与え、飛距離に応じたスタン効果を付与する。氷の矢は砕けると同時に周囲の敵ユニットにもダメージを与え、移動速度を低下させる。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Ashe` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ashe.png)
