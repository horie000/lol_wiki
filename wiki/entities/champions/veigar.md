---
title: "ベイガー"
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
  - role-mage
  - data-dragon
champion_id: "Veigar"
champion_key: "45"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Veigar.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Veigar.png"
---

# ベイガー

![[raw/assets/champions/Veigar.png|128]]

## 基本情報

- **英字ID：** `Veigar`
- **キー：** `45`
- **称号：** 小さき大魔王
- **データversion：** `16.18.1`

## 紹介

定命の者が恐れて近づこうとしなかった力を受け入れたベイガーは情熱的な闇の魔術の使い手だ。自由な精神を持つバンドルシティの住人として、彼はヨードルの魔法の限界を超えてみたいと願い、数千年に渡って隠されてきた古文書を紐解いた。世界の謎に尽きぬ興味を持つ頑固者のベイガーだが、周囲からは見くびられることが多く、彼自身は自分は真に邪悪な存在だと思っているにもかかわらず、彼の内面に存在する倫理観を見て、彼の真の動機に疑いを持つ者もいる。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 2 |
| `magic` | 10 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 108 |
| `mp` | 490 |
| `mpperlevel` | 26 |
| `movespeed` | 340 |
| `armor` | 18 |
| `armorperlevel` | 5.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 52 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.24 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 偉大なる悪の力：** ルーンテラを脅かす強大な悪であるベイガー、その力はとどまるところを知らない！敵チャンピオンからキルまたはアシストを獲得したり、スキルを命中させると、ベイガーの魔力は永続的に増加してゆく。

- **Q — イーヴィルストライク：** 指定方向に闇のエネルギーを発射し、最初に命中した敵2体に魔法ダメージを与える。このスキルで敵ユニットにとどめを刺すと、ベイガーの魔力が永続的に増加する。
- **W — ダークマター：** 指定地点に巨大な暗黒物質を降らせ、着地時に魔法ダメージを与える。「偉大なる悪の力」のスタックに応じて「ダークマター」のクールダウンが短縮される。
- **E — イベントホライズン：** 空間の境界をねじ曲げて檻を作り出す。檻を通過した敵はスタンする。
- **R — メテオバースト：** 敵チャンピオン1体に闇の大魔法を放ち、対象の減少体力に応じて増加する大量の魔法ダメージを与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - キル・アシスト・スキル命中で魔力が永続的に増加する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 610試合、全体勝率 53.3%
- **時間帯別勝率：** 〜20分 32.1%（n=81）、20〜25分 54.3%（n=92）、25〜30分 55.9%（n=143）、30〜35分 59.7%（n=144）、35分〜 55.3%（n=150）
- **最高帯：** 30〜35分（判定差 27.6ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-45|ベイガーの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（755試合）

- **実測ビルド候補：** ゾーニャの砂時計 + シャドウフレイム（該当n=33、69.7% / 非該当51.1%、差+18.6pt）；ラバドン デスキャップ + 真紅のアイオニア ブーツ（該当n=45、68.9% / 非該当50.8%、差+18.0pt）
- **ステータス傾向：** 物理防御（該当n=197、56.3% / 非該当50.4%、差+6.0pt）；体力（該当n=591、53.0% / 非該当48.2%、差+4.8pt）
- **理論仮説：** セラフ エンブレイス + ルーデン エコー + ロッド オブ エイジス（n=11（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）；アクチュアライザー + ロッド オブ エイジス（n=6（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）

### BOTTOM（232試合）

- **実測ビルド候補：** ラバドン デスキャップ + ロッド オブ エイジス（該当n=36、72.2% / 非該当52.0%、差+20.2pt）；セラフ エンブレイス + ラバドン デスキャップ + ロッド オブ エイジス（該当n=32、71.9% / 非該当52.5%、差+19.4pt）
- **ステータス傾向：** 物理防御（該当n=94、64.9% / 非該当48.6%、差+16.3pt）；体力（該当n=160、56.9% / 非該当51.4%、差+5.5pt）
- **理論仮説：** ルーデン エコー + ロッド オブ エイジス（n=11（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）；セラフ エンブレイス + ルーデン エコー + ロッド オブ エイジス（n=8（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Veigar` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Veigar.png)
