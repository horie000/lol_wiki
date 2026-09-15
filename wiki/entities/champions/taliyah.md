---
title: "タリヤ"
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
champion_id: "Taliyah"
champion_key: "163"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Taliyah.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Taliyah.png"
---

# タリヤ

![[raw/assets/champions/Taliyah.png|128]]

## 基本情報

- **英字ID：** `Taliyah`
- **キー：** `163`
- **称号：** ストーンウィーバー
- **データversion：** `16.18.1`

## 紹介

タリヤは少女の好奇心と大人の責任感の間で揺れ動く、シュリーマ出身の流浪のメイジだ。強大さを増す自身の力の本質を知るためヴァロラン全域の旅を続けていた彼女だが、最近になって部族を守るためにシュリーマに戻ってきた。彼女の心の優しさを弱さであると見誤る者は、そのはつらつとした振る舞いの下に潜む、山をも動かす強い意志、そして大地さえ揺るがす断固たる精神のもとに、手痛い代償を払うことになる。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 7 |
| `magic` | 8 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 550 |
| `hpperlevel` | 104 |
| `mp` | 470 |
| `mpperlevel` | 30 |
| `movespeed` | 330 |
| `armor` | 18 |
| `armorperlevel` | 4.7 |
| `spellblock` | 28 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.36 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — ロックサーフィン：** 壁の近くで移動速度が増加する。

- **Q — スレッドボレー：** 自由に移動しながら、指定された方向に石の欠片を連続して発射する。「スレッドボレー」を使用すると、自身の足元に「加工された地面」を作り出す。「加工された地面」上でこのスキルを使用するとその地面を消費して、敵にスロウ効果を与える大きな石を1発投げる。
- **W — サイズミックシャーブ：** 一定範囲の地面を隆起させ、範囲内の敵を指定した方向に飛ばす。
- **E — アンレイベルアース：** 一定範囲内に石をばら撒き、スロウ効果を付与する。この範囲内で敵がダッシュするかノックバックさせられると、石が爆発して対象をスタンさせる。
- **R — ウィーバーウォール：** 長い壁を作り、その上を移動する。

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
- **対象試合：** 73試合、全体勝率 41.1%
- **時間帯別勝率：** 〜20分 30.0%（n=20）、20〜25分 50.0%（n=6）、25〜30分 36.4%（n=11）、30〜35分 38.1%（n=21）、35分〜 60.0%（n=15）
- **最高帯：** 35分〜（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Taliyah` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Taliyah.png)
