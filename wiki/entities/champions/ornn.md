---
title: "オーン"
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
  - data-dragon
champion_id: "Ornn"
champion_key: "516"
data_version: "16.18.1"
roles:
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Ornn.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ornn.png"
---

# オーン

![[raw/assets/champions/Ornn.png|128]]

## 基本情報

- **英字ID：** `Ornn`
- **キー：** `516`
- **称号：** 山の下の焔
- **データversion：** `16.18.1`

## 紹介

オーンは鍛冶と技巧を司る、フレヨルドの半神半人だ。彼は“炉床の家”と呼ばれる、火山の地下にある溶岩の洞窟をハンマーで叩いて造った巨大な鍛冶場で独り仕事に打ち込んでいる。そこで大釜を火にかけ、鉱石を溶かして精製し、比類なき武具を鍛造しているのだ。他の半神半人たち──特にボリベア──が大地を歩き定命の者たちの営みに干渉を始める時、オーンは立ち上がる。彼の信頼するハンマーと山脈の炎の力を手に、そういった問題児どもを元いた場所に帰すために。

## 分類

- **役割タグ：** `Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 9 |
| `magic` | 3 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 660 |
| `hpperlevel` | 109 |
| `mp` | 341 |
| `mpperlevel` | 65 |
| `movespeed` | 335 |
| `armor` | 33 |
| `armorperlevel` | 5.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 69 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 歩く鍛冶場：** オーンが獲得するあらゆる追加物理防御と追加魔法防御は、獲得量が増加する。 オーンはどこにいても、ゴールドを消費して消費アイテム以外のアイテムを作り出せる。 さらに、自身と味方のために名匠アイテムを作り出せる。

- **Q — 溶岩隆起：** 地面を叩きつけて裂け目を発生させ、敵ユニットにダメージを与えて移動速度を低下させる。少ししてから、裂け目の終端に溶岩の柱が発生する。
- **W — ふいごの息：** 前進し、炎を吐き出す。炎の最後の塊が当たった敵は「脆弱」状態になる。
- **E — 灼熱の突撃：** ダッシュして当たった敵ユニットにダメージを与える。ダッシュ中に地形にぶつかると周囲に衝撃波が発生し、敵ユニットにダメージを与えてノックアップする。
- **R — 鍛冶神の呼び声：** 指定地点に巨大な精霊を呼び出す。精霊はどんどん速度を上げながらオーンがいる方向に進んでくる。精霊にぶつかった敵ユニットはダメージを受けて移動速度が低下し、「脆弱」状態になる。スキルを再使用するとオーンが精霊に向かって突撃し、彼がぶつかった方向に精霊の進行方向を変える。この精霊に当たった敵ユニットはノックアップされて、最初と同量のダメージを受け、再び「脆弱」が適用される。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 追加物理防御・追加魔法防御の獲得量が増え、名匠アイテムを作れる。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 168試合、全体勝率 47.6%
- **時間帯別勝率：** 〜20分 48.3%（n=29）、20〜25分 44.4%（n=27）、25〜30分 40.5%（n=37）、30〜35分 50.0%（n=46）、35分〜 55.2%（n=29）
- **最高帯：** 35分〜（判定差 14.6ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-516|オーンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（374試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3075|ソーンメイル]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（該当n=42、69.0% / 非該当47.3%、差+21.8pt）；[[wiki/entities/items/item-6664|ホロウ レディアンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（該当n=46、65.2% / 非該当47.6%、差+17.7pt）
- **ステータス傾向：** 魔法防御（該当n=290、54.5% / 非該当33.3%、差+21.1pt）；マナ（該当n=37、54.1% / 非該当49.3%、差+4.8pt）
- **理論仮説：** [[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（n=1（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・魔法防御）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・魔法防御）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-516|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=535）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率62.9%（22/35）、n=35（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率60.0%（21/35）、n=35（十分性の目安を満たす）。
  - [[wiki/entities/champions/yunara|ユナラ（Yunara）]] — 対象側勝率56.7%（17/30）、n=30（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/garen|ガレン（Garen）]] — 対象側勝率46.7%（14/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率48.9%（22/45）、n=45（十分性の目安を満たす）。

### JUNGLE（対象n=11）

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

### TOP（対象621試合、全体勝率47.7%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系不滅：不死者の握撃／打ちこわし・ボーンアーマー・超成長；副系天啓：ビスケットデリバリー・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 176/621 | 28.3% | 50.6% |
| 2 | 主系不滅：不死者の握撃／打ちこわし・心身調整・超成長；副系栄華：レジェンド: ヘイスト・凱旋；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 52/621 | 8.4% | 44.2% |
| 3 | 主系不滅：不死者の握撃／打ちこわし・ボーンアーマー・超成長；副系天啓：魔法の靴・ビスケットデリバリー；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 43/621 | 6.9% | 53.5% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Ornn` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ornn.png)
