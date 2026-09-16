---
title: "ナサス"
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
  - role-tank
  - data-dragon
champion_id: "Nasus"
champion_key: "75"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Nasus.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nasus.png"
---

# ナサス

![[raw/assets/champions/Nasus.png|128]]

## 基本情報

- **英字ID：** `Nasus`
- **キー：** `75`
- **称号：** 砂漠の司書
- **データversion：** `16.18.1`

## 紹介

ジャッカルの頭を持つ超越者ナサスは、古代シュリーマで生を受けた。威風堂々たる体躯を誇る彼を、砂漠の民は半神半人と崇めていた。頭脳明晰で学問を尊び、比類なき戦略家でもあったナサスは、その豊富な知識で古代シュリーマ帝国を何百年も続く栄華の時代へと導いた。やがて帝国が没落すると、ナサスは自ら故郷を離れ、彼の名は伝説と化した。だが今、再び古代都市シュリーマが蘇り、ナサスは故郷へと戻ってきた。二度とこの街を崩壊させはしないと、心に誓って。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 5 |
| `magic` | 6 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 104 |
| `mp` | 326 |
| `mpperlevel` | 62 |
| `movespeed` | 350 |
| `armor` | 34 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 7.45 |
| `mpregenperlevel` | 0.5 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 67 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.48 |
| `attackspeed` | 0.638 |

## アビリティ

- **パッシブ — ソウルイーター：** 敵の魂のエネルギーを吸い取り、自身のライフスティールが増加する。

- **Q — サイフォンストライク：** 敵を攻撃してダメージを与える。さらに、対象にとどめを刺すと「サイフォンストライク」の威力が増していく。
- **W — ウィザー：** 指定した敵チャンピオンを老化させる。効果時間中、敵の移動速度と攻撃速度が徐々に減少する。
- **E — スピリットファイア：** 指定範囲に神秘的な炎を呼び寄せ、範囲内の敵にダメージを与えて物理防御を低下させる。
- **R — アヌビスの怒り：** 巨大化して、強力な砂嵐を身にまとう。砂嵐をまとっている間は、体力と通常攻撃の射程距離が増加する。またその間は、周囲の敵にダメージを与え、「サイフォンストライク」のクールダウンが短くなり、物理防御と魔法防御が増加する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤、終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中8位（上位15%）。体力650、物理防御34、攻撃力67、移動速度350。
  - 「サイフォンストライク」で敵を倒すたびにダメージが恒久的に増加する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 明瞭な傾向なし
- **対象試合：** 447試合、全体勝率 51.0%
- **時間帯別勝率：** 〜20分 52.9%（n=68）、20〜25分 43.3%（n=67）、25〜30分 53.9%（n=115）、30〜35分 55.8%（n=104）、35分〜 46.2%（n=93）
- **最高帯：** 30〜35分（判定差 12.5ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-75|ナサスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（475試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3065|スピリット ビサージュ]] + [[wiki/entities/items/item-3075|ソーンメイル]]（該当n=46、58.7% / 非該当47.3%、差+11.4pt）；[[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（該当n=34、58.8% / 非該当47.6%、差+11.2pt）
- **ステータス傾向：** 魔法防御（該当n=276、53.6% / 非該当41.2%、差+12.4pt）；攻撃速度（該当n=365、51.0% / 非該当40.0%、差+11.0pt）
- **理論仮説：** [[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力・魔法防御）

### JUNGLE（203試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-3110|フローズン ハート]]（該当n=39、69.2% / 非該当51.8%、差+17.4pt）；[[wiki/entities/items/item-2525|プロトプラズム ハーネス]] + [[wiki/entities/items/item-3110|フローズン ハート]]（該当n=42、66.7% / 非該当52.2%、差+14.5pt）
- **ステータス傾向：** マナ（該当n=69、62.3% / 非該当51.5%、差+10.8pt）；魔法防御（該当n=133、58.6% / 非該当48.6%、差+10.1pt）
- **理論仮説：** [[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力・魔法防御）；[[wiki/entities/items/item-2512|フィーンドハンターの矢]] + [[wiki/entities/items/item-6675|ナヴォリ フリッカーブレード]]（未観測；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-75|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=609）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/hwei|フェイ（Hwei）]] — 対象側勝率64.5%（20/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率62.5%（20/32）、n=32（十分性の目安を満たす）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率54.7%（29/53）、n=53（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/yorick|ヨリック（Yorick）]] — 対象側勝率36.1%（13/36）、n=36（十分性の目安を満たす）。
  - [[wiki/entities/champions/garen|ガレン（Garen）]] — 対象側勝率40.4%（21/52）、n=52（十分性の目安を満たす）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率46.0%（23/50）、n=50（十分性の目安を満たす）。

### JUNGLE（対象n=240）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率66.7%（12/18）、サンプル不足（n=18、十分性の目安30未満）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率64.7%（11/17）、サンプル不足（n=17、十分性の目安30未満）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率60.9%（14/23）、サンプル不足（n=23、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率53.3%（8/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率63.2%（12/19）、サンプル不足（n=19、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-16生成、キュー420、ユニーク試合10,000件、[[reports/riot-ranked-match-analysis/run-20260916T081004Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### TOP（対象375試合、全体勝率51.5%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：フリートフットワーク／凱旋・レジェンド: ヘイスト・背水の陣；副系不滅：息継ぎ・気迫；シャードUNKNOWN(5007)・UNKNOWN(5001)・UNKNOWN(5001) | 180/375 | 48.0% | 50.6% |
| 2 | 主系魔道：嵐乗りの勇躍／マナフローバンド・至高・追火；副系天啓：疾駆・ビスケットデリバリー；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 21/375 | 5.6% | 66.7% |
| 3 | 主系栄華：フリートフットワーク／凱旋・レジェンド: ヘイスト・背水の陣；副系不滅：気迫・息継ぎ；シャードUNKNOWN(5007)・UNKNOWN(5001)・UNKNOWN(5001) | 17/375 | 4.5% | 47.1% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Nasus` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nasus.png)
