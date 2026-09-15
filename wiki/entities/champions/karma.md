---
title: "カルマ"
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
  - role-support
  - data-dragon
champion_id: "Karma"
champion_key: "43"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Karma.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Karma.png"
---

# カルマ

![[raw/assets/champions/Karma.png|128]]

## 基本情報

- **英字ID：** `Karma`
- **キー：** `43`
- **称号：** 目覚めし者
- **データversion：** `16.18.1`

## 紹介

カルマは他の誰にも増して、アイオニアの精神性を重んじる伝統を体現する存在だ。彼女は無限に生まれ変わる古代の魂が実体化した存在であり、過去からの記憶をすべて新たな生へと継承するだけでなく、常人には到底理解の及ばない力を授かっている。近年訪れた危機の折には全力で人々を導いた彼女だが、平和と調和を手にするには多大な犠牲を払わなければならない場合があることを知っている──自分自身にとっても、そして何より大切な故郷にとっても。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 7 |
| `magic` | 8 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 109 |
| `mp` | 374 |
| `mpperlevel` | 40 |
| `movespeed` | 335 |
| `armor` | 28 |
| `armorperlevel` | 5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 13 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 49 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.3 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 寄せ火：** 自身の攻撃スキルが「マントラ」のクールダウンを短縮する。

- **Q — 心炎：** 精神の炎を解き放ち、敵に命中すると爆発してダメージを与える。 マントラボーナス: 爆発の威力が増し、さらに対象の足下に力場を発生させて範囲内に時間差でダメージを与える。
- **W — 魂縛：** 自身と標的を鎖でつなぎダメージを与え、ステルス状態を見破る。効果終了時まで鎖が破壊されなければ、敵はその場でスネア状態となり再びダメージを受ける。 マントラボーナス: 鎖が強化され自身の体力を回復し、敵に与えるスネア状態の効果時間が延長される。
- **E — 激励：** 指定した味方ユニットにシールドを付与し、ダメージから守ると同時に移動速度を増加させる。 マントラボーナス: 対象からエネルギーが放射され、初期シールドを強化し、周囲にいる味方チャンピオンにも「激励」の効果を付与する。
- **R — マントラ：** カルマが次に使用するスキルを強化し追加効果を付与する。 「マントラ」はレベル1から使用でき、スキルポイントを必要としない。

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
- **対象試合：** 168試合、全体勝率 57.7%
- **時間帯別勝率：** 〜20分 58.1%（n=31）、20〜25分 62.5%（n=16）、25〜30分 54.1%（n=37）、30〜35分 56.5%（n=46）、35分〜 60.5%（n=38）
- **最高帯：** 20〜25分（判定差 8.4ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-43|カルマの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（460試合）

- **実測ビルド候補：** マリグナンス + 帝国の指令（該当n=55、58.2% / 非該当52.6%、差+5.6pt）；ムーンストーンの再生 + ヘリアの残響（該当n=94、55.3% / 非該当52.7%、差+2.6pt）
- **ステータス傾向：** マナ（該当n=202、54.5% / 非該当52.3%、差+2.1pt）
- **理論仮説：** ソラリのロケット + 変幻自在のジャック＝ショー（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；バンドルパイプ + ソラリのロケット（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Karma` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Karma.png)
