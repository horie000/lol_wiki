---
title: "レナータ・グラスク"
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
  - role-support
  - role-mage
  - data-dragon
champion_id: "Renata"
champion_key: "888"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Renata.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Renata.png"
---

# レナータ・グラスク

![[raw/assets/champions/Renata.png|128]]

## 基本情報

- **英字ID：** `Renata`
- **キー：** `888`
- **称号：** ケミテック長者
- **データversion：** `16.18.1`

## 紹介

レナータ・グラスクは幼少期を過ごした家の焼け跡から、その名前と、両親が遺した錬金術の研究資料だけを手に再び立ち上がった。あれから数十年が過ぎた今、彼女はゾウンで最も裕福なケミ長者となった。ライバルを次々と傘下に引き入れて勢力を広げ、実業界の大物へと成り上がったのだ。レナータと手を組めば巨額の報酬が約束されるが、逆に歯向かえば後悔だけの一生が待っている。いずれにせよ、最後には誰もがレナータの側につくのだ。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 6 |
| `magic` | 9 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 545 |
| `hpperlevel` | 94 |
| `mp` | 350 |
| `mpperlevel` | 50 |
| `movespeed` | 330 |
| `armor` | 27 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.5 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 49 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.11 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — レバレッジ：** 通常攻撃が追加ダメージを与えて敵をマークする。味方はマークされた敵にダメージを与えると追加ダメージを与える。

- **Q — 手荒い挨拶：** ミサイルを発射して、最初に命中した敵にスネア効果を与える。その後、再発動してそのユニットを指定方向に投げ飛ばすことができる。
- **W — 緊急支援：** 味方チャンピオンにバフを付与して戦闘能力を強化し、そのデスを遅らせる。味方はキルかアシストを奪えば、デスを回避できる。
- **E — ロイヤリティープログラム：** 2発のケミテックミサイルを発射する。ミサイルに触れた味方にはシールドを付与し、敵にはダメージとスロウ効果を与える。
- **R — 敵対的買収：** 化学物質の波を送り出し、触れた敵をバーサーク状態にする。

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
- **対象試合：** 28試合、全体勝率 50.0%
- **時間帯別勝率：** 〜20分 50.0%（n=4）、20〜25分 66.7%（n=3）、25〜30分 50.0%（n=8）、30〜35分 60.0%（n=5）、35分〜 37.5%（n=8）
- **最高帯：** 20〜25分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-888|レナータ・グラスクの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（73試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** バンドルパイプ + ソラリのロケット（n=7（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；バンドルパイプ + 騎士の誓い（n=1（15未満）；共通stats: 物理防御・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Renata` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Renata.png)
