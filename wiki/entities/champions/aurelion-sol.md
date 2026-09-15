---
title: "オレリオン・ソル"
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
  - role-mage
  - data-dragon
champion_id: "AurelionSol"
champion_key: "136"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/AurelionSol.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/AurelionSol.png"
---

# オレリオン・ソル

![[raw/assets/champions/AurelionSol.png|128]]

## 基本情報

- **英字ID：** `AurelionSol`
- **キー：** `136`
- **称号：** 星を創りし者
- **データversion：** `16.18.1`

## 紹介

かつて何もない巨大な虚空であった宇宙に己が生み出した煌めく驚異を散りばめ、その恩寵を授けたオレリオン・ソル。しかし彼は今、領土拡大を目論む帝国の罠にかけられ、命ぜられるがままにその凄まじい力を振りかざしている。星を創るという本来の神聖なる役目への回帰を願うオレリオン・ソルは、必要とあらば天空から星をも引き寄せる。自由を再びその手に取り戻すために。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 3 |
| `magic` | 8 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 90 |
| `mp` | 530 |
| `mpperlevel` | 40 |
| `movespeed` | 340 |
| `armor` | 22 |
| `armorperlevel` | 4 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 宇宙の創造者：** 攻撃スキルを敵に命中させると、「星屑」のスタックを獲得できる。このスタックは各スキルを恒久的に強化する。

- **Q — 星炎の息吹：** 数秒間詠唱して炎を吹き出し、最初に命中した敵にダメージを与え、その周囲の敵にはそれよりも少ないダメージを与える。敵に直接炎を吹きかけている間は、毎秒追加ダメージを与える。このダメージは獲得した「星屑」の数に応じて増加する。このスキルの対象がチャンピオンだった場合、「星屑」を獲得できる。
- **W — 天空への飛翔：** 飛翔して、指定方向に地形を超えて移動する。飛翔している間も、他のスキルを発動できる。また、飛翔中は「星炎の呼吸」のクールダウンおよび最大詠唱時間がなくなり、与えるダメージが増加する。 自身がダメージを与えた敵チャンピオンがその直後に倒されるたびに、このスキルの残りクールダウンが短縮される。 獲得した「星屑」の数に応じて、このスキルの最大射程が増加する。
- **E — 特異点：** ブラックホールを召喚して敵にダメージを与え、ゆっくりとその中心に向かって引き寄せる。敵がブラックホールの範囲内で倒されるたびに、「星屑」を獲得する。また、敵チャンピオンを範囲内に捕らえている間も、毎秒「星屑」を獲得できる。ブラックホールの中心部は、体力が最大体力の一定割合を下回っている敵に、とどめを刺すことができる。「星屑」の数に応じて「特異点」の効果範囲が増加し、とどめを刺せる体力割合の基準値が上昇する。
- **R — 星の邂逅/崩れ落つ天穹：** 星の邂逅: 地上に星を降らせ、その衝撃で敵に魔法ダメージを与えて、スタンさせる。また、命中した敵チャンピオン1体ごとに「星屑」を獲得する。「星屑」を一定数獲得すると、次に使用する「星の邂逅」が「崩れ落つ天穹」に変化する。 崩れ落つ天穹: 天空から巨大な星を引き寄せる。この星は落下時の効果範囲とダメージが増加しており、敵をスタンではなくノックアップさせる。また、落下時の効果範囲の端から衝撃波が広がり、命中した敵にダメージとスロウ効果を与える。獲得した「星屑」の数に応じて、「星の邂逅」と「崩れ落つ天穹」は落下時の効果範囲が増加する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 「星屑」のスタックが各スキルを恒久的に強化する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 195試合、全体勝率 55.9%
- **時間帯別勝率：** 〜20分 63.0%（n=27）、20〜25分 51.7%（n=29）、25〜30分 55.6%（n=36）、30〜35分 55.3%（n=47）、35分〜 55.4%（n=56）
- **最高帯：** 〜20分（判定差 11.2ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-136|オレリオン・ソルの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（279試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3157|ゾーニャの砂時計]] + [[wiki/entities/items/item-3175|連呪使いのブーツ]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=34、76.5% / 非該当51.0%、差+25.5pt）；[[wiki/entities/items/item-3157|ゾーニャの砂時計]] + [[wiki/entities/items/item-3175|連呪使いのブーツ]]（該当n=43、72.1% / 非該当50.8%、差+21.2pt）
- **ステータス傾向：** 物理防御（該当n=96、64.6% / 非該当48.6%、差+15.9pt）；魔法防御（該当n=39、59.0% / 非該当53.3%、差+5.6pt）
- **理論仮説：** [[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-8010|ブラッドレターの呪い]]（n=13（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（n=13（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

### BOTTOM（48試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-6653|ライアンドリーの仮面]] + [[wiki/entities/items/item-8010|ブラッドレターの呪い]]（n=11（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-8010|ブラッドレターの呪い]]（n=11（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-136|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=391）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率60.6%（20/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率60.0%（18/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率55.9%（19/34）、n=34（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/viktor|ビクター（Viktor）]] — 対象側勝率40.0%（6/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/akali|アカリ（Akali）]] — 対象側勝率46.7%（7/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率52.4%（11/21）、サンプル不足（n=21、十分性の目安30未満）。

### BOTTOM（対象n=72）

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

### MIDDLE（対象444試合、全体勝率48.2%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：秘儀の彗星／マナフローバンド・英気集中・追火；副系不滅：ボーンアーマー・超成長；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 84/444 | 18.9% | 44.0% |
| 2 | 主系魔道：死神の残り火／マナフローバンド・英気集中・追火；副系不滅：ボーンアーマー・超成長；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 74/444 | 16.7% | 55.4% |
| 3 | 主系魔道：死神の残り火／マナフローバンド・英気集中・追火；副系栄華：切り崩し・冷静沈着；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 49/444 | 11.0% | 44.9% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.AurelionSol` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/AurelionSol.png)
