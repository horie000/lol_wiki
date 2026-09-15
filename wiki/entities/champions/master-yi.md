---
title: "マスター・イー"
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
  - role-assassin
  - data-dragon
champion_id: "MasterYi"
champion_key: "11"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/MasterYi.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/MasterYi.png"
---

# マスター・イー

![[raw/assets/champions/MasterYi.png|128]]

## 基本情報

- **英字ID：** `MasterYi`
- **キー：** `11`
- **称号：** ウージューの剣客
- **データversion：** `16.18.1`

## 紹介

極限まで心身を鍛え上げたマスター・イーは、もはや心技一体の境地へと達している。武力に訴えるのはやむを得ぬ場合のみと己を律しながらも、その優雅で素早い太刀筋には刹那の迷いも見られない。アイオニアに伝わる武術、ウージュースタイルの現存する最後の伝承者の一人として、マスター・イーは洞察の七つのレンズを使い、その生涯をかけて、彼の部族が残した遺産を伝授するのにふさわしい弟子たちを探している。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 10 |
| `defense` | 4 |
| `magic` | 2 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 105 |
| `mp` | 251 |
| `mpperlevel` | 42 |
| `movespeed` | 355 |
| `armor` | 33 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 7.25 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.679 |

## アビリティ

- **パッシブ — ダブルストライク：** 通常攻撃を数回行うごとに、通常攻撃が2回連続攻撃になる。

- **Q — アルファストライク：** 目にもとまらぬ速さで複数の敵を斬り抜け、物理ダメージを与える。この間、マスター・イーは対象指定されない。このスキルの攻撃はクリティカルを発生させる場合もあり、モンスターには追加物理ダメージを与える。通常攻撃をするたびに、このスキルのクールダウンが短縮される。
- **W — 明鏡止水：** 精神を統一して体力を回復する。また効果時間中、受けるダメージを軽減する。さらに、詠唱中は毎秒「ダブルストライク」のスタックを獲得して、「ウージュースタイル」と「ハイランダー」の残り効果時間を一時停止する。
- **E — ウージュースタイル：** 通常攻撃が追加確定ダメージを与える。
- **R — ハイランダー：** 一時的に移動速度と攻撃速度が増加し、あらゆるスロウ効果を受けなくなる。発動中にチャンピオンに対するキルまたはアシストを達成すると「ハイランダー」の効果時間が延びる。またこのスキルは自動効果を持ち、チャンピオンに対するキルまたはアシストを達成すると、他のスキルのクールダウンが短縮されるようになる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中11位（上位15%）。体力640、物理防御33、攻撃力65、移動速度355。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 397試合、全体勝率 54.7%
- **時間帯別勝率：** 〜20分 54.0%（n=63）、20〜25分 45.8%（n=72）、25〜30分 54.4%（n=103）、30〜35分 61.1%（n=90）、35分〜 56.5%（n=69）
- **最高帯：** 30〜35分（判定差 15.3ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-11|マスター・イーの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（705試合）

- **実測ビルド候補：** グインソー レイジブレード + ルインドキング ブレード + ガンメタル ブーツ（該当n=37、78.4% / 非該当51.2%、差+27.2pt）；グインソー レイジブレード + ガンメタル ブーツ（該当n=45、77.8% / 非該当50.9%、差+26.9pt）
- **ステータス傾向：** 物理防御（該当n=250、61.6% / 非該当47.7%、差+13.9pt）；魔法防御（該当n=250、60.0% / 非該当48.6%、差+11.4pt）
- **理論仮説：** ファントム ダンサー + ナヴォリ フリッカーブレード（n=2（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・クリティカル率・移動速度）；フィーンドハンターの矢 + ファントム ダンサー（n=2（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・クリティカル率・移動速度）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.MasterYi` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/MasterYi.png)
