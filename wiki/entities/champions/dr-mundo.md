---
title: "ドクター・ムンド"
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
  - role-tank
  - role-fighter
  - data-dragon
champion_id: "DrMundo"
champion_key: "36"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Fighter"
resource_type: "なし"
image_path: "raw/assets/champions/DrMundo.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/DrMundo.png"
---

# ドクター・ムンド

![[raw/assets/champions/DrMundo.png|128]]

## 基本情報

- **英字ID：** `DrMundo`
- **キー：** `36`
- **称号：** ゾウンの狂人
- **データversion：** `16.18.1`

## 紹介

完全に正気を失った、おぞましい紫色の悲しき殺人鬼。ゾウン市民の多くが闇の深い夜に外を出歩かないのは、ドクター・ムンドがいるためだ。今では“医者”を名乗っているが、以前はゾウンでも特に評判の悪い、とある医療院の患者だった。そこの職員を一人残らず“治療”したのち、ドクター・ムンドはかつて自身が処置を受けていた無人の病棟に診察室を構え、その身で何度も味わってきた非人道的な医療行為を、見よう見まねで行うようになった。棚に入った大量の薬物と、素人以下の医療知識を手に、ドクター・ムンドは今、注射を打つことで自身を...

## 分類

- **役割タグ：** `Tank`、`Fighter`
- **リソース種別：** なし

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 7 |
| `magic` | 6 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 103 |
| `mp` | 0 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 32 |
| `armorperlevel` | 4.5 |
| `spellblock` | 29 |
| `spellblockperlevel` | 2.3 |
| `attackrange` | 125 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.3 |
| `attackspeed` | 0.67 |

## アビリティ

- **パッシブ — 気ままな往診：** 最初に受ける移動不能効果を無効化する。その際、代わりに体力を失い、近くに薬品の入った容器を落とす。落とした容器の上を歩いて回収すると体力が回復し、このスキルのクールダウンが短縮される。 また、ドクター・ムンドは極めて高い体力自動回復能力を持っている。

- **Q — 骨切りノコギリ：** 骨切りノコギリを投げ、最初に命中した敵に対象の現在体力に応じたダメージを与えて、スロウ効果を付与する。
- **W — 心臓ビリビリ：** 自身を感電させて、周囲の敵に継続的にダメージを与え、受けたダメージの一部を蓄える。効果時間の最後か再発動時に、周囲の敵に大ダメージを与える。これが敵に命中した場合は、それまでに蓄えていたダメージの一定割合を体力として回復する。
- **E — 野蛮な痛み：** 自動効果 - 自身の最大体力に応じて増加する、増加攻撃力を獲得する。 発動効果 - “往診用”バッグを敵に叩きつけ、自身の減少体力に応じた追加ダメージを与える。対象をキルした場合はその敵を弾き飛ばし、接触した敵にダメージを与える。
- **R — マキシマム投与：** 自身に薬品を注入し、減少体力の一定割合を瞬時に回復する。さらに移動速度が増加し、長い時間をかけて最大体力の一部を自動回復する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - Eの自動効果で最大体力に応じた増加攻撃力を得る。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 457試合、全体勝率 51.2%
- **時間帯別勝率：** 〜20分 55.3%（n=76）、20〜25分 45.8%（n=72）、25〜30分 43.5%（n=92）、30〜35分 55.7%（n=106）、35分〜 54.1%（n=111）
- **最高帯：** 30〜35分（判定差 12.2ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-36|ドクター・ムンドの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（500試合）

- **実測ビルド候補：** スピリット ビサージュ + ワーモグ アーマー + 心の鋼（該当n=82、67.1% / 非該当47.8%、差+19.2pt）；スピリット ビサージュ + 心の鋼（該当n=138、63.8% / 非該当46.1%、差+17.6pt）
- **ステータス傾向：** 魔法防御（該当n=249、58.2% / 非該当43.8%、差+14.4pt）；攻撃力（該当n=150、56.7% / 非該当48.6%、差+8.1pt）
- **理論仮説：** 覇王のブラッドメイル + タイタン ハイドラ（n=14（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；タイタン ハイドラ + サンダード スカイ（未観測；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

### JUNGLE（300試合）

- **実測ビルド候補：** 終わりなき絶望 + 心の鋼（該当n=31、64.5% / 非該当45.4%、差+19.2pt）；心の鋼 + タイタン ハイドラ（該当n=36、58.3% / 非該当45.8%、差+12.5pt）
- **ステータス傾向：** 攻撃力（該当n=89、56.2% / 非該当43.6%、差+12.6pt）；物理防御（該当n=237、48.5% / 非該当42.9%、差+5.7pt）
- **理論仮説：** 先人の道標 + デッド マン プレート（未観測；共通stats: 物理防御・体力・移動速度／チャンピオン原典にも言及: 体力・移動速度）；覇王のブラッドメイル + タイタン ハイドラ（n=11（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.DrMundo` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/DrMundo.png)
