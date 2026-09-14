---
title: "カミール"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-fighter
  - role-assassin
  - data-dragon
champion_id: "Camille"
champion_key: "164"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Camille.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Camille.png"
---

# カミール

![[raw/assets/champions/Camille.png|128]]

## 基本情報

- **英字ID：** `Camille`
- **キー：** `164`
- **称号：** スチールシャドウ
- **データversion：** `16.18.1`

## 紹介

フェロス一族のエレガントな主席スパイであるカミールは、法の及ばぬ領域で活動するために機械の体になった。彼女の使命はピルトーヴァーというシステムと、内包するゾウンがスムーズに動作し続けるよう保つことにある。正確無比で適応力に富む彼女は、雑な手際は恥ずべき汚点とみなしている。その身にまとう刃にも劣らない鋭い意志で、己の能力を極めるためにヘクステック技術による身体拡張を繰り返すカミールを、もはや女性ではなく機械なのではないかと考える者も多い。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 6 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 99 |
| `mp` | 375 |
| `mpperlevel` | 52 |
| `movespeed` | 340 |
| `armor` | 35 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 8.15 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — アダプティブディフェンス：** 敵チャンピオンに通常攻撃すると、その敵の主なダメージの種類(物理または魔法)に応じて、少しの間だけ自身の最大体力の一定割合にあたるシールドを獲得する。

- **Q — プレシジョンプロトコル：** 次の通常攻撃が追加ダメージを与え、移動速度が増加する。このスキルは少しの間だけ再発動することが可能で、再発動までの間に一定の間隔を置くと追加ダメージが大きく増加する。
- **W — タクティカルスイープ：** 少し間を置いてから扇状の範囲に攻撃を行ってダメージを与える。攻撃範囲の外側半分にいた敵ユニットにはスロウ効果と追加ダメージを与え、また同時に自身を回復する。
- **E — フックショット：** 壁に飛びついてから跳躍して、着地時に敵チャンピオンをノックアップする。
- **R — ヘクステック・アルティメイタム：** 指定した敵チャンピオンに向かってダッシュして、対象を一定エリア内に閉じ込める。さらに通常攻撃がその対象に追加魔法ダメージを与えるようになる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中16位（上位15%）。体力650、物理防御35、攻撃力68、移動速度340。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Camille` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Camille.png)
