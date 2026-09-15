---
title: "トゥイッチ"
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
  - role-assassin
  - data-dragon
champion_id: "Twitch"
champion_key: "29"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Twitch.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Twitch.png"
---

# トゥイッチ

![[raw/assets/champions/Twitch.png|128]]

## 基本情報

- **英字ID：** `Twitch`
- **キー：** `29`
- **称号：** 黒死のドブネズミ
- **データversion：** `16.18.1`

## 紹介

トゥイッチは汚物を漁ることに情熱を持つ、生まれながらの疫病ネズミで、そのためなら前足を汚すことも恐れはしない。化学物質によって強化されたクロスボウを豊かなピルトーヴァーの中心部に向けて、上にある都市に住む者たちに彼らが本当はいかに汚れた存在であるかを示してやろうと誓っている。常に忍び足で歩き回り、下層でゴミを漁っていない時は、他人のゴミの山の中に潜り込んでお宝を探している…カビたサンドイッチでも見つかれば御の字だ。

## 分類

- **役割タグ：** `Marksman`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 2 |
| `magic` | 3 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 98 |
| `mp` | 300 |
| `mpperlevel` | 40 |
| `movespeed` | 330 |
| `armor` | 27 |
| `armorperlevel` | 4 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 7.25 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.679 |

## アビリティ

- **パッシブ — スゴイ毒ダ！：** 通常攻撃で対象を毒%i:OnHit%通常攻撃時効果に侵し、毎秒確定ダメージを与える。

- **Q — オイラだヨ！：** 数秒間カモフラージュ状態になり、その間移動速度が増加する。カモフラージュの解除時に短時間攻撃速度が増加する。 「スゴイ毒ダ！」でチャンピオンを倒すと、「オイラだヨ！」のクールダウンがリセットされる。
- **W — コイツを食らエ！：** 毒物が入った容器を投げて破裂させ、効果範囲内の敵ユニットをスロウ状態にし、猛毒効果をかける。
- **E — ボーン！：** 猛毒状態にした敵を病原菌に侵し、さらにダメージを与える。
- **R — ヒャッハー！：** クロスボウの最大威力を引き出し、射程距離を大幅に拡大する。発射した矢は命中した敵ユニットを貫通してダメージを与える。

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
- **対象試合：** 84試合、全体勝率 51.2%
- **時間帯別勝率：** 〜20分 62.5%（n=16）、20〜25分 42.9%（n=14）、25〜30分 45.0%（n=20）、30〜35分 43.8%（n=16）、35分〜 61.1%（n=18）
- **最高帯：** 〜20分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-29|トゥイッチの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（182試合）

- **実測ビルド候補：** フィーンドハンターの矢 + インフィニティ エッジ（該当n=45、60.0% / 非該当53.3%、差+6.7pt）；フィーンドハンターの矢 + インフィニティ エッジ + コレクター（該当n=41、58.5% / 非該当53.9%、差+4.6pt）
- **ステータス傾向：** ライフスティール（該当n=49、63.3% / 非該当51.9%、差+11.4pt）；体力（該当n=76、59.2% / 非該当51.9%、差+7.3pt）
- **理論仮説：** スタティック シヴ + クラーケン スレイヤー（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・攻撃速度・移動速度）；スタティック シヴ + グインソー レイジブレード（n=1（15未満）；共通stats: 魔力・攻撃力・攻撃速度／チャンピオン原典にも言及: 攻撃力・攻撃速度）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Twitch` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Twitch.png)
