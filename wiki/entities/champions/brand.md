---
title: "ブランド"
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
champion_id: "Brand"
champion_key: "63"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Brand.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Brand.png"
---

# ブランド

![[raw/assets/champions/Brand.png|128]]

## 基本情報

- **英字ID：** `Brand`
- **キー：** `63`
- **称号：** 復讐の炎
- **データversion：** `16.18.1`

## 紹介

ブランドとして知られる生命体は、かつてキーガン・ローデという名の凍てつくフレヨルドの部族の一員だったが、今では偉大な力への誘惑に溺れることへの教訓としてその存在を知られるようになった。伝説のワールドルーンのひとつを求めて、キーガンは仲間を裏切り、それを自らの手で奪った──その瞬間、彼は人間ではなくなった。魂は燃え去り、肉体は生きた炎の器となった。ブランドとなったその男は、いくつの命があっても足りない苦痛を味わわされることへの復讐を誓いながら、他のルーンを求めてヴァロランをさまよっている。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 2 |
| `magic` | 9 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 570 |
| `hpperlevel` | 105 |
| `mp` | 469 |
| `mpperlevel` | 21 |
| `movespeed` | 340 |
| `armor` | 24 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 11 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 57 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.681 |

## アビリティ

- **パッシブ — 炎上：** スキルで攻撃するたびに対象が炎上し、4秒かけて魔法ダメージを与える。この効果は3回までスタックする。炎上中の敵ユニットを倒すとマナを回復する。チャンピオンまたは大型モンスターに付与されたスタックが最大になると臨界点に達して2秒後に爆発し、周囲の敵にスキル命中時効果を付与して大ダメージを与える。

- **Q — 焦炎：** 指定方向に火の玉を放ち、最初に命中した敵ユニットに魔法ダメージを与える。炎上中の対象は、このスキルが命中するとスタン状態になる。
- **W — 烈火の柱：** 発動から一瞬遅れて指定地点に火柱を発生させ、範囲内の敵ユニットに魔法ダメージを与える。炎上中の対象は、火柱から受けるダメージが25%増加する。
- **E — 焼灼：** 強力な爆風で対象を攻撃し、周囲の敵も巻き込んで魔法ダメージを与える。炎上中の対象に爆風が命中すると、効果範囲が2倍になる。
- **R — 業火：** 指定した対象に最大5回まで跳ね返る強力な火炎弾を放つ。この火炎弾は自身と付近にいる敵の間で跳ね返り、敵に命中するたびに魔法ダメージを与える。この跳ね返りは、優先的に敵チャンピオンの「炎上」スタックを最大にしようとする。炎上中の対象に命中すると、短い間その対象にスロウを与える。

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

- **観測分類：** 中盤寄り
- **対象試合：** 270試合、全体勝率 51.9%
- **時間帯別勝率：** 〜20分 35.6%（n=45）、20〜25分 64.5%（n=31）、25〜30分 64.3%（n=56）、30〜35分 50.0%（n=64）、35分〜 48.6%（n=74）
- **最高帯：** 20〜25分（判定差 15.9ポイント）
- **判定根拠：** 中間帯が最高、端点との差 15.9%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-63|ブランドの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（302試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=144、52.8% / 非該当48.1%、差+4.7pt）
- **ステータス傾向：** 物理防御（該当n=47、51.1% / 非該当50.2%、差+0.9pt）
- **理論仮説：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3118|マリグナンス]]（n=8（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-3118|マリグナンス]]（未観測；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

### BOTTOM（104試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=61、70.5% / 非該当58.1%、差+12.4pt）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3116|リーライ クリスタル セプター]]（該当n=50、70.0% / 非該当61.1%、差+8.9pt）
- **ステータス傾向：** 物理防御（該当n=35、74.3% / 非該当60.9%、差+13.4pt）
- **理論仮説：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3118|マリグナンス]]（未観測；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-6653|ライアンドリーの仮面]] + [[wiki/entities/items/item-8010|ブラッドレターの呪い]]（n=8（15未満）；共通stats: 魔力・体力／スキル相互作用は未検証）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-63|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=378）

- **高勝率コンボ候補：** [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率73.0%（27/37）、n=37（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率50.0%（15/30）、n=30（十分性の目安を満たす）。

### BOTTOM（対象n=161）

- **高勝率コンボ候補：** [[wiki/entities/champions/briar|ブライアー（Briar）]] — 対象側勝率76.5%（13/17）、サンプル不足（n=17、十分性の目安30未満）。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Brand` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Brand.png)
