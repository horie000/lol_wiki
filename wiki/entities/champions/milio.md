---
title: "ミリオ"
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
champion_id: "Milio"
champion_key: "902"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Milio.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Milio.png"
---

# ミリオ

![[raw/assets/champions/Milio.png|128]]

## 基本情報

- **英字ID：** `Milio`
- **キー：** `902`
- **称号：** やさしき炎
- **データversion：** `16.18.1`

## 紹介

イシュタル出身の心あたたかい少年。わずか12歳にして火のアクシオムを使いこなし、「癒やしの炎」という未知なる力を発見した。この新たな力を用い、ミリオはかつての祖母のように、ユン・タルの一員となることを目指す。それがかなえば、現在流謫の身にある故郷の家族を、正当な地位に引き上げることができるからだ。イシュタルのジャングルを抜け、首都イシャオカンまではるばる旅をしてきたミリオは、ユン・タルの座に就くため、ヴィダリオンの試練に備えて修練を積んでいる。その試練の内容も、それに伴う危険についても知らずに。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 4 |
| `magic` | 8 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 560 |
| `hpperlevel` | 88 |
| `mp` | 365 |
| `mpperlevel` | 43 |
| `movespeed` | 330 |
| `armor` | 26 |
| `armorperlevel` | 4.6 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 48 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ファイヤーアップ！：** ミリオのスキルに触れた味方は、次の攻撃で追加のバーストダメージを与え、対象を炎上させる。

- **Q — ウルトラメガファイヤーキック：** 敵1体をノックバックさせるボールをキックする。ボールは敵に命中すると、跳ね上がってから対象に向かって落下し、着地時に範囲内の敵にダメージとスロウ効果を与える。
- **W — 癒しの焚き火：** 範囲内の味方の体力を回復し、その射程距離を延長するゾーンを作り出す。このゾーンは発動地点から一番近い味方を追従する。
- **E — 抱擁のぬくもり：** 味方1体にシールドを付与し、一時的に対象の移動速度を上昇させる。このスキルは2回までチャージできる。
- **R — 生命の息吹：** 穏やかな炎の波動を放ち、範囲内の味方の体力を回復して、行動妨害効果を除去する。

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
- **対象試合：** 91試合、全体勝率 49.5%
- **時間帯別勝率：** 〜20分 57.1%（n=7）、20〜25分 57.9%（n=19）、25〜30分 35.7%（n=28）、30〜35分 73.7%（n=19）、35分〜 33.3%（n=18）
- **最高帯：** 30〜35分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-902|ミリオの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（217試合）

- **実測ビルド候補：** アーデント センサー + ヘリアの残響（該当n=45、62.2% / 非該当45.9%、差+16.3pt）；ムーンストーンの再生 + ヘリアの残響（該当n=73、52.1% / 非該当47.9%、差+4.1pt）
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** 旋律のダイアデム + ロッド オブ エイジス（n=1（15未満）；共通stats: 体力・マナ／チャンピオン原典にも言及: 体力・マナ）；シュレリアの戦歌 + アーデント センサー（n=5（15未満）；共通stats: 魔力・移動速度／チャンピオン原典にも言及: 移動速度）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Milio` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Milio.png)
