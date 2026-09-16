---
title: "リサンドラ"
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
  - data-dragon
champion_id: "Lissandra"
champion_key: "127"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Lissandra.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lissandra.png"
---

# リサンドラ

![[raw/assets/champions/Lissandra.png|128]]

## 基本情報

- **英字ID：** `Lissandra`
- **キー：** `127`
- **称号：** 氷の魔女
- **データversion：** `16.18.1`

## 紹介

リサンドラの魔力は清らかな氷さえも闇で汚し、暗く恐ろしいモノへとねじ曲げる。彼女が操る黒き氷はただ物を凍らせるだけにとどまらず、彼女に従わぬ者を刺し貫き、押しつぶす武器となる。北部の民からは“氷の魔女”と呼ばれ恐れられるリサンドラだが、その実体は遥かに邪悪だ。彼女は世界に氷河期をもたらさんとたくらむ、自然の破壊者なのだ。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 5 |
| `magic` | 8 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 110 |
| `mp` | 475 |
| `mpperlevel` | 30 |
| `movespeed` | 325 |
| `armor` | 22 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.5 |
| `attackspeed` | 0.656 |

## アビリティ

- **パッシブ — アイスボーンへの服従：** リサンドラの近くで倒された敵チャンピオンは「氷の奴隷」になる。「氷の奴隷」は周囲の敵にスロウ効果を与え、少ししてから極度の寒さに砕け散り、周囲の対象に魔法ダメージを与える。

- **Q — アイスシャード：** 氷の槍を放ち、最初に命中した敵に魔法ダメージとスロウ効果を与える。槍は対象に当たると破片になって、背後にいる敵に同量の魔法ダメージを与える。
- **W — リング・オブ・フロスト：** 周囲にいる敵ユニットを氷漬けにして魔法ダメージを与え、スネア効果を付与する。
- **E — グラシアルパス：** 前進する氷の爪を召喚し、触れた敵ユニットに魔法ダメージを与える。効果時間内に再度発動すると、爪の位置へワープする。
- **R — フローズングレイブ：** 敵チャンピオンに使用した場合、対象は凍結してスタン状態になる。自身に使用すると、体が闇の氷で覆われ体力を回復するとともに、対象指定されず無敵になる。発動後対象の足元から闇の氷が広がり、触れた敵ユニットに魔法ダメージとスロウ効果を付与する。

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
- **観測分類：** 判定保留（分母不足）
- **対象試合：** 64試合、全体勝率 53.1%
- **時間帯別勝率：** 〜20分 55.6%（n=9）、20〜25分 66.7%（n=9）、25〜30分 56.2%（n=16）、30〜35分 41.2%（n=17）、35分〜 53.8%（n=13）
- **最高帯：** 20〜25分（判定差 不明）
- **判定根拠：** 全5帯で各15試合未満の帯がある。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-127|リサンドラの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（157試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-3175|連呪使いのブーツ]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=38、63.2% / 非該当48.7%、差+14.4pt）；[[wiki/entities/items/item-3175|連呪使いのブーツ]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=46、60.9% / 非該当48.6%、差+12.2pt）
- **ステータス傾向：** 物理防御（該当n=104、58.7% / 非該当39.6%、差+19.0pt）；体力（該当n=119、54.6% / 非該当44.7%、差+9.9pt）
- **理論仮説：** [[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=3（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）；[[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（n=3（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-127|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=247）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率62.5%（10/16）、サンプル不足（n=16、十分性の目安30未満）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率58.8%（10/17）、サンプル不足（n=17、十分性の目安30未満）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率53.3%（8/15）、サンプル不足（n=15、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率36.8%（7/19）、サンプル不足（n=19、十分性の目安30未満）。
  - [[wiki/entities/champions/yasuo|ヤスオ（Yasuo）]] — 対象側勝率42.1%（8/19）、サンプル不足（n=19、十分性の目安30未満）。

### TOP（対象n=27）

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

### MIDDLE（対象187試合、全体勝率51.3%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系覇道：電撃／追い打ち・グリスリー メメント・至極の賞金首狩り；副系魔道：マナフローバンド・至高；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 61/187 | 32.6% | 50.8% |
| 2 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系覇道：追い打ち・至極の賞金首狩り；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 37/187 | 19.8% | 51.4% |
| 3 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系覇道：追い打ち・至極の賞金首狩り；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 7/187 | 3.7% | 57.1% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

<!-- champion-tier-analysis:start -->
## 観測ランク帯別チャンピオン候補

- **スナップショット：** 2026-09-16生成、キュー420、観測10帯、各1,000試合、統合後9,761試合、min-games 15、[[reports/riot-ranked-tier-analysis/run-20260916T083219Z/report|ランク帯別詳細レポート]]。
- **根拠：** [[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis|Riotランク戦試合データ：観測ランク帯別特徴]]、[[wiki/syntheses/ranked-tier-characteristics|ランク帯別の試合特徴と全帯共通傾向]]。
- **読み方：** `observed_tier` はその試合を発見したプレイヤーの収集時点の所属帯であり、10人全員の試合時ランクではない。以下は各帯の上位選択と、min-games以上で機械的に抽出した高低勝率の探索候補で、推奨・因果効果・有意差を示さない。

### 低勝率候補（下位5）

| 観測帯 | 候補順位 | 試合数 | 勝敗 | 勝率 |
| --- | ---: | ---: | --- | ---: |
| GOLD | 5 | 27 | 9勝/18敗 | 33.3% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Lissandra` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lissandra.png)
