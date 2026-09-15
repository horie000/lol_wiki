---
title: "グラガス"
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
  - role-mage
  - data-dragon
champion_id: "Gragas"
champion_key: "79"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Gragas.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gragas.png"
---

# グラガス

![[raw/assets/champions/Gragas.png|128]]

## 基本情報

- **英字ID：** `Gragas`
- **キー：** `79`
- **称号：** 騒乱の飲んだくれ
- **データversion：** `16.18.1`

## 紹介

陽気で立派な巨体を持つ、荒くれた風貌のグラガスは、常に人々の気持ちを明るくさせる新たな方法を探している醸造家だ。どこの出身なのかは不明だが、彼は完璧な調合を見つけるため、フレヨルドの誰も足を踏み入れない荒野で貴重な醸造材料を探している。向こう見ずで頑固な性格で、彼が始めた喧嘩の話は広く知られ、最後はいつも朝までどんちゃん騒ぎになって建物のあちこちが破壊されることになる。グラガスの現れるところ、必ずお祭り騒ぎと破壊が巻き起こる──いつもこの順番だ。

## 分類

- **役割タグ：** `Fighter`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 7 |
| `magic` | 6 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 115 |
| `mp` | 400 |
| `mpperlevel` | 47 |
| `movespeed` | 330 |
| `armor` | 38 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.05 |
| `attackspeed` | 0.675 |

## アビリティ

- **パッシブ — ハッピーアワー：** 一定時間ごとにスキル使用時に体力を回復する。

- **Q — タル転がし：** 指定地点にタルを転がし、4秒後に爆発させる。タルは自分で起爆させることもできる。時間経過とともに爆発の威力が増加する。爆風を浴びた敵はスロウ状態になる。
- **W — 飲みすぎ注意：** 最新の醸造酒を1秒間試飲し、飲み終えると騒々しく好戦的になる。効果時間中は受けるダメージが軽減され、次の通常攻撃で付近のすべての敵に魔法ダメージを与える。
- **E — ボディスラム：** 指定方向へ突進し、最初に衝突した敵ユニットとその周囲の敵にダメージを与え、ノックバックとスタンを付与する。
- **R — ワシの奢りじゃ！：** 指定地点にタルを放り投げる。着弾したタルは大爆発し、爆発範囲内の敵ユニットにダメージを与えてノックバックさせる。

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
- **対象試合：** 65試合、全体勝率 41.5%
- **時間帯別勝率：** 〜20分 46.2%（n=13）、20〜25分 40.0%（n=10）、25〜30分 38.5%（n=13）、30〜35分 42.9%（n=14）、35分〜 40.0%（n=15）
- **最高帯：** 〜20分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-79|グラガスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（125試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** 冬の訪れ + ロッド オブ エイジス（n=4（15未満）；共通stats: 体力・マナ／チャンピオン原典にも言及: 体力・マナ）；冬の訪れ + フィンブルウィンター（未観測；共通stats: 体力・マナ／チャンピオン原典にも言及: 体力・マナ）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Gragas` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gragas.png)
