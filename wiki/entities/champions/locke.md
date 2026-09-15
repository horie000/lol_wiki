---
title: "ロック"
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
champion_id: "Locke"
champion_key: "805"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Locke.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Locke.png"
---

# ロック

![[raw/assets/champions/Locke.png|128]]

## 基本情報

- **英字ID：** `Locke`
- **キー：** `805`
- **称号：** 灰の祓魔師
- **データversion：** `16.18.1`

## 紹介

禁忌の儀式に通じ、釘を武器にする祓魔師コーヴィン・ロックは、デマーシアの秘術師たちの末裔である。嘘と偽善に囲まれて育った彼は、悪魔が人間の闇を生むのではなく、人間の闇が悪魔を呼び寄せるのだと若くして悟った。時を経てロックは、次々と魂の闇を暴き浄め続ける。嘘偽りのない世界をつくる覚悟で…

## 分類

- **役割タグ：** `Assassin`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 4 |
| `magic` | 2 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 109 |
| `mp` | 280 |
| `mpperlevel` | 70 |
| `movespeed` | 340 |
| `armor` | 32 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.3 |
| `attackspeed` | 0.688 |

## アビリティ

- **パッシブ — シルバー・ステイク：** 通常攻撃は命中時に追加魔法ダメージを与える。このダメージは対象の減少体力に応じて増加する。

- **Q — リチュアル・ネイル：** 「魂の釘」を構えて投げ、命中した敵にダメージを与えてマークを付与する。マークを消費して、通常攻撃で追加ダメージを与えられる。
- **W — ソウル・イグニッション：** 魂を燃やし、攻撃速度と移動速度を増加させ、自身にダメージを与える。効果時間終了時、効果中に受けたダメージの一部を回復する。
- **E — 灰塵の追撃：** 指定地点にテレポートしてから次の対象へダッシュし、通過した敵にダメージを与える。
- **R — 煉獄：** 拘束のアーティファクトを投げ、命中した敵にダメージを与え、場合によってはとどめを刺す。敵チャンピオンを封印すると、さらなる力を獲得する。

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

- **観測分類：** 序盤寄り
- **対象試合：** 164試合、全体勝率 43.3%
- **時間帯別勝率：** 〜20分 67.6%（n=34）、20〜25分 37.5%（n=24）、25〜30分 40.0%（n=35）、30〜35分 29.7%（n=37）、35分〜 41.2%（n=34）
- **最高帯：** 〜20分（判定差 26.5ポイント）
- **判定根拠：** 〜20分が最高、長時間帯との差 26.5%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-805|ロックの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（158試合）

- **実測ビルド候補：** リッチ ベイン + ゾーニャの砂時計（該当n=49、44.9% / 非該当38.5%、差+6.4pt）；リッチ ベイン + 連呪使いのブーツ（該当n=88、43.2% / 非該当37.1%、差+6.0pt）
- **ステータス傾向：** 体力（該当n=120、44.2% / 非該当28.9%、差+15.2pt）
- **理論仮説：** メジャイ ソウルスティーラー + ヘクステック ロケットベルト（n=1（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；リッチ ベイン + コズミック ドライブ（n=1（15未満）；共通stats: 魔力・移動速度／チャンピオン原典にも言及: 移動速度）

### JUNGLE（58試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** 黄昏と暁 + リフトメーカー（n=3（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；リッチ ベイン + コズミック ドライブ（n=1（15未満）；共通stats: 魔力・移動速度／チャンピオン原典にも言及: 移動速度）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Locke` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Locke.png)
