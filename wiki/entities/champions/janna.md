---
title: "ジャンナ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]"
tags:
  - champion
  - role-support
  - role-mage
  - data-dragon
champion_id: "Janna"
champion_key: "40"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Janna.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Janna.png"
---

# ジャンナ

![[raw/assets/champions/Janna.png|128]]

## 基本情報

- **英字ID：** `Janna`
- **キー：** `40`
- **称号：** 嵐の怒り
- **データversion：** `16.18.1`

## 紹介

ルーンテラの嵐を操るジャンナは、謎めいた風の精霊として寄る辺ないゾウンの人々を守っている。彼女は、大嵐に遭う危険も顧みず海に出るルーンテラの船乗りたちが、無事に航海できるよう乞い願う気持ちから生まれたとも言われる。ジャンナの恵みと庇護はゾウンの奥深くにまで届き、救いを求める人々に希望の光を与える。いつ、どこに現れるかは誰にもわからないが、彼女は窮地に陥った者に手を差し伸べてくれるのだ。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 5 |
| `magic` | 7 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 570 |
| `hpperlevel` | 90 |
| `mp` | 360 |
| `mpperlevel` | 50 |
| `movespeed` | 325 |
| `armor` | 28 |
| `armorperlevel` | 4.5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 47 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — テイルウィンド：** ジャンナに向かって移動する際、味方チャンピオンは移動速度が増加する。 通常攻撃時効果および「ゼファー」で、増加移動速度の一定割合にあたる追加魔法ダメージを与える。

- **Q — ハウリングゲイル：** 大気を操り、小さな竜巻を生み出す。竜巻は時間とともに成長し、時間がたつか再度このスキルを使うことで指定方向へ直進して、進路上の敵ユニットにダメージとノックアップを与える。
- **W — ゼファー：** 風の精霊を召喚し、自動効果として移動速度が増加すると同時に、ユニットをすり抜けるようになる。発動すると対象に風の精霊を飛ばして、ダメージとスロウ効果を与える。
- **E — ストームブレス：** 対象に魔法の風を呼び寄せる。風はシールドとなって味方チャンピオンやタワーをダメージから守ると同時に、攻撃力を増加させる。
- **R — モンスーン：** 魔法の嵐に包まれ、周囲の敵を吹き飛ばす。その後詠唱を続け、癒しの風によって範囲内の味方の体力を回復する。

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
- **対象試合：** 23試合、全体勝率 56.5%
- **時間帯別勝率：** 〜20分 33.3%（n=3）、20〜25分 100.0%（n=3）、25〜30分 60.0%（n=5）、30〜35分 50.0%（n=8）、35分〜 50.0%（n=4）
- **最高帯：** 20〜25分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-40|ジャンナの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（63試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3002|先人の道標]] + [[wiki/entities/items/item-3742|デッド マン プレート]]（未観測；共通stats: 物理防御・体力・移動速度／チャンピオン原典にも言及: 体力・移動速度）；[[wiki/entities/items/item-3742|デッド マン プレート]] + [[wiki/entities/items/item-4629|コズミック ドライブ]]（未観測；共通stats: 体力・移動速度／チャンピオン原典にも言及: 体力・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-40|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=118）

- **高勝率コンボ候補：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

### TOP（対象n=1）

- **高勝率コンボ候補：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Janna` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Janna.png)
