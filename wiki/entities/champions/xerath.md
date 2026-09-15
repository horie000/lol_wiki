---
title: "ゼラス"
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
champion_id: "Xerath"
champion_key: "101"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Xerath.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Xerath.png"
---

# ゼラス

![[raw/assets/champions/Xerath.png|128]]

## 基本情報

- **英字ID：** `Xerath`
- **キー：** `101`
- **称号：** 超越魔神
- **データversion：** `16.18.1`

## 紹介

古代シュリーマの超越魔人ゼラスは、魔法の石棺の破片に封じられ、悶え苦しむ神秘のエネルギー体である。彼は数千年の間、砂漠の底に閉じ込められていたが、シュリーマが砂の中から現れたことで彼もまた古代の牢獄から解放された。力を手に入れたことで正気を失った彼は、自分のものであると信じてやまないものを自らの手で奪い取り、世界中の新しい文明を、自らが思い描いたそれで置き換えようと企んでいる。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 3 |
| `magic` | 10 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 575 |
| `hpperlevel` | 106 |
| `mp` | 400 |
| `mpperlevel` | 22 |
| `movespeed` | 340 |
| `armor` | 22 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 6.85 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.36 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — マナサージ：** 一定時間ごとに、通常攻撃でダメージを与えると自身のマナを回復する。ユニットをキルするたびに、このクールダウンが短縮される。

- **Q — アルカノパルス：** 長射程のエネルギービームを発射し、命中したすべての敵ユニットに魔法ダメージを与える。
- **W — デストラクションアイ：** 神秘のエネルギーを空から撃ち落とし、範囲内の敵ユニットにスロウと魔法ダメージを与える。範囲内の中心にいる敵ユニットは、より大きなダメージとスロウを受ける。
- **E — ショックオーブ：** 敵ユニットに魔法ダメージとスタンを与える。
- **R — アーケーンライト：** 移動できなくなるかわりに、超長距離射程の攻撃を行えるようになる。

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

- **観測分類：** 序盤寄り
- **対象試合：** 501試合、全体勝率 55.5%
- **時間帯別勝率：** 〜20分 65.1%（n=86）、20〜25分 54.0%（n=63）、25〜30分 53.0%（n=100）、30〜35分 54.3%（n=127）、35分〜 52.8%（n=125）
- **最高帯：** 〜20分（判定差 12.3ポイント）
- **判定根拠：** 〜20分が最高、長時間帯との差 12.3%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-101|ゼラスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（439試合）

- **実測ビルド候補：** [[wiki/entities/items/item-4628|ホライゾン フォーカス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（該当n=159、61.6% / 非該当57.1%、差+4.5pt）；[[wiki/entities/items/item-4645|シャドウフレイム]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（該当n=108、61.1% / 非該当58.0%、差+3.1pt）
- **ステータス傾向：** 体力（該当n=71、69.0% / 非該当56.8%、差+12.2pt）；移動速度（該当n=394、59.6% / 非該当51.1%、差+8.5pt）
- **理論仮説：** [[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=9（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=4（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

### MIDDLE（404試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（該当n=32、78.1% / 非該当47.8%、差+30.3pt）；[[wiki/entities/items/item-3089|ラバドン デスキャップ]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（該当n=94、58.5% / 非該当47.7%、差+10.8pt）
- **ステータス傾向：** 体力（該当n=273、52.4% / 非該当45.8%、差+6.6pt）；物理防御（該当n=43、53.5% / 非該当49.9%、差+3.6pt）
- **理論仮説：** [[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=12（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=7（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-101|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=554）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率62.8%（27/43）、n=43（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率61.8%（21/34）、n=34（十分性の目安を満たす）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率57.6%（95/165）、n=165（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率50.0%（20/40）、n=40（十分性の目安を満たす）。
  - [[wiki/entities/champions/lux|ラックス（Lux）]] — 対象側勝率60.0%（21/35）、n=35（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率65.2%（30/46）、n=46（十分性の目安を満たす）。

### MIDDLE（対象n=544）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率64.3%（27/42）、n=42（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率61.1%（33/54）、n=54（十分性の目安を満たす）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率59.5%（25/42）、n=42（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/hwei|フェイ（Hwei）]] — 対象側勝率46.2%（18/39）、n=39（十分性の目安を満たす）。
  - [[wiki/entities/champions/viktor|ビクター（Viktor）]] — 対象側勝率54.1%（20/37）、n=37（十分性の目安を満たす）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合20,010件、[[reports/riot-ranked-match-analysis/run-20260915T103154Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### MIDDLE（対象806試合、全体勝率49.5%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系栄華：最期の慈悲・冷静沈着；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 240/806 | 29.8% | 46.2% |
| 2 | 主系魔道：秘儀の彗星／マナフローバンド・英気集中・追火；副系栄華：冷静沈着・切り崩し；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 80/806 | 9.9% | 55.0% |
| 3 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系栄華：冷静沈着・最期の慈悲；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 53/806 | 6.6% | 52.8% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Xerath` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Xerath.png)
