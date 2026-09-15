---
title: "タム・ケンチ"
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
  - role-tank
  - role-support
  - data-dragon
champion_id: "TahmKench"
champion_key: "223"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/TahmKench.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/TahmKench.png"
---

# タム・ケンチ

![[raw/assets/champions/TahmKench.png|128]]

## 基本情報

- **英字ID：** `TahmKench`
- **キー：** `223`
- **称号：** 川の王様
- **データversion：** `16.18.1`

## 紹介

タム・ケンチは過去に様々な名前で呼ばれてきた悪魔であり、ルーンテラの水路を移ろいながら、尽きることのない食欲を満たすために他者を餌食にしている。彼は非常に魅力的で誇り高き存在の振りをして、自信たっぷりな態度で物質世界を放浪しながら不用心な獲物を探している。彼の長い舌は頑丈な鎧に身を包んだ戦士ですら離れた場所から気絶させることが可能で、音を立てる奈落のような彼の腹の中に納まれば、そこから戻れる可能性はほとんどない。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 9 |
| `magic` | 6 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 103 |
| `mp` | 325 |
| `mpperlevel` | 50 |
| `movespeed` | 335 |
| `armor` | 39 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 1 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 56 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 舌慣らし：** 巨大な体躯から繰り出す通常攻撃に、自身の合計体力に応じた追加ダメージを付与する。ダメージを受けた敵チャンピオンには「舌慣らし」がスタックされ、3スタックたまった敵チャンピオンに対しては「丸呑み」を使えるようになる。

- **Q — 味見：** 舌をムチを打つように放つ。最初に命中したユニットにダメージを与え、スロウ効果を付与する。対象が敵チャンピオンだった場合は自分の体力を回復する。 敵チャンピオンに「舌慣らし」のスタックを付与する。「舌慣らし」を3スタック付与しているチャンピオンにこのスキルを使用すると、スタックを消費して対象をスタンさせる。
- **W — 川潜り：** 水中に潜ってから指定地点に現れ、範囲内のすべての敵にダメージを与えてノックアップさせる。
- **E — ゆるゆる皮膜：** 自動効果: 受けたダメージの一定割合を蓄え、非戦闘時にそれに応じて体力を回復する。 発動効果: 蓄えていた全ダメージを一時的なシールドに変換する。
- **R — 丸呑み：** 数秒間チャンピオンを丸呑みし、敵には魔法ダメージを与え、味方にはシールドを付与する。

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
- **対象試合：** 227試合、全体勝率 50.2%
- **時間帯別勝率：** 〜20分 48.3%（n=29）、20〜25分 57.1%（n=42）、25〜30分 55.8%（n=52）、30〜35分 37.3%（n=59）、35分〜 55.6%（n=45）
- **最高帯：** 20〜25分（判定差 19.9ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-223|タム・ケンチの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（378試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3065|スピリット ビサージュ]] + [[wiki/entities/items/item-3084|心の鋼]]（該当n=58、60.3% / 非該当48.1%、差+12.2pt）；[[wiki/entities/items/item-2502|終わりなき絶望]] + [[wiki/entities/items/item-3084|心の鋼]]（該当n=67、52.2% / 非該当49.5%、差+2.7pt）
- **ステータス傾向：** 魔力（該当n=33、57.6% / 非該当49.3%、差+8.3pt）；物理防御（該当n=316、50.3% / 非該当48.4%、差+1.9pt）
- **理論仮説：** [[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=7（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-3190|ソラリのロケット]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）

### TOP（93試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 魔法防御（該当n=45、48.9% / 非該当43.8%、差+5.1pt）
- **理論仮説：** [[wiki/entities/items/item-3190|ソラリのロケット]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-2510|黄昏と暁]] + [[wiki/entities/items/item-4633|リフトメーカー]]（n=6（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-223|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=490）

- **高勝率コンボ候補：** [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率76.7%（23/30）、n=30（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率38.9%（14/36）、n=36（十分性の目安を満たす）。

### TOP（対象n=134）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.TahmKench` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/TahmKench.png)
