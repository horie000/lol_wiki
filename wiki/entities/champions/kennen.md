---
title: "ケネン"
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
  - role-mage
  - data-dragon
champion_id: "Kennen"
champion_key: "85"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "気"
image_path: "raw/assets/champions/Kennen.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kennen.png"
---

# ケネン

![[raw/assets/champions/Kennen.png|128]]

## 基本情報

- **英字ID：** `Kennen`
- **キー：** `85`
- **称号：** 雷雲の担い手
- **データversion：** `16.18.1`

## 紹介

ケネンは電光石化の素早さでアイオニアの均衡を保つだけでなく、「均衡の守人」の中で唯一のヨードルでもある。小さな毛皮で覆われた姿とは裏腹に、彼は手裏剣の竜巻と底知れぬ熱意を持ってあらゆる脅威に立ち向かっていく。破壊的な電気エネルギーを浴びせて現れた敵を倒しながら、彼は師匠のシェンとともに霊的領域を巡回している。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** 気

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 4 |
| `magic` | 7 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 98 |
| `mp` | 200 |
| `mpperlevel` | 0 |
| `movespeed` | 335 |
| `armor` | 29 |
| `armorperlevel` | 4.95 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 50 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 48 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.4 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 嵐の刻印：** スキルを3回命中させた敵をスタンさせる。

- **Q — 雷遁手裏剣：** ケネンが狙った場所に手裏剣を連投し、命中した敵ユニットにダメージと「嵐の刻印」を与える。
- **W — 稲妻の奔流：** 自動効果: ケネンの数回ごとの攻撃が、対象に追加ダメージと「嵐の刻印」を与えるようになる。 発動効果: 周囲の刻印を受けている対象にダメージを与え、 新たに「嵐の刻印」を付与する。
- **E — 疾風迅雷：** 稲妻と化したケネンがユニットをすり抜け、接触したユニットに「嵐の刻印」を与える。この形態になるときに移動速度が増加し、この形態から抜けるときには攻撃速度が増加する。
- **R — 雷撃の大嵐：** ケネンが雷雲を召喚し、周囲にいる敵チャンピオンに魔法ダメージを与える。

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
- **対象試合：** 43試合、全体勝率 44.2%
- **時間帯別勝率：** 〜20分 33.3%（n=6）、20〜25分 42.9%（n=7）、25〜30分 25.0%（n=8）、30〜35分 60.0%（n=10）、35分〜 50.0%（n=12）
- **最高帯：** 30〜35分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-85|ケネンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（98試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 物理防御（該当n=55、41.8% / 非該当34.9%、差+6.9pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃速度・移動速度）；[[wiki/entities/items/item-3085|ルナーン ハリケーン]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（未観測；共通stats: 攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃速度・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-85|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=138）

- **高勝率コンボ候補：** [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率58.8%（10/17）、サンプル不足（n=17、十分性の目安30未満）。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

### MIDDLE（対象n=17）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kennen` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kennen.png)
