---
title: "ザヤ"
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
  - "[[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis]]"
tags:
  - champion
  - role-marksman
  - data-dragon
champion_id: "Xayah"
champion_key: "498"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Xayah.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Xayah.png"
---

# ザヤ

![[raw/assets/champions/Xayah.png|128]]

## 基本情報

- **英字ID：** `Xayah`
- **キー：** `498`
- **称号：** 反逆の刃
- **データversion：** `16.18.1`

## 紹介

危険で正確。ザヤは同胞を救うために戦い続けるヴァスタヤの革命の闘士だ。彼女の武器はスピードと抜け目なさ、そして立ちはだかる全てを切り裂く、カミソリのように鋭い羽根の刃である。自らの衰えゆく部族を守り、その種族に彼女が理想とするかつての栄光を取り戻すため、ザヤは愛するパートナーのラカンと肩を並べて戦うのだ。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 10 |
| `defense` | 6 |
| `magic` | 1 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 107 |
| `mp` | 340 |
| `mpperlevel` | 40 |
| `movespeed` | 330 |
| `armor` | 25 |
| `armorperlevel` | 4.2 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 525 |
| `hpregen` | 3.25 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 8.25 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.9 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — クリーンカット：** スキル使用後、次に行う数回の通常攻撃が軌道上のすべての敵にダメージを与え、「羽根」を落とすようになる。

- **Q — ダブルダガー：** 2枚の羽根の刃を投げてダメージを与え、呼び戻すことができる「羽根」を落とす。
- **W — デッドリープルーム：** 羽根の刃の嵐を作り出し、攻撃速度とダメージを増加させる。敵チャンピオンを攻撃した場合は移動速度も増加する。
- **E — ブレードコーラー：** 落とした「羽根」をすべて呼び戻し、敵ユニットにダメージとスネア効果を与える。
- **R — フェザーストーム：** 空中に飛んでしばらく対象指定されなくなり、複数の羽根の刃を投げ、呼び戻すことができる「羽根」を落とす。

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
- **観測分類：** 終盤寄り
- **対象試合：** 147試合、全体勝率 50.3%
- **時間帯別勝率：** 〜20分 35.3%（n=17）、20〜25分 52.9%（n=17）、25〜30分 48.6%（n=37）、30〜35分 45.7%（n=46）、35分〜 66.7%（n=30）
- **最高帯：** 35分〜（判定差 31.4ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 31.4%。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-498|ザヤの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（327試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3172|ガンメタル ブーツ]] + [[wiki/entities/items/item-6675|ナヴォリ フリッカーブレード]]（該当n=32、90.6% / 非該当45.4%、差+45.2pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3036|ドミニク リガード]]（該当n=60、66.7% / 非該当46.1%、差+20.6pt）
- **ステータス傾向：** ライフスティール（該当n=68、69.1% / 非該当44.8%、差+24.3pt）；物理防御（該当n=43、58.1% / 非該当48.6%、差+9.5pt）
- **理論仮説：** [[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-6675|ナヴォリ フリッカーブレード]]（n=3（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・移動速度）；[[wiki/entities/items/item-3094|ラピッド ファイアキャノン]] + [[wiki/entities/items/item-6675|ナヴォリ フリッカーブレード]]（n=1（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-498|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=439）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率50.0%（17/34）、n=34（十分性の目安を満たす）。
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率47.5%（19/40）、n=40（十分性の目安を満たす）。
  - [[wiki/entities/champions/rakan|ラカン（Rakan）]] — 対象側勝率45.6%（47/103）、n=103（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/kaisa|カイ＝サ（Kaisa）]] — 対象側勝率45.5%（20/44）、n=44（十分性の目安を満たす）。
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率48.5%（16/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率51.5%（17/33）、n=33（十分性の目安を満たす）。

### TOP（対象n=2）

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

### BOTTOM（対象247試合、全体勝率48.6%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：リーサルテンポ／冷静沈着・レジェンド: 血脈・最期の慈悲；副系天啓：ビスケットデリバリー・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 60/247 | 24.3% | 45.0% |
| 2 | 主系栄華：リーサルテンポ／冷静沈着・レジェンド: 血脈・最期の慈悲；副系天啓：魔法の靴・ビスケットデリバリー；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 24/247 | 9.7% | 37.5% |
| 3 | 主系栄華：リーサルテンポ／冷静沈着・レジェンド: 血脈・最期の慈悲；副系天啓：ビスケットデリバリー・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 9/247 | 3.6% | 11.1% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

<!-- champion-tier-analysis:start -->
## 観測ランク帯別チャンピオン候補

- **スナップショット：** 2026-09-16生成、キュー420、観測10帯、各1,000試合、統合後9,761試合、min-games 15、[[reports/riot-ranked-tier-analysis/run-20260916T083219Z/report|ランク帯別詳細レポート]]。
- **根拠：** [[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis|Riotランク戦試合データ：観測ランク帯別特徴]]、[[wiki/syntheses/ranked-tier-characteristics|ランク帯別の試合特徴と全帯共通傾向]]。
- **読み方：** `observed_tier` はその試合を発見したプレイヤーの収集時点の所属帯であり、10人全員の試合時ランクではない。以下は各帯の上位選択と、min-games以上で機械的に抽出した高低勝率の探索候補で、推奨・因果効果・有意差を示さない。

### 低勝率候補（下位5）

| 観測帯 | 候補順位 | 試合数 | 勝敗 | 勝率 |
| --- | ---: | ---: | --- | ---: |
| SILVER | 4 | 30 | 10勝/20敗 | 33.3% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Xayah` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Xayah.png)
