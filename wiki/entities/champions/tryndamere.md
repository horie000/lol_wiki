---
title: "トリンダメア"
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
champion_id: "Tryndamere"
champion_key: "23"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "フューリー"
image_path: "raw/assets/champions/Tryndamere.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Tryndamere.png"
---

# トリンダメア

![[raw/assets/champions/Tryndamere.png|128]]

## 基本情報

- **英字ID：** `Tryndamere`
- **キー：** `23`
- **称号：** 孤高の蛮王
- **データversion：** `16.18.1`

## 紹介

決して鎮まることのない激しい怒りに駆り立てられたトリンダメアは、かつては暗雲のかかる未来に備えるために北部で最強の戦士たちに次々と戦いを挑み、フレヨルド中に知られる存在だった。この激怒する蛮族は何年も同胞を滅ぼした者への復讐を果たそうとしていたが、最近になってアヴァローサンの戦母、アッシュの仲間となり、彼女の部族と共に生活するようになった。彼の人間離れした腕力と精神力は伝説となっており、幾度となく絶対的に不利な状況を乗り越えて新たな仲間たちに勝利をもたらしている。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** フューリー

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 10 |
| `defense` | 5 |
| `magic` | 2 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 696 |
| `hpperlevel` | 108 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 33 |
| `armorperlevel` | 4.8 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 66 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.4 |
| `attackspeed` | 0.67 |

## アビリティ

- **パッシブ — 戦場の咆哮：** 通常攻撃やクリティカル発生、敵にとどめを刺した際に「フューリー」がたまっていく。 自動効果: たまった「フューリー」の量に応じてクリティカル率が増加する。 たまった「フューリー」を消費して「血の欲望」を強化して発動できる。

- **Q — 血の欲望：** 戦闘で負傷するほど攻撃力が増加する。発動させるとたまっている「フューリー」を消費し、体力を回復する。
- **W — 嘲りの叫び：** 敵を嘲る言葉を叫び、周囲にいる敵チャンピオンの攻撃力を低下させる。トリンダメアに背を向けている敵は、移動速度も低下する。
- **E — スピンスラッシュ：** 指定地点へ回転しながら移動し、移動中に当たった敵ユニットにダメージを与える。
- **R — 不死の憤激：** 戦い続けたいという強い欲望に取りつかれ、一定時間はどれだけダメージを受けても体力がゼロにならない。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中6位（上位15%）。体力696、物理防御33、攻撃力66、移動速度345。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 151試合、全体勝率 49.0%
- **時間帯別勝率：** 〜20分 54.8%（n=31）、20〜25分 57.9%（n=19）、25〜30分 45.7%（n=35）、30〜35分 54.8%（n=31）、35分〜 37.1%（n=35）
- **最高帯：** 20〜25分（判定差 20.8ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-23|トリンダメアの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（250試合）

- **実測ビルド候補：** ファントム ダンサー + ラヴァナス ハイドラ（該当n=75、56.0% / 非該当46.3%、差+9.7pt）；ファントム ダンサー + ルインドキング ブレード（該当n=42、54.8% / 非該当48.1%、差+6.7pt）
- **ステータス傾向：** クリティカル率（該当n=212、49.5% / 非該当47.4%、差+2.2pt）
- **理論仮説：** ファントム ダンサー + ナヴォリ フリッカーブレード（n=12（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: クリティカル率・移動速度）；フィーンドハンターの矢 + ナヴォリ フリッカーブレード（n=1（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: クリティカル率・移動速度）

### JUNGLE（67試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** スタティック シヴ + クラーケン スレイヤー（n=1（15未満）；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・移動速度）；フィーンドハンターの矢 + ファントム ダンサー（n=1（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: クリティカル率・移動速度）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Tryndamere` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Tryndamere.png)
