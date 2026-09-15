---
title: "ヴェックス"
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
champion_id: "Vex"
champion_key: "711"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Vex.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vex.png"
---

# ヴェックス

![[raw/assets/champions/Vex.png|128]]

## 基本情報

- **英字ID：** `Vex`
- **キー：** `711`
- **称号：** 終わりなき憂鬱
- **データversion：** `16.18.1`

## 紹介

闇深きシャドウアイルの中心には、不気味な濃霧の中を一人満足げに歩くヨードルがいる。彼女の名はヴェックス。無限に湧き出る十代特有のイライラと強力な「影」を引き連れ、大嫌いな「凡人たち」の喧騒から遠く離れて、自分が作り出した安らかで憂鬱な世界に引きこもっている。野心もやる気もない彼女だが、自分の世界に「色」や「幸せ」を持ち込む者との戦いにだけはやる気が出る。そして人を憂鬱にさせる魔法を駆使してあらゆる邪魔者を蹴散らしている。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 0 |
| `defense` | 0 |
| `magic` | 0 |
| `difficulty` | 0 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 590 |
| `hpperlevel` | 104 |
| `mp` | 490 |
| `mpperlevel` | 32 |
| `movespeed` | 335 |
| `armor` | 23 |
| `armorperlevel` | 4.45 |
| `spellblock` | 28 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 54 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1 |
| `attackspeed` | 0.669 |

## データ品質上の注意

- `info` の4項目がすべて `0` である。未収録値か実値かは原典だけでは判定できない。

## アビリティ

- **パッシブ — フコウとユーウツ：** 一定時間ごとに強化され、次の通常スキルが敵にフィアー効果を与えてダッシュを阻止する。周囲の敵がダッシュするたびにマークを付与する。マークを消費すると追加ダメージを与え、強化効果のクールダウンも短縮される。

- **Q — 無気力ショット：** 途中で加速する飛翔物を発射してダメージを与える。
- **W — パーソナルスペース：** シールドを獲得して周囲の敵にダメージを与える。
- **E — ヤミとばし：** 敵にダメージとスロウ効果を与えて、「ユーウツ」を付与するゾーンを発生させる。
- **R — 影法師：** 敵チャンピオンをマークする飛翔物を発射する。再発動すると対象までダッシュしてダメージを与える。

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
- **対象試合：** 400試合、全体勝率 47.8%
- **時間帯別勝率：** 〜20分 49.4%（n=79）、20〜25分 42.3%（n=52）、25〜30分 45.2%（n=84）、30〜35分 53.9%（n=89）、35分〜 45.8%（n=96）
- **最高帯：** 30〜35分（判定差 11.6ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-711|ヴェックスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（693試合）

- **実測ビルド候補：** ゾーニャの砂時計 + 連呪使いのブーツ（該当n=142、60.6% / 非該当44.5%、差+16.1pt）；ゾーニャの砂時計 + 連呪使いのブーツ + シャドウフレイム（該当n=123、60.2% / 非該当45.1%、差+15.1pt）
- **ステータス傾向：** 物理防御（該当n=350、50.6% / 非該当44.9%、差+5.7pt）
- **理論仮説：** 黒炎のトーチ + ルーデン エコー（n=11（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；ライアンドリーの仮面 + ロッド オブ エイジス（n=2（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Vex` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vex.png)
