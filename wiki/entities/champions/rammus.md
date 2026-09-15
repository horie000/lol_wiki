---
title: "ラムス"
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
  - data-dragon
champion_id: "Rammus"
champion_key: "33"
data_version: "16.18.1"
roles:
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Rammus.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rammus.png"
---

# ラムス

![[raw/assets/champions/Rammus.png|128]]

## 基本情報

- **英字ID：** `Rammus`
- **キー：** `33`
- **称号：** アーマージロ
- **データversion：** `16.18.1`

## 紹介

ラムス──謎に包まれたこの生き物を、聖なる存在と崇拝してやまない者は多い。一方で、ただの動物に過ぎないと見る者もいる。その素性は誰にも分からない。人々は棘の付いた甲羅を持つラムスについて様々な説を打ち立てる。ラムスの姿が確認された場所では、半神だ、いや神聖なる神の遣いだ、魔術で姿を変えられたただの獣だ、などと論争が巻き起こる。真実がどうであれラムスは沈黙を守り、独り砂漠を彷徨って、他者と関わろうとはしない。

## 分類

- **役割タグ：** `Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 10 |
| `magic` | 5 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 645 |
| `hpperlevel` | 100 |
| `mp` | 310 |
| `mpperlevel` | 33 |
| `movespeed` | 335 |
| `armor` | 35 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7.85 |
| `mpregenperlevel` | 0.5 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.215 |
| `attackspeed` | 0.7 |

## アビリティ

- **パッシブ — トゲトゲ：** 自身の物理防御と魔法防御に応じて攻撃力が増加する。

- **Q — ころころ：** 体を丸めて高速回転し、移動速度が増加する。衝突した敵に突進してダメージを与え、スロウ効果を付与する。
- **W — かたくなる：** 防御体勢を取って物理防御と魔法防御を大幅に増加させ、通常攻撃を行ってきた相手にダメージを跳ね返す。
- **E — ぴりぴり：** 敵チャンピオンまたは中立モンスターをタウントし、固い甲羅に無謀な攻撃をさせる。
- **R — どーんどーん：** ジャンプしてから指定地点に勢いよく着地し、敵に魔法ダメージとスロウ効果を与える。「ころころ」発動中に使用した場合、範囲の中心付近にいる敵にはノックアップも与える。

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
- **対象試合：** 65試合、全体勝率 40.0%
- **時間帯別勝率：** 〜20分 30.0%（n=10）、20〜25分 55.6%（n=9）、25〜30分 36.8%（n=19）、30〜35分 45.5%（n=11）、35分〜 37.5%（n=16）
- **最高帯：** 20〜25分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-33|ラムスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（133試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3075|ソーンメイル]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（該当n=41、58.5% / 非該当40.2%、差+18.3pt）；[[wiki/entities/items/item-3068|サンファイア イージス]] + [[wiki/entities/items/item-3075|ソーンメイル]]（該当n=55、50.9% / 非該当42.3%、差+8.6pt）
- **ステータス傾向：** 魔法防御（該当n=89、48.3% / 非該当40.9%、差+7.4pt）
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・魔法防御）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・魔法防御）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-33|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=185）

- **高勝率コンボ候補：** [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率62.5%（10/16）、サンプル不足（n=16、十分性の目安30未満）。
- **カウンターピック候補：** [[wiki/entities/champions/master-yi|マスター・イー（MasterYi）]] — 対象側勝率54.2%（13/24）、サンプル不足（n=24、十分性の目安30未満）。

### UTILITY（対象n=10）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Rammus` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rammus.png)
