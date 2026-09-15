---
title: "レク＝サイ"
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
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "RekSai"
champion_key: "421"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "怒り"
image_path: "raw/assets/champions/RekSai.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/RekSai.png"
---

# レク＝サイ

![[raw/assets/champions/RekSai.png|128]]

## 基本情報

- **英字ID：** `RekSai`
- **キー：** `421`
- **称号：** 地底の恐怖
- **データversion：** `16.18.1`

## 紹介

頂点捕食者であるレク＝サイは地中を移動し、獲物を奇襲して貪り食う無情なヴォイドの生物だ。かつて栄華を誇ったシュリーマ帝国があった一帯は、今や彼女の飽くなき食欲の犠牲となって荒廃している。行商や貿易商、武装隊商ですら、彼女とその子供たちの狩場を避けるために、わざわざ数百キロもの回り道をする。地平線にレク＝サイの姿が見えた時、足元から訪れる死から逃れられる者はいない。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** 怒り

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 2 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 99 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 340 |
| `armor` | 35 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 2.5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.667 |

## アビリティ

- **パッシブ — ゼル＝サイの怒り：** 通常攻撃または通常スキルを当てると「フューリー」がたまる。地中潜伏中に「フューリー」を消費して自身の体力を回復する。

- **Q — 女王の怒り/獲物定め：** 次の3回の通常攻撃が近接する周囲の敵に追加物理ダメージを与える。 「潜伏」を発動すると、ヴォイドのエネルギーを帯びた大地を打ち上げ、敵にダメージを与えて命中した敵を可視化する。
- **W — 潜伏/襲撃：** 地中に潜伏して地中専用のスキルを使用できるようになり、移動速度が増加する。視界範囲は狭まり、通常攻撃を行えなくなる。 「潜伏」発動中は、「襲撃」を発動して近接する敵をノックアップさせてダメージを与えることができる。
- **E — 激情の牙/掘削：** 対象に噛み付いて物理ダメージを与え、「フューリー」が最大の場合は、2倍の確定ダメージを与える。 「潜伏」を発動すると、長時間持続し、何度も使用することができるトンネルを作る。敵は、このトンネルの開口部の上に立つことで、これを崩壊させることができる。
- **R — ヴォイドラッシュ：** ダメージを与えた対象を自動的にマークする。このスキルを発動させると、少しの間対象指定不可になり、マークした対象に突進して、相手の最大体力に応じた大ダメージを与える。

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
- **対象試合：** 25試合、全体勝率 40.0%
- **時間帯別勝率：** 〜20分 0.0%（n=2）、20〜25分 100.0%（n=1）、25〜30分 25.0%（n=4）、30〜35分 50.0%（n=14）、35分〜 25.0%（n=4）
- **最高帯：** 20〜25分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-421|レク＝サイの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（63試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=14（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-421|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=129）

- **高勝率コンボ候補：** [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率46.7%（7/15）、サンプル不足（n=15、十分性の目安30未満）。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

### TOP（対象n=22）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.RekSai` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/RekSai.png)
