---
title: "メル"
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
  - role-support
  - data-dragon
champion_id: "Mel"
champion_key: "800"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Mel.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Mel.png"
---

# メル

![[raw/assets/champions/Mel.png|128]]

## 基本情報

- **英字ID：** `Mel`
- **キー：** `800`
- **称号：** 魂の反照
- **データversion：** `16.18.1`

## 紹介

メル・メダルダは、かつてはノクサスで最大の権勢を誇ったメダルダ家の後継者と目される人物。表向きは優雅な貴族のように見えるが、その実体は、出会う相手のすべてについて知り尽くそうとする、卓越した政治家。謎に満ちた黒薔薇団との邂逅を経て、母の欺瞞の深さを知ることとなったメルは、自分自身の手に余る可能性がある状況に直面する。新たに目覚めた魔法の力を携え、答えを求めて故郷へと出帆したメル。その内なる光を押さえ込もうとする者が後を絶たない中でも、彼女の魂は決して屈することはない。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 4 |
| `magic` | 9 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 99 |
| `mp` | 480 |
| `mpperlevel` | 28 |
| `movespeed` | 330 |
| `armor` | 21 |
| `armorperlevel` | 5.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 9 |
| `mpregenperlevel` | 0.9 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 54 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 灼熱の輝き：** スキルを使用するたび、次の通常攻撃で追加の飛翔物を3発発射する(最大9発までスタック可能)。 スキルまたは通常攻撃でダメージを与えると、敵に「圧倒」のスタックを付与する。これは無限にスタックする。敵に蓄積した「圧倒」スタックが一定のダメージ量に達すると、スタックを消費して敵にとどめを刺す。

- **Q — 輝きの連撃：** 指定地点に向かって複数の飛翔物を連続で発射する。飛翔物は爆発して範囲内の敵に繰り返しダメージを与える。
- **W — 反駁：** 自身の周囲にバリアを形成する。このバリアは敵の発射物をその敵に向けて反射し、自身が受けるダメージを防ぎ、自身の移動速度を増加させる。
- **E — 陽光の枷：** 前方に輝くオーブを発射し、中心にいた敵にはスネア効果を与え、周囲にいた敵にはスロウ効果と継続ダメージを与える。
- **R — 黄金蝕：** 距離に関係なく、「圧倒」を付与しているすべての敵を攻撃し、「圧倒」のスタック数に応じて追加ダメージを与える。 「黄金蝕」のスキルレベルが上がると、「圧倒」のダメージが増加する。

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
- **対象試合：** 518試合、全体勝率 46.5%
- **時間帯別勝率：** 〜20分 47.2%（n=89）、20〜25分 45.1%（n=71）、25〜30分 50.0%（n=100）、30〜35分 43.3%（n=127）、35分〜 47.3%（n=131）
- **最高帯：** 25〜30分（判定差 6.7ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-800|メルの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（512試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3175|連呪使いのブーツ]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=31、64.5% / 非該当46.4%、差+18.2pt）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3157|ゾーニャの砂時計]]（該当n=33、60.6% / 非該当46.6%、差+14.1pt）
- **ステータス傾向：** 体力（該当n=375、48.8% / 非該当43.8%、差+5.0pt）
- **理論仮説：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3040|セラフ エンブレイス]]（n=14（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=14（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

### UTILITY（272試合）

- **実測ビルド候補：** [[wiki/entities/items/item-4645|シャドウフレイム]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（該当n=67、58.2% / 非該当45.9%、差+12.4pt）；[[wiki/entities/items/item-6653|ライアンドリーの仮面]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（該当n=43、53.5% / 非該当48.0%、差+5.5pt）
- **ステータス傾向：** 物理防御（該当n=43、55.8% / 非該当47.6%、差+8.2pt）；体力（該当n=122、50.0% / 非該当48.0%、差+2.0pt）
- **理論仮説：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=13（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3040|セラフ エンブレイス]]（n=5（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-800|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=628）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/darius|ダリウス（Darius）]] — 対象側勝率63.3%（19/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率61.0%（25/41）、n=41（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率56.7%（34/60）、n=60（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/viktor|ビクター（Viktor）]] — 対象側勝率29.0%（9/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/hwei|フェイ（Hwei）]] — 対象側勝率38.9%（14/36）、n=36（十分性の目安を満たす）。
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率53.2%（42/79）、n=79（十分性の目安を満たす）。

### UTILITY（対象n=332）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率40.0%（14/35）、n=35（十分性の目安を満たす）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率36.1%（13/36）、n=36（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率35.5%（11/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率48.6%（17/35）、n=35（十分性の目安を満たす）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合20,010件、[[reports/riot-ranked-match-analysis/run-20260915T103154Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### MIDDLE（対象647試合、全体勝率49.5%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系栄華：最期の慈悲・冷静沈着；シャードUNKNOWN(5007)・UNKNOWN(5008)・UNKNOWN(5001) | 302/647 | 46.7% | 49.0% |
| 2 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系栄華：冷静沈着・最期の慈悲；シャードUNKNOWN(5007)・UNKNOWN(5008)・UNKNOWN(5001) | 101/647 | 15.6% | 50.5% |
| 3 | 主系天啓：ファーストストライク／魔法の靴・ビスケットデリバリー・宇宙の英知；副系魔道：強まる嵐・マナフローバンド；シャードUNKNOWN(5007)・UNKNOWN(5008)・UNKNOWN(5001) | 33/647 | 5.1% | 39.4% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Mel` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Mel.png)
