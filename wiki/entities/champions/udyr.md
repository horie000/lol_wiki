---
title: "ウディア"
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
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "Udyr"
champion_key: "77"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Udyr.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Udyr.png"
---

# ウディア

![[raw/assets/champions/Udyr.png|128]]

## 基本情報

- **英字ID：** `Udyr`
- **キー：** `77`
- **称号：** 精霊と歩む者
- **データversion：** `16.18.1`

## 紹介

現存するスピリットウォーカーの中でも最大の力を持つウディアは、フレヨルドのあらゆる精霊と心を通わせることができる。彼らの欲求に共感して理解を示したり、その霊的なエネルギーを変換して、自身の原始的な戦闘法に取り入れることができるのだ。自らの心が周囲の心の声に埋もれてしまわないように、ウディアは内なる均衡を求めているが、外の世界についても均衡を欲している──フレヨルドの神秘的な風景は、対立と争いから生まれる成長によってのみ、繁栄することができるのだ。ウディアは、平和という停滞を避けるためには、犠牲を払うこ...

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 7 |
| `magic` | 4 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 664 |
| `hpperlevel` | 92 |
| `mp` | 271 |
| `mpperlevel` | 50 |
| `movespeed` | 350 |
| `armor` | 31 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.65 |

## アビリティ

- **パッシブ — 精霊の繋ぎ手：** 4つの通常スキルで「型」を切り替え、スキルを再発動すると「型」がリフレッシュされて究極の効果を得る。さらに、スキル使用後、次の2回の通常攻撃の攻撃速度が増加する。

- **Q — 野性の爪：** 攻撃速度が増加し、次の2回の通常攻撃が追加物理ダメージを与える。 再発動: 攻撃速度がさらに増加し、次の2回の通常攻撃が対象に電撃を放つようになる。
- **W — 鉄の外皮：** シールドを獲得し、次の2回の通常攻撃で自身の体力を回復する。 再発動: より耐久値の高いシールドを獲得し、数秒間かけて最大体力の一定割合を回復する。
- **E — 焔の猛進：** 移動速度が増加し、各対象への最初の通常攻撃が対象をスタンさせる。 再発動: 少しの間、移動速度がさらに増加し、移動不能効果を受けなくなる。
- **R — 氷翼の嵐：** 極寒の嵐に身を包み、周囲の敵にダメージとスロウ効果を与える。 再発動: 嵐を強化して解き放ち、敵を追跡させて追加ダメージを与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中15位（上位15%）。体力664、物理防御31、攻撃力62、移動速度350。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 判定保留（分母不足）
- **対象試合：** 95試合、全体勝率 55.8%
- **時間帯別勝率：** 〜20分 53.3%（n=15）、20〜25分 66.7%（n=12）、25〜30分 45.5%（n=22）、30〜35分 63.0%（n=27）、35分〜 52.6%（n=19）
- **最高帯：** 20〜25分（判定差 不明）
- **判定根拠：** 全5帯で各15試合未満の帯がある。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-77|ウディアの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（150試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 物理防御（該当n=104、48.1% / 非該当41.3%、差+6.8pt）；魔法防御（該当n=72、48.6% / 非該当43.6%、差+5.0pt）
- **理論仮説：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=3（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）

### TOP（80試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 魔法防御（該当n=38、71.1% / 非該当50.0%、差+21.1pt）；マナ（該当n=47、66.0% / 非該当51.5%、差+14.4pt）
- **理論仮説：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-77|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=213）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率75.0%（15/20）、サンプル不足（n=20、十分性の目安30未満）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率66.7%（10/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率64.7%（11/17）、サンプル不足（n=17、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率56.2%（9/16）、サンプル不足（n=16、十分性の目安30未満）。

### TOP（対象n=126）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率60.0%（9/15）、サンプル不足（n=15、十分性の目安30未満）。
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

### JUNGLE（対象100試合、全体勝率42.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：プレスアタック／凱旋・レジェンド: ヘイスト・最期の慈悲；副系天啓：疾駆・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 12/100 | 12.0% | 66.7% |
| 2 | 主系栄華：征服者／凱旋・レジェンド: ヘイスト・背水の陣；副系天啓：疾駆・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 8/100 | 8.0% | 50.0% |
| 3 | 主系栄華：プレスアタック／凱旋・レジェンド: ヘイスト・最期の慈悲；副系天啓：魔法の靴・疾駆；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 7/100 | 7.0% | 28.6% |

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
| PLATINUM | 2 | 23 | 6勝/17敗 | 26.1% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Udyr` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Udyr.png)
