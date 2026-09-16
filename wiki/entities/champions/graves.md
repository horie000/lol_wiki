---
title: "グレイブス"
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
champion_id: "Graves"
champion_key: "104"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Graves.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Graves.png"
---

# グレイブス

![[raw/assets/champions/Graves.png|128]]

## 基本情報

- **英字ID：** `Graves`
- **キー：** `104`
- **称号：** 無法者
- **データversion：** `16.18.1`

## 紹介

マルコム・グレイブスは傭兵、ギャンブラー、泥棒としてその名を知られた存在で、訪れたあらゆる街や帝国で指名手配されている。激しい気性ながら犯罪者としての名誉を維持することを重視し、逆らう者にはダブルバレルショットガン「デスティニー」の銃口でそれを思い知らせる。ここ数年は問題を抱えていた相棒のツイステッド・フェイトと和解し、混沌としたビルジウォーターの闇社会で協力して再び成功を手にしている。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 625 |
| `hpperlevel` | 106 |
| `mp` | 325 |
| `mpperlevel` | 40 |
| `movespeed` | 340 |
| `armor` | 33 |
| `armorperlevel` | 4.6 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 425 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 66 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.475 |

## アビリティ

- **パッシブ — ニュー・デスティニー：** ショットガンには独特の特性がある。弾を撃ち尽くしたらリロードが必要となる。通常攻撃は弾丸を4発発射する。弾丸はユニットを貫通しない。チャンピオン以外のユニットは、複数の弾丸が命中するとノックバックする。

- **Q — エンドライン：** 爆薬の詰まった弾を発射する。弾は発射してから1秒後、あるいは地形に当たると爆発する。
- **W — スモークスクリーン：** 指定地点に発煙弾を発射し、煙幕を発生させて範囲内の敵の視界を低下させる。着弾時の爆発に巻き込まれた敵は魔法ダメージを受け、一時的に移動速度が低下する。
- **E — クイックドロー：** グレイブスが前方にダッシュして物理防御と魔法防御が数秒間増加する。敵チャンピオンに向かってダッシュすると、代わりに「確固たる信念」を2スタック獲得する。敵ユニットに通常攻撃を行うと、このスキルのクールダウンが短縮され、防御力増加時間が更新される。
- **R — コラテラルダメージ：** 強力な炸裂弾を発射して、最初に命中した敵チャンピオンに大ダメージを与える。弾は敵チャンピオンに命中するか、最大射程に達すると炸裂し、扇状の範囲内にいる敵にダメージを与える。

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
- **対象試合：** 162試合、全体勝率 46.9%
- **時間帯別勝率：** 〜20分 57.1%（n=28）、20〜25分 57.9%（n=19）、25〜30分 52.5%（n=40）、30〜35分 31.1%（n=45）、35分〜 46.7%（n=30）
- **最高帯：** 20〜25分（判定差 26.8ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-104|グレイブスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（407試合）

- **実測ビルド候補：** [[wiki/entities/items/item-6673|イモータル シールドボウ]] + [[wiki/entities/items/item-6676|コレクター]] + [[wiki/entities/items/item-6697|ヒュブリス]]（該当n=32、68.8% / 非該当46.9%、差+21.8pt）；[[wiki/entities/items/item-6673|イモータル シールドボウ]] + [[wiki/entities/items/item-6697|ヒュブリス]]（該当n=32、68.8% / 非該当46.9%、差+21.8pt）
- **ステータス傾向：** クリティカル率（該当n=351、49.9% / 非該当41.1%、差+8.8pt）
- **理論仮説：** [[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-6333|デス ダンス]]（未観測；共通stats: 物理防御・攻撃力／チャンピオン原典にも言及: 物理防御・攻撃力）；[[wiki/entities/items/item-3139|マーキュリアル シミター]] + [[wiki/entities/items/item-3156|マルモティウスの胃袋]]（未観測；共通stats: 攻撃力・魔法防御／チャンピオン原典にも言及: 攻撃力・魔法防御）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-104|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=684）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/akali|アカリ（Akali）]] — 対象側勝率65.8%（25/38）、n=38（十分性の目安を満たす）。
  - [[wiki/entities/champions/malzahar|マルザハール（Malzahar）]] — 対象側勝率54.8%（17/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率54.7%（29/53）、n=53（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率36.8%（14/38）、n=38（十分性の目安を満たす）。
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率57.6%（19/33）、n=33（十分性の目安を満たす）。

### TOP（対象n=12）

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

### JUNGLE（対象847試合、全体勝率49.4%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系覇道：魂の収穫／サドンインパクト・グリスリー メメント・貪欲な賞金首狩り；副系栄華：レジェンド: 迅速・凱旋；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 292/847 | 34.5% | 53.8% |
| 2 | 主系栄華：フリートフットワーク／凱旋・レジェンド: 迅速・最期の慈悲；副系天啓：宇宙の英知・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 86/847 | 10.2% | 39.5% |
| 3 | 主系覇道：魂の収穫／サドンインパクト・グリスリー メメント・貪欲な賞金首狩り；副系栄華：凱旋・レジェンド: 迅速；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 49/847 | 5.8% | 38.8% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Graves` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Graves.png)
