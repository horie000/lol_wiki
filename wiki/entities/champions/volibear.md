---
title: "ボリベア"
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
champion_id: "Volibear"
champion_key: "106"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Volibear.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Volibear.png"
---

# ボリベア

![[raw/assets/champions/Volibear.png|128]]

## 基本情報

- **英字ID：** `Volibear`
- **キー：** `106`
- **称号：** 無慈悲の嵐
- **データversion：** `16.18.1`

## 紹介

彼を崇敬する者にとって、ボリベアは嵐を体現した存在だ。破壊的で、野蛮で、頑固なまでに意思が固く、彼は定命の者たちがフレヨルドのツンドラに足を踏み入れる前からそこに存在しており、彼と半神の同族たちが創り出したその土地を獰猛に守ろうとしている。ボリベアは文明とそれがもたらす弱さに激しい憎悪を募らせており、この土地を野生のままで自由に血が流されていた昔の姿に戻すために、敵対する者すべてに自身の爪と牙と容赦なき雷鳴を向けて戦いを挑む。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 7 |
| `magic` | 4 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 104 |
| `mp` | 350 |
| `mpperlevel` | 70 |
| `movespeed` | 340 |
| `armor` | 35 |
| `armorperlevel` | 5.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 6.25 |
| `mpregenperlevel` | 0.5 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 無慈悲の嵐：** 通常攻撃およびスキルの使用で攻撃速度が増加していき、最終的に通常攻撃が周囲の敵に追加魔法ダメージを与えるようになる。

- **Q — 稲妻の猛攻：** 敵に向かう際の移動速度が増加し、発動後最初に通常攻撃を行った対象にスタン効果とダメージを与える。
- **W — 激昂の斬撃：** 敵にダメージと通常攻撃時効果を与えてマークする。同じ対象にもう一度発動すると追加ダメージを与えて自身の体力を回復する。
- **E — 天破の一撃：** 指定地点に雷を落として周囲の敵にダメージとスロウ効果を与え、自身が範囲内にいた場合はシールドを獲得する。
- **R — 嵐を起こす者：** 指定地点に飛びかかって踏みつけた敵にスロウ効果とダメージを与え、自身は体力が増加する。着地地点の近くにある敵のタワーは一時的に無効化される。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中26位（上位15%）。体力650、物理防御35、攻撃力65、移動速度340。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 終盤寄り
- **対象試合：** 275試合、全体勝率 49.5%
- **時間帯別勝率：** 〜20分 47.9%（n=48）、20〜25分 43.2%（n=44）、25〜30分 48.3%（n=58）、30〜35分 46.4%（n=69）、35分〜 60.7%（n=56）
- **最高帯：** 35分〜（判定差 12.8ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 12.8%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-106|ボリベアの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（385試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3065|スピリット ビサージュ]] + [[wiki/entities/items/item-6675|ナヴォリ フリッカーブレード]]（該当n=112、62.5% / 非該当42.9%、差+19.6pt）；[[wiki/entities/items/item-3742|デッド マン プレート]] + [[wiki/entities/items/item-4629|コズミック ドライブ]] + [[wiki/entities/items/item-6675|ナヴォリ フリッカーブレード]]（該当n=32、65.6% / 非該当47.0%、差+18.6pt）
- **ステータス傾向：** クリティカル率（該当n=287、52.6% / 非該当36.7%、差+15.9pt）；攻撃速度（該当n=328、50.3% / 非該当38.6%、差+11.7pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・攻撃速度・移動速度）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（n=2（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

### TOP（159試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2510|黄昏と暁]] + [[wiki/entities/items/item-6675|ナヴォリ フリッカーブレード]]（該当n=48、60.4% / 非該当54.1%、差+6.4pt）
- **ステータス傾向：** 魔法防御（該当n=81、65.4% / 非該当46.2%、差+19.3pt）；物理防御（該当n=102、60.8% / 非該当47.4%、差+13.4pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・攻撃速度・移動速度）；[[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-106|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=454）

- **高勝率コンボ候補：** [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率61.1%（22/36）、n=36（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率34.4%（11/32）、n=32（十分性の目安を満たす）。

### TOP（対象n=257）

- **高勝率コンボ候補：** [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率73.3%（11/15）、サンプル不足（n=15、十分性の目安30未満）。
- **カウンターピック候補：** [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率33.3%（5/15）、サンプル不足（n=15、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Volibear` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Volibear.png)
