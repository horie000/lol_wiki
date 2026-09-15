---
title: "ドレイヴン"
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
champion_id: "Draven"
champion_key: "119"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Draven.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Draven.png"
---

# ドレイヴン

![[raw/assets/champions/Draven.png|128]]

## 基本情報

- **英字ID：** `Draven`
- **キー：** `119`
- **称号：** 栄光ある処刑人
- **データversion：** `16.18.1`

## 紹介

ノクサスでは清算人として知られる戦士たちは闘技場で血を流して戦って力を競い合うが、その中でドレイヴンほどの人気を得た者はいない。元兵士である彼は、独特のドラマチックな演出と、回転する斧の類まれな手さばきで観客を魅了する。自らの厚かましいほどの完璧さに夢中になり、ドレイヴンは自身の名を呼ぶ歓声がいつまでも帝国に響くように、現れる敵すべてに勝利することを誓っている。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 3 |
| `magic` | 1 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 675 |
| `hpperlevel` | 104 |
| `mp` | 361 |
| `mpperlevel` | 39 |
| `movespeed` | 330 |
| `armor` | 29 |
| `armorperlevel` | 4.5 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 8.05 |
| `mpregenperlevel` | 0.65 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.7 |
| `attackspeed` | 0.679 |

## アビリティ

- **パッシブ — リーグ・オブ・ドレイヴン：** ドレイヴンが「回転斬斧」をキャッチするか、ミニオンおよび中立モンスター、タワーを破壊すると「名声」がたまる。敵チャンピオンを倒すとドレイヴンがスポットライトと喝采を浴び、「名声」の量に応じてゴールドを獲得する。

- **Q — 回転斬斧：** 次の通常攻撃に追加物理ダメージが付与される。対象に命中した斧は空中に跳ね返り、キャッチすると次の攻撃にも「回転斬斧」の効果がつく。 「回転斬斧」は2回までスタックする。
- **W — 血の疼き：** 移動速度と攻撃速度が増加する。増加移動速度は、時間の経過とともに急速に減少する。 「回転斬斧」をキャッチすると「血の疼き」のクールダウンがリセットされる。
- **E — 薙ぎ払い：** 斧を投げ、命中した敵に物理ダメージを与えて横に弾き飛ばし、スロウ効果を付与する。
- **R — 死の車輪：** 巨大な斧を2丁投げ、命中した全ユニットに物理ダメージを与える。敵チャンピオンに命中すると斧は自身のもとへ戻ってくる。斧が飛んでいる間に再度このスキルを発動すれば、途中で呼び戻すことも可能。ユニットに命中するごとに与えるダメージが減少するが、進行方向が変わると減少はリセットされる。敵の体力が「名声」のスタック数を下回る場合はとどめを刺す。

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

- **観測分類：** 判定保留（分母不足）
- **対象試合：** 76試合、全体勝率 60.5%
- **時間帯別勝率：** 〜20分 44.4%（n=9）、20〜25分 83.3%（n=12）、25〜30分 56.5%（n=23）、30〜35分 57.9%（n=19）、35分〜 61.5%（n=13）
- **最高帯：** 20〜25分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-119|ドレイヴンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（160試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3072|ブラッドサースター]] + [[wiki/entities/items/item-6676|コレクター]]（該当n=67、62.7% / 非該当49.5%、差+13.2pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-6676|コレクター]]（該当n=39、64.1% / 非該当52.1%、差+12.0pt）
- **ステータス傾向：** 攻撃速度（該当n=100、57.0% / 非該当51.7%、差+5.3pt）；移動速度（該当n=108、56.5% / 非該当51.9%、差+4.6pt）
- **理論仮説：** [[wiki/entities/items/item-2512|フィーンドハンターの矢]] + [[wiki/entities/items/item-3094|ラピッド ファイアキャノン]]（未観測；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・移動速度）；[[wiki/entities/items/item-3094|ラピッド ファイアキャノン]] + [[wiki/entities/items/item-3172|ガンメタル ブーツ]]（n=5（15未満）；共通stats: 攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃速度・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-119|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=270）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/blitzcrank|ブリッツクランク（Blitzcrank）]] — 対象側勝率65.9%（27/41）、n=41（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率67.7%（21/31）、n=31（十分性の目安を満たす）。

### MIDDLE（対象n=5）

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

### BOTTOM（対象232試合、全体勝率54.3%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：リーサルテンポ／冷静沈着・レジェンド: 迅速・切り崩し；副系天啓：キャッシュバック・トリプル トニック；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 48/232 | 20.7% | 54.2% |
| 2 | 主系栄華：プレスアタック／冷静沈着・レジェンド: 迅速・背水の陣；副系魔道：英気集中・強まる嵐；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 18/232 | 7.8% | 50.0% |
| 3 | 主系栄華：プレスアタック／冷静沈着・レジェンド: 迅速・背水の陣；副系天啓：キャッシュバック・トリプル トニック；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 11/232 | 4.7% | 36.4% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Draven` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Draven.png)
