---
title: "ジャックス"
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
  - data-dragon
champion_id: "Jax"
champion_key: "24"
data_version: "16.18.1"
roles:
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Jax.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jax.png"
---

# ジャックス

![[raw/assets/champions/Jax.png|128]]

## 基本情報

- **英字ID：** `Jax`
- **キー：** `24`
- **称号：** 最強の武器使い
- **データversion：** `16.18.1`

## 紹介

ジャックスはイカシアで現存する最後の武器使いだ。独特な武器を使う技術と辛辣な皮肉で彼の右に出る者はいない。傲慢さにより解放されたヴォイドによって故郷が破壊され、ジャックスは仲間とともに残ったわずかな土地を守り抜くことを誓った。魔法が世界に広まり、この眠れる脅威が再び騒動を巻き起こす中、ジャックスはイカシアの最後の灯りを武器に、共に戦ってくれる仲間を求めて、出会ったあらゆる戦士に戦いを挑んでその実力を測りながらヴァロランを旅している。

## 分類

- **役割タグ：** `Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 5 |
| `magic` | 7 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 103 |
| `mp` | 339 |
| `mpperlevel` | 52 |
| `movespeed` | 350 |
| `armor` | 36 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8.2 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.4 |
| `attackspeed` | 0.638 |

## アビリティ

- **パッシブ — アサルトアタック：** ジャックスは通常攻撃ごとにスタックが溜まり、そのスタック数に応じて攻撃速度が増加する。

- **Q — リープストライク：** 対象のユニットに跳躍し、敵ユニットの場合は武器で攻撃する。
- **W — パワーバッシュ：** 武器に力を込め、次の攻撃で追加ダメージを与える。
- **E — カウンターストライク：** 短時間、その卓越した戦闘技術を用いてあらゆる通常攻撃を回避した後、すばやく反撃に転じて、周囲の敵ユニットにスタン効果を付与する。
- **R — ウェポングランドマスター：** 3回連続して通常攻撃を行うたびに、追加魔法ダメージを与える。また、このスキルを発動すると周囲にダメージを与え、決意を固めて短時間、物理防御と魔法防御が増加する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中3位（上位15%）。体力650、物理防御36、攻撃力68、移動速度350。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 393試合、全体勝率 51.9%
- **時間帯別勝率：** 〜20分 54.8%（n=62）、20〜25分 61.5%（n=52）、25〜30分 55.3%（n=114）、30〜35分 48.8%（n=84）、35分〜 42.0%（n=81）
- **最高帯：** 20〜25分（判定差 19.6ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Jax` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jax.png)
