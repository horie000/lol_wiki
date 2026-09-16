---
title: "ラックス"
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
  - role-mage
  - role-support
  - data-dragon
champion_id: "Lux"
champion_key: "99"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Lux.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lux.png"
---

# ラックス

![[raw/assets/champions/Lux.png|128]]

## 基本情報

- **英字ID：** `Lux`
- **キー：** `99`
- **称号：** 光の才女
- **データversion：** `16.18.1`

## 紹介

ラクサーナ・クラウンガードは魔法の才能を恐怖と疑惑の目で見る偏狭な国、デマーシアで生まれた。意思の力で光を自在に操ることができる彼女だったが、力を持つことを見つけられて追放されることを恐れながら育ち、名門一家の権威を守るためにそれを秘密にすることを強いられてきた。しかし、持ち前の楽観主義と負けん気で自らのユニークな能力を受け入れることを決めて、今では祖国のためにその力を密かに行使するようになったのである。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 4 |
| `magic` | 9 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 99 |
| `mp` | 440 |
| `mpperlevel` | 23.5 |
| `movespeed` | 330 |
| `armor` | 21 |
| `armorperlevel` | 5.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 9 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 54 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.669 |

## アビリティ

- **パッシブ — イルミネーション：** 攻撃スキルが命中した対象を数秒間「イルミネーション」でマークする。マークした対象にラックスの攻撃が命中すると、エネルギーが爆発して追加魔法ダメージを与える(追加ダメージの量はラックスのレベルに比例する)。

- **Q — ライトバインド：** 光の玉を発射し、最大2体までの敵にダメージを与えてスネア効果を付与する。
- **W — プリズムバリア：** 指定方向に杖を投げ、自身と杖に触れた味方チャンピオンに光を屈折させたシールドを付与する。杖は最大距離に達するとラックスのもとへ戻り、触れた味方チャンピオンと杖をキャッチしたラックスに再びシールドを付与する。
- **E — シンギュラリティ：** 指定地点に特異な光の玉を放ち、範囲内の敵にスロウ効果を付与する。効果時間内に再度発動すると光の玉が爆発し、範囲内の敵にダメージを与える。
- **R — ファイナルスパーク：** 光のエネルギーを集めてビームを発射し、範囲内の敵にダメージを与える。「イルミネーション」効果を受けている敵に命中すると爆発させて追加魔法ダメージを与え、再度「イルミネーション」を付与する。

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
- **対象試合：** 751試合、全体勝率 50.3%
- **時間帯別勝率：** 〜20分 56.7%（n=127）、20〜25分 46.7%（n=107）、25〜30分 53.6%（n=166）、30〜35分 50.9%（n=165）、35分〜 44.6%（n=186）
- **最高帯：** 〜20分（判定差 12.1ポイント）
- **判定根拠：** 〜20分が最高、長時間帯との差 12.1%。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-99|ラックスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（911試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3175|連呪使いのブーツ]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（該当n=51、60.8% / 非該当50.7%、差+10.1pt）；[[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=56、60.7% / 非該当50.6%、差+10.1pt）
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3003|アークエンジェル スタッフ]] + [[wiki/entities/items/item-3118|マリグナンス]]（n=3（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-3165|モレロノミコン]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=3（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

### MIDDLE（238試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3089|ラバドン デスキャップ]] + [[wiki/entities/items/item-3175|連呪使いのブーツ]]（該当n=36、63.9% / 非該当55.4%、差+8.4pt）；[[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-3175|連呪使いのブーツ]]（該当n=32、62.5% / 非該当55.8%、差+6.7pt）
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=10（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=6（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-99|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=1,043）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/dr-mundo|ドクター・ムンド（DrMundo）]] — 対象側勝率65.6%（21/32）、n=32（十分性の目安を満たす）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率59.2%（45/76）、n=76（十分性の目安を満たす）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率54.2%（150/277）、n=277（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/xerath|ゼラス（Xerath）]] — 対象側勝率40.0%（14/35）、n=35（十分性の目安を満たす）。
  - [[wiki/entities/champions/zyra|ザイラ（Zyra）]] — 対象側勝率41.7%（15/36）、n=36（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率44.3%（43/97）、n=97（十分性の目安を満たす）。

### MIDDLE（対象n=288）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率55.9%（19/34）、n=34（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率44.4%（12/27）、サンプル不足（n=27、十分性の目安30未満）。
  - [[wiki/entities/champions/malzahar|マルザハール（Malzahar）]] — 対象側勝率52.9%（9/17）、サンプル不足（n=17、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-16生成、キュー420、ユニーク試合10,000件、[[reports/riot-ranked-match-analysis/run-20260916T081004Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### UTILITY（対象568試合、全体勝率50.4%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系覇道：追い打ち・至極の賞金首狩り；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 294/568 | 51.8% | 48.6% |
| 2 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系天啓：ビスケットデリバリー・宇宙の英知；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 74/568 | 13.0% | 51.4% |
| 3 | 主系覇道：魂の収穫／追い打ち・グリスリー メメント・至極の賞金首狩り；副系魔道：マナフローバンド・至高；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 45/568 | 7.9% | 53.3% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

<!-- champion-tier-analysis:start -->
## 観測ランク帯別チャンピオン候補

- **スナップショット：** 2026-09-16生成、キュー420、観測10帯、各1,000試合、統合後9,761試合、min-games 15、[[reports/riot-ranked-tier-analysis/run-20260916T083219Z/report|ランク帯別詳細レポート]]。
- **根拠：** [[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis|Riotランク戦試合データ：観測ランク帯別特徴]]、[[wiki/syntheses/ranked-tier-characteristics|ランク帯別の試合特徴と全帯共通傾向]]。
- **読み方：** `observed_tier` はその試合を発見したプレイヤーの収集時点の所属帯であり、10人全員の試合時ランクではない。以下は各帯の上位選択と、min-games以上で機械的に抽出した高低勝率の探索候補で、推奨・因果効果・有意差を示さない。

### 高勝率候補（上位5）

| 観測帯 | 候補順位 | 試合数 | 勝敗 | 勝率 |
| --- | ---: | ---: | --- | ---: |
| GOLD | 5 | 89 | 56勝/33敗 | 62.9% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Lux` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lux.png)
