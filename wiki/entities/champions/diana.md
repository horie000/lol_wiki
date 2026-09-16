---
title: "ダイアナ"
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
tags:
  - champion
  - role-fighter
  - role-assassin
  - data-dragon
champion_id: "Diana"
champion_key: "131"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Diana.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Diana.png"
---

# ダイアナ

![[raw/assets/champions/Diana.png|128]]

## 基本情報

- **英字ID：** `Diana`
- **キー：** `131`
- **称号：** 嘲りの月
- **データversion：** `16.18.1`

## 紹介

三日月形の剣を掲げ振るうダイアナは、霊峰ターゴンの周辺においては迫害により途絶えて久しいルナリの教えに信仰を寄せる女戦士だ。闇の中で冷たく輝く真冬の雪を思わせる鎧を身にまとうその姿は、まさに銀月の力の具現と呼ぶに相応しい。そびえ立つ霊峰ターゴンの頂の向こうから神髄を授かったダイアナは、もはや人間を超越した存在となり、自身の力とこの世における存在意義を見出そうと模索している。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 6 |
| `magic` | 8 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 109 |
| `mp` | 375 |
| `mpperlevel` | 25 |
| `movespeed` | 345 |
| `armor` | 31 |
| `armorperlevel` | 4.3 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.85 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 57 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 繊月の刃：** 通常攻撃3回ごとに周囲の敵に追加魔法ダメージを与える。スキル使用後、5秒間、攻撃速度が増加する。

- **Q — 月影：** 弧を描くように月の力を放ち、命中した敵ユニットに魔法ダメージを与える。 命中した敵には「月光」を付与し、ステルス状態の敵をのぞいて3秒間可視状態にする。
- **W — 朧月の羽衣：** 体の周囲を3つの月光の玉が旋回し、敵と接触すると爆発して有効範囲内の敵ユニットにダメージを与える。さらに発動と同時に、ダイアナを守るシールドが発生する。3つ目の光の玉が爆発すると、シールドを再び展開する。
- **E — 月下美刃：** 復讐心に燃える月の化身となり、敵のところまでダッシュして魔法ダメージを与える。 「月光」が付与された敵に使用した場合、クールダウンがリセットされると同時に、全ての敵ユニットの「月光」が解除される。
- **R — 崩月：** 周囲のすべての敵を可視化して自身の方向に引き寄せ、スロウ効果を与える。 1体以上の敵チャンピオンを引き寄せると、少ししてから自身の上に月光が降り注ぎ、周囲の範囲内の敵に魔法ダメージを与える。このダメージは2体目以降に引き寄せた対象が1体増えるごとに増加する。

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
- **対象試合：** 495試合、全体勝率 49.9%
- **時間帯別勝率：** 〜20分 50.9%（n=57）、20〜25分 40.3%（n=62）、25〜30分 52.2%（n=134）、30〜35分 50.4%（n=125）、35分〜 51.3%（n=117）
- **最高帯：** 25〜30分（判定差 11.9ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-131|ダイアナの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（601試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3157|ゾーニャの砂時計]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=52、67.3% / 非該当50.1%、差+17.2pt）；[[wiki/entities/items/item-3115|ナッシャー トゥース]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=37、62.2% / 非該当50.9%、差+11.3pt）
- **ステータス傾向：** 体力（該当n=503、53.3% / 非該当42.9%、差+10.4pt）；攻撃速度（該当n=408、53.9% / 非該当46.6%、差+7.3pt）
- **理論仮説：** [[wiki/entities/items/item-3124|グインソー レイジブレード]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度／チャンピオン原典にも言及: 攻撃力・攻撃速度）；[[wiki/entities/items/item-3124|グインソー レイジブレード]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度／チャンピオン原典にも言及: 攻撃力・攻撃速度）

### MIDDLE（374試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3175|連呪使いのブーツ]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=164、58.5% / 非該当39.5%、差+19.0pt）；[[wiki/entities/items/item-3157|ゾーニャの砂時計]] + [[wiki/entities/items/item-3175|連呪使いのブーツ]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=85、60.0% / 非該当44.3%、差+15.7pt）
- **ステータス傾向：** 攻撃速度（該当n=53、56.6% / 非該当46.4%、差+10.2pt）；体力（該当n=273、49.1% / 非該当44.6%、差+4.5pt）
- **理論仮説：** [[wiki/entities/items/item-3121|フィンブルウィンター]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（未観測；共通stats: 体力・マナ／チャンピオン原典にも言及: 体力・マナ）；[[wiki/entities/items/item-2510|黄昏と暁]] + [[wiki/entities/items/item-3115|ナッシャー トゥース]]（n=8（15未満）；共通stats: 魔力・攻撃速度／チャンピオン原典にも言及: 攻撃速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-131|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=761）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/smolder|スモルダー（Smolder）]] — 対象側勝率70.3%（26/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/malzahar|マルザハール（Malzahar）]] — 対象側勝率64.9%（24/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/kaisa|カイ＝サ（Kaisa）]] — 対象側勝率63.4%（26/41）、n=41（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率36.2%（17/47）、n=47（十分性の目安を満たす）。
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率42.2%（19/45）、n=45（十分性の目安を満たす）。
  - [[wiki/entities/champions/briar|ブライアー（Briar）]] — 対象側勝率44.1%（15/34）、n=34（十分性の目安を満たす）。

### MIDDLE（対象n=504）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率58.8%（30/51）、n=51（十分性の目安を満たす）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率55.6%（20/36）、n=36（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率53.2%（25/47）、n=47（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率39.4%（13/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率56.7%（17/30）、n=30（十分性の目安を満たす）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-16生成、キュー420、ユニーク試合10,000件、[[reports/riot-ranked-match-analysis/run-20260916T081004Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### MIDDLE（対象294試合、全体勝率47.3%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系覇道：電撃／サドンインパクト・グリスリー メメント・貪欲な賞金首狩り；副系不滅：ボーンアーマー・シールドバッシュ；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 102/294 | 34.7% | 43.1% |
| 2 | 主系覇道：電撃／サドンインパクト・グリスリー メメント・貪欲な賞金首狩り；副系魔道：マナフローバンド・追火；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 34/294 | 11.6% | 41.2% |
| 3 | 主系魔道：嵐乗りの勇躍／マナフローバンド・英気集中・追火；副系不滅：シールドバッシュ・ボーンアーマー；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 19/294 | 6.5% | 57.9% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Diana` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Diana.png)
