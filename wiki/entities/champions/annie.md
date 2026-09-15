---
title: "アニー"
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
  - role-support
  - data-dragon
champion_id: "Annie"
champion_key: "1"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Annie.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Annie.png"
---

# アニー

![[raw/assets/champions/Annie.png|128]]

## 基本情報

- **英字ID：** `Annie`
- **キー：** `1`
- **称号：** 闇の申し子
- **データversion：** `16.18.1`

## 紹介

危険極まりなく、それでいて無邪気でおませなアニーは、強力な発火能力を持つ小さな魔女だ。ノクサスの北に位置する山々の影に忍んでいてもなお、アニーは異端者として果てしない孤独の中に生きている。生まれ持った炎を操る力は、彼女が感情をほとばしらせることになった思いがけない出来事がきっかけで目覚めた。そして次第に、アニーは「火遊び」のやり方を覚えていく。 アニーのお気に入りはクマのぬいぐるみのティバーズで、呼べばすぐにそばに来て、炎で彼女を守ってくれる。永遠に無垢な子供のままであるアニーは、暗い森をさまよい続け...

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 3 |
| `magic` | 10 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 560 |
| `hpperlevel` | 96 |
| `mp` | 418 |
| `mpperlevel` | 25 |
| `movespeed` | 335 |
| `armor` | 23 |
| `armorperlevel` | 4 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 625 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 50 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.36 |
| `attackspeed` | 0.61 |

## アビリティ

- **パッシブ — 火遊びだいすき：** スキルを4回使用すると、次に行う攻撃スキルが対象をスタンさせる。 試合開始時および復活時は「火遊びだいすき」が使用可能な状態でスタートする。

- **Q — ファイアボール：** 火の玉を放って、指定した対象にダメージを与える。このスキルで敵ユニットを倒すと、消費したマナが回復しクールダウンが短縮する。
- **W — バーニングファイア：** 指定方向に扇状の炎を放ち、範囲内のすべての敵ユニットにダメージを与える。
- **E — モルテンシールド：** 自身または味方1体にシールドを付与し、移動速度が一時的に上昇する。また、通常攻撃かスキルで自身を攻撃した敵にダメージを与える。
- **R — やっちゃえ！ティバーズ！：** クマのティバーズを召喚し、範囲内の敵ユニットにダメージを与える。召喚されたティバーズは敵ユニットを攻撃し、身にまとう炎で周囲にいる敵に継続ダメージを与える。

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
- **対象試合：** 63試合、全体勝率 54.0%
- **時間帯別勝率：** 〜20分 47.1%（n=17）、20〜25分 42.9%（n=7）、25〜30分 63.6%（n=11）、30〜35分 52.9%（n=17）、35分〜 63.6%（n=11）
- **最高帯：** 25〜30分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-1|アニーの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（99試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=31、64.5% / 非該当52.9%、差+11.6pt）
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=5（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-3152|ヘクステック ロケットベルト]]（n=2（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-1|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=154）

- **高勝率コンボ候補：** [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率61.9%（13/21）、サンプル不足（n=21、十分性の目安30未満）。
- **カウンターピック候補：** [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率68.2%（15/22）、サンプル不足（n=22、十分性の目安30未満）。

### UTILITY（対象n=32）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Annie` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Annie.png)
