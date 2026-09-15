---
title: "ジェイス"
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
  - role-marksman
  - data-dragon
champion_id: "Jayce"
champion_key: "126"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Jayce.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jayce.png"
---

# ジェイス

![[raw/assets/champions/Jayce.png|128]]

## 基本情報

- **英字ID：** `Jayce`
- **キー：** `126`
- **称号：** 未来への希望
- **データversion：** `16.18.1`

## 紹介

ジェイス・タリスは天才的な発明家であり、友人のビクターと共にヘクステックの秘密を初めて大きく解き明かした人物でもある。ピルトーヴァー全域で称賛された彼は、「進歩の男」という呼び名に相応しい存在たるべく努めてはいるものの、その期待からくる重圧に苦しむことも多い。そんな中、自身の発明がピルトーヴァーとゾウンの分断を助長していることに気づき始めた彼は、未来を守るべくヘクステックハンマーを手に戦うことを決意した。

## 分類

- **役割タグ：** `Fighter`、`Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 4 |
| `magic` | 3 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 590 |
| `hpperlevel` | 109 |
| `mp` | 375 |
| `mpperlevel` | 45 |
| `movespeed` | 335 |
| `armor` | 22 |
| `armorperlevel` | 5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 125 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — ヘクステック・コンデンサー：** 武器を切り替えると少しの間移動速度が増加する。

- **Q — スカイバスター/ショックブラスト：** ハンマーモード: 敵に飛びかかって物理ダメージとスロウ効果を与える。 キャノンモード: 電流の玉を発射し、敵に命中するか最大射程に達すると爆発して、範囲内の敵ユニットに物理ダメージを与える。
- **W — ライトニング/ハイパーチャージ：** ハンマーモード: 自動効果: 攻撃のたびにマナが回復する。 発動効果: 雷のフィールドを発生させ、周囲の敵に数秒間ダメージを与える。 キャノンモード: 爆発的なエネルギーを得て、次の数回の攻撃速度が最大まで増加する。
- **E — サンダーブロー/アクセルゲート：** ハンマーモード: 敵に魔法ダメージを与え、わずかに突き飛ばす。 キャノンモード: そこを通過したすべての味方チャンピオンの移動速度が増加する「アクセルゲート」を配備する。「ショックブラスト」が「アクセルゲート」を通過すると、弾速、射程、ダメージが増加する。
- **R — マーキュリーキャノン/マーキュリーハンマー：** ハンマーモード: 「マーキュリーハンマー」が「マーキュリーキャノン」に切り替わり、スキルが変化すると同時に射程距離が広がる。モード変更後の最初の一撃には、対象の物理防御と魔法防御を低下させる効果がつく。 キャノンモード: 「マーキュリーキャノン」が「マーキュリーハンマー」に切り替わり、変化と同時に物理防御と魔法防御が増加する。モード変更後の最初の一撃には魔法ダメージが追加される。

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
- **対象試合：** 116試合、全体勝率 45.7%
- **時間帯別勝率：** 〜20分 42.1%（n=19）、20〜25分 47.6%（n=21）、25〜30分 41.7%（n=24）、30〜35分 50.0%（n=22）、35分〜 46.7%（n=30）
- **最高帯：** 30〜35分（判定差 8.3ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-126|ジェイスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（193試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3142|妖夢の霊剣]] + [[wiki/entities/items/item-6694|セリルダの怨恨]]（該当n=40、67.5% / 非該当41.8%、差+25.7pt）；[[wiki/entities/items/item-3042|ムラマナ]] + [[wiki/entities/items/item-3142|妖夢の霊剣]] + [[wiki/entities/items/item-6694|セリルダの怨恨]]（該当n=35、65.7% / 非該当43.0%、差+22.7pt）
- **ステータス傾向：** 体力（該当n=151、48.3% / 非該当42.9%、差+5.5pt）
- **理論仮説：** [[wiki/entities/items/item-3173|チェインレースド クラッシャー]] + [[wiki/entities/items/item-4401|自然の力]]（未観測；共通stats: 魔法防御・移動速度／チャンピオン原典にも言及: 魔法防御・移動速度）；[[wiki/entities/items/item-2502|終わりなき絶望]] + [[wiki/entities/items/item-3075|ソーンメイル]]（n=2（15未満）；共通stats: 物理防御・体力／チャンピオン原典にも言及: 物理防御）

### MIDDLE（79試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3042|ムラマナ]] + [[wiki/entities/items/item-3142|妖夢の霊剣]]（該当n=30、66.7% / 非該当46.9%、差+19.7pt）
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-6333|デス ダンス]]（未観測；共通stats: 物理防御・攻撃力／チャンピオン原典にも言及: 物理防御）；[[wiki/entities/items/item-3065|スピリット ビサージュ]] + [[wiki/entities/items/item-6664|ホロウ レディアンス]]（未観測；共通stats: 体力・魔法防御／チャンピオン原典にも言及: 魔法防御）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-126|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=324）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率38.7%（12/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率35.5%（11/31）、n=31（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/malphite|マルファイト（Malphite）]] — 対象側勝率33.3%（6/18）、サンプル不足（n=18、十分性の目安30未満）。
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率40.0%（6/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率46.7%（7/15）、サンプル不足（n=15、十分性の目安30未満）。

### JUNGLE（対象n=152）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/ezreal|エズリアル（Ezreal）]] — 対象側勝率62.5%（10/16）、サンプル不足（n=16、十分性の目安30未満）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率45.0%（9/20）、サンプル不足（n=20、十分性の目安30未満）。
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

### TOP（対象581試合、全体勝率49.2%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：嵐乗りの勇躍／マナフローバンド・英気集中・強まる嵐；副系天啓：ビスケットデリバリー・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 64/581 | 11.0% | 50.0% |
| 2 | 主系栄華：征服者／冷静沈着・レジェンド: 迅速・背水の陣；副系天啓：ビスケットデリバリー・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 39/581 | 6.7% | 61.5% |
| 3 | 主系不滅：不死者の握撃／打ちこわし・息継ぎ・超成長；副系天啓：ビスケットデリバリー・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 31/581 | 5.3% | 45.2% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Jayce` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jayce.png)
