---
title: "ケイン"
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
champion_id: "Kayn"
champion_key: "141"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Kayn.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kayn.png"
---

# ケイン

![[raw/assets/champions/Kayn.png|128]]

## 基本情報

- **英字ID：** `Kayn`
- **キー：** `141`
- **称号：** 無情の影
- **データversion：** `16.18.1`

## 紹介

恐るべき影の魔術の卓越した使い手であるシエダ・ケイン。彼は己の真の運命──いつの日か自分が「影の一団」を率い、アイオニアが覇権を握る新時代を拓く、という未来のために戦っている。彼が手にする、自我を持つダーキンの武器「ラースト」はケインの心身を着実に侵しつつあるが、気に留める様子はない。あり得る結末はただ二つ。ケインが強い意志で武器をねじ伏せるか、または邪悪な武器に完全に乗っ取られ、ルーンテラを滅亡の道へと誘う扉を開くかだ。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 10 |
| `defense` | 6 |
| `magic` | 1 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 655 |
| `hpperlevel` | 103 |
| `mp` | 410 |
| `mpperlevel` | 50 |
| `movespeed` | 340 |
| `armor` | 38 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.95 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.7 |
| `attackspeed` | 0.669 |

## アビリティ

- **パッシブ — 緋眼の大鎌：** ケインは自我を持つダーキンの古代武器ラーストを用いており、両者は常に互いの支配権をかけて争っている。この戦いはダーキンがケインを取り込むか、ケインがラーストを使いこなし影の暗殺者となるまで続く。 ダーキン: 敵チャンピオンにスキルで与えたダメージの一定割合にあたる体力を回復する。 影の暗殺者: 敵チャンピオンと戦闘開始直後の数秒間、追加ダメージを与える。

- **Q — 飛影斬：** ダッシュしてから斬りつける。その両方でダメージを与える。
- **W — 刃影襲：** 直線上にいる敵にダメージとスロウ効果を与える。
- **E — 影抜き：** ケインが地形を無視して歩くことができる。
- **R — 真影侵壊：** 敵の体の中に侵入して、出てくる時に大ダメージを与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中13位（上位15%）。体力655、物理防御38、攻撃力68、移動速度340。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 明瞭な傾向なし
- **対象試合：** 300試合、全体勝率 52.7%
- **時間帯別勝率：** 〜20分 54.5%（n=44）、20〜25分 46.5%（n=43）、25〜30分 54.9%（n=71）、30〜35分 58.7%（n=75）、35分〜 46.3%（n=67）
- **最高帯：** 30〜35分（判定差 12.4ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-141|ケインの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（573試合）

- **実測ビルド候補：** [[wiki/entities/items/item-6696|アクシオム アーク]] + [[wiki/entities/items/item-6699|ボルテイク サイクロソード]]（該当n=61、68.9% / 非該当47.3%、差+21.6pt）；[[wiki/entities/items/item-6696|アクシオム アーク]] + [[wiki/entities/items/item-6697|ヒュブリス]] + [[wiki/entities/items/item-6699|ボルテイク サイクロソード]]（該当n=31、67.7% / 非該当48.5%、差+19.2pt）
- **ステータス傾向：** 体力（該当n=397、50.9% / 非該当46.6%、差+4.3pt）
- **理論仮説：** [[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-6333|デス ダンス]]（n=10（15未満）；共通stats: 物理防御・攻撃力／チャンピオン原典にも言及: 物理防御・攻撃力）；[[wiki/entities/items/item-3161|ショウジンの矛]] + [[wiki/entities/items/item-3814|ナイト エッジ]]（n=4（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

### TOP（39試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3161|ショウジンの矛]]（n=8（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3161|ショウジンの矛]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=1（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-141|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=791）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/malphite|マルファイト（Malphite）]] — 対象側勝率64.9%（24/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/yasuo|ヤスオ（Yasuo）]] — 対象側勝率63.3%（19/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率62.7%（47/75）、n=75（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/master-yi|マスター・イー（MasterYi）]] — 対象側勝率33.3%（11/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率52.9%（18/34）、n=34（十分性の目安を満たす）。
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率64.7%（33/51）、n=51（十分性の目安を満たす）。

### TOP（対象n=104）

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

### JUNGLE（対象598試合、全体勝率52.3%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系覇道：魂の収穫／サドンインパクト・グリスリー メメント・貪欲な賞金首狩り；副系天啓：宇宙の英知・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 92/598 | 15.4% | 54.3% |
| 2 | 主系栄華：征服者／凱旋・レジェンド: ヘイスト・背水の陣；副系魔道：アクシオム アルカニスト・至高；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 77/598 | 12.9% | 46.8% |
| 3 | 主系栄華：征服者／凱旋・レジェンド: ヘイスト・背水の陣；副系天啓：宇宙の英知・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 67/598 | 11.2% | 59.7% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kayn` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kayn.png)
