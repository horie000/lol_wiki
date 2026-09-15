---
title: "マルファイト"
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
  - role-tank
  - role-mage
  - data-dragon
champion_id: "Malphite"
champion_key: "54"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Malphite.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Malphite.png"
---

# マルファイト

![[raw/assets/champions/Malphite.png|128]]

## 基本情報

- **英字ID：** `Malphite`
- **キー：** `54`
- **称号：** モノリスの欠片
- **データversion：** `16.18.1`

## 紹介

マルファイトは混沌とした世界に祝福の秩序をもたらそうと苦闘する、生きた岩石の巨大な生物だ。モノリスとして知られる異世界のオベリスクに奉仕するかけらとして生まれた彼は、自らの強大な元素の力を使って先祖を何とか守ろうとしたが、その願いは果たせなかった。その後に続いた爆発で唯一の生き残りとなったマルファイトは、今ではルーンテラの移り気で柔らかい者たちの間で暮らしながら、種族の最後の生き残りにふさわしい新たな役割を見つけようとしている。

## 分類

- **役割タグ：** `Tank`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 9 |
| `magic` | 7 |
| `difficulty` | 2 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 665 |
| `hpperlevel` | 104 |
| `mp` | 280 |
| `mpperlevel` | 60 |
| `movespeed` | 335 |
| `armor` | 40 |
| `armorperlevel` | 4.95 |
| `spellblock` | 28 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7.3 |
| `mpregenperlevel` | 0.55 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.4 |
| `attackspeed` | 0.736 |

## アビリティ

- **パッシブ — グラナイトシールド：** 自身の最大体力の10%までのダメージを吸収する岩のシールドを生成する。このシールドは数秒間攻撃を受けないと再生する。

- **Q — サイズミックシャード：** 指定した敵に向かって岩の円盤を転がし、衝突時にダメージを与えて3秒間移動速度を奪う。
- **W — サンダークラップ：** 大きな力で攻撃してソニックブームを発生させる。その後数秒間、通常攻撃で自身の前方に余波が発生する。
- **E — グラウンドスラム：** 地面を強打して衝撃波を起こし、自身の物理防御に応じた魔法ダメージを与える。衝撃波に当たった敵は、攻撃速度が短時間低下する。
- **R — アンストッパブル・フォース：** 指定地点に勢いよく跳躍し、敵ユニットにダメージを与えてノックアップさせる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中25位（上位15%）。体力665、物理防御40、攻撃力62、移動速度335。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 582試合、全体勝率 46.6%
- **時間帯別勝率：** 〜20分 48.4%（n=91）、20〜25分 40.0%（n=75）、25〜30分 45.5%（n=132）、30〜35分 45.8%（n=131）、35分〜 50.3%（n=153）
- **最高帯：** 35分〜（判定差 10.3ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-54|マルファイトの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（725試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3068|サンファイア イージス]] + [[wiki/entities/items/item-3174|装甲強化の進撃]]（該当n=33、75.8% / 非該当45.1%、差+30.7pt）；[[wiki/entities/items/item-2504|ケイニック ルーケルン]] + [[wiki/entities/items/item-3110|フローズン ハート]]（該当n=64、62.5% / 非該当44.9%、差+17.6pt）
- **ステータス傾向：** 体力再生（該当n=50、54.0% / 非該当45.9%、差+8.1pt）；移動速度（該当n=689、46.9% / 非該当38.9%、差+8.0pt）
- **理論仮説：** [[wiki/entities/items/item-3002|先人の道標]] + [[wiki/entities/items/item-3742|デッド マン プレート]]（未観測；共通stats: 物理防御・体力・移動速度／チャンピオン原典にも言及: 物理防御・体力・移動速度）；[[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）

### JUNGLE（224試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2504|ケイニック ルーケルン]] + [[wiki/entities/items/item-3075|ソーンメイル]]（該当n=36、61.1% / 非該当41.5%、差+19.6pt）；[[wiki/entities/items/item-2504|ケイニック ルーケルン]] + [[wiki/entities/items/item-3068|サンファイア イージス]]（該当n=42、57.1% / 非該当41.8%、差+15.4pt）
- **ステータス傾向：** 物理防御（該当n=165、47.9% / 非該当35.6%、差+12.3pt）；体力（該当n=167、47.3% / 非該当36.8%、差+10.5pt）
- **理論仮説：** [[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（n=4（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=1（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-54|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=932）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/master-yi|マスター・イー（MasterYi）]] — 対象側勝率68.8%（22/32）、n=32（十分性の目安を満たす）。
  - [[wiki/entities/champions/kayn|ケイン（Kayn）]] — 対象側勝率64.9%（24/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率56.9%（37/65）、n=65（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/irelia|イレリア（Irelia）]] — 対象側勝率43.3%（13/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率43.5%（27/62）、n=62（十分性の目安を満たす）。
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率47.0%（31/66）、n=66（十分性の目安を満たす）。

### JUNGLE（対象n=311）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率50.0%（15/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率38.7%（12/31）、n=31（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/briar|ブライアー（Briar）]] — 対象側勝率56.2%（9/16）、サンプル不足（n=16、十分性の目安30未満）。
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率61.1%（11/18）、サンプル不足（n=18、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合20,010件、[[reports/riot-ranked-match-analysis/run-20260915T103154Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### TOP（対象1,214試合、全体勝率50.9%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系不滅：超成長・息継ぎ；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 426/1,214 | 35.1% | 48.8% |
| 2 | 主系不滅：不死者の握撃／シールドバッシュ・心身調整・超成長；副系魔道：マナフローバンド・至高；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 218/1,214 | 18.0% | 50.9% |
| 3 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系不滅：息継ぎ・超成長；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 103/1,214 | 8.5% | 51.5% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Malphite` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Malphite.png)
