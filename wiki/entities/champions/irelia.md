---
title: "イレリア"
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
champion_id: "Irelia"
champion_key: "39"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Irelia.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Irelia.png"
---

# イレリア

![[raw/assets/champions/Irelia.png|128]]

## 基本情報

- **英字ID：** `Irelia`
- **キー：** `39`
- **称号：** 飛刃の舞い手
- **データversion：** `16.18.1`

## 紹介

ノクサスのアイオニア占領は数多くの英雄を生み出すことになったが、ナヴォリ出身の若きイレリアほど傑出した才能は存在しない。地域に伝わる古代舞踊の訓練を通じて戦いの技術を身に付けた彼女は、優雅かつ繊細な動きで複数の刃を宙に浮かべることができる。戦士としての実力を評価され反乱軍の指導者となった彼女は、今でも故郷を守るためにすべてを捧げて戦い続けている。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 4 |
| `magic` | 5 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 115 |
| `mp` | 350 |
| `mpperlevel` | 50 |
| `movespeed` | 335 |
| `armor` | 36 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 200 |
| `hpregen` | 3.5 |
| `hpregenperlevel` | 0.85 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.656 |

## アビリティ

- **パッシブ — アイオニアの熱情：** 敵にスキルを当てるとスタックを獲得する。スタック数に応じて増加攻撃速度を獲得し、最大スタックになると通常攻撃時に追加ダメージを付与する。

- **Q — 瞬刃：** 前方にダッシュして対象を攻撃し、自身の体力を回復する。これによって対象をキルするか、対象がマークされていた場合は、「瞬刃」のクールダウンが解消される。
- **W — 不屈の舞：** チャージ攻撃を行う。チャージ時間が長いほど、与えるダメージが増加する。チャージ中は被物理ダメージが減少する。
- **E — 無欠の連舞：** 2枚の刃を飛ばす。これらの刃は互いの方向に飛んで収束する。2枚の刃に挟まれた敵はダメージとスタン効果を受けてマークされる。
- **R — 先陣の刃：** 大量の刃を飛ばす。刃は敵チャンピオンに当たると放射状に広がり、当たった敵はダメージを受けてマークされる。その後、刃が壁を形成し、この壁を越えた敵はダメージとスロウ効果を受ける。

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
- **対象試合：** 435試合、全体勝率 51.5%
- **時間帯別勝率：** 〜20分 50.0%（n=68）、20〜25分 53.6%（n=69）、25〜30分 54.0%（n=113）、30〜35分 47.1%（n=87）、35分〜 52.0%（n=98）
- **最高帯：** 25〜30分（判定差 6.9ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-39|イレリアの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（427試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3091|ウィッツ エンド]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（該当n=54、68.5% / 非該当48.8%、差+19.7pt）；[[wiki/entities/items/item-3091|ウィッツ エンド]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（該当n=54、68.5% / 非該当48.8%、差+19.7pt）
- **ステータス傾向：** 物理防御（該当n=279、54.1% / 非該当45.9%、差+8.2pt）；魔法防御（該当n=321、53.3% / 非該当45.3%、差+8.0pt）
- **理論仮説：** [[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-3153|ルインドキング ブレード]] + [[wiki/entities/items/item-3302|テルミヌス]]（n=3（15未満）；共通stats: 攻撃力・攻撃速度／チャンピオン原典にも言及: 攻撃力・攻撃速度）

### TOP（389試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3153|ルインドキング ブレード]] + [[wiki/entities/items/item-3181|ハルブレイカー]]（該当n=204、53.4% / 非該当46.5%、差+6.9pt）；[[wiki/entities/items/item-3091|ウィッツ エンド]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]]（該当n=138、53.6% / 非該当48.2%、差+5.4pt）
- **ステータス傾向：** 物理防御（該当n=302、51.7% / 非該当44.8%、差+6.8pt）；体力（該当n=336、50.9% / 非該当45.3%、差+5.6pt）
- **理論仮説：** [[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-3181|ハルブレイカー]] + [[wiki/entities/items/item-6609|ケミパンク チェーンソード]]（n=5（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-39|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=538）

- **高勝率コンボ候補：** [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率63.5%（33/52）、n=52（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/garen|ガレン（Garen）]] — 対象側勝率40.0%（12/30）、n=30（十分性の目安を満たす）。

### MIDDLE（対象n=535）

- **高勝率コンボ候補：** [[wiki/entities/champions/yunara|ユナラ（Yunara）]] — 対象側勝率67.7%（21/31）、n=31（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率45.0%（18/40）、n=40（十分性の目安を満たす）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Irelia` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Irelia.png)
