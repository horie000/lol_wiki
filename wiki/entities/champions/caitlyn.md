---
title: "ケイトリン"
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
  - role-marksman
  - data-dragon
champion_id: "Caitlyn"
champion_key: "51"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Caitlyn.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Caitlyn.png"
---

# ケイトリン

![[raw/assets/champions/Caitlyn.png|128]]

## 基本情報

- **英字ID：** `Caitlyn`
- **キー：** `51`
- **称号：** ピルトーヴァーの保安官
- **データversion：** `16.18.1`

## 紹介

卓越した治安維持能力を有することで名高いケイトリン・キラマンは、都市に潜む犯罪者の撲滅を掲げるピルトーヴァーにとっての切り札的存在でもある。彼女はヴァイとパートナーを組むことが多く、激しい気性のヴァイとは対照的に冷静な彼女の存在が二人の釣り合いを保っている。この世に一つしか存在しないヘクステックライフルを持っているものの、彼女の真の武器は「進歩の都市」で犯罪を目論む愚か者たちに巧妙な罠を仕掛けるその知性だ。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 2 |
| `magic` | 2 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 107 |
| `mp` | 315 |
| `mpperlevel` | 40 |
| `movespeed` | 325 |
| `armor` | 27 |
| `armorperlevel` | 4.7 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 650 |
| `hpregen` | 3.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7.4 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 4 |
| `attackspeed` | 0.681 |

## アビリティ

- **パッシブ — ヘッドショット：** 通常攻撃数回ごと、または自身のトラップやネットにかけた対象に、クリティカル率によってダメージが増加する「ヘッドショット」を発射できる。トラップまたはネットにかけた対象に対しては「ヘッドショット」の射程が2倍になる。

- **Q — ピースメーカー：** 1秒間ライフルをチャージし、指定方向に貫通弾を発射する。貫通弾は命中した敵ユニットに物理ダメージを与える。 (2体目以降へのダメージは徐々に減少する)
- **W — ヨードルトラップ：** トラップを仕掛ける。トラップに触れた敵チャンピオンに1.5秒間スネア効果を付与し、可視状態にする。また、強化された「ヘッドショット」が1回可能になる。
- **E — L-90 カリバーネット：** 重たいネットを発射して、対象に魔法ダメージとスロウ効果を与える。自身はネットを発射した反動で、反対方向にとぶ。
- **R — ブルズアイ：** 1秒かけて狙いを定め、指定した敵チャンピオンを狙撃する。別の敵チャンピオンが射線を塞いだ場合、弾丸はそのチャンピオンに命中する。

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
- **対象試合：** 792試合、全体勝率 49.5%
- **時間帯別勝率：** 〜20分 43.3%（n=127）、20〜25分 53.0%（n=117）、25〜30分 49.2%（n=187）、30〜35分 50.6%（n=174）、35分〜 50.8%（n=187）
- **最高帯：** 20〜25分（判定差 9.7ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-51|ケイトリンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（1,434試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2523|ヘクスオプティックC44]] + [[wiki/entities/items/item-3072|ブラッドサースター]]（該当n=39、74.4% / 非該当48.9%、差+25.5pt）；[[wiki/entities/items/item-3032|ユン・タル ワイルドアロー]] + [[wiki/entities/items/item-3172|ガンメタル ブーツ]]（該当n=31、74.2% / 非該当49.0%、差+25.2pt）
- **ステータス傾向：** ライフスティール（該当n=254、61.8% / 非該当46.9%、差+14.9pt）；物理防御（該当n=190、58.9% / 非該当48.2%、差+10.8pt）
- **理論仮説：** [[wiki/entities/items/item-2523|ヘクスオプティックC44]] + [[wiki/entities/items/item-6673|イモータル シールドボウ]]（n=13（15未満）；共通stats: 攻撃力・クリティカル率／チャンピオン原典にも言及: 攻撃力・クリティカル率）；[[wiki/entities/items/item-2523|ヘクスオプティックC44]] + [[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-6673|イモータル シールドボウ]]（n=12（15未満）；共通stats: 攻撃力・クリティカル率／チャンピオン原典にも言及: 攻撃力・クリティカル率）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-51|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=1,837）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/warwick|ワーウィック（Warwick）]] — 対象側勝率66.7%（26/39）、n=39（十分性の目安を満たす）。
  - [[wiki/entities/champions/karma|カルマ（Karma）]] — 対象側勝率64.7%（33/51）、n=51（十分性の目安を満たす）。
  - [[wiki/entities/champions/malzahar|マルザハール（Malzahar）]] — 対象側勝率63.5%（47/74）、n=74（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率43.6%（78/179）、n=179（十分性の目安を満たす）。
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率44.8%（77/172）、n=172（十分性の目安を満たす）。
  - [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率47.0%（63/134）、n=134（十分性の目安を満たす）。

### MIDDLE（対象n=15）

- **高勝率コンボ候補（最大3件）：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **低勝率カウンターピック候補（最大3件）：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合20,010件、[[reports/riot-ranked-match-analysis/run-20260915T103154Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### BOTTOM（対象2,199試合、全体勝率49.2%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：リーサルテンポ／冷静沈着・レジェンド: 血脈・最期の慈悲；副系魔道：英気集中・強まる嵐；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 917/2,199 | 41.7% | 50.3% |
| 2 | 主系栄華：フリートフットワーク／冷静沈着・レジェンド: 血脈・最期の慈悲；副系魔道：英気集中・強まる嵐；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 247/2,199 | 11.2% | 49.0% |
| 3 | 主系栄華：リーサルテンポ／冷静沈着・レジェンド: 血脈・切り崩し；副系天啓：キャッシュバック・トリプル トニック；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 134/2,199 | 6.1% | 50.0% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Caitlyn` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Caitlyn.png)
