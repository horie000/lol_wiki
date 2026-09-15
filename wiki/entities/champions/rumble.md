---
title: "ランブル"
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
champion_id: "Rumble"
champion_key: "68"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Mage"
resource_type: "ヒート"
image_path: "raw/assets/champions/Rumble.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rumble.png"
---

# ランブル

![[raw/assets/champions/Rumble.png|128]]

## 基本情報

- **英字ID：** `Rumble`
- **キー：** `68`
- **称号：** 戦慄の機甲兵
- **データversion：** `16.18.1`

## 紹介

ランブルは若くて気性の荒い発明家だ。この気骨のあるヨードルは、ガラクタの山を使って、たった一人の力で電撃ハープーンと焼夷ロケット弾を搭載した巨大なメカスーツを作り出した。廃品置き場で作り出された彼の発明品を冷笑する者がいても、ランブルは気にしない──いざとなれば、火炎放射器で黙らせてやればいいだけだ。

## 分類

- **役割タグ：** `Fighter`、`Mage`
- **リソース種別：** ヒート

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 6 |
| `magic` | 8 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 105 |
| `mp` | 150 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 36 |
| `armorperlevel` | 4.7 |
| `spellblock` | 28 |
| `spellblockperlevel` | 1.55 |
| `attackrange` | 125 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.85 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — ポンコツタイタン：** スキルを使用するたび、ヒートが溜まっていく。ヒートゲージが50%に達すると「デンジャーゾーン」に突入し、すべての通常スキルに追加効果が付与される。100%に達すると「オーバーヒート」し、攻撃速度が増加して通常攻撃に追加ダメージがつくが、数秒間スキルを使えなくなる。

- **Q — スピットファイア：** 扇状の範囲を3秒間にわたって焼き払い魔法ダメージを与える。「デンジャーゾーン」突入時はダメージが増加する。
- **W — ジャンクシールド：** シールドを発生させてダメージを防ぎ、さらに移動速度が一瞬増加する。「デンジャーゾーン」突入時はシールド耐久値と、増加移動速度が増加する。
- **E — エレクトロハープーン：** 銛を発射し、対象を感電させて魔法ダメージとスロウ効果を与え、魔法防御を低下させる。2発まで発射できる。「デンジャーゾーン」突入時はダメージとスロウ効果が増加する。
- **R — イコライザー：** 複数のロケット弾を投下し、その地点を炎上させて敵にダメージとスロウ効果を与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中18位（上位15%）。体力640、物理防御36、攻撃力64、移動速度345。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 中盤寄り
- **対象試合：** 133試合、全体勝率 58.6%
- **時間帯別勝率：** 〜20分 56.0%（n=25）、20〜25分 52.9%（n=17）、25〜30分 66.7%（n=30）、30〜35分 60.0%（n=20）、35分〜 56.1%（n=41）
- **最高帯：** 25〜30分（判定差 10.6ポイント）
- **判定根拠：** 中間帯が最高、端点との差 10.6%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-68|ランブルの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（319試合）

- **実測ビルド候補：** シャドウフレイム + ライアンドリーの仮面（該当n=52、59.6% / 非該当44.9%、差+14.7pt）；ゾーニャの砂時計 + シャドウフレイム（該当n=31、58.1% / 非該当46.2%、差+11.9pt）
- **ステータス傾向：** 物理防御（該当n=177、50.8% / 非該当43.0%、差+7.9pt）
- **理論仮説：** スピリット ビサージュ + アビサル マスク（未観測；共通stats: 体力・魔法防御／チャンピオン原典にも言及: 体力・魔法防御）；終わりなき絶望 + ランデュイン オーメン（未観測；共通stats: 物理防御・体力／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Rumble` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rumble.png)
