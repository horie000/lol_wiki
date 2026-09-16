---
title: "モルガナ"
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
  - "[[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis]]"
tags:
  - champion
  - role-support
  - role-mage
  - data-dragon
champion_id: "Morgana"
champion_key: "25"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Morgana.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Morgana.png"
---

# モルガナ

![[raw/assets/champions/Morgana.png|128]]

## 基本情報

- **英字ID：** `Morgana`
- **キー：** `25`
- **称号：** 堕天の高潔
- **データversion：** `16.18.1`

## 紹介

天界の存在であると同時に定命でもあるという二つの性質の間で葛藤を抱えるモルガナは、人間性をつなぎとめるために自身の翼を縛り付け、己の苦痛と悔恨を味わわせるために、偽善者や腐敗した者たちに挑みかかる。法律や伝統であっても、自分が不当だと思えば断固として拒絶する。彼女はデマーシアの影に身を潜め──たとえ他の者たちが圧制を試みようと──闇の炎で自らを守り、あるいはそれを鎖として用い、真実のために戦う。そんなモルガナは流刑者や追放の身にある者たちであっても、いつの日か立ち上がることができるのだと信じてやまない。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 6 |
| `magic` | 8 |
| `difficulty` | 1 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 104 |
| `mp` | 340 |
| `mpperlevel` | 60 |
| `movespeed` | 335 |
| `armor` | 25 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 450 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.4 |
| `mpregen` | 11 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 56 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.53 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ソウルサイフォン：** 敵チャンピオン、大型ミニオン、中型および大型ジャングルモンスターにダメージを与えると自身の体力を回復する。

- **Q — ダークバインド：** 闇の魔力で敵にスネア効果と魔法ダメージを与え、冒した罪の深さを思い知らせる。
- **W — 苦悶の影：** 周囲に呪いの闇を発生させ、範囲内にいる敵に継続的な魔法ダメージを与える。このダメージは対象の体力が低いほど増加する。
- **E — ブラックシールド：** 仲間のチャンピオンに星炎の加護によるバリアを付与する。このバリアは魔法ダメージと行動妨害を無効化する。
- **R — 魂の足枷：** 天界の力を解放し、翼を広げて空中に浮かぶ。周囲の敵チャンピオンを黒き痛みの鎖で縛り、そのチャンピオンへ向かう際の移動速度が上昇する。命中時にダメージとスロウ効果を与え、一定時間内に鎖から逃れることができなかった敵には追加でスタン効果を与える。

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
- **対象試合：** 527試合、全体勝率 53.3%
- **時間帯別勝率：** 〜20分 60.8%（n=79）、20〜25分 52.8%（n=53）、25〜30分 54.5%（n=156）、30〜35分 49.2%（n=128）、35分〜 51.4%（n=111）
- **最高帯：** 〜20分（判定差 9.4ポイント）
- **判定根拠：** 〜20分が最高、長時間帯との差 9.4%。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-25|モルガナの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（755試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3116|リーライ クリスタル セプター]]（該当n=30、76.7% / 非該当52.6%、差+24.1pt）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=71、63.4% / 非該当52.5%、差+10.9pt）
- **ステータス傾向：** 移動速度（該当n=716、54.3% / 非該当38.5%、差+15.9pt）；マナ（該当n=284、57.7% / 非該当51.0%、差+6.8pt）
- **理論仮説：** [[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-3165|モレロノミコン]]（n=12（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）；[[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-3165|モレロノミコン]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=5（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）

### MIDDLE（123試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=53、54.7% / 非該当48.6%、差+6.1pt）
- **ステータス傾向：** 物理防御（該当n=67、52.2% / 非該当50.0%、差+2.2pt）
- **理論仮説：** [[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=5（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）；[[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=3（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-25|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=915）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/briar|ブライアー（Briar）]] — 対象側勝率65.1%（28/43）、n=43（十分性の目安を満たす）。
  - [[wiki/entities/champions/garen|ガレン（Garen）]] — 対象側勝率65.1%（28/43）、n=43（十分性の目安を満たす）。
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率63.1%（41/65）、n=65（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/rell|レル（Rell）]] — 対象側勝率40.5%（15/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/blitzcrank|ブリッツクランク（Blitzcrank）]] — 対象側勝率43.6%（17/39）、n=39（十分性の目安を満たす）。
  - [[wiki/entities/champions/thresh|スレッシュ（Thresh）]] — 対象側勝率45.3%（24/53）、n=53（十分性の目安を満たす）。

### MIDDLE（対象n=165）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率53.3%（8/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率50.0%（10/20）、サンプル不足（n=20、十分性の目安30未満）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率50.0%（8/16）、サンプル不足（n=16、十分性の目安30未満）。
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

### UTILITY（対象478試合、全体勝率54.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系覇道：追い打ち・至極の賞金首狩り；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 182/478 | 38.1% | 52.7% |
| 2 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系天啓：ビスケットデリバリー・キャッシュバック；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 85/478 | 17.8% | 61.2% |
| 3 | 主系天啓：グレイシャルオーグメント／キャッシュバック・ビスケットデリバリー・宇宙の英知；副系魔道：マナフローバンド・至高；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 26/478 | 5.4% | 46.2% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

<!-- champion-tier-analysis:start -->
## 観測ランク帯別チャンピオン候補

- **スナップショット：** 2026-09-16生成、キュー420、観測10帯、各1,000試合、統合後9,761試合、min-games 15、[[reports/riot-ranked-tier-analysis/run-20260916T083219Z/report|ランク帯別詳細レポート]]。
- **根拠：** [[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis|Riotランク戦試合データ：観測ランク帯別特徴]]、[[wiki/syntheses/ranked-tier-characteristics|ランク帯別の試合特徴と全帯共通傾向]]。
- **読み方：** `observed_tier` はその試合を発見したプレイヤーの収集時点の所属帯であり、10人全員の試合時ランクではない。以下は各帯の上位選択と、min-games以上で機械的に抽出した高低勝率の探索候補で、推奨・因果効果・有意差を示さない。

### 低勝率候補（下位5）

| 観測帯 | 候補順位 | 試合数 | 勝敗 | 勝率 |
| --- | ---: | ---: | --- | ---: |
| DIAMOND | 5 | 43 | 14勝/29敗 | 32.6% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Morgana` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Morgana.png)
