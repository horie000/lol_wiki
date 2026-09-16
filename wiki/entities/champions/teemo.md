---
title: "ティーモ"
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
  - role-marksman
  - role-mage
  - data-dragon
champion_id: "Teemo"
champion_key: "17"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Teemo.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Teemo.png"
---

# ティーモ

![[raw/assets/champions/Teemo.png|128]]

## 基本情報

- **英字ID：** `Teemo`
- **キー：** `17`
- **称号：** 俊足の斥候
- **データversion：** `16.18.1`

## 紹介

どのような恐ろしい危険や脅威が待っていようとも、ティーモは底知れぬ情熱と陽気さで世界を偵察し続ける。揺らぐことなき道徳観を持ったこのヨードルは、誇りを持ってひたむきに「バンドルの偵察兵の掟」を守っている。時には自らの行動が周囲に与える影響に気づかないこともあるが…。そもそも偵察兵の必要性自体を疑問視する声もある中、ひとつだけはっきりしていることがある──ティーモの強い信念を侮る者は、痛い目を見ることになる。

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 3 |
| `magic` | 7 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 615 |
| `hpperlevel` | 104 |
| `mp` | 334 |
| `mpperlevel` | 25 |
| `movespeed` | 330 |
| `armor` | 24 |
| `armorperlevel` | 4.5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 500 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 9.6 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 54 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.38 |
| `attackspeed` | 0.69 |

## アビリティ

- **パッシブ — やぶからヨードル：** 短時間行動せずにいると無限にインビジブル状態になる。茂みの中であれば移動中でもインビジブル状態になり、動き回っても解除されない。インビジブル状態が解除されると「奇襲モード」になり、攻撃速度が数秒間増加する。

- **Q — 目つぶしダーツ：** 強力な毒で敵1体の視力を低下させる。攻撃を受けた敵はダメージを受け、一定時間ブラインド状態になる。
- **W — 駆け足！：** 移動速度が増加。ただし、敵チャンピオンまたはタワーから攻撃を受けると効果が消滅する。数秒間、移動速度が増加。この間は、攻撃を受けても効果が持続する。
- **E — 毒たっぷり吹き矢：** 通常攻撃のたびに、対象を毒状態%i:OnHit%通常攻撃時効果にする。攻撃を受けた対象は命中時にダメージを受け、さらにその後4秒にわたって毎秒ダメージを受ける。
- **R — 毒キノコ：** バックパックに収納した「毒キノコ」を1つ取り出し、破裂性の毒トラップを仕掛ける。敵がトラップを踏むと毒霧が放出され、近くにいる敵ユニットをスロウ状態にし、継続ダメージを与える。毒キノコを他の毒キノコに投げつけると、バウンドしてさらに遠くに飛んでいく。

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
- **対象試合：** 304試合、全体勝率 48.7%
- **時間帯別勝率：** 〜20分 45.3%（n=53）、20〜25分 43.6%（n=39）、25〜30分 55.0%（n=60）、30〜35分 46.6%（n=73）、35分〜 50.6%（n=79）
- **最高帯：** 25〜30分（判定差 11.4ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-17|ティーモの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（326試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=32、78.1% / 非該当47.3%、差+30.8pt）；[[wiki/entities/items/item-4645|シャドウフレイム]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=55、65.5% / 非該当47.2%、差+18.2pt）
- **ステータス傾向：** マナ（該当n=163、55.8% / 非該当44.8%、差+11.0pt）；攻撃速度（該当n=277、51.3% / 非該当44.9%、差+6.4pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・攻撃速度・移動速度）；[[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-3124|グインソー レイジブレード]]（n=3（15未満）；共通stats: 魔力・攻撃力・攻撃速度／チャンピオン原典にも言及: 攻撃力・攻撃速度）

### JUNGLE（94試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・攻撃速度・移動速度）；[[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-3124|グインソー レイジブレード]]（n=1（15未満）；共通stats: 魔力・攻撃力・攻撃速度／チャンピオン原典にも言及: 攻撃力・攻撃速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-17|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=414）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率68.2%（30/44）、n=44（十分性の目安を満たす）。
  - [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率62.9%（22/35）、n=35（十分性の目安を満たす）。
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率59.5%（22/37）、n=37（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率31.2%（5/16）、サンプル不足（n=16、十分性の目安30未満）。
  - [[wiki/entities/champions/renekton|レネクトン（Renekton）]] — 対象側勝率37.5%（6/16）、サンプル不足（n=16、十分性の目安30未満）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率40.7%（11/27）、サンプル不足（n=27、十分性の目安30未満）。

### JUNGLE（対象n=125）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率66.7%（10/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/kaisa|カイ＝サ（Kaisa）]] — 対象側勝率66.7%（10/15）、サンプル不足（n=15、十分性の目安30未満）。
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

### TOP（対象266試合、全体勝率49.2%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：プレスアタック／凱旋・レジェンド: 迅速・背水の陣；副系不滅：ボーンアーマー・超成長；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 79/266 | 29.7% | 57.0% |
| 2 | 主系栄華：プレスアタック／凱旋・レジェンド: 迅速・最期の慈悲；副系魔道：強まる嵐・マナフローバンド；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 22/266 | 8.3% | 40.9% |
| 3 | 主系不滅：不死者の握撃／打ちこわし・ボーンアーマー・超成長；副系覇道：追い打ち・至極の賞金首狩り；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 14/266 | 5.3% | 42.9% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Teemo` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Teemo.png)
