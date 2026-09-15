---
title: "ケイトリン"
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
  - role-marksman
  - data-dragon
champion_id: "Caitlyn"
champion_key: "51"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Caitlyn.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Caitlyn.png"
---

# ケイトリン

![[raw/assets/champions/Caitlyn.png|128]]

## 基本情報

- **英字ID：** `Caitlyn`
- **キー：** `51`
- **称号：** ピルトーヴァーの保安官
- **データversion：** `16.18.1`

## 紹介

卓越した治安維持能力を有することで名高いケイトリン・キラマンは、都市に潜む犯罪者の撲滅を掲げるピルトーヴァーにとっての切り札的存在でもある。彼女はヴァイとパートナーを組むことが多く、激しい気性のヴァイとは対照的に冷静な彼女の存在が二人の釣り合いを保っている。この世に一つしか存在しないヘクステックライフルを持っているものの、彼女の真の武器は「進歩の都市」で犯罪を目論む愚か者たちに巧妙な罠を仕掛けるその知性だ。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 2 |
| `magic` | 2 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 107 |
| `mp` | 315 |
| `mpperlevel` | 40 |
| `movespeed` | 325 |
| `armor` | 27 |
| `armorperlevel` | 4.7 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 650 |
| `hpregen` | 3.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7.4 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 4 |
| `attackspeed` | 0.681 |

## アビリティ

- **パッシブ — ヘッドショット：** 通常攻撃数回ごと、または自身のトラップやネットにかけた対象に、クリティカル率によってダメージが増加する「ヘッドショット」を発射できる。トラップまたはネットにかけた対象に対しては「ヘッドショット」の射程が2倍になる。

- **Q — ピースメーカー：** 1秒間ライフルをチャージし、指定方向に貫通弾を発射する。貫通弾は命中した敵ユニットに物理ダメージを与える。 (2体目以降へのダメージは徐々に減少する)
- **W — ヨードルトラップ：** トラップを仕掛ける。トラップに触れた敵チャンピオンに1.5秒間スネア効果を付与し、可視状態にする。また、強化された「ヘッドショット」が1回可能になる。
- **E — L-90 カリバーネット：** 重たいネットを発射して、対象に魔法ダメージとスロウ効果を与える。自身はネットを発射した反動で、反対方向にとぶ。
- **R — ブルズアイ：** 1秒かけて狙いを定め、指定した敵チャンピオンを狙撃する。別の敵チャンピオンが射線を塞いだ場合、弾丸はそのチャンピオンに命中する。

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
- **対象試合：** 792試合、全体勝率 49.5%
- **時間帯別勝率：** 〜20分 43.3%（n=127）、20〜25分 53.0%（n=117）、25〜30分 49.2%（n=187）、30〜35分 50.6%（n=174）、35分〜 50.8%（n=187）
- **最高帯：** 20〜25分（判定差 9.7ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Caitlyn` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Caitlyn.png)
