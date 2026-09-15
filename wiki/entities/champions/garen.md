---
title: "ガレン"
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
champion_id: "Garen"
champion_key: "86"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "なし"
image_path: "raw/assets/champions/Garen.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Garen.png"
---

# ガレン

![[raw/assets/champions/Garen.png|128]]

## 基本情報

- **英字ID：** `Garen`
- **キー：** `86`
- **称号：** デマーシアの勇士
- **データversion：** `16.18.1`

## 紹介

仲間からは好かれ、敵からも尊敬を集めているガレンは誇り高きドーントレス前衛隊の戦士だ。彼は名門クラウンガード家の後継ぎとして、デマーシアの国家とその理念を守る任務を与えられている。魔力を防ぐ鎧を身に付けて、強力なブロードソードを振りかざし、ガレンは魔術師たちが待つ戦場に、鋼鉄の勇気の竜巻となって飛び込んでいく。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** なし

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 7 |
| `magic` | 1 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 690 |
| `hpperlevel` | 98 |
| `mp` | 0 |
| `mpperlevel` | 0 |
| `movespeed` | 340 |
| `armor` | 38 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 1.55 |
| `attackrange` | 175 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 69 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.65 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — タフガイ：** 一定時間ダメージや敵のスキルを受けていなければ、毎秒最大体力の一定割合を回復する。

- **Q — 断固たる一撃：** 自身にかけられたスロウ効果を解除し、移動速度が増加する。次の攻撃で敵の急所を斬りつけて追加ダメージを与え、サイレンス効果を付与する。
- **W — 勇気の護り：** 自動効果: 敵ユニットを倒すたびに物理防御と魔法防御が増加する。 発動効果: 瞬間的にシールドと行動妨害耐性を獲得し、その後は軽減率が低下するものの、ダメージ軽減効果が長い時間持続する。
- **E — ジャッジメント：** 高速で回転しながら剣を振り回し、周囲の敵に物理ダメージを与える。
- **R — デマーシアの正義：** デマーシア魂を燃え上がらせ、指定した敵チャンピオンに必殺の一撃を繰り出す。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤、終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中2位（上位15%）。体力690、物理防御38、攻撃力69、移動速度340。
  - 敵ユニットを倒すたびに物理防御と魔法防御が増加する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 中盤寄り
- **対象試合：** 472試合、全体勝率 53.2%
- **時間帯別勝率：** 〜20分 51.2%（n=80）、20〜25分 60.9%（n=69）、25〜30分 53.0%（n=115）、30〜35分 51.0%（n=98）、35分〜 51.8%（n=110）
- **最高帯：** 20〜25分（判定差 9.1ポイント）
- **判定根拠：** 中間帯が最高、端点との差 9.1%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-86|ガレンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（882試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（該当n=48、70.8% / 非該当51.2%、差+19.6pt）；[[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-3071|ブラック クリーバー]]（該当n=51、70.6% / 非該当51.1%、差+19.4pt）
- **ステータス傾向：** ライフスティール（該当n=43、65.1% / 非該当51.6%、差+13.5pt）；クリティカル率（該当n=661、54.2% / 非該当46.6%、差+7.6pt）
- **理論仮説：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=9（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-3161|ショウジンの矛]]（n=7（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

### MIDDLE（92試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（該当n=60、61.7% / 非該当50.0%、差+11.7pt）；[[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-3172|ガンメタル ブーツ]]（該当n=36、58.3% / 非該当57.1%、差+1.2pt）
- **ステータス傾向：** 物理防御（該当n=38、68.4% / 非該当50.0%、差+18.4pt）
- **理論仮説：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=6（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-86|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=1,113）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/lee-sin|リー・シン（LeeSin）]] — 対象側勝率66.7%（26/39）、n=39（十分性の目安を満たす）。
  - [[wiki/entities/champions/morgana|モルガナ（Morgana）]] — 対象側勝率65.1%（28/43）、n=43（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率61.7%（58/94）、n=94（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/sion|サイオン（Sion）]] — 対象側勝率35.3%（12/34）、n=34（十分性の目安を満たす）。
  - [[wiki/entities/champions/darius|ダリウス（Darius）]] — 対象側勝率39.0%（23/59）、n=59（十分性の目安を満たす）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率45.2%（28/62）、n=62（十分性の目安を満たす）。

### MIDDLE（対象n=146）

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

### TOP（対象1,204試合、全体勝率53.2%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：征服者／凱旋・レジェンド: ヘイスト・背水の陣；副系魔道：アクシオム アルカニスト・追い風；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 547/1,204 | 45.4% | 53.0% |
| 2 | 主系栄華：征服者／凱旋・レジェンド: ヘイスト・背水の陣；副系不滅：心身調整・超成長；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 152/1,204 | 12.6% | 52.6% |
| 3 | 主系魔道：嵐乗りの勇躍／アクシオム アルカニスト・追い風・強まる嵐；副系不滅：超成長・息継ぎ；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 121/1,204 | 10.0% | 57.9% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Garen` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Garen.png)
