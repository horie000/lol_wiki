---
title: "ルル"
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
champion_id: "Lulu"
champion_key: "117"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Lulu.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lulu.png"
---

# ルル

![[raw/assets/champions/Lulu.png|128]]

## 基本情報

- **英字ID：** `Lulu`
- **キー：** `117`
- **称号：** 森の妖精使い
- **データversion：** `16.18.1`

## 紹介

ルルは魔法で夢のような幻想や空想の生き物を作り出すことで知られるヨードルのメイジで、ピックスという妖精の相棒と一緒にルーンテラを放浪している。ルルはこの平凡な物質世界を制約だと感じており、気まぐれに世界の法則を捻じ曲げては物体を作り出している。周囲の者は彼女の魔法を異常で危険なものだと感じているが、彼女はみんなには魔法が足りないと感じている。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 5 |
| `magic` | 7 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 565 |
| `hpperlevel` | 92 |
| `mp` | 350 |
| `mpperlevel` | 55 |
| `movespeed` | 330 |
| `armor` | 26 |
| `armorperlevel` | 4.6 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 11 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 47 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.25 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 仲良し妖精ピックス：** ピックスがくっついているチャンピオンが敵ユニットを攻撃するたびに、ピックスも魔法のビームで援護する。このビームは対象に追従するが、射線に別のユニットが割り込むと、そのユニットに遮られる。

- **Q — ぴかぴかビーム：** ピックスとルルが同時に魔法のビームを発射し、命中したすべての敵にダメージと重度のスロウ効果を付与する。
- **W — イタズラ：** 味方に使用した場合、短時間攻撃速度と移動速度を増加させる。敵に使用した場合、かわいらしい動物に変身させ、通常攻撃とスキルの使用を封じる。
- **E — ピックス、おねがい！：** 味方に使用した場合、ピックスをそばに送り込んでダメージを防ぐシールドを付与する。その後ピックスは対象にくっついて移動し、通常攻撃時に魔法のビームで援護する。敵に使用した場合、対象のもとへピックスが飛んでいきダメージを与える。その後ピックスは対象にくっついて移動し、可視状態にする。
- **R — おおきくなぁれ！：** 味方1体を巨大化させ、周囲にいる敵をノックアップさせる。巨大化した味方は体力が大幅に増加し、体の周囲に数秒間光の輪が発生する。輪の中に入った敵はスロウ状態になる。

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

- **観測分類：** 終盤寄り
- **対象試合：** 169試合、全体勝率 45.0%
- **時間帯別勝率：** 〜20分 45.8%（n=24）、20〜25分 43.5%（n=23）、25〜30分 34.2%（n=38）、30〜35分 46.7%（n=45）、35分〜 53.8%（n=39）
- **最高帯：** 35分〜（判定差 8.0ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 8.0%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-117|ルルの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（435試合）

- **実測ビルド候補：** 真紅のアイオニア ブーツ + アーデント センサー（該当n=40、77.5% / 非該当44.8%、差+32.7pt）；リデンプション + ムーンストーンの再生（該当n=32、62.5% / 非該当46.7%、差+15.8pt）
- **ステータス傾向：** 体力（該当n=321、49.5% / 非該当43.0%、差+6.6pt）
- **理論仮説：** バンドルパイプ + ソラリのロケット（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；ムーンストーンの再生 + ヘリアの残響（n=2（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Lulu` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lulu.png)
