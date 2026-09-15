---
title: "ソラカ"
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
champion_id: "Soraka"
champion_key: "16"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Soraka.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Soraka.png"
---

# ソラカ

![[raw/assets/champions/Soraka.png|128]]

## 基本情報

- **英字ID：** `Soraka`
- **キー：** `16`
- **称号：** 星の子
- **データversion：** `16.18.1`

## 紹介

霊峰ターゴンの彼方にある宇宙の次元をさまよっていたソラカは、定命の種族を彼らの暴力的な本能から守るために、自らの永遠の命を手放してやってきた。彼女は出会ったものすべてに慈悲と情けの美徳を広めようと努めており、彼女を傷つけようとするものですら治癒を施す。この世界で様々な紛争を目にしてきたにもかかわらず、彼女は今も、ルーンテラの人々には可能性が残っていると信じている。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 5 |
| `magic` | 7 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 605 |
| `hpperlevel` | 88 |
| `mp` | 425 |
| `mpperlevel` | 40 |
| `movespeed` | 325 |
| `armor` | 32 |
| `armorperlevel` | 5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 2.5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 50 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.14 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 救済の足音：** 近くにいる体力の少ない味方に向かって移動する際に、ソラカの移動速度が増加する。

- **Q — 星のささやき：** 指定地点に流れ星が落ち、周囲の敵ユニットに魔法ダメージとスロウ効果を与える。敵チャンピオンに「星のささやき」が命中した場合、ソラカの体力が回復する。
- **W — 星霊の癒し：** 自身の体力を消費し、指定した味方チャンピオンの体力を回復する。
- **E — 星の静寂：** 指定した場所に時空の渦を生じさせ、巻き込んだ敵チャンピオンすべてにサイレンス効果を付与する。さらに渦が消滅した瞬間に渦の範囲内に居るすべての敵チャンピオンにスネア効果を付与する。
- **R — 星に願いを：** ソラカとすべての味方チャンピオンが降り注ぐ希望の光で満たされ、瞬時に体力が回復する。

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
- **対象試合：** 50試合、全体勝率 52.0%
- **時間帯別勝率：** 〜20分 60.0%（n=5）、20〜25分 20.0%（n=5）、25〜30分 53.3%（n=15）、30〜35分 54.5%（n=11）、35分〜 57.1%（n=14）
- **最高帯：** 〜20分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-16|ソラカの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（141試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** シュレリアの戦歌 + アーデント センサー（n=6（15未満）；共通stats: 魔力・移動速度／チャンピオン原典にも言及: 移動速度）；ムーンストーンの再生 + ヘリアの残響（n=2（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Soraka` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Soraka.png)
