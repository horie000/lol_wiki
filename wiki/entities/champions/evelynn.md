---
title: "イブリン"
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
  - role-assassin
  - role-mage
  - data-dragon
champion_id: "Evelynn"
champion_key: "28"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Evelynn.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Evelynn.png"
---

# イブリン

![[raw/assets/champions/Evelynn.png|128]]

## 基本情報

- **英字ID：** `Evelynn`
- **キー：** `28`
- **称号：** 苦悶の抱擁
- **データversion：** `16.18.1`

## 紹介

ルーンテラ中の暗がりで悪魔イブリンは次の犠牲者を物色する。艶かしい女性の姿で獲物を誘い、相手を魅了したところで真の姿を露わす。そして彼女は、言葉では言い表せないほどの苦痛を相手に与え、苦悶する様を糧（かて）に愉悦に浸る。だがこの悪魔にとっては、そんな火遊びもただの気まぐれに過ぎない。ルーンテラの人々にとって、それは欲望が暴走した末路を描くおぞましい物語であり、節度なき快楽がもたらす代償を思い知らせる恐怖の象徴なのだ。

## 分類

- **役割タグ：** `Assassin`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 2 |
| `magic` | 7 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 642 |
| `hpperlevel` | 98 |
| `mp` | 315 |
| `mpperlevel` | 42 |
| `movespeed` | 335 |
| `armor` | 37 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 8.11 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.1 |
| `attackspeed` | 0.667 |

## アビリティ

- **パッシブ — 妖魔の影：** 戦闘中以外は「妖魔の影」に包まれ、体力が低下している場合は体力が回復する。レベル6以降は「妖魔の影」でカモフラージュも獲得する。

- **Q — ヘイトスパイク：** 鞭を振って最初に当たった敵ユニットにダメージを与える。その後、地面から一直線に貫通するトゲを近くの敵に数回放つことができる。
- **W — アリュール：** 対象に呪いをかける。少ししてから次に行う通常攻撃またはスキルがその敵にチャーム効果を与え、魔法防御を低下させる。
- **E — ウィップラッシュ：** 対象を鞭で打ってダメージを与え、その後少しの間だけ移動速度が増加する。
- **R — ラストカレス：** 少しの間だけ対象指定不可になり、自身の正面の範囲内にいる敵に大ダメージを与えてから後方に大きくワープする。

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

- **観測分類：** 中盤寄り
- **対象試合：** 133試合、全体勝率 48.9%
- **時間帯別勝率：** 〜20分 44.8%（n=29）、20〜25分 50.0%（n=20）、25〜30分 50.0%（n=28）、30〜35分 55.6%（n=27）、35分〜 44.8%（n=29）
- **最高帯：** 30〜35分（判定差 10.7ポイント）
- **判定根拠：** 中間帯が最高、端点との差 10.7%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-28|イブリンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（273試合）

- **実測ビルド候補：** メジャイ ソウルスティーラー + リッチ ベイン（該当n=88、65.9% / 非該当37.8%、差+28.1pt）；メジャイ ソウルスティーラー + ラバドン デスキャップ（該当n=66、62.1% / 非該当42.0%、差+20.1pt）
- **ステータス傾向：** 体力（該当n=198、51.0% / 非該当36.0%、差+15.0pt）；魔法防御（該当n=49、57.1% / 非該当44.6%、差+12.5pt）
- **理論仮説：** メジャイ ソウルスティーラー + ヘクステック ロケットベルト（n=1（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；リッチ ベイン + 永遠の前進（n=1（15未満）；共通stats: 移動速度／チャンピオン原典にも言及: 移動速度）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Evelynn` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Evelynn.png)
