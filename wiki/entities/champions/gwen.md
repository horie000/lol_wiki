---
title: "グウェン"
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
  - data-dragon
champion_id: "Gwen"
champion_key: "887"
data_version: "16.18.1"
roles:
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Gwen.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gwen.png"
---

# グウェン

![[raw/assets/champions/Gwen.png|128]]

## 基本情報

- **英字ID：** `Gwen`
- **キー：** `887`
- **称号：** 聖なるお針子
- **データversion：** `16.18.1`

## 紹介

魔法によって人間となり、命を与えられた元人形のグウェンは、かつて自分を生み出したまさにその道具を携えている。一歩ごとに作り手の愛の重みを感じながら、あらゆることに感謝を忘れない。グウェンが意のままに操る「聖なる霧」は、古代の防護魔法であり、自身が手にしたハサミ、針、そして縫い糸もその祝福を授かっている。目新しいものに囲まれながらも、グウェンは壊れた世界に生き残っている善意を守るため、大いなる喜びをもって戦い続けようと固く誓っている。

## 分類

- **役割タグ：** `Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 4 |
| `magic` | 5 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 115 |
| `mp` | 330 |
| `mpperlevel` | 40 |
| `movespeed` | 340 |
| `armor` | 39 |
| `armorperlevel` | 4.9 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.25 |
| `attackspeed` | 0.69 |

## アビリティ

- **パッシブ — 裁断：** 通常攻撃が対象の体力に応じて追加魔法ダメージを与える。この効果でチャンピオンに与えたダメージの一定割合を体力として回復する。

- **Q — チョキチョキッ！：** ハサミで扇状の範囲を最大6回切りつけて魔法ダメージを与える。範囲の中心にいるユニットには確定ダメージを与え、切るたびに固有スキルの効果を適用する。
- **W — 聖なる霧：** 霧を召喚して、霧の外にいる敵から身を守る。霧の中にいる敵からしか対象指定されない。
- **E — スキップスラッシュ：** 短い距離をダッシュして数秒間、攻撃速度と射程が増加し、通常攻撃時効果で魔法ダメージを与える。効果時間中に通常攻撃を命中させた場合、このスキルのクールダウンが一定割合解消される。
- **R — 針仕事：** 針を投げ、命中した敵にスロウ効果と魔法ダメージを与えて、チャンピオンに命中した場合は「裁断」を適用する。 このスキルは最大2回まで再発動可能で、再発動するたびに投げる針の本数とダメージが増加する。

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
- **対象試合：** 299試合、全体勝率 47.8%
- **時間帯別勝率：** 〜20分 46.5%（n=43）、20〜25分 48.9%（n=45）、25〜30分 53.0%（n=66）、30〜35分 48.1%（n=77）、35分〜 42.6%（n=68）
- **最高帯：** 25〜30分（判定差 10.4ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-887|グウェンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（378試合）

- **実測ビルド候補：** ラバドン デスキャップ + ナッシャー トゥース（該当n=47、68.1% / 非該当44.7%、差+23.4pt）；ラバドン デスキャップ + ナッシャー トゥース + リフトメーカー（該当n=35、65.7% / 非該当45.8%、差+19.9pt）
- **ステータス傾向：** 物理防御（該当n=201、51.2% / 非該当43.5%、差+7.7pt）；攻撃速度（該当n=348、47.7% / 非該当46.7%、差+1.0pt）
- **理論仮説：** コズミック ドライブ + リフトメーカー（n=8（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；メジャイ ソウルスティーラー + リフトメーカー（n=5（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

### JUNGLE（143試合）

- **実測ビルド候補：** ナッシャー トゥース + リフトメーカー（該当n=51、52.9% / 非該当52.2%、差+0.8pt）
- **ステータス傾向：** 物理防御（該当n=57、57.9% / 非該当48.8%、差+9.1pt）
- **理論仮説：** 黄昏と暁 + メジャイ ソウルスティーラー（n=4（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；コズミック ドライブ + リフトメーカー（n=3（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Gwen` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gwen.png)
