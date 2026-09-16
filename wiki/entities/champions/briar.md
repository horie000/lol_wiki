---
title: "ブライアー"
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
  - role-assassin
  - data-dragon
champion_id: "Briar"
champion_key: "233"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "フューリー"
image_path: "raw/assets/champions/Briar.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Briar.png"
---

# ブライアー

![[raw/assets/champions/Briar.png|128]]

## 基本情報

- **英字ID：** `Briar`
- **キー：** `233`
- **称号：** 枷と飢え
- **データversion：** `16.18.1`

## 紹介

黒薔薇団の実験の失敗により、制御不能な血の渇きとともに生まれ落ちたブライアーは、特殊な拘束具がなければ狂乱の精神を抑えられない。彼女は数年間の幽閉の末に自由を手に入れ、世に解き放たれた。今は誰にも管理されることなく、ただ知識と血への渇望に突き動かされ、自らを解き放つ機会を楽しんでいる。狂乱の精神を制御するのは容易ではないにしても。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** フューリー

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 625 |
| `hpperlevel` | 95 |
| `mp` | 0 |
| `mpperlevel` | 0 |
| `movespeed` | 340 |
| `armor` | 30 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 0 |
| `hpregenperlevel` | 0 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — 真紅の呪い：** 通常攻撃とスキルが出血のスタックを付与し、与えたダメージの一定割合にあたる体力を回復する。絶えず飢えているブライアーは、減少体力に応じて回復量が増加するが、体力自動回復は備わっていない。

- **Q — ヘッドラッシュ：** ユニットのもとに跳躍して、強烈なかかと落としで敵を攻撃し、対象をスタンさせて物理防御を低下させる。
- **W — 血の狂乱/衝動噛み：** 前方に跳躍して首枷を破壊し、「血の狂乱」状態になる。効果時間中は最も近くの敵(チャンピオンを優先)を執拗に追いかけて通常攻撃する。狂乱状態では攻撃速度と移動速度が増加し、通常攻撃が対象を中心に範囲ダメージを与えるようになる。 狂乱中にこのスキルを再発動すると、次の通常攻撃で対象に噛みつき、対象の減少体力に応じて追加ダメージを与える。さらに、与えたダメージに応じて自身の体力を回復する。
- **E — 呪福の叫び：** 精神を集中して「血の狂乱」状態を解除し、エネルギーを溜めて凄まじい叫び声を上げ、敵にダメージとスロウ効果を与える。チャージ中はダメージ軽減効果を獲得し、最大体力の一定割合にあたる体力を回復する。最大までチャージすると、叫び声が敵をノックバックさせる。対象が壁に当たった場合、追加ダメージを与えてスタンさせる。
- **R — 迫りくる死：** 首枷に付けられた魔石ヘモリスを蹴り飛ばし、最初に命中したチャンピオンを獲物としてマークする。その後、獲物まで一直線に飛んでいき、到着時に周囲の他の敵にフィアー効果を与え、完全な渇血状態になる。この間は「血の狂乱」の効果を得て、物理防御、魔法防御、ライフスティール、移動速度が増加し、デスするまで獲物を追いかけ通常攻撃する。

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
- **対象試合：** 507試合、全体勝率 52.7%
- **時間帯別勝率：** 〜20分 55.8%（n=77）、20〜25分 48.6%（n=70）、25〜30分 51.3%（n=113）、30〜35分 58.0%（n=119）、35分〜 49.2%（n=128）
- **最高帯：** 30〜35分（判定差 9.4ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-233|ブライアーの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（800試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-3036|ドミニク リガード]]（該当n=33、81.8% / 非該当51.0%、差+30.8pt）；[[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-3036|ドミニク リガード]] + [[wiki/entities/items/item-6676|コレクター]]（該当n=33、81.8% / 非該当51.0%、差+30.8pt）
- **ステータス傾向：** 移動速度（該当n=746、53.1% / 非該当40.7%、差+12.3pt）；体力（該当n=595、53.3% / 非該当49.3%、差+4.0pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・攻撃速度・移動速度）；[[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-233|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=958）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/galio|ガリオ（Galio）]] — 対象側勝率65.2%（30/46）、n=46（十分性の目安を満たす）。
  - [[wiki/entities/champions/morgana|モルガナ（Morgana）]] — 対象側勝率65.1%（28/43）、n=43（十分性の目安を満たす）。
  - [[wiki/entities/champions/smolder|スモルダー（Smolder）]] — 対象側勝率63.0%（29/46）、n=46（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率46.8%（29/62）、n=62（十分性の目安を満たす）。
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率46.9%（23/49）、n=49（十分性の目安を満たす）。
  - [[wiki/entities/champions/diana|ダイアナ（Diana）]] — 対象側勝率55.9%（19/34）、n=34（十分性の目安を満たす）。

### MIDDLE（対象n=15）

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

### JUNGLE（対象541試合、全体勝率51.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：プレスアタック／凱旋・レジェンド: 迅速・最期の慈悲；副系覇道：サドンインパクト・貪欲な賞金首狩り；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 243/541 | 44.9% | 51.0% |
| 2 | 主系栄華：プレスアタック／凱旋・レジェンド: 迅速・最期の慈悲；副系天啓：宇宙の英知・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 47/541 | 8.7% | 42.6% |
| 3 | 主系覇道：ヘイルブレード／サドンインパクト・第六感・貪欲な賞金首狩り；副系天啓：キャッシュバック・トリプル トニック；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 45/541 | 8.3% | 51.1% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Briar` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Briar.png)
