---
title: "ザイラ"
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
  - role-mage
  - role-support
  - data-dragon
champion_id: "Zyra"
champion_key: "143"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Zyra.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zyra.png"
---

# ザイラ

![[raw/assets/champions/Zyra.png|128]]

## 基本情報

- **英字ID：** `Zyra`
- **キー：** `143`
- **称号：** 茨の目覚め
- **データversion：** `16.18.1`

## 紹介

古代の魔法の大惨事の中で生まれたザイラは自然の怒りが具現化した存在であり、人間と植物が融合した妖艶な姿で、一歩進むたびに新たな生命を生み出していく。彼女はヴァロランに住む定命の者たちを自分の種から生まれた子供たちの餌食としか見ておらず、恐ろしい棘を使って平気な顔で彼らを抹殺している。その真の目的は定かではないが、ザイラは世界中を歩き回り、本能の赴くままに根を生やして繁殖しては、他のあらゆる生物を絡めとって絞め殺している。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 3 |
| `magic` | 8 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 574 |
| `hpperlevel` | 93 |
| `mp` | 418 |
| `mpperlevel` | 25 |
| `movespeed` | 340 |
| `armor` | 29 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 575 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 53 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.11 |
| `attackspeed` | 0.681 |

## アビリティ

- **パッシブ — 茨の楽園：** 定期的に自身の周囲に種を発生させる。その周期はレベルに応じて速くなる。種の近くで「死華の棘」または「捕縛の根」を使用すると種は植物に成長し、自身の味方となって戦う。

- **Q — 死華の棘：** 太いツルが地中に広がって鋭いトゲを生やし、範囲内の敵に魔法ダメージを与える。「死華の棘」を種の近くで使用すると、遠距離の敵を射撃する「棘吹草」に成長させる。
- **W — 狂い咲き：** 最大60秒間持続する種を生やす。種の近くで「死華の棘」または「捕縛の根」を使用すると種は植物に成長し、味方として戦う。同時に複数の種を蓄えておくことが可能で、敵ユニットを倒すと「狂い咲き」のチャージ時間が短縮される。
- **E — 捕縛の根：** 地中から伸びる巨大なツタが対象を絡めとり、ダメージを与え移動不能にする。「捕縛の根」を種の近くで使用すると「棘鞭草」に成長させ、近距離の敵を攻撃しダメージを与え、移動速度を低下させる。
- **R — 茨のゆりかご：** 指定地点から茨を放射状に成長させて範囲内の敵にダメージを与え、茨が地中に戻る際に触れた敵をノックアップさせる。茨の範囲内の植物は怒り狂う。

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
- **観測分類：** 明瞭な傾向なし
- **対象試合：** 372試合、全体勝率 53.2%
- **時間帯別勝率：** 〜20分 57.4%（n=61）、20〜25分 47.1%（n=51）、25〜30分 54.5%（n=77）、30〜35分 54.1%（n=74）、35分〜 52.3%（n=109）
- **最高帯：** 〜20分（判定差 10.3ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-143|ザイラの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（568試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3175|連呪使いのブーツ]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=42、83.3% / 非該当49.0%、差+34.3pt）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3116|リーライ クリスタル セプター]]（該当n=37、56.8% / 非該当51.2%、差+5.5pt）
- **ステータス傾向：** 体力（該当n=524、51.9% / 非該当47.7%、差+4.2pt）；マナ（該当n=148、52.0% / 非該当51.4%、差+0.6pt）
- **理論仮説：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3118|マリグナンス]]（n=8（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-3118|マリグナンス]]（未観測；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

### JUNGLE（427試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3157|ゾーニャの砂時計]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=205、56.6% / 非該当51.4%、差+5.2pt）；[[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-4645|シャドウフレイム]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=48、58.3% / 非該当53.3%、差+5.0pt）
- **ステータス傾向：** 物理防御（該当n=282、55.0% / 非該当51.7%、差+3.2pt）
- **理論仮説：** [[wiki/entities/items/item-2065|シュレリアの戦歌]] + [[wiki/entities/items/item-4629|コズミック ドライブ]]（未観測；共通stats: 魔力・移動速度／チャンピオン原典にも言及: 移動速度）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3118|マリグナンス]]（未観測；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-143|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=733）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率69.2%（27/39）、n=39（十分性の目安を満たす）。
  - [[wiki/entities/champions/malzahar|マルザハール（Malzahar）]] — 対象側勝率63.6%（21/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率61.4%（27/44）、n=44（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率46.8%（29/62）、n=62（十分性の目安を満たす）。
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率55.0%（22/40）、n=40（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率57.1%（28/49）、n=49（十分性の目安を満たす）。

### JUNGLE（対象n=551）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率59.1%（26/44）、n=44（十分性の目安を満たす）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率58.5%（31/53）、n=53（十分性の目安を満たす）。
  - [[wiki/entities/champions/akshan|アクシャン（Akshan）]] — 対象側勝率55.4%（46/83）、n=83（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/jarvan-iv|ジャーヴァンⅣ（JarvanIV）]] — 対象側勝率25.0%（5/20）、サンプル不足（n=20、十分性の目安30未満）。
  - [[wiki/entities/champions/graves|グレイブス（Graves）]] — 対象側勝率38.5%（10/26）、サンプル不足（n=26、十分性の目安30未満）。
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率44.0%（11/25）、サンプル不足（n=25、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-16生成、キュー420、ユニーク試合10,000件、[[reports/riot-ranked-match-analysis/run-20260916T081004Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### UTILITY（対象437試合、全体勝率50.1%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系覇道：執拗な賞金首狩り・血の味わい；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 141/437 | 32.3% | 46.1% |
| 2 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系覇道：血の味わい・執拗な賞金首狩り；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 74/437 | 16.9% | 54.1% |
| 3 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系天啓：ビスケットデリバリー・宇宙の英知；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 66/437 | 15.1% | 56.1% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

<!-- champion-tier-analysis:start -->
## 観測ランク帯別チャンピオン候補

- **スナップショット：** 2026-09-16生成、キュー420、観測10帯、各1,000試合、統合後9,761試合、min-games 15、[[reports/riot-ranked-tier-analysis/run-20260916T083219Z/report|ランク帯別詳細レポート]]。
- **根拠：** [[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis|Riotランク戦試合データ：観測ランク帯別特徴]]、[[wiki/syntheses/ranked-tier-characteristics|ランク帯別の試合特徴と全帯共通傾向]]。
- **読み方：** `observed_tier` はその試合を発見したプレイヤーの収集時点の所属帯であり、10人全員の試合時ランクではない。以下は各帯の上位選択と、min-games以上で機械的に抽出した高低勝率の探索候補で、推奨・因果効果・有意差を示さない。

### ピック数上位5に入った帯

| 観測帯 | 帯内順位 | 試合数 | ピック率 | 勝敗 | 勝率 |
| --- | ---: | ---: | ---: | --- | ---: |
| PLATINUM | 2 | 228 | 2.3% | 122勝/106敗 | 53.5% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Zyra` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zyra.png)
