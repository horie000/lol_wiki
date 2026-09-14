---
title: "オリアナ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-mage
  - role-support
  - data-dragon
champion_id: "Orianna"
champion_key: "61"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Orianna.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Orianna.png"
---

# オリアナ

![[raw/assets/champions/Orianna.png|128]]

## 基本情報

- **英字ID：** `Orianna`
- **キー：** `61`
- **称号：** 時計仕掛けの舞姫
- **データversion：** `16.18.1`

## 紹介

オリアナはかつては好奇心旺盛な普通の少女だったが、今では技術の粋を駆使した機械仕掛けの体になってしまった。彼女はゾウンの下層地域で起こった事故で重傷を負い、体の部位を一つずつ精巧に作られた人工物に置き換えなければならなかった。再び自由に動けるようになった今、オリアナは自らを守るお供として作り出した真鍮の球体とともに、ピルトーヴァーやその向こうにある世界の探索を続けている。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 3 |
| `magic` | 9 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 565 |
| `hpperlevel` | 110 |
| `mp` | 418 |
| `mpperlevel` | 25 |
| `movespeed` | 325 |
| `armor` | 20 |
| `armorperlevel` | 4.2 |
| `spellblock` | 26 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 44 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — ぜんまい仕掛け：** 通常攻撃が追加で魔法ダメージを与える。このダメージは同じ対象を続けて攻撃すると増加する。

- **Q — オーダー: 攻撃：** オリアナが指定地点を攻撃するようボールに命じ、軌道上の敵ユニットに魔法ダメージを与える (敵に命中する度にダメージは低下する)。ボールは攻撃後もその場に留まる。
- **W — オーダー: 乱磁場：** オリアナの命令により、ボールがエネルギー波を発射して周囲の敵に魔法ダメージを与える。後には力場が残され、範囲内に入ると、味方の移動速度が増加し、敵はスロウ状態になる。
- **E — オーダー: 防御：** オリアナの命令により、ボールが味方チャンピオンに貼りつき、シールドを付与する。ボールは移動時に触れたすべての敵に魔法ダメージを与える。さらに、ボールは貼り付いたチャンピオンの物理防御と魔法防御を増加させる。
- **R — オーダー: ショックウェーブ：** オリアナが命令してから一瞬後、ボールが衝撃波を発射して周囲の敵に魔法ダメージを与え、ボールの方向へ引き寄せる。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Orianna` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Orianna.png)
