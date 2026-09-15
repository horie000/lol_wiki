---
title: "ダリウス"
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
  - role-tank
  - data-dragon
champion_id: "Darius"
champion_key: "122"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Darius.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Darius.png"
---

# ダリウス

![[raw/assets/champions/Darius.png|128]]

## 基本情報

- **英字ID：** `Darius`
- **キー：** `122`
- **称号：** ノクサスの戦斧
- **データversion：** `16.18.1`

## 紹介

ノクサス国内で最も恐れられる百戦錬磨の戦士、ダリウス。彼ほど、同国の強さを体現する司令官はいないだろう。貧しい育ちでありながら「ノクサスの戦斧」と呼ばれるまでになった彼は、帝国の敵を薙ぎ払い続ける──その多くはノクサス人である。自身の行為の意義に決して疑いを持つことはなく、彼はひとたび斧を振りかざせば決してためらうことはない。彼はトリファリアン・レギオンのリーダーに逆らう者には一切容赦しないのである。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 5 |
| `magic` | 1 |
| `difficulty` | 2 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 652 |
| `hpperlevel` | 114 |
| `mp` | 263 |
| `mpperlevel` | 58 |
| `movespeed` | 340 |
| `armor` | 37 |
| `armorperlevel` | 5.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 10 |
| `hpregenperlevel` | 0.95 |
| `mpregen` | 6.6 |
| `mpregenperlevel` | 0.35 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 大出血：** 通常攻撃または攻撃スキルが命中した敵を出血させ、5秒間物理ダメージを与える。最大5回まで効果をスタックさせることができる。対象のスタックが最大になると、ダリウスが激怒して攻撃力が大幅に増加する。

- **Q — 皆殺しの斧：** 斧を構えて振り抜き、周囲の敵を攻撃する。刃に当たった敵は、内側の柄に当たった敵より大きなダメージを受ける。刃に当たった敵チャンピオンと大型モンスターの数に応じて自身を回復する。
- **W — 脚削ぎ：** 次の通常攻撃で敵の動脈を狙い、出血させることでスロウ効果を付与する。
- **E — 捕縛：** 斧を研ぎ澄まし、対象の物理防御を一部無視して物理ダメージを与えるようになる。スキルを使用すると、刃で敵を引っかけてそばに引き寄せる。
- **R — ノクサスギロチン：** 敵チャンピオンに飛びかかり、斧を振り下ろして確定ダメージを与える。対象の「大出血」のスタック数に応じてダメージが増加する。「ノクサスギロチン」で敵にとどめを刺すと、少しの間クールダウンが解消される。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中21位（上位15%）。体力652、物理防御37、攻撃力64、移動速度340。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 中盤寄り
- **対象試合：** 532試合、全体勝率 50.6%
- **時間帯別勝率：** 〜20分 48.0%（n=98）、20〜25分 49.2%（n=65）、25〜30分 49.6%（n=113）、30〜35分 56.9%（n=130）、35分〜 47.6%（n=126）
- **最高帯：** 30〜35分（判定差 9.0ポイント）
- **判定根拠：** 中間帯が最高、端点との差 9.0%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-122|ダリウスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（825試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3053|ステラックの篭手]] + [[wiki/entities/items/item-3742|デッド マン プレート]] + [[wiki/entities/items/item-4401|自然の力]]（該当n=39、71.8% / 非該当49.7%、差+22.0pt）；[[wiki/entities/items/item-3742|デッド マン プレート]] + [[wiki/entities/items/item-6333|デス ダンス]]（該当n=74、70.3% / 非該当48.9%、差+21.4pt）
- **ステータス傾向：** 魔法防御（該当n=361、55.4% / 非該当47.2%、差+8.2pt）；物理防御（該当n=661、51.7% / 非該当47.0%、差+4.8pt）
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

### JUNGLE（121試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3142|妖夢の霊剣]] + [[wiki/entities/items/item-4401|自然の力]]（該当n=32、53.1% / 非該当46.1%、差+7.1pt）；[[wiki/entities/items/item-3142|妖夢の霊剣]] + [[wiki/entities/items/item-3742|デッド マン プレート]]（該当n=63、49.2% / 非該当46.6%、差+2.7pt）
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3161|ショウジンの矛]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=3（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-122|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=1,010）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/veigar|ベイガー（Veigar）]] — 対象側勝率67.6%（25/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/morgana|モルガナ（Morgana）]] — 対象側勝率66.7%（22/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率61.8%（55/89）、n=89（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/dr-mundo|ドクター・ムンド（DrMundo）]] — 対象側勝率26.7%（8/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率40.0%（16/40）、n=40（十分性の目安を満たす）。
  - [[wiki/entities/champions/yorick|ヨリック（Yorick）]] — 対象側勝率46.8%（22/47）、n=47（十分性の目安を満たす）。

### JUNGLE（対象n=146）

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

### TOP（対象1,125試合、全体勝率50.7%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：征服者／凱旋・レジェンド: 迅速・背水の陣；副系魔道：アクシオム アルカニスト・追い風；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 345/1,125 | 30.7% | 52.2% |
| 2 | 主系栄華：征服者／凱旋・レジェンド: ヘイスト・背水の陣；副系不滅：ボーンアーマー・気迫；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 205/1,125 | 18.2% | 52.2% |
| 3 | 主系魔道：嵐乗りの勇躍／ニンバスクローク・追い風・強まる嵐；副系栄華：レジェンド: 迅速・凱旋；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 83/1,125 | 7.4% | 44.6% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Darius` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Darius.png)
