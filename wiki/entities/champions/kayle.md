---
title: "ケイル"
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
champion_id: "Kayle"
champion_key: "10"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Kayle.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kayle.png"
---

# ケイル

![[raw/assets/champions/Kayle.png|128]]

## 基本情報

- **英字ID：** `Kayle`
- **キー：** `10`
- **称号：** 天空の正義
- **データversion：** `16.18.1`

## 紹介

ルーン戦争の真っただ中にターゴンの神髄の子として生を受けたケイルは、母の意志を引き継いで、聖なる炎の翼を纏い正義のために戦っている。彼女と双子の妹であるモルガナは、長年にわたってデマーシアの守護者だった──しかし、ケイルは定命の者たちの度重なるあやまちに幻滅し、この世界を見放した。それでも、不義なる者に炎の剣で裁きを与えるケイルの伝説は途絶えることなく、いつの日か彼女が再び降臨することを望む者も多い…

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 6 |
| `magic` | 7 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 670 |
| `hpperlevel` | 92 |
| `mp` | 330 |
| `mpperlevel` | 50 |
| `movespeed` | 335 |
| `armor` | 26 |
| `armorperlevel` | 4.2 |
| `spellblock` | 22 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 175 |
| `hpregen` | 5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 50 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 聖なる上昇：** レベルアップしてスキルポイントを使用すると、通常攻撃が天界の力により強化されていく。強化段階にしたがってケイルの翼が炎を帯び、攻撃速度、移動速度、射程距離、通常攻撃時の炎の波動が強化される。

- **Q — 裁きの射光：** 次元の門を作り出し、敵を貫通する天界の剣を召喚する。この剣は命中するごとに敵にダメージを与え、スロウ効果を付与し、防御力を低下させる。
- **W — 天の祝福：** 神の祝福によって自身と近くの味方チャンピオン1体の体力を回復し、移動速度を上昇させる。
- **E — 星炎の刃：** 自動効果: 手にした天界の剣で通常攻撃時に追加魔法ダメージを与える。 発動効果: 次の通常攻撃で対象を天界の炎で打ち抜き、その対象の減少体力に比例した追加ダメージを与える。
- **R — 聖なる審判：** 味方チャンピオンを無敵状態にし、前代の「正義の神髄」の力を借りて対象の周囲を聖なる剣の雨で浄化する。

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
- **対象試合：** 121試合、全体勝率 55.4%
- **時間帯別勝率：** 〜20分 64.3%（n=14）、20〜25分 38.5%（n=13）、25〜30分 46.7%（n=30）、30〜35分 54.1%（n=37）、35分〜 70.4%（n=27）
- **最高帯：** 35分〜（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-10|ケイルの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（208試合）

- **実測ビルド候補：** ナッシャー トゥース + シャドウフレイム（該当n=42、66.7% / 非該当48.2%、差+18.5pt）；ラバドン デスキャップ + ナッシャー トゥース（該当n=80、58.8% / 非該当47.7%、差+11.1pt）
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** スタティック シヴ + クラーケン スレイヤー（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・攻撃速度・移動速度）；スタティック シヴ + グインソー レイジブレード（未観測；共通stats: 魔力・攻撃力・攻撃速度／チャンピオン原典にも言及: 攻撃力・攻撃速度）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kayle` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kayle.png)
