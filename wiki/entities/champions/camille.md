---
title: "カミール"
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
  - role-assassin
  - data-dragon
champion_id: "Camille"
champion_key: "164"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Camille.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Camille.png"
---

# カミール

![[raw/assets/champions/Camille.png|128]]

## 基本情報

- **英字ID：** `Camille`
- **キー：** `164`
- **称号：** スチールシャドウ
- **データversion：** `16.18.1`

## 紹介

フェロス一族のエレガントな主席スパイであるカミールは、法の及ばぬ領域で活動するために機械の体になった。彼女の使命はピルトーヴァーというシステムと、内包するゾウンがスムーズに動作し続けるよう保つことにある。正確無比で適応力に富む彼女は、雑な手際は恥ずべき汚点とみなしている。その身にまとう刃にも劣らない鋭い意志で、己の能力を極めるためにヘクステック技術による身体拡張を繰り返すカミールを、もはや女性ではなく機械なのではないかと考える者も多い。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 6 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 99 |
| `mp` | 375 |
| `mpperlevel` | 52 |
| `movespeed` | 340 |
| `armor` | 35 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 8.15 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — アダプティブディフェンス：** 敵チャンピオンに通常攻撃すると、その敵の主なダメージの種類(物理または魔法)に応じて、少しの間だけ自身の最大体力の一定割合にあたるシールドを獲得する。

- **Q — プレシジョンプロトコル：** 次の通常攻撃が追加ダメージを与え、移動速度が増加する。このスキルは少しの間だけ再発動することが可能で、再発動までの間に一定の間隔を置くと追加ダメージが大きく増加する。
- **W — タクティカルスイープ：** 少し間を置いてから扇状の範囲に攻撃を行ってダメージを与える。攻撃範囲の外側半分にいた敵ユニットにはスロウ効果と追加ダメージを与え、また同時に自身を回復する。
- **E — フックショット：** 壁に飛びついてから跳躍して、着地時に敵チャンピオンをノックアップする。
- **R — ヘクステック・アルティメイタム：** 指定した敵チャンピオンに向かってダッシュして、対象を一定エリア内に閉じ込める。さらに通常攻撃がその対象に追加魔法ダメージを与えるようになる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中16位（上位15%）。体力650、物理防御35、攻撃力68、移動速度340。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 終盤寄り
- **対象試合：** 159試合、全体勝率 48.4%
- **時間帯別勝率：** 〜20分 40.0%（n=25）、20〜25分 45.8%（n=24）、25〜30分 51.4%（n=35）、30〜35分 46.2%（n=39）、35分〜 55.6%（n=36）
- **最高帯：** 35分〜（判定差 15.6ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 15.6%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-164|カミールの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（157試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3053|ステラックの篭手]] + [[wiki/entities/items/item-3074|ラヴァナス ハイドラ]]（該当n=30、63.3% / 非該当43.3%、差+20.0pt）；[[wiki/entities/items/item-3074|ラヴァナス ハイドラ]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（該当n=104、53.8% / 非該当34.0%、差+19.9pt）
- **ステータス傾向：** ライフスティール（該当n=116、53.4% / 非該当29.3%、差+24.2pt）；物理防御（該当n=109、51.4% / 非該当37.5%、差+13.9pt）
- **理論仮説：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（n=8（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-6333|デス ダンス]]（n=2（15未満）；共通stats: 物理防御・攻撃力／チャンピオン原典にも言及: 物理防御・攻撃力）

### UTILITY（143試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 魔法防御（該当n=35、51.4% / 非該当48.1%、差+3.3pt）
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=1（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）；[[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（n=2（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-164|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=299）

- **高勝率コンボ候補：** [[wiki/entities/champions/yunara|ユナラ（Yunara）]] — 対象側勝率64.7%（11/17）、サンプル不足（n=17、十分性の目安30未満）。
- **カウンターピック候補：** [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率55.6%（10/18）、サンプル不足（n=18、十分性の目安30未満）。

### UTILITY（対象n=185）

- **高勝率コンボ候補：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **カウンターピック候補：** [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率35.3%（6/17）、サンプル不足（n=17、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Camille` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Camille.png)
