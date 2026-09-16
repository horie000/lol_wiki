---
title: "アフェリオス"
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
  - data-dragon
champion_id: "Aphelios"
champion_key: "523"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Aphelios.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Aphelios.png"
---

# アフェリオス

![[raw/assets/champions/Aphelios.png|128]]

## 基本情報

- **英字ID：** `Aphelios`
- **キー：** `523`
- **称号：** 信ずる者の武器
- **データversion：** `16.18.1`

## 紹介

月明かりの陰から武器を構えて立ち現れるアフェリオスは、不気味なまでに音も無くルナリの敵の息の根を止める──その存在を示すのは、正確な狙いから放たれる銃声のみ。自らを突き動かす毒の力。アフェリオスは言葉を奪われながらも、その力によって妹のアルーンの導きを受ける。遠く離れた寺院の聖域から、彼女はムーンストーンの武器を兄の手に授けている。頭上に月が輝く限り、アフェリオスが孤独になることは決してない。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 2 |
| `magic` | 1 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 102 |
| `mp` | 348 |
| `mpperlevel` | 42 |
| `movespeed` | 325 |
| `armor` | 26 |
| `armorperlevel` | 4.2 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 3.25 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 6.5 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.1 |
| `attackspeed` | 0.665 |

## アビリティ

- **パッシブ — 殺す者と導く者：** アフェリオスは妹のアルーンが作った5種類のルナリ武器を使って戦う。一度に2種類の武器を保持でき、1つはメインハンド、もう1つはオフハンドに装備する。各武器にはそれぞれ独自の通常攻撃とスキルがある。通常攻撃とスキルは各武器の弾薬を消費する。弾薬が切れるとアフェリオスはその武器を捨て、5種類あるうちの次の武器をアルーンが召喚する。

- **Q — 武器ごとのスキル：** アフェリオスには、メインハンド武器に応じて変化する5種類の発動スキルがある: キャリブラム(ライフル): 長射程攻撃で対象をマークして再度長射程から攻撃する。 セヴェラム(鎌型ピストル): 素早く走りながら近くの敵を両方の武器で攻撃する。 グラヴィタム(キャノン): この武器のスロウ効果を受けているすべての敵にスネア効果を付与する。 インファーナム(火炎放射器): 扇状範囲内の敵に炎を浴びせ、対象をオフハンド武器で攻撃する。 クレッシェンダム(チャクラム): オフハンド武器を搭載したセントリーを設置する。
- **W — フェーズ：** メインハンド武器とオフハンド武器を切り替え、通常攻撃および発動スキルを変化させる。
- **E — 武器キューシステム：** アフェリオスには3つ目のスキルがない。このスロットにはアルーンから次に渡される武器が表示される。武器の登場順は固定だが、試合を進める過程で順番を入れ替えることはできる。弾が切れた武器は順番の最後に回される。
- **R — 月光の祈り：** 凝縮された月光のエネルギーを発射する。月光は敵チャンピオンに命中すると爆発する。メインハンド武器に応じて異なる効果を適用する。

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
- **観測分類：** 序盤寄り
- **対象試合：** 250試合、全体勝率 44.4%
- **時間帯別勝率：** 〜20分 56.4%（n=39）、20〜25分 32.1%（n=28）、25〜30分 47.5%（n=59）、30〜35分 43.1%（n=58）、35分〜 40.9%（n=66）
- **最高帯：** 〜20分（判定差 15.5ポイント）
- **判定根拠：** 〜20分が最高、長時間帯との差 15.5%。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-523|アフェリオスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（664試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-3031|インフィニティ エッジ]]（該当n=54、57.4% / 非該当43.6%、差+13.8pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3172|ガンメタル ブーツ]]（該当n=30、56.7% / 非該当44.2%、差+12.5pt）
- **ステータス傾向：** 物理防御（該当n=84、59.5% / 非該当42.6%、差+16.9pt）；ライフスティール（該当n=110、50.9% / 非該当43.5%、差+7.4pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力）；[[wiki/entities/items/item-3033|モータル リマインダー]] + [[wiki/entities/items/item-6673|イモータル シールドボウ]]（n=14（15未満）；共通stats: 攻撃力・クリティカル率／チャンピオン原典にも言及: 攻撃力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-523|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=983）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率69.4%（25/36）、n=36（十分性の目安を満たす）。
  - [[wiki/entities/champions/master-yi|マスター・イー（MasterYi）]] — 対象側勝率56.7%（17/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/lulu|ルル（Lulu）]] — 対象側勝率51.6%（47/91）、n=91（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率34.3%（24/70）、n=70（十分性の目安を満たす）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率36.2%（29/80）、n=80（十分性の目安を満たす）。
  - [[wiki/entities/champions/smolder|スモルダー（Smolder）]] — 対象側勝率36.7%（18/49）、n=49（十分性の目安を満たす）。

### MIDDLE（対象n=5）

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

### BOTTOM（対象593試合、全体勝率49.2%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：プレスアタック／凱旋・レジェンド: 血脈・切り崩し；副系天啓：キャッシュバック・トリプル トニック；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 120/593 | 20.2% | 46.7% |
| 2 | 主系栄華：プレスアタック／体力吸収・レジェンド: 血脈・切り崩し；副系魔道：英気集中・強まる嵐；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 33/593 | 5.6% | 48.5% |
| 3 | 主系栄華：プレスアタック／凱旋・レジェンド: 血脈・切り崩し；副系天啓：トリプル トニック・キャッシュバック；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 26/593 | 4.4% | 61.5% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Aphelios` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Aphelios.png)
