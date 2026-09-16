---
title: "イラオイ"
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
champion_id: "Illaoi"
champion_key: "420"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Illaoi.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Illaoi.png"
---

# イラオイ

![[raw/assets/champions/Illaoi.png|128]]

## 基本情報

- **英字ID：** `Illaoi`
- **キー：** `420`
- **称号：** 海の女司祭
- **データversion：** `16.18.1`

## 紹介

イラオイは頑強な巨体の持ち主だが、その不屈の信仰心はそれ以上に大きい。「大いなるクラーケン」の預言者である彼女は、巨大な黄金の偶像を使って敵の魂を肉体から引き剥がし、現実の知覚を打ち砕く。「ナーガケイボロスの真実の担い手」に挑むものは、すぐさまイラオイは一人で戦っているのではないということを思い知るだろう。そう──サーペントアイルの名状しがたい神が彼女とともにあり、戦うのだということを。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 6 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 656 |
| `hpperlevel` | 115 |
| `mp` | 350 |
| `mpperlevel` | 50 |
| `movespeed` | 350 |
| `armor` | 35 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9.5 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 旧神の預言者：** イラオイと、イラオイに「器」にされた者は、周囲の地形に一定時間ごとに触手を発生させる。触手は魂、「器」、イラオイの「過酷なる教訓」をくらった者を攻撃する。触手は命中すると敵に物理ダメージを与え、敵チャンピオンにダメージを与えた場合はイラオイを回復する。

- **Q — 触手の鉄槌：** 触手の与ダメージが増加する。発動すると、触手を叩きつけて物理ダメージを与える。
- **W — 過酷なる教訓：** 次の通常攻撃で対象に飛びかかって偶像で殴りつけ、物理ダメージを与える。周囲の触手にも対象を攻撃させる。
- **E — 魂の試練：** 偶像から触手を伸ばし、敵の肉体から魂を引きずり出して、自身の前に立たせる。魂は受けたダメージから一定の割合を、本体に反映させる。魂がキルされるか本体が遠く離れた場合、対象は「器」となり、その周囲に触手が発生するようになる。
- **R — 信仰震：** 偶像を地面に叩きつけて衝撃波を生み出し、周囲の敵に物理ダメージを与える。命中した敵チャンピオン1体ごとに、触手が1本発生する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中9位（上位15%）。体力656、物理防御35、攻撃力65、移動速度350。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 明瞭な傾向なし
- **対象試合：** 324試合、全体勝率 53.7%
- **時間帯別勝率：** 〜20分 59.3%（n=54）、20〜25分 50.0%（n=46）、25〜30分 66.2%（n=74）、30〜35分 44.7%（n=76）、35分〜 48.6%（n=74）
- **最高帯：** 25〜30分（判定差 21.5ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-420|イラオイの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（563試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3053|ステラックの篭手]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（該当n=38、63.2% / 非該当50.9%、差+12.3pt）；[[wiki/entities/items/item-3053|ステラックの篭手]] + [[wiki/entities/items/item-6662|アイスボーン ガントレット]]（該当n=119、61.3% / 非該当49.1%、差+12.2pt）
- **ステータス傾向：** 攻撃力（該当n=529、52.7% / 非該当35.3%、差+17.4pt）；物理防御（該当n=477、52.6% / 非該当46.5%、差+6.1pt）
- **理論仮説：** [[wiki/entities/items/item-3002|先人の道標]] + [[wiki/entities/items/item-3742|デッド マン プレート]]（未観測；共通stats: 物理防御・体力・移動速度／チャンピオン原典にも言及: 物理防御・体力・移動速度）；[[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-420|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=706）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/kaisa|カイ＝サ（Kaisa）]] — 対象側勝率59.6%（34/57）、n=57（十分性の目安を満たす）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率59.6%（28/47）、n=47（十分性の目安を満たす）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率58.7%（27/46）、n=46（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/garen|ガレン（Garen）]] — 対象側勝率29.4%（10/34）、n=34（十分性の目安を満たす）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率34.5%（20/58）、n=58（十分性の目安を満たす）。
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率44.4%（16/36）、n=36（十分性の目安を満たす）。

### MIDDLE（対象n=36）

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

### TOP（対象382試合、全体勝率49.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系不滅：不死者の握撃／打ちこわし・ボーンアーマー・超成長；副系栄華：背水の陣・冷静沈着；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 142/382 | 37.2% | 50.7% |
| 2 | 主系不滅：不死者の握撃／打ちこわし・ボーンアーマー・超成長；副系栄華：冷静沈着・背水の陣；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 51/382 | 13.4% | 52.9% |
| 3 | 主系栄華：征服者／冷静沈着・レジェンド: ヘイスト・背水の陣；副系不滅：ボーンアーマー・打ちこわし；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 41/382 | 10.7% | 56.1% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Illaoi` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Illaoi.png)
