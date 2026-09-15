---
title: "ジリアン"
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
  - role-support
  - role-mage
  - data-dragon
champion_id: "Zilean"
champion_key: "26"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Zilean.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zilean.png"
---

# ジリアン

![[raw/assets/champions/Zilean.png|128]]

## 基本情報

- **英字ID：** `Zilean`
- **キー：** `26`
- **称号：** 時の番人
- **データversion：** `16.18.1`

## 紹介

ジリアンはかつてはイカシアの強力なメイジだったが、故郷がヴォイドに破壊されるのを目撃して、時の流れに執着するようになった。壊滅的な喪失を嘆く暇すら与えられなかった彼は、未来のあらゆる可能性を予言しようと古代の時空魔法を使った。実質的に不死身となったジリアンは過去と現在と未来の狭間を漂うようになり、自身の周囲の時間の流れを捻じ曲げながら、時計を巻き戻して壊滅したイカシアを元に戻す方法を探し続けている。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 5 |
| `magic` | 8 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 574 |
| `hpperlevel` | 96 |
| `mp` | 452 |
| `mpperlevel` | 50 |
| `movespeed` | 335 |
| `armor` | 24 |
| `armorperlevel` | 5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 11.35 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 52 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.13 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — タイムインボトル：** 時間を経験値として溜めて、味方に付与できる。味方のレベルを上げるのに必要な経験値が溜まっている状態で相手を右クリックすると、経験値を与えることができる。同時に、与えた量と同じ経験値を自身も獲得する。

- **Q — タイムボム：** 指定地点に爆弾を投げ、近付いたユニットに付着させる(チャンピオン優先)。付着した爆弾は3秒後に爆発し、範囲ダメージを与える。爆発前にもう一つ「タイムボム」を仕掛けられると即時に爆発し、敵にスタン効果を与える。
- **W — リワインド：** ジリアンは近い未来の戦いに備え、通常スキルのクールダウンを短縮することができる。
- **E — タイムワープ：** 対象ユニット周辺の時間軸を短時間ねじ曲げ、対象が敵の場合はスロウを与え、味方の場合は移動速度を増加させる。
- **R — クロノシフト：** 対象の味方チャンピオンに砂時計の印を付与し、体力がゼロになった瞬間、過去へ遡らせて復活させる。

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

- **観測分類：** 判定保留（分母不足）
- **対象試合：** 63試合、全体勝率 46.0%
- **時間帯別勝率：** 〜20分 50.0%（n=12）、20〜25分 12.5%（n=8）、25〜30分 44.4%（n=9）、30〜35分 28.6%（n=14）、35分〜 70.0%（n=20）
- **最高帯：** 35分〜（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-26|ジリアンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（173試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2065|シュレリアの戦歌]] + [[wiki/entities/items/item-2524|バンドルパイプ]]（該当n=47、53.2% / 非該当51.6%、差+1.6pt）
- **ステータス傾向：** 体力（該当n=116、55.2% / 非該当45.6%、差+9.6pt）；物理防御（該当n=94、53.2% / 非該当50.6%、差+2.6pt）
- **理論仮説：** [[wiki/entities/items/item-2530|旋律のダイアデム]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（未観測；共通stats: 体力・マナ／チャンピオン原典にも言及: 体力・マナ）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=8（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-26|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=314）

- **高勝率コンボ候補：** [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率72.5%（29/40）、n=40（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率47.4%（9/19）、サンプル不足（n=19、十分性の目安30未満）。

### MIDDLE（対象n=36）

- **高勝率コンボ候補：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Zilean` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zilean.png)
