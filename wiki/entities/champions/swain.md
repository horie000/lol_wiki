---
title: "スウェイン"
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
tags:
  - champion
  - role-mage
  - role-support
  - data-dragon
champion_id: "Swain"
champion_key: "50"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Swain.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Swain.png"
---

# スウェイン

![[raw/assets/champions/Swain.png|128]]

## 基本情報

- **英字ID：** `Swain`
- **キー：** `50`
- **称号：** ノクサス帝国元帥
- **データversion：** `16.18.1`

## 紹介

ジェリコ・スウェインは、力のみを正義とする拡大主義国家ノクサスを率いる、先見の明を持つ指導者だ。アイオニアとの戦争で失権して重傷を負い、左腕を失った彼はしかし、非情なまでの決意によって帝国の支配権を握った…その新たな悪魔の腕で。スウェインは今、自ら前線に立って指揮を執り、自らにしか見えぬ闇──影のごとき鴉たちが周囲の死体から集める魂に垣間見える闇に立ち向かうべく、進軍を続けている。多くの秘密と犠牲が彼を中心に渦巻くが、最大の秘密は、真の敵は内にいる、ということだろう。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 6 |
| `magic` | 9 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 595 |
| `hpperlevel` | 99 |
| `mp` | 400 |
| `mpperlevel` | 29 |
| `movespeed` | 330 |
| `armor` | 25 |
| `armorperlevel` | 4.7 |
| `spellblock` | 31 |
| `spellblockperlevel` | 1.55 |
| `attackrange` | 525 |
| `hpregen` | 3 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 10 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.11 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 恐襲の魔鴉：** 鴉たちが「魂のかけら」を回収し、スウェインの体力を回復して、最大体力を恒久的に上昇させる。

- **Q — 死の手：** この世ならざる力の稲妻を複数放ち、敵を貫通する。当たった稲妻の数に応じて与えるダメージが増加する。
- **W — 帝国の眼：** 指定地点に悪魔の眼を開いて視界を得て、敵ユニットにダメージとスロウ効果を与える。その後の爆発が当たった敵チャンピオンは可視状態になり、「魂のかけら」を獲得する。
- **E — 束縛の爪：** 悪魔のエネルギー波を前方に発射する。その後エネルギー波を呼び戻し、命中した敵にスネア効果を与える。スネア効果を与えたすべてのチャンピオンは、任意で引き寄せることができる。「魔帝戴冠」を発動中は、このスキルのクールダウンが短縮される。
- **R — 魔帝戴冠：** 悪魔に変身して周囲の敵チャンピオン、ミニオン、また中立モンスターから体力を吸収する。その後、「悪魔の紅炎」が発動可能になり、周囲の敵ユニットに魂の炎の爆発を浴びせて、スロウ効果を与える。この形態は敵チャンピオンから体力を吸収している間は無限に持続する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 「魂のかけら」で最大体力を恒久的に上昇させる。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 明瞭な傾向なし
- **対象試合：** 342試合、全体勝率 50.0%
- **時間帯別勝率：** 〜20分 46.7%（n=60）、20〜25分 50.0%（n=56）、25〜30分 54.3%（n=81）、30〜35分 47.4%（n=76）、35分〜 50.7%（n=69）
- **最高帯：** 25〜30分（判定差 7.7ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-50|スウェインの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（381試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-3118|マリグナンス]]（該当n=48、56.2% / 非該当46.5%、差+9.7pt）；[[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=81、49.4% / 非該当47.3%、差+2.0pt）
- **ステータス傾向：** 物理防御（該当n=207、54.1% / 非該当40.2%、差+13.9pt）；魔法防御（該当n=104、52.9% / 非該当45.8%、差+7.0pt）
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）

### BOTTOM（174試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-3157|ゾーニャの砂時計]]（該当n=48、66.7% / 非該当52.4%、差+14.3pt）；[[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-3118|マリグナンス]]（該当n=86、62.8% / 非該当50.0%、差+12.8pt）
- **ステータス傾向：** 物理防御（該当n=117、58.1% / 非該当52.6%、差+5.5pt）
- **理論仮説：** [[wiki/entities/items/item-3121|フィンブルウィンター]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（n=1（15未満）；共通stats: 体力・マナ／チャンピオン原典にも言及: 体力・マナ）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-50|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=507）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/kaisa|カイ＝サ（Kaisa）]] — 対象側勝率50.0%（16/32）、n=32（十分性の目安を満たす）。
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率47.7%（21/44）、n=44（十分性の目安を満たす）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率46.0%（23/50）、n=50（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率40.9%（18/44）、n=44（十分性の目安を満たす）。
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率51.6%（16/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率55.7%（39/70）、n=70（十分性の目安を満たす）。

### BOTTOM（対象n=274）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/yorick|ヨリック（Yorick）]] — 対象側勝率50.0%（18/36）、n=36（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率41.2%（7/17）、サンプル不足（n=17、十分性の目安30未満）。
  - [[wiki/entities/champions/varus|ヴァルス（Varus）]] — 対象側勝率46.7%（7/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率57.9%（11/19）、サンプル不足（n=19、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-16生成、キュー420、ユニーク試合10,000件、[[reports/riot-ranked-match-analysis/run-20260916T081004Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### UTILITY（対象274試合、全体勝率43.8%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：征服者／冷静沈着・レジェンド: ヘイスト・背水の陣；副系不滅：心身調整・超成長；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 77/274 | 28.1% | 41.6% |
| 2 | 主系覇道：電撃／追い打ち・グリスリー メメント・至極の賞金首狩り；副系栄華：最期の慈悲・冷静沈着；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 41/274 | 15.0% | 56.1% |
| 3 | 主系覇道：電撃／追い打ち・グリスリー メメント・貪欲な賞金首狩り；副系不滅：ボーンアーマー・気迫；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 30/274 | 10.9% | 30.0% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Swain` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Swain.png)
