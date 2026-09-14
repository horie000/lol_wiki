---
title: "タム・ケンチ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-tank
  - role-support
  - data-dragon
champion_id: "TahmKench"
champion_key: "223"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/TahmKench.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/TahmKench.png"
---

# タム・ケンチ

![[raw/assets/champions/TahmKench.png|128]]

## 基本情報

- **英字ID：** `TahmKench`
- **キー：** `223`
- **称号：** 川の王様
- **データversion：** `16.18.1`

## 紹介

タム・ケンチは過去に様々な名前で呼ばれてきた悪魔であり、ルーンテラの水路を移ろいながら、尽きることのない食欲を満たすために他者を餌食にしている。彼は非常に魅力的で誇り高き存在の振りをして、自信たっぷりな態度で物質世界を放浪しながら不用心な獲物を探している。彼の長い舌は頑丈な鎧に身を包んだ戦士ですら離れた場所から気絶させることが可能で、音を立てる奈落のような彼の腹の中に納まれば、そこから戻れる可能性はほとんどない。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 9 |
| `magic` | 6 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 103 |
| `mp` | 325 |
| `mpperlevel` | 50 |
| `movespeed` | 335 |
| `armor` | 39 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 1 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 56 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 舌慣らし：** 巨大な体躯から繰り出す通常攻撃に、自身の合計体力に応じた追加ダメージを付与する。ダメージを受けた敵チャンピオンには「舌慣らし」がスタックされ、3スタックたまった敵チャンピオンに対しては「丸呑み」を使えるようになる。

- **Q — 味見：** 舌をムチを打つように放つ。最初に命中したユニットにダメージを与え、スロウ効果を付与する。対象が敵チャンピオンだった場合は自分の体力を回復する。 敵チャンピオンに「舌慣らし」のスタックを付与する。「舌慣らし」を3スタック付与しているチャンピオンにこのスキルを使用すると、スタックを消費して対象をスタンさせる。
- **W — 川潜り：** 水中に潜ってから指定地点に現れ、範囲内のすべての敵にダメージを与えてノックアップさせる。
- **E — ゆるゆる皮膜：** 自動効果: 受けたダメージの一定割合を蓄え、非戦闘時にそれに応じて体力を回復する。 発動効果: 蓄えていた全ダメージを一時的なシールドに変換する。
- **R — 丸呑み：** 数秒間チャンピオンを丸呑みし、敵には魔法ダメージを与え、味方にはシールドを付与する。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.TahmKench` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/TahmKench.png)
