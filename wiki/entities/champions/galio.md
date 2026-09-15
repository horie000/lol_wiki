---
title: "ガリオ"
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
  - role-tank
  - role-mage
  - data-dragon
champion_id: "Galio"
champion_key: "3"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Galio.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Galio.png"
---

# ガリオ

![[raw/assets/champions/Galio.png|128]]

## 基本情報

- **英字ID：** `Galio`
- **キー：** `3`
- **称号：** 伝説の巨像
- **データversion：** `16.18.1`

## 紹介

輝ける都市デマーシアの外側で、石の巨像ガリオはずっと見張りを続けている。敵の魔法使いに対する防御機構として建造された彼は、強力な魔法によって生命が満たされるまで何十年も微動だにせず、ただ立ち続ける。そして、ひとたび活動を始めると、ガリオは動ける時間のほとんどを戦いのスリルと同胞たる国民を守るという稀有な名誉を味わうことに費やすのだ。だが彼の勝利はいつも皮肉なもので、彼が打ち倒すべき魔法こそ彼が動くための原動力であるために、勝利するたびに再び動かぬ彫像となってしまうのだ。

## 分類

- **役割タグ：** `Tank`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 10 |
| `magic` | 6 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 126 |
| `mp` | 410 |
| `mpperlevel` | 40 |
| `movespeed` | 340 |
| `armor` | 24 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 9.5 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 巨像の一撃：** 数秒毎に、通常攻撃が一定範囲に追加魔法ダメージを与える。

- **Q — 戦の旋風：** 2つの突風を巻き起こす。突風同士は重なり合い、継続ダメージを与える巨大な竜巻となる。
- **W — デュランドの守り：** 防御の構えを取り移動速度が低下する。構えを解くと、周囲の敵ユニットにタウント効果とダメージを与える。
- **E — 正義の鉄拳：** 少し下がってから前方に突進し、最初に当たった敵チャンピオンをノックアップする。
- **R — 英雄降臨：** 味方1体の位置を着地点として指定し、範囲内のすべての味方に魔法ダメージを防ぐシールドを付与する。少ししてから、着地点に向かって落下し、周囲の敵をノックアップする。

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
- **対象試合：** 424試合、全体勝率 48.8%
- **時間帯別勝率：** 〜20分 46.7%（n=60）、20〜25分 54.7%（n=53）、25〜30分 46.4%（n=110）、30〜35分 48.5%（n=99）、35分〜 50.0%（n=102）
- **最高帯：** 20〜25分（判定差 8.4ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-3|ガリオの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（787試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3075|ソーンメイル]] + [[wiki/entities/items/item-3157|ゾーニャの砂時計]]（該当n=30、70.0% / 非該当49.4%、差+20.6pt）；[[wiki/entities/items/item-3075|ソーンメイル]] + [[wiki/entities/items/item-4633|リフトメーカー]] + [[wiki/entities/items/item-6664|ホロウ レディアンス]]（該当n=42、69.0% / 非該当49.1%、差+19.9pt）
- **ステータス傾向：** 体力再生（該当n=34、55.9% / 非該当49.9%、差+5.9pt）；魔法防御（該当n=638、50.6% / 非該当48.3%、差+2.3pt）
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）

### UTILITY（82試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=5（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=2（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-3|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=999）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率69.0%（29/42）、n=42（十分性の目安を満たす）。
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率65.3%（47/72）、n=72（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率62.4%（53/85）、n=85（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/yasuo|ヤスオ（Yasuo）]] — 対象側勝率33.3%（10/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率45.3%（34/75）、n=75（十分性の目安を満たす）。
  - [[wiki/entities/champions/sylas|サイラス（Sylas）]] — 対象側勝率45.7%（16/35）、n=35（十分性の目安を満たす）。

### UTILITY（対象n=100）

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

### MIDDLE（対象1,288試合、全体勝率50.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系不滅：アフターショック／シールドバッシュ・ボーンアーマー・超成長；副系魔道：ニンバスクローク・至高；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 351/1,288 | 27.3% | 49.6% |
| 2 | 主系魔道：嵐乗りの勇躍／マナフローバンド・至高・追火；副系不滅：息継ぎ・気迫；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 330/1,288 | 25.6% | 50.6% |
| 3 | 主系覇道：電撃／サドンインパクト・グリスリー メメント・貪欲な賞金首狩り；副系魔道：ニンバスクローク・追火；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 66/1,288 | 5.1% | 45.5% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Galio` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Galio.png)
