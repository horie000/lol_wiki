---
title: "ベイガー"
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
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection]]"
tags:
  - champion
  - role-mage
  - data-dragon
champion_id: "Veigar"
champion_key: "45"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Veigar.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Veigar.png"
---

# ベイガー

![[raw/assets/champions/Veigar.png|128]]

## 基本情報

- **英字ID：** `Veigar`
- **キー：** `45`
- **称号：** 小さき大魔王
- **データversion：** `16.18.1`

## 紹介

定命の者が恐れて近づこうとしなかった力を受け入れたベイガーは情熱的な闇の魔術の使い手だ。自由な精神を持つバンドルシティの住人として、彼はヨードルの魔法の限界を超えてみたいと願い、数千年に渡って隠されてきた古文書を紐解いた。世界の謎に尽きぬ興味を持つ頑固者のベイガーだが、周囲からは見くびられることが多く、彼自身は自分は真に邪悪な存在だと思っているにもかかわらず、彼の内面に存在する倫理観を見て、彼の真の動機に疑いを持つ者もいる。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 2 |
| `magic` | 10 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 108 |
| `mp` | 490 |
| `mpperlevel` | 26 |
| `movespeed` | 340 |
| `armor` | 18 |
| `armorperlevel` | 5.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 52 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.24 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 偉大なる悪の力：** ルーンテラを脅かす強大な悪であるベイガー、その力はとどまるところを知らない！敵チャンピオンからキルまたはアシストを獲得したり、スキルを命中させると、ベイガーの魔力は永続的に増加してゆく。

- **Q — イーヴィルストライク：** 指定方向に闇のエネルギーを発射し、最初に命中した敵2体に魔法ダメージを与える。このスキルで敵ユニットにとどめを刺すと、ベイガーの魔力が永続的に増加する。
- **W — ダークマター：** 指定地点に巨大な暗黒物質を降らせ、着地時に魔法ダメージを与える。「偉大なる悪の力」のスタックに応じて「ダークマター」のクールダウンが短縮される。
- **E — イベントホライズン：** 空間の境界をねじ曲げて檻を作り出す。檻を通過した敵はスタンする。
- **R — メテオバースト：** 敵チャンピオン1体に闇の大魔法を放ち、対象の減少体力に応じて増加する大量の魔法ダメージを与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - キル・アシスト・スキル命中で魔力が永続的に増加する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 610試合、全体勝率 53.3%
- **時間帯別勝率：** 〜20分 32.1%（n=81）、20〜25分 54.3%（n=92）、25〜30分 55.9%（n=143）、30〜35分 59.7%（n=144）、35分〜 55.3%（n=150）
- **最高帯：** 30〜35分（判定差 27.6ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-45|ベイガーの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（755試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3157|ゾーニャの砂時計]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=33、69.7% / 非該当51.1%、差+18.6pt）；[[wiki/entities/items/item-3089|ラバドン デスキャップ]] + [[wiki/entities/items/item-3171|真紅のアイオニア ブーツ]]（該当n=45、68.9% / 非該当50.8%、差+18.0pt）
- **ステータス傾向：** 物理防御（該当n=197、56.3% / 非該当50.4%、差+6.0pt）；体力（該当n=591、53.0% / 非該当48.2%、差+4.8pt）
- **理論仮説：** [[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-6655|ルーデン エコー]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（n=11（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）；[[wiki/entities/items/item-2522|アクチュアライザー]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（n=6（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）

### BOTTOM（232試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3089|ラバドン デスキャップ]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（該当n=36、72.2% / 非該当52.0%、差+20.2pt）；[[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-3089|ラバドン デスキャップ]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（該当n=32、71.9% / 非該当52.5%、差+19.4pt）
- **ステータス傾向：** 物理防御（該当n=94、64.9% / 非該当48.6%、差+16.3pt）；体力（該当n=160、56.9% / 非該当51.4%、差+5.5pt）
- **理論仮説：** [[wiki/entities/items/item-6655|ルーデン エコー]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（n=11（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）；[[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-6655|ルーデン エコー]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（n=8（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-45|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=916）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/darius|ダリウス（Darius）]] — 対象側勝率67.6%（25/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率66.7%（46/69）、n=69（十分性の目安を満たす）。
  - [[wiki/entities/champions/thresh|スレッシュ（Thresh）]] — 対象側勝率66.7%（32/48）、n=48（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/vex|ヴェックス（Vex）]] — 対象側勝率46.9%（15/32）、n=32（十分性の目安を満たす）。
  - [[wiki/entities/champions/viktor|ビクター（Viktor）]] — 対象側勝率48.8%（21/43）、n=43（十分性の目安を満たす）。
  - [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率48.9%（22/45）、n=45（十分性の目安を満たす）。

### BOTTOM（対象n=304）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率64.5%（20/31）、n=31（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率37.9%（11/29）、サンプル不足（n=29、十分性の目安30未満）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率48.0%（12/25）、サンプル不足（n=25、十分性の目安30未満）。
  - [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率50.0%（12/24）、サンプル不足（n=24、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合20,010件、[[reports/riot-ranked-match-analysis/run-20260915T103154Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### MIDDLE（対象908試合、全体勝率50.6%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系天啓：ファーストストライク／魔法の靴・ビスケットデリバリー・宇宙の英知；副系魔道：マナフローバンド・至高；シャードUNKNOWN(5007)・UNKNOWN(5008)・UNKNOWN(5001) | 419/908 | 46.1% | 51.3% |
| 2 | 主系魔道：秘儀の彗星／マナフローバンド・至高・強まる嵐；副系覇道：追い打ち・至極の賞金首狩り；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 114/908 | 12.6% | 50.0% |
| 3 | 主系天啓：ファーストストライク／魔法の靴・ビスケットデリバリー・宇宙の英知；副系魔道：至高・マナフローバンド；シャードUNKNOWN(5007)・UNKNOWN(5008)・UNKNOWN(5001) | 40/908 | 4.4% | 47.5% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Veigar` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Veigar.png)
