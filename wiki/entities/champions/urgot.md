---
title: "アーゴット"
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
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "Urgot"
champion_key: "6"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Urgot.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Urgot.png"
---

# アーゴット

![[raw/assets/champions/Urgot.png|128]]

## 基本情報

- **英字ID：** `Urgot`
- **キー：** `6`
- **称号：** ドレッドノート
- **データversion：** `16.18.1`

## 紹介

かつてノクサスの処刑人として数多くの死体を積み上げたアーゴットは、自らが仕えた帝国に裏切られた。ゾウンの地下深くにある監獄鉱山・ドレッジに送られ、鉄の鎖に繋がれた彼は、そこで強さの本当の意味をその身に刻まれることになる。その後、街中に大混乱をもたらした災害に乗じて脱出した彼は、今や闇社会に強烈な影を落とす存在となった。かつて自らをも繋いでいた鎖に縛られる者たちを扇動しながら、自分の新たな“ホーム”から価値なき連中を間引き、苦痛の試練を与えているのだ。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 655 |
| `hpperlevel` | 102 |
| `mp` | 340 |
| `mpperlevel` | 45 |
| `movespeed` | 330 |
| `armor` | 36 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 350 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 7.25 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.75 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — エコーフレイム：** 通常攻撃時と「パージ」発動時にその方向にある脚から散発的に炎が放射され、物理ダメージを与える。

- **Q — コラプトシェル：** 指定地点に榴弾を発射する。周囲の敵に物理ダメージを与えて、移動速度を低下させる。
- **W — パージ：** 最も近くにいる敵に速射攻撃を行う。その間は移動速度が低下する。直前に他のスキルで攻撃した敵チャンピオンを優先して攻撃し、「エコーフレイム」を発動する。
- **E — ディスデイン：** 指定方向に突撃しながらシールドを展開し、チャンピオン以外の敵ユニットを横に弾き飛ばす。敵チャンピオンを捕まえるとその場で止まり、そのチャンピオンを後方に投げ飛ばす。
- **R — デスグラインダー：** ケミドリルを発射する。ドリルは最初に当たった敵チャンピオンに突き刺さる。その敵チャンピオンの体力が一定未満になると、アーゴットが弱者とみなして処刑する。

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

- **観測分類：** 中盤寄り
- **対象試合：** 172試合、全体勝率 52.9%
- **時間帯別勝率：** 〜20分 52.2%（n=23）、20〜25分 61.3%（n=31）、25〜30分 53.7%（n=41）、30〜35分 51.4%（n=35）、35分〜 47.6%（n=42）
- **最高帯：** 20〜25分（判定差 9.1ポイント）
- **判定根拠：** 中間帯が最高、端点との差 9.1%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-6|アーゴットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（352試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3053|ステラックの篭手]] + [[wiki/entities/items/item-3075|ソーンメイル]]（該当n=43、69.8% / 非該当53.4%、差+16.4pt）；[[wiki/entities/items/item-3053|ステラックの篭手]] + [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3075|ソーンメイル]]（該当n=43、69.8% / 非該当53.4%、差+16.4pt）
- **ステータス傾向：** 魔法防御（該当n=187、59.4% / 非該当50.9%、差+8.4pt）
- **理論仮説：** [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-6609|ケミパンク チェーンソード]]（n=11（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-2501|覇王のブラッドメイル]] + [[wiki/entities/items/item-3181|ハルブレイカー]]（n=7（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-6|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=457）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率65.7%（23/35）、n=35（十分性の目安を満たす）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率59.4%（19/32）、n=32（十分性の目安を満たす）。
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率55.9%（19/34）、n=34（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/garen|ガレン（Garen）]] — 対象側勝率38.9%（7/18）、サンプル不足（n=18、十分性の目安30未満）。
  - [[wiki/entities/champions/sion|サイオン（Sion）]] — 対象側勝率38.9%（7/18）、サンプル不足（n=18、十分性の目安30未満）。
  - [[wiki/entities/champions/yorick|ヨリック（Yorick）]] — 対象側勝率43.8%（7/16）、サンプル不足（n=16、十分性の目安30未満）。

### JUNGLE（対象n=14）

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

### TOP（対象329試合、全体勝率52.6%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：プレスアタック／凱旋・レジェンド: ヘイスト・背水の陣；副系不滅：ボーンアーマー・超成長；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 91/329 | 27.7% | 52.7% |
| 2 | 主系栄華：プレスアタック／凱旋・レジェンド: 血脈・背水の陣；副系天啓：疾駆・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 25/329 | 7.6% | 40.0% |
| 3 | 主系栄華：プレスアタック／体力吸収・レジェンド: 血脈・切り崩し；副系天啓：トリプル トニック・疾駆；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 10/329 | 3.0% | 70.0% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Urgot` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Urgot.png)
