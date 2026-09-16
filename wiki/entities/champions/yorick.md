---
title: "ヨリック"
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
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "Yorick"
champion_key: "83"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Yorick.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yorick.png"
---

# ヨリック

![[raw/assets/champions/Yorick.png|128]]

## 基本情報

- **英字ID：** `Yorick`
- **キー：** `83`
- **称号：** 魂の導き手
- **データversion：** `16.18.1`

## 紹介

ヨリックは忘れ去られて久しいある教団の修道士として唯一生き残った。彼は死者を操ることができるが、その力は恵みであり、また呪いでもある。シャドウアイルに囚われた彼の仲間と呼べるのは、朽ちた屍と、甲高い叫び声を上げながら集まってくる亡霊のみだ。ヨリックの恐ろしい行いは、「破滅」の呪いから故郷を解放したいという彼の崇高な決意と相反するようにも見える。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 6 |
| `magic` | 4 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 114 |
| `mp` | 300 |
| `mpperlevel` | 60 |
| `movespeed` | 340 |
| `armor` | 36 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 魂の導き手：** 呪われし一群: 周囲の敵に襲いかかり攻撃する「ミストウォーカー」を召喚する。

- **Q — 葬送：** 次に行う通常攻撃が追加ダメージを与えて自身を回復する。対象がチャンピオンか大型モンスターだった場合、または対象が倒された場合は墓が掘られる。
- **W — 屍の列：** 指定した地点に破壊可能な壁を召喚し、敵ユニットの動きを阻止する。
- **E — 悲嘆の霧：** 「黒き霧」の塊を投げつけて物理防御を低下させ、ダメージとスロウ効果を与え、対象をマークする。召喚したユニットはマークされた対象に向かう際は移動速度が増加する。
- **R — 嘆きの墓標：** ヨリックが「霧の乙女」を召喚する。「霧の乙女」が攻撃している対象を自身が攻撃すると追加ダメージを与える。「霧の乙女」は倒された敵から自動的に「ミストウォーカー」を召喚する。

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
- **対象試合：** 617試合、全体勝率 51.7%
- **時間帯別勝率：** 〜20分 55.6%（n=108）、20〜25分 50.0%（n=90）、25〜30分 59.2%（n=142）、30〜35分 52.1%（n=140）、35分〜 41.6%（n=137）
- **最高帯：** 25〜30分（判定差 17.5ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-83|ヨリックの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（947試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-3174|装甲強化の進撃]]（該当n=35、65.7% / 非該当50.3%、差+15.4pt）；[[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3161|ショウジンの矛]]（該当n=79、59.5% / 非該当50.1%、差+9.4pt）
- **ステータス傾向：** 移動速度（該当n=895、52.5% / 非該当23.1%、差+29.4pt）；攻撃力（該当n=913、51.8% / 非該当26.5%、差+25.3pt）
- **理論仮説：** [[wiki/entities/items/item-3142|妖夢の霊剣]] + [[wiki/entities/items/item-3181|ハルブレイカー]]（n=4（15未満）；共通stats: 攻撃力・移動速度／チャンピオン原典にも言及: 攻撃力・移動速度）；[[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-6333|デス ダンス]]（n=1（15未満）；共通stats: 物理防御・攻撃力／チャンピオン原典にも言及: 物理防御・攻撃力）

### MIDDLE（84試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 体力再生（該当n=33、75.8% / 非該当51.0%、差+24.8pt）；魔法防御（該当n=37、62.2% / 非該当59.6%、差+2.6pt）
- **理論仮説：** [[wiki/entities/items/item-3142|妖夢の霊剣]] + [[wiki/entities/items/item-3181|ハルブレイカー]]（n=1（15未満）；共通stats: 攻撃力・移動速度／チャンピオン原典にも言及: 攻撃力・移動速度）；[[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-3181|ハルブレイカー]]（n=10（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-83|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=1,154）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/warwick|ワーウィック（Warwick）]] — 対象側勝率76.7%（23/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率62.7%（37/59）、n=59（十分性の目安を満たす）。
  - [[wiki/entities/champions/malzahar|マルザハール（Malzahar）]] — 対象側勝率61.1%（33/54）、n=54（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/chogath|チョ＝ガス（Chogath）]] — 対象側勝率40.0%（20/50）、n=50（十分性の目安を満たす）。
  - [[wiki/entities/champions/renekton|レネクトン（Renekton）]] — 対象側勝率43.4%（23/53）、n=53（十分性の目安を満たす）。
  - [[wiki/entities/champions/sett|セト（Sett）]] — 対象側勝率44.0%（22/50）、n=50（十分性の目安を満たす）。

### MIDDLE（対象n=100）

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

### TOP（対象641試合、全体勝率47.9%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系不滅：不死者の握撃／打ちこわし・ボーンアーマー・超成長；副系栄華：レジェンド: 血脈・冷静沈着；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 210/641 | 32.8% | 46.7% |
| 2 | 主系栄華：征服者／凱旋・レジェンド: 血脈・背水の陣；副系不滅：ボーンアーマー・打ちこわし；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 75/641 | 11.7% | 46.7% |
| 3 | 主系魔道：秘儀の彗星／マナフローバンド・至高・強まる嵐；副系天啓：ビスケットデリバリー・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 61/641 | 9.5% | 42.6% |

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
| MASTER | 1 | 20 | 5勝/15敗 | 25.0% |
| GRANDMASTER | 2 | 24 | 7勝/17敗 | 29.2% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Yorick` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yorick.png)
