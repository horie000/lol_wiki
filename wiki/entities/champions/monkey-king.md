---
title: "ウーコン"
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
  - role-tank
  - data-dragon
champion_id: "MonkeyKing"
champion_key: "62"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/MonkeyKing.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/MonkeyKing.png"
---

# ウーコン

![[raw/assets/champions/MonkeyKing.png|128]]

## 基本情報

- **英字ID：** `MonkeyKing`
- **キー：** `62`
- **称号：** 美猴王
- **データversion：** `16.18.1`

## 紹介

ヴァスタヤのトリックスターであるウーコンは、自身の強さと俊敏さ、さらに賢さを駆使して敵を翻弄し、優位に立って戦うことを得意とする。彼はマスター・イーという名の戦士を生涯の友として見出し、古来より伝わる伝説の武術「ウージュー」を学ぶ最後の弟子となった。魔法の棍を得物に、ウーコンはアイオニアを滅亡から守るための手段を探し求めている。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 2 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 99 |
| `mp` | 330 |
| `mpperlevel` | 65 |
| `movespeed` | 340 |
| `armor` | 31 |
| `armorperlevel` | 4.7 |
| `spellblock` | 28 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 3.5 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 66 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.69 |

## アビリティ

- **パッシブ — 岩の皮膚：** チャンピオンまたはモンスターと戦闘中は、スタック可能な物理防御と最大体力に応じた自動回復を獲得する。

- **Q — 強棒打：** 次の通常攻撃の射程が増加して追加ダメージを与え、対象の物理防御を数秒間低下させる。
- **W — 戦士の幻惑：** インビジブル状態になって指定方向にダッシュする。元いた場所には近くの敵を攻撃する分身が残る。
- **E — 乱像猿技：** 指定した対象に向かって突撃し、複数の残像を発生させる。残像は対象の近くにいる敵ユニットを攻撃し、対象それぞれにダメージを与える。
- **R — 旋風猿舞：** 如意棒を伸ばして回転し、自身の移動速度が増加する。 如意棒に触れた敵にダメージを与えてノックアップさせる。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.MonkeyKing` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/MonkeyKing.png)
