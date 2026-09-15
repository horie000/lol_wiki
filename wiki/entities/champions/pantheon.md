---
title: "パンテオン"
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
  - role-assassin
  - data-dragon
champion_id: "Pantheon"
champion_key: "80"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Pantheon.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Pantheon.png"
---

# パンテオン

![[raw/assets/champions/Pantheon.png|128]]

## 基本情報

- **英字ID：** `Pantheon`
- **キー：** `80`
- **称号：** 砕けぬ槍
- **データversion：** `16.18.1`

## 紹介

かつて不本意にも戦の神髄の器となったアトレウスは、天空から星々を切り離した一撃により自身に宿るその天の力を殺されながらも、屈することなく生き延びた。やがて彼は定命であるがゆえの力を、そしてその粘り強い不屈の精神を貴ぶようになった。今は亡き神髄の武器に不屈の意志を注ぎ、パンテオンの生まれ変わりとなったアトレウスは神的な存在に立ち向かう。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 4 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 109 |
| `mp` | 317 |
| `mpperlevel` | 31 |
| `movespeed` | 345 |
| `armor` | 40 |
| `armorperlevel` | 4.95 |
| `spellblock` | 28 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 7.35 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.95 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 定命の意志：** スキルまたは通常攻撃を数回行うと、次のスキルが強化される。

- **Q — 彗星の槍：** 指定方向に槍を突く、または槍を投げる。
- **W — 跳撃の盾：** 対象に向かってダッシュし、ダメージを与えてスタンさせる。
- **E — イージスの猛攻：** 盾を構え、正面からのダメージを無効化しながら、槍で連続攻撃を繰り出す。
- **R — 偉大なる星路：** 精神を集中させて空高く跳びあがり、流星となって指定地点に上空から突撃する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中12位（上位15%）。体力650、物理防御40、攻撃力64、移動速度345。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 中盤寄り
- **対象試合：** 420試合、全体勝率 50.2%
- **時間帯別勝率：** 〜20分 40.9%（n=66）、20〜25分 61.9%（n=63）、25〜30分 47.7%（n=88）、30〜35分 48.0%（n=102）、35分〜 53.5%（n=101）
- **最高帯：** 20〜25分（判定差 8.4ポイント）
- **判定根拠：** 中間帯が最高、端点との差 8.4%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-80|パンテオンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（355試合）

- **実測ビルド候補：** [[wiki/entities/items/item-6610|サンダード スカイ]] + [[wiki/entities/items/item-6692|赤月の刃]]（該当n=39、69.2% / 非該当42.1%、差+27.1pt）；[[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（該当n=53、62.3% / 非該当42.1%、差+20.2pt）
- **ステータス傾向：** 体力（該当n=261、49.4% / 非該当33.0%、差+16.4pt）；魔法防御（該当n=75、46.7% / 非該当44.6%、差+2.0pt）
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

### JUNGLE（231試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3053|ステラックの篭手]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（該当n=47、68.1% / 非該当42.9%、差+25.2pt）；[[wiki/entities/items/item-3053|ステラックの篭手]] + [[wiki/entities/items/item-3071|ブラック クリーバー]]（該当n=45、66.7% / 非該当43.5%、差+23.1pt）
- **ステータス傾向：** 物理防御（該当n=141、51.8% / 非該当42.2%、差+9.6pt）
- **理論仮説：** [[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-6333|デス ダンス]]（n=10（15未満）；共通stats: 物理防御・攻撃力／チャンピオン原典にも言及: 物理防御・攻撃力）；[[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3814|ナイト エッジ]]（n=3（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-80|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=457）

- **高勝率コンボ候補：** [[wiki/entities/champions/ezreal|エズリアル（Ezreal）]] — 対象側勝率62.5%（20/32）、n=32（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率51.5%（17/33）、n=33（十分性の目安を満たす）。

### JUNGLE（対象n=310）

- **高勝率コンボ候補：** [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率64.7%（11/17）、サンプル不足（n=17、十分性の目安30未満）。
- **カウンターピック候補：** [[wiki/entities/champions/lillia|リリア（Lillia）]] — 対象側勝率46.7%（7/15）、サンプル不足（n=15、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Pantheon` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Pantheon.png)
