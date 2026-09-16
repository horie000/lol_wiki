---
title: "レル"
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
  - role-tank
  - role-support
  - data-dragon
champion_id: "Rell"
champion_key: "526"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Rell.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rell.png"
---

# レル

![[raw/assets/champions/Rell.png|128]]

## 基本情報

- **英字ID：** `Rell`
- **キー：** `526`
- **称号：** 鋼鉄の乙女
- **データversion：** `16.18.1`

## 紹介

黒薔薇団による残酷な実験の産物であるレルは、ノクサスの打倒を胸に誓った、反逆の生きた兵器である。レルの幼少期は、惨めで恐ろしいものだった。魔力を完成させ、兵器化するために、彼女は口にするのも憚られるような処置に耐えてきた──暴力的な逃亡を成し遂げ、自分を捕らえようとした者たちの多くを殺めてしまうまでは。犯罪者の烙印を押されたレルは、ノクサス兵を目にした瞬間に攻撃する。かつてのアカデミーの生存者を探す彼女は、従順な者たちを守りながら、かつての教師たちには無慈悲な死を与えている。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 0 |
| `defense` | 0 |
| `magic` | 0 |
| `difficulty` | 0 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 104 |
| `mp` | 320 |
| `mpperlevel` | 40 |
| `movespeed` | 315 |
| `armor` | 30 |
| `armorperlevel` | 4 |
| `spellblock` | 28 |
| `spellblockperlevel` | 1.8 |
| `attackrange` | 175 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.85 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.625 |

## データ品質上の注意

- `info` の4項目がすべて `0` である。未収録値か実値かは原典だけでは判定できない。

## アビリティ

- **パッシブ — 革新の鬨：** 通常攻撃またはスキルを命中させると追加で魔法ダメージを与え、対象から物理防御と魔法防御を奪う。

- **Q — 破鋼撃：** 直線上のユニットに魔法ダメージを与え、対象のシールドを破壊してスタンさせる。
- **W — フェロマンシー: 装着：** 騎馬形態: 「騎馬解除」をして、鎧をまとって突撃し、敵をノックアップさせて大量のシールドを獲得する。騎馬解除中は物理防御、魔法防御、攻撃速度、射程距離が増加するが、移動速度が低下する。 騎馬解除中: 鋼鉄の馬を形成して「騎馬形態」となり、瞬間的に移動速度が増加して、次に通常攻撃を行った敵をノックアップさせる。
- **E — 重槍突貫：** 自動効果: 非戦闘時の移動速度が増加する。 発動効果: 自身と味方1体の移動速度が徐々に増加する。敵またはお互いの方向に移動する場合、この増加量は2倍になる。次の通常攻撃で爆発を引き起こし、魔法ダメージを与える。
- **R — 磁気嵐流：** 猛烈な磁場を発生させ、周囲の敵を自身の方向に引き寄せる。その後も少しの間、継続的に周囲の敵を自身の方向に引き付け、効果時間をかけて魔法ダメージを与える。

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
- **対象試合：** 309試合、全体勝率 45.0%
- **時間帯別勝率：** 〜20分 44.1%（n=34）、20〜25分 48.9%（n=45）、25〜30分 43.0%（n=79）、30〜35分 39.2%（n=74）、35分〜 50.6%（n=77）
- **最高帯：** 35分〜（判定差 11.5ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-526|レルの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（648試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3109|騎士の誓い]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（該当n=60、68.3% / 非該当48.3%、差+20.0pt）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3109|騎士の誓い]]（該当n=87、65.5% / 非該当47.8%、差+17.7pt）
- **ステータス傾向：** 魔法防御（該当n=618、51.1% / 非該当30.0%、差+21.1pt）；魔力（該当n=45、55.6% / 非該当49.8%、差+5.8pt）
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（n=1（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力・魔法防御）；[[wiki/entities/items/item-3190|ソラリのロケット]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力・魔法防御）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-526|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=797）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率66.7%（32/48）、n=48（十分性の目安を満たす）。
  - [[wiki/entities/champions/viktor|ビクター（Viktor）]] — 対象側勝率64.5%（20/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率57.9%（33/57）、n=57（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率35.6%（16/45）、n=45（十分性の目安を満たす）。
  - [[wiki/entities/champions/thresh|スレッシュ（Thresh）]] — 対象側勝率39.6%（21/53）、n=53（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率46.2%（37/80）、n=80（十分性の目安を満たす）。

### JUNGLE（対象n=3）

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

### UTILITY（対象566試合、全体勝率53.9%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系不滅：アフターショック／シールドバッシュ・ボーンアーマー・気迫；副系天啓：宇宙の英知・ヘクステックフラッシュネイター；シャードUNKNOWN(5007)・UNKNOWN(5001)・UNKNOWN(5001) | 185/566 | 32.7% | 50.8% |
| 2 | 主系不滅：アフターショック／シールドバッシュ・ボーンアーマー・気迫；副系栄華：レジェンド: ヘイスト・凱旋；シャードUNKNOWN(5007)・UNKNOWN(5001)・UNKNOWN(5001) | 63/566 | 11.1% | 57.1% |
| 3 | 主系不滅：アフターショック／シールドバッシュ・ボーンアーマー・気迫；副系天啓：ヘクステックフラッシュネイター・宇宙の英知；シャードUNKNOWN(5007)・UNKNOWN(5001)・UNKNOWN(5001) | 41/566 | 7.2% | 61.0% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Rell` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rell.png)
