---
title: "アジール"
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
  - role-marksman
  - data-dragon
champion_id: "Azir"
champion_key: "268"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Azir.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Azir.png"
---

# アジール

![[raw/assets/champions/Azir.png|128]]

## 基本情報

- **英字ID：** `Azir`
- **キー：** `268`
- **称号：** 砂塵の皇帝
- **データversion：** `16.18.1`

## 紹介

遥か昔、アジールは定命なるシュリーマの皇帝であり永遠の命を手にしかけた誇り高き男だったが、傲慢から生み出された裏切りによって、最大の偉業を成し遂げようとした瞬間に殺害されてしまった。しかし今、数千年の時を経て、彼は強大な力を持つ超越者として甦った。埋もれた都市が砂の中から姿を現した今、アジールはシュリーマを復興し、かつての栄光を取り戻そうとしている。

## 分類

- **役割タグ：** `Mage`、`Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 3 |
| `magic` | 8 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 575 |
| `hpperlevel` | 108 |
| `mp` | 320 |
| `mpperlevel` | 40 |
| `movespeed` | 330 |
| `armor` | 25 |
| `armorperlevel` | 5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 56 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — シュリーマの遺産：** アジールは敵や味方のタワーの残骸から「太陽の円盤」を召喚できる。

- **Q — 征服の勅命：** すべての砂塵兵を指定地点に集結させる。砂塵兵は進路上でぶつかった全ての敵ユニットに、魔法ダメージと1秒間のスロウ効果を与える。
- **W — 目覚めよ！：** アジールに代わって敵を攻撃する砂塵兵を1体召喚する。砂塵兵の射程距離内にいる対象にアジールが通常攻撃をすると、砂塵兵が対象の敵に向かって槍を突く。砂塵兵は直線上にいる敵ユニットすべてに魔法ダメージを与える。
- **E — 流砂の衝撃：** アジールが少しの間だけシールドを獲得して、指定した砂塵兵に向かってダッシュし、触れた敵ユニットにダメージを与える。敵チャンピオンに衝突するとその場で停止し、直ちに新たな砂塵兵のチャージを獲得する。
- **R — 皇帝の分砂嶺：** 兵士たちの壁を召喚する。兵士たちは前方に突進し、衝突した敵にダメージとノックバックを与えたあと、その場で敵の進行を防ぐ壁となる。

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
- **対象試合：** 61試合、全体勝率 45.9%
- **時間帯別勝率：** 〜20分 25.0%（n=8）、20〜25分 50.0%（n=10）、25〜30分 62.5%（n=16）、30〜35分 7.1%（n=14）、35分〜 76.9%（n=13）
- **最高帯：** 35分〜（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Azir` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Azir.png)
