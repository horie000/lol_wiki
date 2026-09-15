---
title: "ザーヘン"
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
  - data-dragon
champion_id: "Zaahen"
champion_key: "904"
data_version: "16.18.1"
roles:
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Zaahen.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zaahen.png"
---

# ザーヘン

![[raw/assets/champions/Zaahen.png|128]]

## 基本情報

- **英字ID：** `Zaahen`
- **キー：** `904`
- **称号：** 沈まぬ者
- **データversion：** `16.18.1`

## 紹介

光と闇、相反する力の両方を操る堕ちし者、ザーヘンは、己を蝕もうとする穢れに抗い続けながら、同胞であるダーキンたちを狩る。かつては狂気を抑えるため、自ら望んでグレイヴの中に封印された。しかし今、彼は解き放たれ、心は高貴でありながらも、その目的において容赦はない。ザーヘンの戦いは永遠に続く内なる闘争だ。それでも彼が耐え抜く限り、ルーンテラを滅ぼさんとする者の上に、彼は再び立ち上がる。

## 分類

- **役割タグ：** `Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 6 |
| `magic` | 1 |
| `difficulty` | 2 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 114 |
| `mp` | 350 |
| `mpperlevel` | 55 |
| `movespeed` | 345 |
| `armor` | 36 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 8.15 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 戦威修養：** 敵チャンピオンに対する攻撃およびスキルで「不退転」のスタックを獲得し、スタックごとに攻撃力が増加する。「不退転」が最大スタックになると、攻撃力が増加し、復活できるようになる。

- **Q — ダーキングレイヴ：** 次の通常攻撃で2回斬りつけ、追加ダメージを与え、自身を回復する。スキルを再使用すると、次の通常攻撃で追加ダメージを与え、対象をノックアップさせる。
- **W — 戦慄の再臨：** 指定方向を突き刺し、命中した敵にダメージを与えた後、自身の方向へ引き寄せる。
- **E — 絢爛たる進撃：** 前方に突進し、周囲を斬りつける。
- **R — 無慈悲なる裁き：** 上昇した後、下方へ突き刺し、敵にダメージを与え、与えたダメージの一定割合の体力を回復する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中20位（上位15%）。体力640、物理防御36、攻撃力63、移動速度345。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 102試合、全体勝率 52.0%
- **時間帯別勝率：** 〜20分 57.9%（n=19）、20〜25分 58.8%（n=17）、25〜30分 43.8%（n=16）、30〜35分 53.8%（n=26）、35分〜 45.8%（n=24）
- **最高帯：** 20〜25分（判定差 15.1ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-904|ザーヘンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（175試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（該当n=54、53.7% / 非該当45.5%、差+8.2pt）
- **ステータス傾向：** 魔法防御（該当n=65、61.5% / 非該当40.0%、差+21.5pt）
- **理論仮説：** [[wiki/entities/items/item-6610|サンダード スカイ]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=11（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（n=7（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

### JUNGLE（83試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6333|デス ダンス]]（該当n=33、66.7% / 非該当46.0%、差+20.7pt）；[[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（該当n=52、55.8% / 非該当51.6%、差+4.2pt）
- **ステータス傾向：** 魔法防御（該当n=36、55.6% / 非該当53.2%、差+2.4pt）
- **理論仮説：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=3（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-6333|デス ダンス]]（n=4（15未満）；共通stats: 物理防御・攻撃力／チャンピオン原典にも言及: 物理防御・攻撃力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-904|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=261）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率65.4%（17/26）、サンプル不足（n=26、十分性の目安30未満）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率61.9%（13/21）、サンプル不足（n=21、十分性の目安30未満）。
  - [[wiki/entities/champions/ezreal|エズリアル（Ezreal）]] — 対象側勝率54.5%（12/22）、サンプル不足（n=22、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/k-sante|カ・サンテ（KSante）]] — 対象側勝率37.5%（6/16）、サンプル不足（n=16、十分性の目安30未満）。
  - [[wiki/entities/champions/ambessa|アンベッサ（Ambessa）]] — 対象側勝率56.2%（9/16）、サンプル不足（n=16、十分性の目安30未満）。

### JUNGLE（対象n=137）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率50.0%（9/18）、サンプル不足（n=18、十分性の目安30未満）。
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

### TOP（対象504試合、全体勝率53.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：征服者／凱旋・レジェンド: ヘイスト・最期の慈悲；副系不滅：ボーンアーマー・生気付与；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 133/504 | 26.4% | 48.9% |
| 2 | 主系不滅：不死者の握撃／打ちこわし・息継ぎ・生気付与；副系天啓：ビスケットデリバリー・宇宙の英知；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 59/504 | 11.7% | 54.2% |
| 3 | 主系覇道：ヘイルブレード／サドンインパクト・グリスリー メメント・至極の賞金首狩り；副系魔道：ニンバスクローク・至高；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 26/504 | 5.2% | 61.5% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Zaahen` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zaahen.png)
