---
title: "エコー"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-assassin
  - role-mage
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

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Ekko` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ekko.png)
