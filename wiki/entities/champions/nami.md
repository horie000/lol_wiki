---
title: "ナミ"
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
champion_id: "Nami"
champion_key: "267"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Nami.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nami.png"
---

# ナミ

![[raw/assets/champions/Nami.png|128]]

## 基本情報

- **英字ID：** `Nami`
- **キー：** `267`
- **称号：** 潮呼びの巫女
- **データversion：** `16.18.1`

## 紹介

向こう見ずな性格の海の若きヴァスタヤであるナミは、ターゴン人たちとの間で太古から続いていた協約が破られた時、マライの民として初めて海を離れて陸地に上がることになった。それ以外に方法がなかったことから、彼女は部族の安全を守るための聖なる儀式を自らの手で完遂することを決めた。この新たな混沌の時代の中で、ナミは潮呼びの巫女の杖を使って海の力を召喚しながら、不安だらけの未来に固い決意で挑んでいる。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 3 |
| `magic` | 7 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 560 |
| `hpperlevel` | 88 |
| `mp` | 365 |
| `mpperlevel` | 43 |
| `movespeed` | 335 |
| `armor` | 29 |
| `armorperlevel` | 5.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 54 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.61 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — さざなみの後押し：** スキルが味方チャンピオンに命中するたびに、命中した相手の移動速度が短時間増加する。

- **Q — 水の牢獄：** 指定地点に水泡を飛ばし、着弾時に範囲内の敵ユニットにダメージを与えてスタン効果を付与する。
- **W — 潮の流れ：** 味方と敵チャンピオンの間を交互に跳ね返る水流を放つ。命中した味方は体力が回復し、敵はダメージを受ける。
- **E — 潮使いの祝福：** 短時間、味方チャンピオンに力を与える。強化された味方は次の数回の通常攻撃とスキルで、対象に追加魔法ダメージとスロウ効果を付与する。
- **R — 海神の舞：** ナミが海の力を借りて「海神の舞」を呼び寄せる。波に触れた敵ユニットはダメージを受け、ノックアップされてスロウ状態になる。命中した味方は「さざなみの後押し」の2倍の効果を得る。

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
- **対象試合：** 163試合、全体勝率 46.0%
- **時間帯別勝率：** 〜20分 37.9%（n=29）、20〜25分 54.5%（n=22）、25〜30分 51.4%（n=35）、30〜35分 48.7%（n=39）、35分〜 39.5%（n=38）
- **最高帯：** 20〜25分（判定差 15.1ポイント）
- **判定根拠：** 中間帯が最高、端点との差 15.1%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-267|ナミの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（425試合）

- **実測ビルド候補：** 真紅のアイオニア ブーツ + 帝国の指令（該当n=33、72.7% / 非該当48.7%、差+24.0pt）；リデンプション + 帝国の指令（該当n=35、65.7% / 非該当49.2%、差+16.5pt）
- **ステータス傾向：** 体力（該当n=298、53.0% / 非該当44.9%、差+8.1pt）
- **理論仮説：** バンドルパイプ + ソラリのロケット（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；シュレリアの戦歌 + アーデント センサー（n=13（15未満）；共通stats: 魔力・移動速度／チャンピオン原典にも言及: 移動速度）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Nami` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nami.png)
