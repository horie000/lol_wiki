---
title: "ランブル"
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
  - role-mage
  - data-dragon
champion_id: "Rumble"
champion_key: "68"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Mage"
resource_type: "ヒート"
image_path: "raw/assets/champions/Rumble.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rumble.png"
---

# ランブル

![[raw/assets/champions/Rumble.png|128]]

## 基本情報

- **英字ID：** `Rumble`
- **キー：** `68`
- **称号：** 戦慄の機甲兵
- **データversion：** `16.18.1`

## 紹介

ランブルは若くて気性の荒い発明家だ。この気骨のあるヨードルは、ガラクタの山を使って、たった一人の力で電撃ハープーンと焼夷ロケット弾を搭載した巨大なメカスーツを作り出した。廃品置き場で作り出された彼の発明品を冷笑する者がいても、ランブルは気にしない──いざとなれば、火炎放射器で黙らせてやればいいだけだ。

## 分類

- **役割タグ：** `Fighter`、`Mage`
- **リソース種別：** ヒート

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 6 |
| `magic` | 8 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 105 |
| `mp` | 150 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 36 |
| `armorperlevel` | 4.7 |
| `spellblock` | 28 |
| `spellblockperlevel` | 1.55 |
| `attackrange` | 125 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.85 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — ポンコツタイタン：** スキルを使用するたび、ヒートが溜まっていく。ヒートゲージが50%に達すると「デンジャーゾーン」に突入し、すべての通常スキルに追加効果が付与される。100%に達すると「オーバーヒート」し、攻撃速度が増加して通常攻撃に追加ダメージがつくが、数秒間スキルを使えなくなる。

- **Q — スピットファイア：** 扇状の範囲を3秒間にわたって焼き払い魔法ダメージを与える。「デンジャーゾーン」突入時はダメージが増加する。
- **W — ジャンクシールド：** シールドを発生させてダメージを防ぎ、さらに移動速度が一瞬増加する。「デンジャーゾーン」突入時はシールド耐久値と、増加移動速度が増加する。
- **E — エレクトロハープーン：** 銛を発射し、対象を感電させて魔法ダメージとスロウ効果を与え、魔法防御を低下させる。2発まで発射できる。「デンジャーゾーン」突入時はダメージとスロウ効果が増加する。
- **R — イコライザー：** 複数のロケット弾を投下し、その地点を炎上させて敵にダメージとスロウ効果を与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中18位（上位15%）。体力640、物理防御36、攻撃力64、移動速度345。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 中盤寄り
- **対象試合：** 133試合、全体勝率 58.6%
- **時間帯別勝率：** 〜20分 56.0%（n=25）、20〜25分 52.9%（n=17）、25〜30分 66.7%（n=30）、30〜35分 60.0%（n=20）、35分〜 56.1%（n=41）
- **最高帯：** 25〜30分（判定差 10.6ポイント）
- **判定根拠：** 中間帯が最高、端点との差 10.6%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-68|ランブルの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（319試合）

- **実測ビルド候補：** [[wiki/entities/items/item-4645|シャドウフレイム]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=52、59.6% / 非該当44.9%、差+14.7pt）；[[wiki/entities/items/item-3157|ゾーニャの砂時計]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=31、58.1% / 非該当46.2%、差+11.9pt）
- **ステータス傾向：** 物理防御（該当n=177、50.8% / 非該当43.0%、差+7.9pt）
- **理論仮説：** [[wiki/entities/items/item-3065|スピリット ビサージュ]] + [[wiki/entities/items/item-8020|アビサル マスク]]（未観測；共通stats: 体力・魔法防御／チャンピオン原典にも言及: 体力・魔法防御）；[[wiki/entities/items/item-2502|終わりなき絶望]] + [[wiki/entities/items/item-3143|ランデュイン オーメン]]（未観測；共通stats: 物理防御・体力／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-68|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=421）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率63.2%（24/38）、n=38（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率58.3%（21/36）、n=36（十分性の目安を満たす）。
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率54.3%（19/35）、n=35（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率36.0%（9/25）、サンプル不足（n=25、十分性の目安30未満）。
  - [[wiki/entities/champions/illaoi|イラオイ（Illaoi）]] — 対象側勝率37.5%（6/16）、サンプル不足（n=16、十分性の目安30未満）。
  - [[wiki/entities/champions/renekton|レネクトン（Renekton）]] — 対象側勝率38.9%（7/18）、サンプル不足（n=18、十分性の目安30未満）。

### MIDDLE（対象n=19）

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

### TOP（対象561試合、全体勝率48.7%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：秘儀の彗星／ニンバスクローク・英気集中・追火；副系不滅：ボーンアーマー・気迫；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 102/561 | 18.2% | 55.9% |
| 2 | 主系魔道：死神の残り火／ニンバスクローク・英気集中・追火；副系不滅：ボーンアーマー・気迫；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 85/561 | 15.2% | 54.1% |
| 3 | 主系魔道：秘儀の彗星／ニンバスクローク・英気集中・追火；副系覇道：血の味わい・至極の賞金首狩り；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 25/561 | 4.5% | 52.0% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Rumble` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rumble.png)
