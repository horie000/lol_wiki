---
title: "カ・サンテ"
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
  - role-tank
  - role-fighter
  - data-dragon
champion_id: "KSante"
champion_key: "897"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/KSante.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/KSante.png"
---

# カ・サンテ

![[raw/assets/champions/KSante.png|128]]

## 基本情報

- **英字ID：** `KSante`
- **キー：** `897`
- **称号：** ナズーマの誇り
- **データversion：** `16.18.1`

## 紹介

シュリーマの砂漠に位置する貴重なオアシス、ナズーマ。自らの故郷であるその地を守るため、尊大で勇敢なカ・サンテは巨大な獣や無慈悲な超越者と戦っている。だが、かつての相棒と仲たがいした彼は、民を率いるにふさわしい戦士となるには、成功を求めて身勝手になりがちな自己を抑えなければならないと悟る。それができて初めて、自らのうぬぼれに溺れることなく、民をおびやかす狂暴な怪物を倒すための知恵を見出せるのだ。

## 分類

- **役割タグ：** `Tank`、`Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 8 |
| `magic` | 7 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 625 |
| `hpperlevel` | 120 |
| `mp` | 320 |
| `mpperlevel` | 60 |
| `movespeed` | 330 |
| `armor` | 36 |
| `armorperlevel` | 5.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 2.1 |
| `attackrange` | 150 |
| `hpregen` | 9.5 |
| `hpregenperlevel` | 1 |
| `mpregen` | 7 |
| `mpregenperlevel` | 1 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.688 |

## アビリティ

- **パッシブ — 不屈の本能：** スキルが対象をマークする。マークされた対象への次の通常攻撃は、与えるダメージが増加する。 「オールアウト」中はあらゆる通常攻撃とスキルが与えるダメージが増加する。

- **Q — 破撃のエントーフォ：** 武器を叩きつけ、短い直線上にいた敵にダメージとスロウ効果を与える。 命中時に「破撃のエントーフォ」のスタックを獲得する。2スタックになると衝撃波を放って、敵を自身の方向に引き寄せる。 「オールアウト」中はクールダウンが短縮される。
- **W — 切り開く猛進：** 被ダメージを軽減させながらチャージし、その後ダッシュして敵をノックバックしてスタンさせる。 「オールアウト」中は与ダメージが増加するが、ノックバックとスタンを与えなくなる。
- **E — 辰砂の足取り：** ダッシュしてシールドを獲得する。味方を対象にした場合は距離が増加し、自身と味方の両方がシールドを獲得する。 「オールアウト」中はクールダウンが短縮され、速度が増加する。
- **R — オールアウト：** 敵をノックバックし、敵は通り道のあらゆる壁を通り抜けて弾き飛ばされる。その後、自身は「オールアウト」状態になり、その敵をダッシュして追いかけ、防御力が低下する代わりにダメージと体力回復量が大幅に増加し、スキルが変化する。

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
- **対象試合：** 173試合、全体勝率 46.2%
- **時間帯別勝率：** 〜20分 45.8%（n=24）、20〜25分 42.1%（n=19）、25〜30分 46.9%（n=49）、30〜35分 50.0%（n=44）、35分〜 43.2%（n=37）
- **最高帯：** 30〜35分（判定差 7.9ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.KSante` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/KSante.png)
