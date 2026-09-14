---
title: "セラフィーン"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-support
  - role-mage
  - data-dragon
champion_id: "Seraphine"
champion_key: "147"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Seraphine.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Seraphine.png"
---

# セラフィーン

![[raw/assets/champions/Seraphine.png|128]]

## 基本情報

- **英字ID：** `Seraphine`
- **キー：** `147`
- **称号：** 希望のメロディー
- **データversion：** `16.18.1`

## 紹介

ピルトーヴァーでゾウン人の両親のもとに生まれたセラフィーンは、他者の魂の声を聴くことができる──世界が彼女に歌いかけ、彼女も歌い返す。若い頃は耳の中の喧噪に耐えられなかったが、今のセラフィーンはこの声からインスピレーションを得ることで、混沌を交響曲へと変えている。セラフィーンは二つの姉妹都市のために歌い、住民たちに自分たちが独りではないこと、団結すればより強くなれること、そして、彼女の目には無限の可能性が見えていることを伝えようとしている。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 0 |
| `defense` | 0 |
| `magic` | 0 |
| `difficulty` | 0 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 570 |
| `hpperlevel` | 95 |
| `mp` | 360 |
| `mpperlevel` | 40 |
| `movespeed` | 330 |
| `armor` | 26 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.95 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 50 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.669 |

## データ品質上の注意

- `info` の4項目がすべて `0` である。未収録値か実値かは原典だけでは判定できない。

## アビリティ

- **パッシブ — ステージプレゼンス：** 通常スキルを3回使用すると、3回目のスキルが2連続で発動する。さらに味方の近くでスキルを使用すると、自身の次の通常攻撃は射程が増加し、追加魔法ダメージを与える。

- **Q — ハイノート：** 一定範囲内にダメージを与える。
- **W — サラウンドサウンド：** 周囲の味方にシールドを付与して移動速度を増加させる。自身がすでにシールドを獲得している場合は、周囲の味方の体力を回復する。
- **E — ビートドロップ：** 直線上の敵にダメージと移動妨害効果を与える。
- **R — アンコール：** 敵にダメージとチャーム効果を与え、味方および敵のチャンピオンに触れるたびに射程がリフレッシュされていく。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 中盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 本分類で採用した序盤の基礎ステータス上位15%と、終盤の能力の蓄積成長・明示的なステータス連動のいずれにも当たらないため、中盤を暫定指定する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Seraphine` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Seraphine.png)
