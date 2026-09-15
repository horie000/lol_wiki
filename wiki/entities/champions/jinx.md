---
title: "ジンクス"
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
  - data-dragon
champion_id: "Jinx"
champion_key: "222"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Jinx.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jinx.png"
---

# ジンクス

![[raw/assets/champions/Jinx.png|128]]

## 基本情報

- **英字ID：** `Jinx`
- **キー：** `222`
- **称号：** 暴走パンクガール
- **データversion：** `16.18.1`

## 紹介

ジンクスは地下都市出身の、常軌を逸し、衝動的な犯罪者の一人だ。彼女は自らの過去が生んだ帰結に苛まれながらも、ピルトーヴァーとゾウンに独自のやり方で破壊と混沌をもたらし続けている。自作した強力な武器を使って派手な爆発を引き起こし、銃弾の雨を降らせ、行く先々で大混乱を生み出す彼女は、持たざる者たちを感化し、抵抗と反乱へといざなう存在でもあるのだ。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 2 |
| `magic` | 4 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 105 |
| `mp` | 260 |
| `mpperlevel` | 50 |
| `movespeed` | 325 |
| `armor` | 26 |
| `armorperlevel` | 4.2 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 525 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 6.7 |
| `mpregenperlevel` | 1 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 超エキサイティン！：** 敵チャンピオン、エピックジャングルモンスター、建造物のキルまたは破壊に貢献すると、移動速度と攻撃速度が大幅に増加する。

- **Q — スイッチング！：** スキルを使用するたび、通常攻撃が「パウパウガン」(ミニガン)と「フィッシュボーン」(ロケットランチャー)の間で切り替わる。「パウパウガン」で敵を攻撃し続けると攻撃速度が増加する。「フィッシュボーン」は射程が長く、範囲ダメージを発生させることができるが、攻撃速度が低下してマナを消費するようになる。
- **W — シビレーザー！：** スタンガンの一種であるシビレーザーを発射する。最初に命中した敵にダメージとスロウ効果を与え、さらに可視状態にする。
- **E — パックンチョッパー！：** 一列にならんだ爆雷を3個投げる。敵チャンピオンが爆雷に触れるとトラップが起動してスネア効果を与える。爆雷は触れられなくても5秒後に自動的に爆発し、周囲にいる敵にダメージを与える。
- **R — スーパーメガデスロケット！：** 指定方向にどこまでも直進してゆくスーパーメガデスロケットを発射する。 発射したロケット弾が敵チャンピオンに命中すればその場で爆発し、周囲の敵にもダメージを与える。ダメージは敵の現在体力が少ないほど威力が増加する。

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

- **観測分類：** 中盤寄り
- **対象試合：** 764試合、全体勝率 50.5%
- **時間帯別勝率：** 〜20分 40.3%（n=144）、20〜25分 50.0%（n=104）、25〜30分 52.2%（n=186）、30〜35分 61.4%（n=176）、35分〜 46.1%（n=154）
- **最高帯：** 30〜35分（判定差 15.3ポイント）
- **判定根拠：** 中間帯が最高、端点との差 15.3%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-222|ジンクスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（1,537試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3036|ドミニク リガード]] + [[wiki/entities/items/item-3172|ガンメタル ブーツ]]（該当n=31、87.1% / 非該当50.1%、差+37.0pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3032|ユン・タル ワイルドアロー]] + [[wiki/entities/items/item-3172|ガンメタル ブーツ]]（該当n=68、85.3% / 非該当49.2%、差+36.1pt）
- **ステータス傾向：** ライフスティール（該当n=253、70.8% / 非該当46.9%、差+23.9pt）；クリティカル率（該当n=1354、53.6% / 非該当30.1%、差+23.6pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・攻撃速度・移動速度）；[[wiki/entities/items/item-3085|ルナーン ハリケーン]] + [[wiki/entities/items/item-3094|ラピッド ファイアキャノン]]（n=7（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-222|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=1,908）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/zyra|ザイラ（Zyra）]] — 対象側勝率69.2%（27/39）、n=39（十分性の目安を満たす）。
  - [[wiki/entities/champions/veigar|ベイガー（Veigar）]] — 対象側勝率66.7%（46/69）、n=69（十分性の目安を満たす）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率60.7%（88/145）、n=145（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/twitch|トゥイッチ（Twitch）]] — 対象側勝率41.2%（14/34）、n=34（十分性の目安を満たす）。
  - [[wiki/entities/champions/varus|ヴァルス（Varus）]] — 対象側勝率44.6%（25/56）、n=56（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率46.5%（87/187）、n=187（十分性の目安を満たす）。

### MIDDLE（対象n=2）

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

### BOTTOM（対象2,276試合、全体勝率51.1%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：リーサルテンポ／冷静沈着・レジェンド: 血脈・最期の慈悲；副系魔道：英気集中・強まる嵐；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 769/2,276 | 33.8% | 50.6% |
| 2 | 主系栄華：リーサルテンポ／冷静沈着・レジェンド: 血脈・切り崩し；副系天啓：キャッシュバック・トリプル トニック；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 541/2,276 | 23.8% | 52.7% |
| 3 | 主系栄華：リーサルテンポ／冷静沈着・レジェンド: 血脈・最期の慈悲；副系魔道：英気集中・強まる嵐；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 90/2,276 | 4.0% | 58.9% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Jinx` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jinx.png)
