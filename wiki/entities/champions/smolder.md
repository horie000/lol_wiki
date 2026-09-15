---
title: "スモルダー"
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
  - role-marksman
  - role-mage
  - data-dragon
champion_id: "Smolder"
champion_key: "901"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Smolder.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Smolder.png"
---

# スモルダー

![[raw/assets/champions/Smolder.png|128]]

## 基本情報

- **英字ID：** `Smolder`
- **キー：** `901`
- **称号：** 炎の幼龍
- **データversion：** `16.18.1`

## 紹介

ノクサスの辺境にある岩だらけの崖に身を隠し、幼きドラゴンは母親に見守られながら、カマヴォールのインペリアルドラゴンの継承者とは何たるかを学んでいる。遊び好きで意欲旺盛なスモルダーは急成長を遂げており、能力を磨けるならどんな機会も逃さない。まだ幼くともスモルダーの力は決して侮れず、火のつくものなら何でも簡単に燃やしてしまう。

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 2 |
| `magic` | 5 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 575 |
| `hpperlevel` | 100 |
| `mp` | 300 |
| `mpperlevel` | 40 |
| `movespeed` | 330 |
| `armor` | 24 |
| `armorperlevel` | 4 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8.5 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 4 |
| `attackspeed` | 0.638 |

## アビリティ

- **パッシブ — 駆けだしドラゴン：** スキルをチャンピオンに命中させる、または「スーパーこげこげブレス」で敵をキルすると、「駆けだしドラゴン」のスタックを1つ獲得する。スタック数に応じて通常スキルのダメージが増加する。

- **Q — スーパーこげこげブレス：** 敵1体に炎のブレスを吐きかける。スタックを獲得するほど、このスキルが強化されていく。
- **W — くしゅん！：** 可愛らしいくしゃみと共に炎を吐く。この炎は敵チャンピオンに命中すると爆発する。
- **E — パタパタパタ：** 飛翔して地形を無視するようになり、最も体力が低い敵を空から攻撃する。
- **R — ママーッ！！：** 母ドラゴンを呼び寄せて、上空から炎を吐いてもらう。炎の中心部にいる敵には、追加ダメージとスロウ効果を与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 「駆けだしドラゴン」のスタック数に応じて通常スキルのダメージが増加する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 終盤寄り
- **対象試合：** 479試合、全体勝率 48.4%
- **時間帯別勝率：** 〜20分 44.6%（n=74）、20〜25分 54.2%（n=59）、25〜30分 41.3%（n=92）、30〜35分 46.8%（n=126）、35分〜 54.7%（n=128）
- **最高帯：** 35分〜（判定差 10.1ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 10.1%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-901|スモルダーの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（886試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-3161|ショウジンの矛]] + [[wiki/entities/items/item-3508|エッセンス リーバー]]（該当n=39、84.6% / 非該当51.1%、差+33.5pt）；[[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3508|エッセンス リーバー]]（該当n=32、84.4% / 非該当51.4%、差+33.0pt）
- **ステータス傾向：** 物理防御（該当n=133、62.4% / 非該当50.9%、差+11.5pt）；体力（該当n=811、53.3% / 非該当45.3%、差+7.9pt）
- **理論仮説：** [[wiki/entities/items/item-2501|覇王のブラッドメイル]] + [[wiki/entities/items/item-3161|ショウジンの矛]]（n=3（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-2501|覇王のブラッドメイル]] + [[wiki/entities/items/item-3071|ブラック クリーバー]]（n=3（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 体力）

### MIDDLE（101試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3171|真紅のアイオニア ブーツ]] + [[wiki/entities/items/item-3508|エッセンス リーバー]]（該当n=32、50.0% / 非該当44.9%、差+5.1pt）
- **ステータス傾向：** 攻撃速度（該当n=53、58.5% / 非該当33.3%、差+25.2pt）
- **理論仮説：** [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3161|ショウジンの矛]]（n=11（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-3161|ショウジンの矛]]（n=4（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-901|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=1,188）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/diana|ダイアナ（Diana）]] — 対象側勝率70.3%（26/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/shyvana|シヴァーナ（Shyvana）]] — 対象側勝率70.3%（26/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率65.5%（36/55）、n=55（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/tristana|トリスターナ（Tristana）]] — 対象側勝率41.0%（16/39）、n=39（十分性の目安を満たす）。
  - [[wiki/entities/champions/varus|ヴァルス（Varus）]] — 対象側勝率43.1%（25/58）、n=58（十分性の目安を満たす）。
  - [[wiki/entities/champions/lucian|ルシアン（Lucian）]] — 対象側勝率44.2%（19/43）、n=43（十分性の目安を満たす）。

### MIDDLE（対象n=139）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/ezreal|エズリアル（Ezreal）]] — 対象側勝率37.5%（6/16）、サンプル不足（n=16、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/malzahar|マルザハール（Malzahar）]] — 対象側勝率39.5%（17/43）、n=43（十分性の目安を満たす）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合20,010件、[[reports/riot-ranked-match-analysis/run-20260915T103154Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### BOTTOM（対象1,400試合、全体勝率51.3%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：フリートフットワーク／冷静沈着・レジェンド: 血脈・切り崩し；副系天啓：ビスケットデリバリー・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 237/1,400 | 16.9% | 48.1% |
| 2 | 主系魔道：死神の残り火／ニンバスクローク・追い風・強まる嵐；副系天啓：なんでも屋・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5010)・UNKNOWN(5001) | 194/1,400 | 13.9% | 56.7% |
| 3 | 主系栄華：フリートフットワーク／冷静沈着・レジェンド: ヘイスト・最期の慈悲；副系魔道：強まる嵐・至高；シャードUNKNOWN(5007)・UNKNOWN(5008)・UNKNOWN(5011) | 115/1,400 | 8.2% | 40.9% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Smolder` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Smolder.png)
