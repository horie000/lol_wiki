---
title: "ニーコ"
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
champion_id: "Neeko"
champion_key: "518"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Neeko.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Neeko.png"
---

# ニーコ

![[raw/assets/champions/Neeko.png|128]]

## 基本情報

- **英字ID：** `Neeko`
- **キー：** `518`
- **称号：** 不思議のカメレオン
- **データversion：** `16.18.1`

## 紹介

遥か昔に途絶えたヴァスタヤ部族の末裔であるニーコは、他者の風貌を拝借してどんな集団にでも溶け込むことができる。彼女は相手の感情を吸収し、即座に敵か味方かを判別することができるのだ。ニーコがどこにいるのか、あるいはニーコの正体が何者なのか、確信を持てる者はいない。だが彼女に害をなそうという者は、やがてその真の力を目の当たりにするだろう。そして原初の霊的魔法の威力を身をもって知ることになるのだ。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 1 |
| `magic` | 9 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 104 |
| `mp` | 450 |
| `mpperlevel` | 30 |
| `movespeed` | 340 |
| `armor` | 21 |
| `armorperlevel` | 5.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 48 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 駆け巡る色彩：** 味方チャンピオンまたはマップ上の他のユニットの姿に化けることができる。行動妨害効果を受けるか、ダメージスキルを詠唱するか、チャンピオン以外のユニットに擬態した状態で敵タワーにダメージを与えるか、擬態したユニットの体力バーと同量のダメージを受けると擬態が解除される。

- **Q — 弾ける花弁：** 魔法ダメージを与える種を投げる。種はチャンピオンに当たるか敵ユニットをキルすると再度爆発する。
- **W — シェイプスプリッター：** 自動効果により通常攻撃3回ごとに追加魔法ダメージを与え、少しの間、移動速度が増加する。発動すると指定方向にクローンを送り出し、再発動するとクローンの進行方向を変えられる。
- **E — からまれ！：** 輪を飛ばして当たった敵すべてにダメージとスネア効果を与える。輪は敵をキルするかチャンピオンに触れると大きくなり、速度とスネア効果時間が増加する。
- **R — ポップブロッサム：** 少しの間準備してから宙に舞い上がり、周囲のすべての敵をノックアップさせる。さらに着地時に周囲の敵にダメージを与えてスタンさせる。擬態中は密かに準備を行える。

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
- **対象試合：** 207試合、全体勝率 51.2%
- **時間帯別勝率：** 〜20分 60.7%（n=28）、20〜25分 58.6%（n=29）、25〜30分 52.1%（n=48）、30〜35分 40.4%（n=57）、35分〜 53.3%（n=45）
- **最高帯：** 〜20分（判定差 20.4ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-518|ニーコの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（363試合）

- **実測ビルド候補：** ヘクステック ロケットベルト + ゾーニャの砂時計（該当n=140、50.7% / 非該当48.0%、差+2.7pt）
- **ステータス傾向：** 体力（該当n=313、49.2% / 非該当48.0%、差+1.2pt）
- **理論仮説：** バンドルパイプ + ジーク コンバージェンス（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；ヘクステック ロケットベルト + モレロノミコン（n=14（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

### MIDDLE（42試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** メジャイ ソウルスティーラー + ヘクステック ロケットベルト（n=2（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；ヘクステック ロケットベルト + モレロノミコン（n=1（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Neeko` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Neeko.png)
