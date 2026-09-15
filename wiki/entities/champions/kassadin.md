---
title: "カサディン"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
tags:
  - champion
  - role-assassin
  - role-mage
  - data-dragon
champion_id: "Kassadin"
champion_key: "38"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Kassadin.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kassadin.png"
---

# カサディン

![[raw/assets/champions/Kassadin.png|128]]

## 基本情報

- **英字ID：** `Kassadin`
- **キー：** `38`
- **称号：** ヴォイドを歩む者
- **データversion：** `16.18.1`

## 紹介

世界の最も昏き闇を炎で切り裂くカサディンは、自身にあまり時間が残されていないことを理解している。案内人として、そして冒険家としてシュリーマ全土を旅してまわった彼はかつて、南部の平和な部族に囲まれて家族を育む人生を選んだ──だがヴォイドが、彼の村を飲み込んだ。彼は復讐を誓い、先で待ち受ける困難に立ち向かうため、いくつもの古代の秘宝と禁じられた技術をかき集めた。そしてついに、荒涼としたイカシアの地へと出発したのだ。“預言者”を僭称するマルザハールを見つけ出すためであれば、彼はいかなる悪鬼のごときヴォイドの...

## 分類

- **役割タグ：** `Assassin`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 5 |
| `magic` | 8 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 646 |
| `hpperlevel` | 113 |
| `mp` | 400 |
| `mpperlevel` | 87 |
| `movespeed` | 335 |
| `armor` | 21 |
| `armorperlevel` | 4 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 150 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.7 |
| `attackspeed` | 0.64 |

## アビリティ

- **パッシブ — ヴォイドストーン：** 受ける魔法ダメージが減少し、ユニットをすり抜けられるようになる。

- **Q — ヴォイドスフィア：** 指定した対象にヴォイドエネルギーの球体を発射してダメージを与え、詠唱を妨害する。 さらに余ったエネルギーがカサディンを包み込み、短時間魔法ダメージを防ぐシールドを発生させる。
- **W — ネザーブレード：** 自動効果: 通常攻撃に追加魔法ダメージが付与される。 発動効果: 次の通常攻撃に強烈な追加魔法ダメージが付与され、敵に命中するとマナが回復する。
- **E — ヴォイドパルス：** 自身の付近でスキルが使用されると、そのエネルギーを「ヴォイドパルス」にスタックする。スタックが溜まると同時に「ヴォイドパルス」が発動可能になり、使用すると扇状の範囲内の敵にダメージを与え、スロウ効果を付与する。
- **R — リフトウォーク：** 近くの地点に瞬間移動し、付近の敵ユニットにダメージを与える。連続して使うとマナコストが増加するが、同時に与えるダメージも増えていく。

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
- **対象試合：** 19試合、全体勝率 57.9%
- **時間帯別勝率：** 〜20分 50.0%（n=2）、20〜25分 50.0%（n=4）、25〜30分 50.0%（n=6）、30〜35分 75.0%（n=4）、35分〜 66.7%（n=3）
- **最高帯：** 30〜35分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-38|カサディンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（66試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** フィンブルウィンター + ロッド オブ エイジス（n=2（15未満）；共通stats: 体力・マナ／チャンピオン原典にも言及: 体力・マナ）；冬の訪れ + ロッド オブ エイジス（n=1（15未満）；共通stats: 体力・マナ／チャンピオン原典にも言及: 体力・マナ）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kassadin` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kassadin.png)
