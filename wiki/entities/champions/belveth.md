---
title: "ベル＝ヴェス"
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
  - role-fighter
  - data-dragon
champion_id: "Belveth"
champion_key: "200"
data_version: "16.18.1"
roles:
  - "Fighter"
resource_type: ""
image_path: "raw/assets/champions/Belveth.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Belveth.png"
---

# ベル＝ヴェス

![[raw/assets/champions/Belveth.png|128]]

## 基本情報

- **英字ID：** `Belveth`
- **キー：** `200`
- **称号：** ヴォイドの女帝
- **データversion：** `16.18.1`

## 紹介

ヴォイドが呑み込んだ街一つ分の物質から生み出された悪夢のような女帝ベル＝ヴェスは、ルーンテラの終焉そのもの…そして彼女が造り出す醜悪な現実の始まりだ。我がものとした地上世界の膨大な歴史、そして知識や記憶に駆り立てられ、彼女はますます増大する新たな経験や感情への渇望を満たそうと、行く手を阻むものすべてを貪り喰う。しかし、たった一つの世界で彼女の欲望が満たされるはずもない。ベル＝ヴェスは飢えた目をヴォイドの古き主たちに向ける…

## 分類

- **役割タグ：** `Fighter`
- **リソース種別：** 原典では空文字列

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 2 |
| `magic` | 7 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 105 |
| `mp` | 45 |
| `mpperlevel` | 0 |
| `movespeed` | 340 |
| `armor` | 28 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 0 |
| `attackspeed` | 0.67 |

## データ品質上の注意

- `partype` が空文字列である。リソース種別を原典から確定できない。

## アビリティ

- **パッシブ — 死のラベンダー：** 大型ミニオン、大型モンスター、チャンピオンからキルまたはアシストを獲得すると、攻撃速度のスタックを恒久的に獲得する。また、スキル使用後に一時的に攻撃速度が増加する。

- **Q — ヴォイドサージ：** 選択した方向にダッシュして、接触したすべての敵にダメージを与える。
- **W — 天と地：** 尻尾を地面に叩きつけ、敵にダメージを与えてノックアップさせ、スロウ効果を付与する。
- **E — ロイヤルストーム：** その場で動きを止めて自身の周囲に強烈な嵐を召喚し、最も体力の低い敵を切り裂いて、ライフスティールとダメージ軽減効果を獲得する。
- **R — 終わりなき晩餐：** ヴォイドコーラルの残片を吸収し、真の姿に変身して最大体力、射程距離、攻撃速度が増加する。ヴォイド出身のエピックモンスターが残したヴォイドコーラルの残片を吸収すると、ヴォイドレモラを召喚できるようになる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - キルまたはアシストで攻撃速度のスタックを恒久的に獲得する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 判定保留（分母不足）
- **対象試合：** 85試合、全体勝率 45.9%
- **時間帯別勝率：** 〜20分 38.9%（n=18）、20〜25分 47.4%（n=19）、25〜30分 52.4%（n=21）、30〜35分 46.7%（n=15）、35分〜 41.7%（n=12）
- **最高帯：** 25〜30分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-200|ベル＝ヴェスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（181試合）

- **実測ビルド候補：** ルインドキング ブレード + クラーケン スレイヤー（該当n=45、60.0% / 非該当36.0%、差+24.0pt）；テルミヌス + クラーケン スレイヤー（該当n=31、54.8% / 非該当39.3%、差+15.5pt）
- **ステータス傾向：** ライフスティール（該当n=74、50.0% / 非該当36.4%、差+13.6pt）；魔力（該当n=41、48.8% / 非該当40.0%、差+8.8pt）
- **理論仮説：** ルインドキング ブレード + ガンメタル ブーツ（n=1（15未満）；共通stats: 攻撃速度・ライフスティール／チャンピオン原典にも言及: 攻撃速度・ライフスティール）；ルインドキング ブレード + ストライドブレイカー（n=10（15未満）；共通stats: 攻撃力・攻撃速度／チャンピオン原典にも言及: 攻撃速度）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Belveth` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Belveth.png)
