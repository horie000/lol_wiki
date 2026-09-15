---
title: "ゼド"
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
  - role-assassin
  - data-dragon
champion_id: "Zed"
champion_key: "238"
data_version: "16.18.1"
roles:
  - "Assassin"
resource_type: "気"
image_path: "raw/assets/champions/Zed.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zed.png"
---

# ゼド

![[raw/assets/champions/Zed.png|128]]

## 基本情報

- **英字ID：** `Zed`
- **キー：** `238`
- **称号：** 影の頭領
- **データversion：** `16.18.1`

## 紹介

無慈悲で非情なゼドは、ノクサスの侵略者たちを追い出すためにアイオニアの伝統的な魔法と武術を軍事利用することを目的とした組織、「影の一団」の頭領である。戦争のさなか、追い込まれた彼は強力だが危険な穢れをもたらす邪悪な霊界の魔法を使い、秘密の影の形態を解放した。あらゆる禁忌の術を身に付けたゼドは、自分の祖国と自分が新たに創設した組織の脅威とみなした者は、誰であろうと抹殺する。

## 分類

- **役割タグ：** `Assassin`
- **リソース種別：** 気

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 2 |
| `magic` | 1 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 654 |
| `hpperlevel` | 99 |
| `mp` | 200 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 32 |
| `armorperlevel` | 4.7 |
| `spellblock` | 29 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 50 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.3 |
| `attackspeed` | 0.651 |

## アビリティ

- **パッシブ — 弱者必衰：** 残り体力の少ない敵を通常攻撃した場合、追加魔法ダメージを与える。同じ敵チャンピオンには数秒に1度しか効果が発生しない。

- **Q — 風魔手裏剣：** 自身と影が平型手裏剣を投げる。 手裏剣が命中した敵それぞれにダメージを与える。
- **W — 影分身：** 自動効果: 自身と影が特定の敵に同一のスキルを命中させるたびに、気が回復する(各スキルの発動中、一度のみ有効)。 発動効果: 影を指定方向に放つ。影は数秒間その場に留まる。再発動で自身と影の位置が入れ替わる。
- **E — 影薙ぎ：** 自身と影が回転斬りを放ち、周囲の敵にダメージを与える。影の回転斬りが命中した敵はスロウ効果を受ける。
- **R — 死の刻印：** 対象指定されなくなり、指定した敵チャンピオンにダッシュして印を付与する。3秒後に印が爆発して、印が付与されている間に自身が対象に与えた全ダメージの一定割合のダメージをもう一度与える。

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
- **対象試合：** 165試合、全体勝率 49.7%
- **時間帯別勝率：** 〜20分 53.6%（n=28）、20〜25分 62.1%（n=29）、25〜30分 44.4%（n=27）、30〜35分 42.9%（n=35）、35分〜 47.8%（n=46）
- **最高帯：** 20〜25分（判定差 8.5ポイント）
- **判定根拠：** 中間帯が最高、端点との差 8.5%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-238|ゼドの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（318試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3168|不滅の道]] + [[wiki/entities/items/item-6699|ボルテイク サイクロソード]]（該当n=31、58.1% / 非該当47.0%、差+11.0pt）；[[wiki/entities/items/item-3171|真紅のアイオニア ブーツ]] + [[wiki/entities/items/item-6699|ボルテイク サイクロソード]]（該当n=117、52.1% / 非該当45.8%、差+6.4pt）
- **ステータス傾向：** 体力（該当n=208、50.0% / 非該当44.5%、差+5.5pt）；体力再生（該当n=30、50.0% / 非該当47.9%、差+2.1pt）
- **理論仮説：** [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3814|ナイト エッジ]]（n=13（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3161|ショウジンの矛]] + [[wiki/entities/items/item-3814|ナイト エッジ]]（n=7（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

### JUNGLE（120試合）

- **実測ビルド候補：** [[wiki/entities/items/item-6692|赤月の刃]] + [[wiki/entities/items/item-6699|ボルテイク サイクロソード]]（該当n=30、46.7% / 非該当44.4%、差+2.2pt）
- **ステータス傾向：** 体力（該当n=74、45.9% / 非該当43.5%、差+2.5pt）
- **理論仮説：** [[wiki/entities/items/item-3161|ショウジンの矛]] + [[wiki/entities/items/item-3814|ナイト エッジ]]（n=5（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3814|ナイト エッジ]]（n=5（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-238|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=553）

- **高勝率コンボ候補：** [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率60.0%（21/35）、n=35（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率50.0%（16/32）、n=32（十分性の目安を満たす）。

### JUNGLE（対象n=220）

- **高勝率コンボ候補：** [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率66.7%（10/15）、サンプル不足（n=15、十分性の目安30未満）。
- **カウンターピック候補：** [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率43.8%（7/16）、サンプル不足（n=16、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Zed` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zed.png)
