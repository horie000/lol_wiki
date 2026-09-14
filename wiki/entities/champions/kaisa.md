---
title: "カイ＝サ"
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
  - role-mage
  - data-dragon
champion_id: "Kaisa"
champion_key: "145"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Kaisa.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kaisa.png"
---

# カイ＝サ

![[raw/assets/champions/Kaisa.png|128]]

## 基本情報

- **英字ID：** `Kaisa`
- **キー：** `145`
- **称号：** 虚無を知る娘
- **データversion：** `16.18.1`

## 紹介

幼少期にヴォイドに囚われたカイ＝サは、不屈の精神と意志の力で生き延びた。経験を積んで卓越した狩人となった彼女であったが、一部の者にとってその存在は望まれぬ未来の先触れであった。不本意ながらヴォイド生命体の殻と共生関係を結んだカイ＝サ。自分を怪物と呼ぶ定命の者を許し、共に闇の勢力を打ち負かすのか、それとも他者のことなど忘れ、自分を置き去りにした世界をヴォイドに食い尽くさせるのか…彼女はやがて選択を迫られることになるだろう。

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 102 |
| `mp` | 345 |
| `mpperlevel` | 40 |
| `movespeed` | 335 |
| `armor` | 25 |
| `armorperlevel` | 4.2 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 525 |
| `hpregen` | 4 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8.2 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.8 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — ヴォイドスキン：** カイ＝サの通常攻撃はプラズマスタックを付与し、スタック数に応じて与える追加魔法ダメージが増加していく。味方の移動不能効果もプラズマスタックを付与する。さらに、アイテム購入によってアルティメット以外のスキルがアップグレードされる。

- **Q — イカシアの雨：** 多数のミサイルを乱射する。ミサイルは周囲の敵を追尾する。 共生兵器: 「イカシアの雨」がアップグレードされて、ミサイル数が増加する。
- **W — ヴォイドシーカー：** 遠距離ミサイルを発射して、命中した敵にプラズマスタックを付与する。 共生兵器: 「ヴォイドシーカー」がアップグレードされて、付与するスタック数が増加し、チャンピオンに当たるとクールダウンが短縮されるようになる。
- **E — スーパーチャージ：** 一時的に移動速度が増加し、その後攻撃速度が増加する。 共生兵器: 「スーパーチャージ」がアップグレードされて、一時的にインビジブル状態を獲得できるようになる。
- **R — キラーヴォイド：** 敵チャンピオンの近くまでダッシュする。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - アイテム購入により通常スキルがアップグレードされる。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kaisa` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kaisa.png)
