---
title: "ボリベア"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "Volibear"
champion_key: "106"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Volibear.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Volibear.png"
---

# ボリベア

![[raw/assets/champions/Volibear.png|128]]

## 基本情報

- **英字ID：** `Volibear`
- **キー：** `106`
- **称号：** 無慈悲の嵐
- **データversion：** `16.18.1`

## 紹介

彼を崇敬する者にとって、ボリベアは嵐を体現した存在だ。破壊的で、野蛮で、頑固なまでに意思が固く、彼は定命の者たちがフレヨルドのツンドラに足を踏み入れる前からそこに存在しており、彼と半神の同族たちが創り出したその土地を獰猛に守ろうとしている。ボリベアは文明とそれがもたらす弱さに激しい憎悪を募らせており、この土地を野生のままで自由に血が流されていた昔の姿に戻すために、敵対する者すべてに自身の爪と牙と容赦なき雷鳴を向けて戦いを挑む。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 7 |
| `magic` | 4 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 104 |
| `mp` | 350 |
| `mpperlevel` | 70 |
| `movespeed` | 340 |
| `armor` | 35 |
| `armorperlevel` | 5.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 6.25 |
| `mpregenperlevel` | 0.5 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 無慈悲の嵐：** 通常攻撃およびスキルの使用で攻撃速度が増加していき、最終的に通常攻撃が周囲の敵に追加魔法ダメージを与えるようになる。

- **Q — 稲妻の猛攻：** 敵に向かう際の移動速度が増加し、発動後最初に通常攻撃を行った対象にスタン効果とダメージを与える。
- **W — 激昂の斬撃：** 敵にダメージと通常攻撃時効果を与えてマークする。同じ対象にもう一度発動すると追加ダメージを与えて自身の体力を回復する。
- **E — 天破の一撃：** 指定地点に雷を落として周囲の敵にダメージとスロウ効果を与え、自身が範囲内にいた場合はシールドを獲得する。
- **R — 嵐を起こす者：** 指定地点に飛びかかって踏みつけた敵にスロウ効果とダメージを与え、自身は体力が増加する。着地地点の近くにある敵のタワーは一時的に無効化される。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中26位（上位15%）。体力650、物理防御35、攻撃力65、移動速度340。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Volibear` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Volibear.png)
