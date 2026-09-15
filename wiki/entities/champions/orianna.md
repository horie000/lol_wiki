---
title: "オリアナ"
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
  - role-mage
  - role-support
  - data-dragon
champion_id: "Orianna"
champion_key: "61"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Orianna.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Orianna.png"
---

# オリアナ

![[raw/assets/champions/Orianna.png|128]]

## 基本情報

- **英字ID：** `Orianna`
- **キー：** `61`
- **称号：** 時計仕掛けの舞姫
- **データversion：** `16.18.1`

## 紹介

オリアナはかつては好奇心旺盛な普通の少女だったが、今では技術の粋を駆使した機械仕掛けの体になってしまった。彼女はゾウンの下層地域で起こった事故で重傷を負い、体の部位を一つずつ精巧に作られた人工物に置き換えなければならなかった。再び自由に動けるようになった今、オリアナは自らを守るお供として作り出した真鍮の球体とともに、ピルトーヴァーやその向こうにある世界の探索を続けている。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 3 |
| `magic` | 9 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 565 |
| `hpperlevel` | 110 |
| `mp` | 418 |
| `mpperlevel` | 25 |
| `movespeed` | 325 |
| `armor` | 20 |
| `armorperlevel` | 4.2 |
| `spellblock` | 26 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 44 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — ぜんまい仕掛け：** 通常攻撃が追加で魔法ダメージを与える。このダメージは同じ対象を続けて攻撃すると増加する。

- **Q — オーダー: 攻撃：** オリアナが指定地点を攻撃するようボールに命じ、軌道上の敵ユニットに魔法ダメージを与える (敵に命中する度にダメージは低下する)。ボールは攻撃後もその場に留まる。
- **W — オーダー: 乱磁場：** オリアナの命令により、ボールがエネルギー波を発射して周囲の敵に魔法ダメージを与える。後には力場が残され、範囲内に入ると、味方の移動速度が増加し、敵はスロウ状態になる。
- **E — オーダー: 防御：** オリアナの命令により、ボールが味方チャンピオンに貼りつき、シールドを付与する。ボールは移動時に触れたすべての敵に魔法ダメージを与える。さらに、ボールは貼り付いたチャンピオンの物理防御と魔法防御を増加させる。
- **R — オーダー: ショックウェーブ：** オリアナが命令してから一瞬後、ボールが衝撃波を発射して周囲の敵に魔法ダメージを与え、ボールの方向へ引き寄せる。

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
- **対象試合：** 135試合、全体勝率 41.5%
- **時間帯別勝率：** 〜20分 48.0%（n=25）、20〜25分 38.5%（n=13）、25〜30分 50.0%（n=26）、30〜35分 44.1%（n=34）、35分〜 29.7%（n=37）
- **最高帯：** 25〜30分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-61|オリアナの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（328試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3175|連呪使いのブーツ]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（該当n=89、56.2% / 非該当41.0%、差+15.2pt）；[[wiki/entities/items/item-3175|連呪使いのブーツ]] + [[wiki/entities/items/item-4645|シャドウフレイム]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（該当n=58、55.2% / 非該当43.0%、差+12.2pt）
- **ステータス傾向：** 体力（該当n=231、46.8% / 非該当41.2%、差+5.5pt）；物理防御（該当n=125、48.0% / 非該当43.3%、差+4.7pt）
- **理論仮説：** [[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（n=11（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-6653|ライアンドリーの仮面]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（n=4（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-61|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=471）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率55.3%（21/38）、n=38（十分性の目安を満たす）。
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率51.3%（20/39）、n=39（十分性の目安を満たす）。
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率49.1%（26/53）、n=53（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/sylas|サイラス（Sylas）]] — 対象側勝率25.0%（6/24）、サンプル不足（n=24、十分性の目安30未満）。
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率34.8%（8/23）、サンプル不足（n=23、十分性の目安30未満）。
  - [[wiki/entities/champions/viktor|ビクター（Viktor）]] — 対象側勝率36.4%（8/22）、サンプル不足（n=22、十分性の目安30未満）。

### UTILITY（対象n=7）

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

### MIDDLE（対象561試合、全体勝率47.8%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：嵐乗りの勇躍／マナフローバンド・至高・追火；副系栄華：レジェンド: ヘイスト・冷静沈着；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 88/561 | 15.7% | 47.7% |
| 2 | 主系魔道：エアリー召喚／マナフローバンド・至高・追火；副系栄華：最期の慈悲・冷静沈着；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 70/561 | 12.5% | 50.0% |
| 3 | 主系魔道：嵐乗りの勇躍／マナフローバンド・至高・追火；副系天啓：ビスケットデリバリー・宇宙の英知；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 32/561 | 5.7% | 34.4% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Orianna` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Orianna.png)
