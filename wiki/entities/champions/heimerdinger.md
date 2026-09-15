---
title: "ハイマーディンガー"
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
champion_id: "Heimerdinger"
champion_key: "74"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Heimerdinger.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Heimerdinger.png"
---

# ハイマーディンガー

![[raw/assets/champions/Heimerdinger.png|128]]

## 基本情報

- **英字ID：** `Heimerdinger`
- **キー：** `74`
- **称号：** 誉れ高き発明王
- **データversion：** `16.18.1`

## 紹介

変わり者のセシル・B・ハイマーディンガー教授は、史上稀にみる革新的な発明家の一人として称賛される存在だ。ピルトーヴァーの評議会でも最古参となる彼は、飽くなき進歩を求めるこの都市の良い部分のみならず、悪しき部分もまた等しく見てきた。それでも天才的な科学者であり教師としての顔も持つ彼は、自らの風変わりな装置を使って人々の生活を向上させるべくその身を捧げ続けている。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 6 |
| `magic` | 8 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 558 |
| `hpperlevel` | 105 |
| `mp` | 385 |
| `mpperlevel` | 20 |
| `movespeed` | 340 |
| `armor` | 19 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 56 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.36 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — ヘクステックの親和性：** 味方のタワーまたは自身が配置した砲台の近くにいると移動速度が増加する。

- **Q — H-28G革新砲：** 砲台を設置する。砲台は通常攻撃だけでなく、一定時間ごとに貫通レーザーを発射する(タワーに対して与えるダメージは半減する)。
- **W — ヘクステック小型ロケット：** 指定地点へ向け、長射程のロケット弾を5発発射する。
- **E — CH-2超電磁グレネード：** 指定地点にグレネード弾を投げ、敵ユニットにダメージを与える。さらに中心で直撃した敵をスタンさせ、周囲の敵にスロウを与える。
- **R — アップグレード！！！：** 天才的なひらめきによってアップグレードを開発し、次に発動するスキルを強化できる。

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
- **対象試合：** 193試合、全体勝率 52.3%
- **時間帯別勝率：** 〜20分 54.3%（n=35）、20〜25分 63.2%（n=19）、25〜30分 53.5%（n=43）、30〜35分 46.5%（n=43）、35分〜 50.9%（n=53）
- **最高帯：** 20〜25分（判定差 8.9ポイント）
- **判定根拠：** 中間帯が最高、端点との差 8.9%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-74|ハイマーディンガーの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（234試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3089|ラバドン デスキャップ]]（該当n=34、70.6% / 非該当50.0%、差+20.6pt）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=100、59.0% / 非該当48.5%、差+10.5pt）
- **ステータス傾向：** 物理防御（該当n=141、53.9% / 非該当51.6%、差+2.3pt）；マナ（該当n=184、53.3% / 非該当52.0%、差+1.3pt）
- **理論仮説：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3040|セラフ エンブレイス]]（n=2（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=2（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

### MIDDLE（69試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3175|連呪使いのブーツ]]（該当n=35、57.1% / 非該当50.0%、差+7.1pt）
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=3（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=11（15未満）；共通stats: 魔力・体力／スキル相互作用は未検証）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-74|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=289）

- **高勝率コンボ候補：** [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率77.8%（14/18）、サンプル不足（n=18、十分性の目安30未満）。
- **カウンターピック候補：** [[wiki/entities/champions/garen|ガレン（Garen）]] — 対象側勝率33.3%（6/18）、サンプル不足（n=18、十分性の目安30未満）。

### MIDDLE（対象n=96）

- **高勝率コンボ候補：** [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率35.3%（6/17）、サンプル不足（n=17、十分性の目安30未満）。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Heimerdinger` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Heimerdinger.png)
