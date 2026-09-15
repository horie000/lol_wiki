---
title: "ポッピー"
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
  - role-tank
  - role-fighter
  - data-dragon
champion_id: "Poppy"
champion_key: "78"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Poppy.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Poppy.png"
---

# ポッピー

![[raw/assets/champions/Poppy.png|128]]

## 基本情報

- **英字ID：** `Poppy`
- **キー：** `78`
- **称号：** 大鎚の守護者
- **データversion：** `16.18.1`

## 紹介

ルーンテラの地に勇敢なチャンピオンは数多いものの、ポッピーほど粘り強い者はそうはいない。自分の身長の二倍ほどもある伝説のハンマー、オーロンを携えた不屈のヨードルは、もう何年もの間、彼女のハンマーの「真の持ち主」であるといわれている伝説の戦士「デマーシアの勇者」を密かに探し続けているのだ。真の持ち主が見つかるまで、彼女は使命感を持って戦闘に挑み、ハンマーを振り回して王国の敵を押し返している。

## 分類

- **役割タグ：** `Tank`、`Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 7 |
| `magic` | 2 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 110 |
| `mp` | 300 |
| `mpperlevel` | 45 |
| `movespeed` | 345 |
| `armor` | 35 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 56 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 鋼鉄の大使：** 対象にバックラーを投げつける。対象に命中し跳ね返って落ちたバックラーを拾うことで、一時的にシールドを得る。

- **Q — ハンマーショック：** ハンマーを振り下ろしてダメージを与え、敵をスロウ状態にした後時間を置いて爆発する効果範囲を作り出す。
- **W — ステッドファスト：** 自動効果で物理防御と魔法防御が増加する。このボーナスは体力が低下するとさらに増加する。発動すると移動速度が増加し、自身の周囲にいる敵のダッシュ行動を阻止する。ダッシュを中断させられた敵はスロウ状態および釘付け状態になる。
- **E — ヒロイックチャージ：** 対象に向かってダッシュし、突き飛ばす。対象が壁にぶつかった場合、スタン状態になる。
- **R — 守護者の鉄鎚：** ハンマーに力を溜め、敵を遥か彼方に殴り飛ばす。

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

- **観測分類：** 序盤寄り
- **対象試合：** 179試合、全体勝率 50.8%
- **時間帯別勝率：** 〜20分 65.6%（n=32）、20〜25分 42.9%（n=21）、25〜30分 51.0%（n=51）、30〜35分 43.2%（n=44）、35分〜 51.6%（n=31）
- **最高帯：** 〜20分（判定差 14.0ポイント）
- **判定根拠：** 〜20分が最高、長時間帯との差 14.0%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-78|ポッピーの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（274試合）

- **実測ビルド候補：** ソラリのロケット + デッド マン プレート（該当n=68、58.8% / 非該当47.1%、差+11.7pt）；ソーンメイル + デッド マン プレート（該当n=37、54.1% / 非該当49.4%、差+4.7pt）
- **ステータス傾向：** 魔法防御（該当n=159、50.9% / 非該当48.7%、差+2.2pt）
- **理論仮説：** バンドルパイプ + ソラリのロケット（n=9（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力・魔法防御）；ジーク コンバージェンス + ソラリのロケット（n=1（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力・魔法防御）

### TOP（65試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** サンファイア イージス + ソーンメイル（n=7（15未満）；共通stats: 物理防御・体力／チャンピオン原典にも言及: 物理防御・体力）；サンファイア イージス + アイスボーン ガントレット（n=2（15未満）；共通stats: 物理防御・体力／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Poppy` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Poppy.png)
