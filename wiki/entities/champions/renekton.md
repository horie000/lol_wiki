---
title: "レネクトン"
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
champion_id: "Renekton"
champion_key: "58"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "フューリー"
image_path: "raw/assets/champions/Renekton.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Renekton.png"
---

# レネクトン

![[raw/assets/champions/Renekton.png|128]]

## 基本情報

- **英字ID：** `Renekton`
- **キー：** `58`
- **称号：** 砂漠の解体屋
- **データversion：** `16.18.1`

## 紹介

威圧的な巨体に怒りをみなぎらせた超越者レネクトンは、灼熱のシュリーマに生まれ出でた。レネクトンはかつて、帝国随一と目されていた戦士であった。彼の率いる軍隊は、シュリーマを数限りない勝利に導いた。しかし、帝国は崩壊し、レネクトンは砂の下に幽閉される運命を辿る。時が流れ、世が変わりゆく間に、じわじわと彼は狂気に支配されていった。今や自由の身となったレネクトンは、兄ナサスを見つけ出し、葬り去ることに執念を燃やす。狂気の中、彼は数百年にも渡って自分を闇に封じ込めたのは、全てナサスの仕業だという妄想に憑りつかれ...

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** フューリー

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 2 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 660 |
| `hpperlevel` | 111 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 35 |
| `armorperlevel` | 5.2 |
| `spellblock` | 28 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 69 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.75 |
| `attackspeed` | 0.665 |

## アビリティ

- **パッシブ — 激情の支配：** 攻撃に「フューリー」を獲得する。自身の体力が低下していると「フューリー」の獲得量が増加する。「フューリー」を消費するとスキルに追加効果を付与できる。

- **Q — ミートカット：** 武器を振り回して周囲の敵に物理ダメージを与え、ダメージの数パーセントに相当する体力を回復する。「フューリー」が50以上たまっている場合は、ダメージと回復量が増える。
- **W — メッタ斬り：** 敵を2回斬りつけて物理ダメージを与え、0.75秒間スタン効果を付与する。「フューリー」が50以上たまっている場合は攻撃回数が3回に増え、対象のダメージシールドを消滅させてより多くのダメージを与える。また、スタン時間が1.5秒に延びる。
- **E — スライス・アンド・ダイス：** ダッシュ攻撃を繰り出し、進路上の敵にダメージを与える。強化時は与えるダメージが増え、2回目のダッシュ攻撃が命中した敵の物理防御を低下させる。
- **R — セベクの怒り：** 凶暴化して最大体力が増加し、周囲の敵にダメージを与える。凶暴化中は毎秒「フューリー」がたまっていく。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中7位（上位15%）。体力660、物理防御35、攻撃力69、移動速度345。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 320試合、全体勝率 49.1%
- **時間帯別勝率：** 〜20分 50.0%（n=56）、20〜25分 54.8%（n=42）、25〜30分 55.9%（n=68）、30〜35分 36.0%（n=75）、35分〜 51.9%（n=79）
- **最高帯：** 25〜30分（判定差 19.9ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-58|レネクトンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（613試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3174|装甲強化の進撃]]（該当n=34、70.6% / 非該当47.7%、差+22.9pt）；[[wiki/entities/items/item-3174|装甲強化の進撃]] + [[wiki/entities/items/item-6692|赤月の刃]]（該当n=40、65.0% / 非該当47.8%、差+17.2pt）
- **ステータス傾向：** 魔法防御（該当n=229、53.3% / 非該当46.4%、差+6.9pt）；物理防御（該当n=443、49.2% / 非該当48.2%、差+1.0pt）
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-58|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=833）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/lee-sin|リー・シン（LeeSin）]] — 対象側勝率66.7%（22/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率64.7%（22/34）、n=34（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率63.8%（37/58）、n=58（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/illaoi|イラオイ（Illaoi）]] — 対象側勝率35.1%（13/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/sett|セト（Sett）]] — 対象側勝率44.2%（19/43）、n=43（十分性の目安を満たす）。
  - [[wiki/entities/champions/ambessa|アンベッサ（Ambessa）]] — 対象側勝率44.8%（26/58）、n=58（十分性の目安を満たす）。

### MIDDLE（対象n=44）

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

### TOP（対象1,064試合、全体勝率49.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：征服者／凱旋・レジェンド: 迅速・背水の陣；副系不滅：ボーンアーマー・気迫；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 405/1,064 | 38.1% | 49.6% |
| 2 | 主系栄華：プレスアタック／凱旋・レジェンド: 迅速・背水の陣；副系不滅：ボーンアーマー・気迫；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 102/1,064 | 9.6% | 47.1% |
| 3 | 主系栄華：征服者／凱旋・レジェンド: 迅速・背水の陣；副系不滅：ボーンアーマー・気迫；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 52/1,064 | 4.9% | 48.1% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Renekton` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Renekton.png)
