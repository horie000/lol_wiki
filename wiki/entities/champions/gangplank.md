---
title: "ガングプランク"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
tags:
  - champion
  - role-fighter
  - data-dragon
champion_id: "Gangplank"
champion_key: "41"
data_version: "16.18.1"
roles:
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Gangplank.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gangplank.png"
---

# ガングプランク

![[raw/assets/champions/Gangplank.png|128]]

## 基本情報

- **英字ID：** `Gangplank`
- **キー：** `41`
- **称号：** 大海原の大災厄
- **データversion：** `16.18.1`

## 紹介

気まぐれにして残忍、「略奪の王」を名乗るもその玉座を追われたガングプランクの名は、七つの海に轟き恐れられていた。かつてビルジウォーターの港町を牛耳っていた彼だが、その座を奪われた今、逆に彼はさらに危険な存在になったと考える者もいる。誰かにこの街を奪われるくらいなら、ガングプランクは再びビルジウォーターを血の海にしてやるだろう。ピストル、カトラス、火薬の樽を携え、彼は何としてでも奪われたものを取り返すつもりだ。

## 分類

- **役割タグ：** `Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 6 |
| `magic` | 4 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 114 |
| `mp` | 280 |
| `mpperlevel` | 60 |
| `movespeed` | 345 |
| `armor` | 31 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.2 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 背水の銃剣：** 数秒毎に近接攻撃で敵に火を点ける。

- **Q — 偽りの発砲：** 対象を撃ち抜き、そのユニットを倒すことでゴールドを奪うことができる。
- **W — 壊血病治癒：** オレンジをかじり、自身が受けている行動妨害効果を解消し、体力を回復する。
- **E — 火薬樽：** 指定地点に火薬樽を設置する。火薬樽はガングプランクが攻撃すると爆発し、範囲内の敵にその攻撃と同じダメージを与え、スロウ効果を付与する。
- **R — 一斉砲撃：** 海賊船に合図を送って指定したエリアを砲撃させ、効果範囲内の敵にスロウ効果とダメージを与える。

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
- **対象試合：** 72試合、全体勝率 43.1%
- **時間帯別勝率：** 〜20分 23.5%（n=17）、20〜25分 75.0%（n=8）、25〜30分 80.0%（n=15）、30〜35分 20.0%（n=10）、35分〜 31.8%（n=22）
- **最高帯：** 25〜30分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-41|ガングプランクの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（192試合）

- **実測ビルド候補：** インフィニティ エッジ + トリニティ フォース + コレクター（該当n=30、60.0% / 非該当44.4%、差+15.6pt）；インフィニティ エッジ + トリニティ フォース（該当n=34、58.8% / 非該当44.3%、差+14.5pt）
- **ステータス傾向：** 攻撃速度（該当n=79、51.9% / 非該当43.4%、差+8.5pt）；体力（該当n=115、47.8% / 非該当45.5%、差+2.4pt）
- **理論仮説：** ブラック クリーバー + トリニティ フォース（n=1（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 体力）；ランデュイン オーメン + アイスボーン ガントレット（n=1（15未満）；共通stats: 物理防御・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Gangplank` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gangplank.png)
