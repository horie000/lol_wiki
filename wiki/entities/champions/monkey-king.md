---
title: "ウーコン"
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
champion_id: "MonkeyKing"
champion_key: "62"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/MonkeyKing.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/MonkeyKing.png"
---

# ウーコン

![[raw/assets/champions/MonkeyKing.png|128]]

## 基本情報

- **英字ID：** `MonkeyKing`
- **キー：** `62`
- **称号：** 美猴王
- **データversion：** `16.18.1`

## 紹介

ヴァスタヤのトリックスターであるウーコンは、自身の強さと俊敏さ、さらに賢さを駆使して敵を翻弄し、優位に立って戦うことを得意とする。彼はマスター・イーという名の戦士を生涯の友として見出し、古来より伝わる伝説の武術「ウージュー」を学ぶ最後の弟子となった。魔法の棍を得物に、ウーコンはアイオニアを滅亡から守るための手段を探し求めている。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

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
| `hp` | 610 |
| `hpperlevel` | 99 |
| `mp` | 330 |
| `mpperlevel` | 65 |
| `movespeed` | 340 |
| `armor` | 31 |
| `armorperlevel` | 4.7 |
| `spellblock` | 28 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 3.5 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 66 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.69 |

## アビリティ

- **パッシブ — 岩の皮膚：** チャンピオンまたはモンスターと戦闘中は、スタック可能な物理防御と最大体力に応じた自動回復を獲得する。

- **Q — 強棒打：** 次の通常攻撃の射程が増加して追加ダメージを与え、対象の物理防御を数秒間低下させる。
- **W — 戦士の幻惑：** インビジブル状態になって指定方向にダッシュする。元いた場所には近くの敵を攻撃する分身が残る。
- **E — 乱像猿技：** 指定した対象に向かって突撃し、複数の残像を発生させる。残像は対象の近くにいる敵ユニットを攻撃し、対象それぞれにダメージを与える。
- **R — 旋風猿舞：** 如意棒を伸ばして回転し、自身の移動速度が増加する。 如意棒に触れた敵にダメージを与えてノックアップさせる。

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

- **観測分類：** 序盤寄り
- **対象試合：** 249試合、全体勝率 51.8%
- **時間帯別勝率：** 〜20分 63.9%（n=36）、20〜25分 55.3%（n=38）、25〜30分 51.6%（n=64）、30〜35分 48.4%（n=62）、35分〜 44.9%（n=49）
- **最高帯：** 〜20分（判定差 19.0ポイント）
- **判定根拠：** 〜20分が最高、長時間帯との差 19.0%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-62|ウーコンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（416試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6333|デス ダンス]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（該当n=37、70.3% / 非該当49.3%、差+20.9pt）；[[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6333|デス ダンス]]（該当n=64、68.8% / 非該当48.0%、差+20.7pt）
- **ステータス傾向：** 攻撃速度（該当n=375、52.3% / 非該当41.5%、差+10.8pt）；物理防御（該当n=278、54.7% / 非該当44.2%、差+10.5pt）
- **理論仮説：** [[wiki/entities/items/item-3161|ショウジンの矛]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（n=1（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6609|ケミパンク チェーンソード]]（n=1（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-62|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=528）

- **高勝率コンボ候補：** [[wiki/entities/champions/viktor|ビクター（Viktor）]] — 対象側勝率62.9%（22/35）、n=35（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率36.4%（12/33）、n=33（十分性の目安を満たす）。

### TOP（対象n=42）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.MonkeyKing` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/MonkeyKing.png)
