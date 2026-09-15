---
title: "ミス・フォーチュン"
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
  - role-marksman
  - role-mage
  - data-dragon
champion_id: "MissFortune"
champion_key: "21"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/MissFortune.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/MissFortune.png"
---

# ミス・フォーチュン

![[raw/assets/champions/MissFortune.png|128]]

## 基本情報

- **英字ID：** `MissFortune`
- **キー：** `21`
- **称号：** 美貌の賞金稼ぎ
- **データversion：** `16.18.1`

## 紹介

美貌で名高く、容赦のなさで恐れられるビルジウォーターの船長サラ・フォーチュンは、面の皮の厚い港町の犯罪者たちの中でも一線を画して不屈である。子供の頃、略奪王のガングプランクに家族を殺されるのを目撃した彼女だが、数年後に彼を船ごと爆破して無慈悲な復讐を遂げた。彼女の力を侮る者は、魅力的で予測不能な彼女と対峙し…腹に銃弾を喰らうことになるだろう。

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 2 |
| `magic` | 5 |
| `difficulty` | 1 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 625 |
| `hpperlevel` | 100 |
| `mp` | 300 |
| `mpperlevel` | 40 |
| `movespeed` | 325 |
| `armor` | 25 |
| `armorperlevel` | 4 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.656 |

## アビリティ

- **パッシブ — ラブタップ：** 新しい対象に通常攻撃するたびに追加物理ダメージを与える。

- **Q — ダブルアップ：** 指定した敵に発砲しダメージを与える。対象の背後に敵がいた場合、跳弾して後ろの敵にもダメージを与える。弾丸はどちらも「ラブタップ」の効果が適用される。
- **W — ストラット：** 攻撃を受けずにいると、自動効果により移動速度が増加するようになる。発動すると、短時間攻撃速度が増加する。クールダウン中は、「ラブタップ」によってクールダウンが短縮される。
- **E — レイニングバレット：** 一定範囲内に弾丸の雨を降らせて視界を確保するとともに、範囲内の敵に継続ダメージを与えてスロウ効果を付与する。
- **R — バレットタイム：** 前方の扇状範囲に大量の銃弾を放ち、範囲内にいる敵に大量のダメージを与える。波状に発射される弾丸の各ウェーブ毎にクリティカル判定を持つ。

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
- **対象試合：** 1041試合、全体勝率 51.3%
- **時間帯別勝率：** 〜20分 54.4%（n=171）、20〜25分 53.5%（n=142）、25〜30分 53.2%（n=250）、30〜35分 50.6%（n=239）、35分〜 46.4%（n=239）
- **最高帯：** 〜20分（判定差 7.9ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-21|ミス・フォーチュンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（1,754試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3142|妖夢の霊剣]] + [[wiki/entities/items/item-3170|スイフトマーチ]]（該当n=48、77.1% / 非該当50.4%、差+26.7pt）；[[wiki/entities/items/item-3142|妖夢の霊剣]] + [[wiki/entities/items/item-3170|スイフトマーチ]] + [[wiki/entities/items/item-6676|コレクター]]（該当n=46、76.1% / 非該当50.5%、差+25.6pt）
- **ステータス傾向：** クリティカル率（該当n=1549、51.8% / 非該当45.9%、差+6.0pt）；ライフスティール（該当n=966、52.9% / 非該当49.0%、差+3.9pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・攻撃速度・移動速度）；[[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-3094|ラピッド ファイアキャノン]]（未観測；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・クリティカル率・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-21|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=2,121）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/galio|ガリオ（Galio）]] — 対象側勝率62.4%（53/85）、n=85（十分性の目安を満たす）。
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率61.4%（54/88）、n=88（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率55.9%（142/254）、n=254（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率44.2%（88/199）、n=199（十分性の目安を満たす）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率47.6%（89/187）、n=187（十分性の目安を満たす）。
  - [[wiki/entities/champions/ezreal|エズリアル（Ezreal）]] — 対象側勝率50.6%（89/176）、n=176（十分性の目安を満たす）。

### UTILITY（対象n=29）

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

### BOTTOM（対象2,401試合、全体勝率51.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系天啓：ファーストストライク／キャッシュバック・ビスケットデリバリー・なんでも屋；副系魔道：強まる嵐・マナフローバンド；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 446/2,401 | 18.6% | 50.2% |
| 2 | 主系栄華：プレスアタック／冷静沈着・レジェンド: 血脈・最期の慈悲；副系天啓：ビスケットデリバリー・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 313/2,401 | 13.0% | 49.5% |
| 3 | 主系天啓：ファーストストライク／キャッシュバック・ビスケットデリバリー・宇宙の英知；副系魔道：強まる嵐・マナフローバンド；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 268/2,401 | 11.2% | 48.9% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.MissFortune` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/MissFortune.png)
