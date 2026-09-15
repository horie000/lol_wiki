---
title: "エコー"
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
champion_id: "Ekko"
champion_key: "245"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Ekko.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ekko.png"
---

# エコー

![[raw/assets/champions/Ekko.png|128]]

## 基本情報

- **英字ID：** `Ekko`
- **キー：** `245`
- **称号：** 砕けた時を渡る少年
- **データversion：** `16.18.1`

## 紹介

ゾウンの荒っぽい裏街で育った天才少年エコーは、どんな逆境も自分の有利になるよう時を捻じ曲げる。自ら発明した「ゼロ・ドライブ」を使い、枝分かれしたあり得る未来を見比べて最適な瞬間を作り出す。彼はこの自由を謳歌しているが、ひとたび仲間に危機が迫れば、彼らを守るためにどんなことでもする。真実を知らない者の目には、エコーはおよそ不可能な離れ業をいつでも一発で成し遂げているように見えるだろう。

## 分類

- **役割タグ：** `Assassin`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 3 |
| `magic` | 7 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 655 |
| `hpperlevel` | 99 |
| `mp` | 280 |
| `mpperlevel` | 70 |
| `movespeed` | 340 |
| `armor` | 32 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.3 |
| `attackspeed` | 0.688 |

## アビリティ

- **パッシブ — ゼロ・ドライブ：** 同一の敵ユニットに通常攻撃または攻撃スキルが3回命中するたび、追加魔法ダメージを与える。対象がチャンピオンの場合、一時的に移動速度が増加する。

- **Q — タイムワインダー：** 次元を捻じ曲げる一次元的グレネードを投げ、命中した敵ユニットにダメージとスロウ効果を与える。 数秒後、グレネードは巻き戻されて自身の元へ戻ってくる。グレネードは戻る時もダメージ判定を持ち、触れた敵ユニットにダメージを与える。
- **W — パラレルトラップ：** 残り体力の少ない敵に対する通常攻撃が追加魔法ダメージを与える。「パラレルトラップ」を発動すると時間軸を分岐させて数秒後に次元歪曲空間を出現させ、効果範囲内にいる敵にスロウ効果を与える。この次元歪曲空間へエコーが進入するとシールドを獲得し、範囲内の敵ユニットの時間を停止させてスタン効果を与える。
- **E — フェイズダイブ：** 指定方向へ短い距離ダッシュし「ゼロ・ドライブ」にエネルギーをチャージする。次の通常攻撃の射程が延び、時空を歪曲させて対象のもとへ瞬間移動すると同時に追加ダメージを与える。
- **R — クロノブレイク：** エコーが時間軸を砕いて敵から対象指定されなくなり、時を巻き戻して数秒前に自身がいた場所へタイムワープする。数秒前の地点に戻ると、その間に受けたダメージの一部を回復する。到着地点付近にいる敵はエコー出現による時空共振により大ダメージを受ける。

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

- **観測分類：** 中盤寄り
- **対象試合：** 188試合、全体勝率 51.6%
- **時間帯別勝率：** 〜20分 46.4%（n=28）、20〜25分 48.6%（n=35）、25〜30分 58.7%（n=46）、30〜35分 54.5%（n=33）、35分〜 47.8%（n=46）
- **最高帯：** 25〜30分（判定差 10.9ポイント）
- **判定根拠：** 中間帯が最高、端点との差 10.9%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-245|エコーの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（258試合）

- **実測ビルド候補：** ラバドン デスキャップ + リッチ ベイン（該当n=30、63.3% / 非該当46.9%、差+16.4pt）；リッチ ベイン + ヘクステック ロケットベルト（該当n=45、60.0% / 非該当46.5%、差+13.5pt）
- **ステータス傾向：** 体力（該当n=220、50.5% / 非該当39.5%、差+11.0pt）；攻撃速度（該当n=173、49.1% / 非該当48.2%、差+0.9pt）
- **理論仮説：** メジャイ ソウルスティーラー + ヘクステック ロケットベルト（n=10（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；黄昏と暁 + ヘクステック ロケットベルト（n=9（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

### MIDDLE（164試合）

- **実測ビルド候補：** リッチ ベイン + 連呪使いのブーツ（該当n=33、66.7% / 非該当49.6%、差+17.0pt）；黄昏と暁 + 連呪使いのブーツ（該当n=54、57.4% / 非該当50.9%、差+6.5pt）
- **ステータス傾向：** 攻撃速度（該当n=97、56.7% / 非該当47.8%、差+8.9pt）
- **理論仮説：** 黄昏と暁 + メジャイ ソウルスティーラー（n=6（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；黄昏と暁 + ヘクステック ロケットベルト（n=4（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Ekko` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ekko.png)
