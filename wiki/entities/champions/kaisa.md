---
title: "カイ＝サ"
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
  - role-marksman
  - role-mage
  - data-dragon
champion_id: "Kaisa"
champion_key: "145"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Kaisa.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kaisa.png"
---

# カイ＝サ

![[raw/assets/champions/Kaisa.png|128]]

## 基本情報

- **英字ID：** `Kaisa`
- **キー：** `145`
- **称号：** 虚無を知る娘
- **データversion：** `16.18.1`

## 紹介

幼少期にヴォイドに囚われたカイ＝サは、不屈の精神と意志の力で生き延びた。経験を積んで卓越した狩人となった彼女であったが、一部の者にとってその存在は望まれぬ未来の先触れであった。不本意ながらヴォイド生命体の殻と共生関係を結んだカイ＝サ。自分を怪物と呼ぶ定命の者を許し、共に闇の勢力を打ち負かすのか、それとも他者のことなど忘れ、自分を置き去りにした世界をヴォイドに食い尽くさせるのか…彼女はやがて選択を迫られることになるだろう。

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 102 |
| `mp` | 345 |
| `mpperlevel` | 40 |
| `movespeed` | 335 |
| `armor` | 25 |
| `armorperlevel` | 4.2 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 525 |
| `hpregen` | 4 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8.2 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.8 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — ヴォイドスキン：** カイ＝サの通常攻撃はプラズマスタックを付与し、スタック数に応じて与える追加魔法ダメージが増加していく。味方の移動不能効果もプラズマスタックを付与する。さらに、アイテム購入によってアルティメット以外のスキルがアップグレードされる。

- **Q — イカシアの雨：** 多数のミサイルを乱射する。ミサイルは周囲の敵を追尾する。 共生兵器: 「イカシアの雨」がアップグレードされて、ミサイル数が増加する。
- **W — ヴォイドシーカー：** 遠距離ミサイルを発射して、命中した敵にプラズマスタックを付与する。 共生兵器: 「ヴォイドシーカー」がアップグレードされて、付与するスタック数が増加し、チャンピオンに当たるとクールダウンが短縮されるようになる。
- **E — スーパーチャージ：** 一時的に移動速度が増加し、その後攻撃速度が増加する。 共生兵器: 「スーパーチャージ」がアップグレードされて、一時的にインビジブル状態を獲得できるようになる。
- **R — キラーヴォイド：** 敵チャンピオンの近くまでダッシュする。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - アイテム購入により通常スキルがアップグレードされる。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 序盤寄り
- **対象試合：** 554試合、全体勝率 46.2%
- **時間帯別勝率：** 〜20分 57.0%（n=86）、20〜25分 39.8%（n=83）、25〜30分 41.8%（n=134）、30〜35分 45.1%（n=122）、35分〜 48.8%（n=129）
- **最高帯：** 〜20分（判定差 8.1ポイント）
- **判定根拠：** 〜20分が最高、長時間帯との差 8.1%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-145|カイ＝サの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（1,123試合）

- **実測ビルド候補：** ガンメタル ブーツ + クラーケン スレイヤー（該当n=52、78.8% / 非該当46.7%、差+32.2pt）；グインソー レイジブレード + ガンメタル ブーツ + クラーケン スレイヤー（該当n=51、78.4% / 非該当46.7%、差+31.7pt）
- **ステータス傾向：** ライフスティール（該当n=104、66.3% / 非該当46.3%、差+20.0pt）；物理防御（該当n=455、54.7% / 非該当43.7%、差+11.0pt）
- **理論仮説：** フィーンドハンターの矢 + ファントム ダンサー（n=1（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・移動速度）；ファントム ダンサー + ナヴォリ フリッカーブレード（未観測；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・移動速度）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kaisa` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kaisa.png)
