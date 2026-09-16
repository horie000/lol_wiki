---
title: "ポッピー"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-16
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection]]"
  - "[[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis]]"
tags:
  - champion
  - role-tank
  - role-fighter
  - data-dragon
champion_id: "Poppy"
champion_key: "78"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Poppy.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Poppy.png"
---

# ポッピー

![[raw/assets/champions/Poppy.png|128]]

## 基本情報

- **英字ID：** `Poppy`
- **キー：** `78`
- **称号：** 大鎚の守護者
- **データversion：** `16.18.1`

## 紹介

ルーンテラの地に勇敢なチャンピオンは数多いものの、ポッピーほど粘り強い者はそうはいない。自分の身長の二倍ほどもある伝説のハンマー、オーロンを携えた不屈のヨードルは、もう何年もの間、彼女のハンマーの「真の持ち主」であるといわれている伝説の戦士「デマーシアの勇者」を密かに探し続けているのだ。真の持ち主が見つかるまで、彼女は使命感を持って戦闘に挑み、ハンマーを振り回して王国の敵を押し返している。

## 分類

- **役割タグ：** `Tank`、`Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 7 |
| `magic` | 2 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 110 |
| `mp` | 300 |
| `mpperlevel` | 45 |
| `movespeed` | 345 |
| `armor` | 35 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 56 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 鋼鉄の大使：** 対象にバックラーを投げつける。対象に命中し跳ね返って落ちたバックラーを拾うことで、一時的にシールドを得る。

- **Q — ハンマーショック：** ハンマーを振り下ろしてダメージを与え、敵をスロウ状態にした後時間を置いて爆発する効果範囲を作り出す。
- **W — ステッドファスト：** 自動効果で物理防御と魔法防御が増加する。このボーナスは体力が低下するとさらに増加する。発動すると移動速度が増加し、自身の周囲にいる敵のダッシュ行動を阻止する。ダッシュを中断させられた敵はスロウ状態および釘付け状態になる。
- **E — ヒロイックチャージ：** 対象に向かってダッシュし、突き飛ばす。対象が壁にぶつかった場合、スタン状態になる。
- **R — 守護者の鉄鎚：** ハンマーに力を溜め、敵を遥か彼方に殴り飛ばす。

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

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 序盤寄り
- **対象試合：** 179試合、全体勝率 50.8%
- **時間帯別勝率：** 〜20分 65.6%（n=32）、20〜25分 42.9%（n=21）、25〜30分 51.0%（n=51）、30〜35分 43.2%（n=44）、35分〜 51.6%（n=31）
- **最高帯：** 〜20分（判定差 14.0ポイント）
- **判定根拠：** 〜20分が最高、長時間帯との差 14.0%。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-78|ポッピーの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（274試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3190|ソラリのロケット]] + [[wiki/entities/items/item-3742|デッド マン プレート]]（該当n=68、58.8% / 非該当47.1%、差+11.7pt）；[[wiki/entities/items/item-3075|ソーンメイル]] + [[wiki/entities/items/item-3742|デッド マン プレート]]（該当n=37、54.1% / 非該当49.4%、差+4.7pt）
- **ステータス傾向：** 魔法防御（該当n=159、50.9% / 非該当48.7%、差+2.2pt）
- **理論仮説：** [[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=9（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力・魔法防御）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=1（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力・魔法防御）

### TOP（65試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3068|サンファイア イージス]] + [[wiki/entities/items/item-3075|ソーンメイル]]（n=7（15未満）；共通stats: 物理防御・体力／チャンピオン原典にも言及: 物理防御・体力）；[[wiki/entities/items/item-3068|サンファイア イージス]] + [[wiki/entities/items/item-6662|アイスボーン ガントレット]]（n=2（15未満）；共通stats: 物理防御・体力／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-78|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=366）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/kaisa|カイ＝サ（Kaisa）]] — 対象側勝率46.9%（15/32）、n=32（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率52.4%（22/42）、n=42（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率66.7%（24/36）、n=36（十分性の目安を満たす）。

### TOP（対象n=114）

- **高勝率コンボ候補（最大3件）：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **低勝率カウンターピック候補（最大3件）：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-16生成、キュー420、ユニーク試合10,000件、[[reports/riot-ranked-match-analysis/run-20260916T081004Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### UTILITY（対象198試合、全体勝率53.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系不滅：アフターショック／生命の泉・ボーンアーマー・気迫；副系天啓：宇宙の英知・ヘクステックフラッシュネイター；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 44/198 | 22.2% | 50.0% |
| 2 | 主系覇道：ヘイルブレード／サドンインパクト・第六感・貪欲な賞金首狩り；副系天啓：宇宙の英知・ヘクステックフラッシュネイター；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 40/198 | 20.2% | 57.5% |
| 3 | 主系覇道：ヘイルブレード／サドンインパクト・第六感・貪欲な賞金首狩り；副系栄華：最期の慈悲・凱旋；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 14/198 | 7.1% | 50.0% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

<!-- champion-tier-analysis:start -->
## 観測ランク帯別チャンピオン候補

- **スナップショット：** 2026-09-16生成、キュー420、観測10帯、各1,000試合、統合後9,761試合、min-games 15、[[reports/riot-ranked-tier-analysis/run-20260916T083219Z/report|ランク帯別詳細レポート]]。
- **根拠：** [[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis|Riotランク戦試合データ：観測ランク帯別特徴]]、[[wiki/syntheses/ranked-tier-characteristics|ランク帯別の試合特徴と全帯共通傾向]]。
- **読み方：** `observed_tier` はその試合を発見したプレイヤーの収集時点の所属帯であり、10人全員の試合時ランクではない。以下は各帯の上位選択と、min-games以上で機械的に抽出した高低勝率の探索候補で、推奨・因果効果・有意差を示さない。

### 高勝率候補（上位5）

| 観測帯 | 候補順位 | 試合数 | 勝敗 | 勝率 |
| --- | ---: | ---: | --- | ---: |
| PLATINUM | 2 | 26 | 18勝/8敗 | 69.2% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Poppy` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Poppy.png)
