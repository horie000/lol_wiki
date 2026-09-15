---
title: "モルデカイザー"
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
tags:
  - champion
  - role-fighter
  - role-mage
  - data-dragon
champion_id: "Mordekaiser"
champion_key: "82"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Mage"
resource_type: "シールド"
image_path: "raw/assets/champions/Mordekaiser.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Mordekaiser.png"
---

# モルデカイザー

![[raw/assets/champions/Mordekaiser.png|128]]

## 基本情報

- **英字ID：** `Mordekaiser`
- **キー：** `82`
- **称号：** 鋼の魂奪者
- **データversion：** `16.18.1`

## 紹介

二度殺され、三度生まれたモルデカイザーは死霊術によって人の魂を拘束し、彼らを永遠の奴隷に変えてしまう、古の時代の残忍な武闘王である。彼の過去の覇業を覚えている者や、真の力を知る者はほとんど残っていないが、モルデカイザーを知るわずかな者たちは、彼が再び現れて生ける者も死せる者も支配してしまう日が来ることを恐れている。

## 分類

- **役割タグ：** `Fighter`、`Mage`
- **リソース種別：** シールド

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 6 |
| `magic` | 7 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 645 |
| `hpperlevel` | 104 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 335 |
| `armor` | 37 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 無窮の闇：** チャンピオンまたはモンスターに通常攻撃かスキルを3回命中させると、ダメージを与える強力なオーラを発生させ、移動速度が増加する。

- **Q — 滅魂の一撃：** 地面にメイスを叩きつけ、命中したすべての敵にダメージを与える。対象が1体のみだった場合はダメージが上昇する。
- **W — 不滅の鎧：** 与えたダメージや受けたダメージを蓄え、シールドを作り出す。シールドを消費して体力を回復することも可能。
- **E — 死の呪縛：** 範囲内にいるすべての敵を引き寄せる。
- **R — 死の国：** 獲物を別の次元へと引きずり込み、ステータスの一部を奪い取る。対象を倒した場合は、その対象が復活するまで奪ったステータスが維持される。

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
- **対象試合：** 919試合、全体勝率 51.7%
- **時間帯別勝率：** 〜20分 53.8%（n=143）、20〜25分 48.9%（n=141）、25〜30分 47.6%（n=212）、30〜35分 51.2%（n=211）、35分〜 56.6%（n=212）
- **最高帯：** 35分〜（判定差 9.0ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-82|モルデカイザーの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（1,450試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3174|装甲強化の進撃]] + [[wiki/entities/items/item-4633|リフトメーカー]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=30、76.7% / 非該当51.7%、差+25.0pt）；[[wiki/entities/items/item-3174|装甲強化の進撃]] + [[wiki/entities/items/item-4633|リフトメーカー]]（該当n=55、74.5% / 非該当51.3%、差+23.2pt）
- **ステータス傾向：** 攻撃速度（該当n=212、57.5% / 非該当51.3%、差+6.3pt）；攻撃力（該当n=209、56.9% / 非該当51.4%、差+5.5pt）
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）

### JUNGLE（142試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-4633|リフトメーカー]]（該当n=48、54.2% / 非該当45.7%、差+8.4pt）；[[wiki/entities/items/item-3075|ソーンメイル]] + [[wiki/entities/items/item-3116|リーライ クリスタル セプター]]（該当n=30、53.3% / 非該当47.3%、差+6.0pt）
- **ステータス傾向：** 魔法防御（該当n=73、60.3% / 非該当36.2%、差+24.0pt）；攻撃速度（該当n=47、63.8% / 非該当41.1%、差+22.8pt）
- **理論仮説：** [[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3161|ショウジンの矛]]（n=2（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-82|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=1,703）

- **高勝率コンボ候補：** [[wiki/entities/champions/tahm-kench|タム・ケンチ（TahmKench）]] — 対象側勝率76.7%（23/30）、n=30（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率41.2%（40/97）、n=97（十分性の目安を満たす）。

### JUNGLE（対象n=167）

- **高勝率コンボ候補：** [[wiki/entities/champions/ambessa|アンベッサ（Ambessa）]] — 対象側勝率50.0%（9/18）、サンプル不足（n=18、十分性の目安30未満）。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Mordekaiser` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Mordekaiser.png)
