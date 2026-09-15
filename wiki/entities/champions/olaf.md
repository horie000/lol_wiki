---
title: "オラフ"
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
  - role-tank
  - data-dragon
champion_id: "Olaf"
champion_key: "2"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Olaf.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Olaf.png"
---

# オラフ

![[raw/assets/champions/Olaf.png|128]]

## 基本情報

- **英字ID：** `Olaf`
- **キー：** `2`
- **称号：** 狂戦士
- **データversion：** `16.18.1`

## 紹介

制止不能な破壊の力、斧を振りかざすオラフが求めているのは栄光にあふれる戦いの中での自らの死だ。過酷な環境のフレヨルドのロクファール半島出身の彼は、ある日、安らかな死を迎えるという予言を受けた──それは一族の間では臆病者の死を意味し、大いなる屈辱とされていた。怒りに燃えた彼は自らの死を求め、自分にとどめを刺してくれる相手を探して、偉大な戦士や伝説の野獣たちを打ち負かしながら国中を暴れまわった。今ではウィンタークロウの容赦なき用心棒となった彼は、やがて訪れる偉大な戦いの中で自らの死に場所を探そうとしている。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 645 |
| `hpperlevel` | 119 |
| `mp` | 316 |
| `mpperlevel` | 50 |
| `movespeed` | 350 |
| `armor` | 35 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.7 |
| `attackspeed` | 0.72 |

## アビリティ

- **パッシブ — 狂戦士の怒り：** 減少体力に応じて攻撃速度とライフスティールが増加する。

- **Q — 斧投げ：** 指定地点の地面をめがけて斧を投げ、命中した敵にダメージを与えて、物理防御と移動速度を低下させる。斧を拾うと、このスキルのクールダウンがリセットされる。
- **W — 根性比べ：** 攻撃速度が増加し、シールドを獲得する。
- **E — 捨て身切り：** 体力を消費して強烈な攻撃を繰り出し、対象に確定ダメージを与える。対象を倒した場合は消費した体力が回復する。
- **R — ラグナロク：** 自動効果で物理防御と魔法防御が増加する。このスキルを発動すると、通常攻撃を続けている限りは行動妨害効果を受けなくなる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中4位（上位15%）。体力645、物理防御35、攻撃力68、移動速度350。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 判定保留（分母不足）
- **対象試合：** 95試合、全体勝率 40.0%
- **時間帯別勝率：** 〜20分 17.6%（n=17）、20〜25分 44.4%（n=9）、25〜30分 28.6%（n=21）、30〜35分 53.6%（n=28）、35分〜 50.0%（n=20）
- **最高帯：** 30〜35分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Olaf` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Olaf.png)
