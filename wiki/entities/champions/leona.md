---
title: "レオナ"
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
  - role-support
  - data-dragon
champion_id: "Leona"
champion_key: "89"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Leona.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Leona.png"
---

# レオナ

![[raw/assets/champions/Leona.png|128]]

## 基本情報

- **英字ID：** `Leona`
- **キー：** `89`
- **称号：** 暁光の戦士
- **データversion：** `16.18.1`

## 紹介

太陽の熱をもって闘志を燃やすレオナは、天陽の剣と暁の盾をもって霊峰ターゴンを守るソラリの騎士だ。彼女の肌は星の火のように煌めき、その瞳は内なる天の神髄の力で燃えている。黄金の鎧に身を包み、太古の真実という重責を背負う彼女は、ある者には啓示を、またある者には死をもたらす。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 8 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 646 |
| `hpperlevel` | 101 |
| `mp` | 302 |
| `mpperlevel` | 40 |
| `movespeed` | 335 |
| `armor` | 43 |
| `armorperlevel` | 4.8 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.85 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.9 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — サンライト：** 攻撃スキルが命中した敵に1.5秒間「サンライト」の効果を付与する。この状態の対象に味方チャンピオンがダメージを与えると「サンライト」を消費して追加魔法ダメージを与える。

- **Q — シールド・オブ・デイブレイク：** 次の通常攻撃時に盾を使って攻撃し、追加魔法ダメージを与えて対象にスタン効果を付与する。
- **W — エクリプス：** 自身の体を盾で保護し、ダメージ軽減率、物理防御、魔法防御を増加させる。効果時間終了時に近くに敵がいる場合は、その全員に魔法ダメージを与え、さらにシールドの効果時間が延長される。
- **E — ゼニスブレード：** 剣から太陽のエネルギーを放ち、直線上のすべての敵に魔法ダメージを与える。最後に命中した敵チャンピオンに一時的なスネア効果を付与し、レオナが近くまで素早く移動する。
- **R — ソーラーフレア：** 指定地点に太陽の力を呼び寄せ、効果範囲内の敵ユニットにダメージを与える。範囲の中心部にいる敵にスタン効果を与え、外側にいる敵にはスロウ効果を与える。

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

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 816試合、全体勝率 53.9%
- **時間帯別勝率：** 〜20分 58.8%（n=131）、20〜25分 48.0%（n=125）、25〜30分 54.8%（n=199）、30〜35分 53.2%（n=171）、35分〜 54.2%（n=190）
- **最高帯：** 〜20分（判定差 10.8ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-89|レオナの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（1,544試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3174|装甲強化の進撃]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（該当n=62、74.2% / 非該当52.4%、差+21.8pt）；[[wiki/entities/items/item-3109|騎士の誓い]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（該当n=380、63.2% / 非該当50.0%、差+13.2pt）
- **ステータス傾向：** マナ（該当n=35、71.4% / 非該当52.8%、差+18.6pt）；魔法防御（該当n=1398、53.7% / 非該当48.6%、差+5.1pt）
- **理論仮説：** [[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]]（n=6（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力・魔法防御）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=4（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力・魔法防御）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-89|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=1,936）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/kayn|ケイン（Kayn）]] — 対象側勝率62.7%（47/75）、n=75（十分性の目安を満たす）。
  - [[wiki/entities/champions/garen|ガレン（Garen）]] — 対象側勝率61.7%（58/94）、n=94（十分性の目安を満たす）。
  - [[wiki/entities/champions/kaisa|カイ＝サ（Kaisa）]] — 対象側勝率59.1%（91/154）、n=154（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/xerath|ゼラス（Xerath）]] — 対象側勝率34.8%（16/46）、n=46（十分性の目安を満たす）。
  - [[wiki/entities/champions/morgana|モルガナ（Morgana）]] — 対象側勝率38.2%（34/89）、n=89（十分性の目安を満たす）。
  - [[wiki/entities/champions/lux|ラックス（Lux）]] — 対象側勝率45.4%（44/97）、n=97（十分性の目安を満たす）。

### JUNGLE（対象n=1）

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

### UTILITY（対象2,524試合、全体勝率54.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系不滅：アフターショック／生命の泉・ボーンアーマー・気迫；副系天啓：ビスケットデリバリー・宇宙の英知；シャードUNKNOWN(5007)・UNKNOWN(5001)・UNKNOWN(5001) | 1,176/2,524 | 46.6% | 54.7% |
| 2 | 主系不滅：アフターショック／生命の泉・息継ぎ・超成長；副系栄華：レジェンド: ヘイスト・凱旋；シャードUNKNOWN(5007)・UNKNOWN(5001)・UNKNOWN(5001) | 347/2,524 | 13.7% | 51.9% |
| 3 | 主系不滅：アフターショック／生命の泉・ボーンアーマー・気迫；副系天啓：ビスケットデリバリー・宇宙の英知；シャードUNKNOWN(5007)・UNKNOWN(5001)・UNKNOWN(5011) | 81/2,524 | 3.2% | 48.1% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Leona` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Leona.png)
