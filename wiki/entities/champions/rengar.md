---
title: "レンガー"
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
  - role-assassin
  - role-fighter
  - data-dragon
champion_id: "Rengar"
champion_key: "107"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Fighter"
resource_type: "フェロシティ"
image_path: "raw/assets/champions/Rengar.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rengar.png"
---

# レンガー

![[raw/assets/champions/Rengar.png|128]]

## 基本情報

- **英字ID：** `Rengar`
- **キー：** `107`
- **称号：** 孤高のハンター
- **データversion：** `16.18.1`

## 紹介

獰猛にして卓越…ヴァスタヤのハンターであるレンガーは、危険な生物を追跡して殺す、そのスリルを味わうために生きている。彼は強く恐ろしい猛獣たち、そしてかつて彼自身の片目を奪ったヴォイドの怪物カ＝ジックスの痕跡を求めて、世界中をさまよい歩く。レンガーは食事や名誉のために狩りをすることはない。狩猟は彼にとって美であり、その美しさのためにこそ、彼は獲物を追跡し引き裂くのだ。

## 分類

- **役割タグ：** `Assassin`、`Fighter`
- **リソース種別：** フェロシティ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 4 |
| `magic` | 2 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 590 |
| `hpperlevel` | 104 |
| `mp` | 4 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 34 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.667 |

## アビリティ

- **パッシブ — 見えざる襲撃者：** 茂みの中にいると、通常攻撃で対象に向かって飛びつく。 スキルを使用するたびにフェロシティを獲得する。フェロシティが最大になると次に使用するスキルが強化される。 敵チャンピオンを倒すと「骨牙の首飾り」のトロフィーを獲得し、増加攻撃力を獲得する。

- **Q — 逆上：** 次の通常攻撃が追加ダメージを与える。 フェロシティボーナス: 与えるダメージと攻撃速度が増加。
- **W — 狩りの雄叫び：** レンガーが雄叫びをあげて周囲の敵にダメージを与え、直前に受けたダメージの一部を回復する。 フェロシティボーナス: 自身が受けている行動妨害効果を除去する。
- **E — 鉄球の投げ縄：** 投げ縄を投げ、最初に命中した対象に短時間スロウ効果を付与する。 フェロシティボーナス: 対象にスネア効果を付与する。
- **R — 狩猟本能：** 「狩猟本能」の覚醒によってレンガーがカモフラージュ状態となり、広範囲にわたって敵チャンピオンの位置を把握する。「狩猟本能」の覚醒中は移動速度が増加し、茂みの中にいなくても発見した敵に向かってジャンプ攻撃が可能になり、対象の物理防御を低下させる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - チャンピオン撃破時のトロフィーで増加攻撃力を獲得する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 判定保留（分母不足）
- **対象試合：** 46試合、全体勝率 52.2%
- **時間帯別勝率：** 〜20分 46.2%（n=13）、20〜25分 66.7%（n=9）、25〜30分 42.9%（n=7）、30〜35分 40.0%（n=5）、35分〜 58.3%（n=12）
- **最高帯：** 20〜25分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-107|レンガーの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（111試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 体力（該当n=35、57.1% / 非該当55.3%、差+1.9pt）；クリティカル率（該当n=62、56.5% / 非該当55.1%、差+1.3pt）
- **理論仮説：** [[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-6333|デス ダンス]]（未観測；共通stats: 物理防御・攻撃力／チャンピオン原典にも言及: 物理防御・攻撃力）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-6676|コレクター]]（n=4（15未満）；共通stats: 攻撃力・クリティカル率／チャンピオン原典にも言及: 攻撃力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-107|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=209）

- **高勝率コンボ候補：** [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率70.6%（12/17）、サンプル不足（n=17、十分性の目安30未満）。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

### TOP（対象n=20）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Rengar` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rengar.png)
