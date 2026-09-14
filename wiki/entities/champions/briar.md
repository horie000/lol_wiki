---
title: "ブライアー"
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
champion_id: "Briar"
champion_key: "233"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "フューリー"
image_path: "raw/assets/champions/Briar.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Briar.png"
---

# ブライアー

![[raw/assets/champions/Briar.png|128]]

## 基本情報

- **英字ID：** `Briar`
- **キー：** `233`
- **称号：** 枷と飢え
- **データversion：** `16.18.1`

## 紹介

黒薔薇団の実験の失敗により、制御不能な血の渇きとともに生まれ落ちたブライアーは、特殊な拘束具がなければ狂乱の精神を抑えられない。彼女は数年間の幽閉の末に自由を手に入れ、世に解き放たれた。今は誰にも管理されることなく、ただ知識と血への渇望に突き動かされ、自らを解き放つ機会を楽しんでいる。狂乱の精神を制御するのは容易ではないにしても。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** フューリー

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 625 |
| `hpperlevel` | 95 |
| `mp` | 0 |
| `mpperlevel` | 0 |
| `movespeed` | 340 |
| `armor` | 30 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 0 |
| `hpregenperlevel` | 0 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — 真紅の呪い：** 通常攻撃とスキルが出血のスタックを付与し、与えたダメージの一定割合にあたる体力を回復する。絶えず飢えているブライアーは、減少体力に応じて回復量が増加するが、体力自動回復は備わっていない。

- **Q — ヘッドラッシュ：** ユニットのもとに跳躍して、強烈なかかと落としで敵を攻撃し、対象をスタンさせて物理防御を低下させる。
- **W — 血の狂乱/衝動噛み：** 前方に跳躍して首枷を破壊し、「血の狂乱」状態になる。効果時間中は最も近くの敵(チャンピオンを優先)を執拗に追いかけて通常攻撃する。狂乱状態では攻撃速度と移動速度が増加し、通常攻撃が対象を中心に範囲ダメージを与えるようになる。 狂乱中にこのスキルを再発動すると、次の通常攻撃で対象に噛みつき、対象の減少体力に応じて追加ダメージを与える。さらに、与えたダメージに応じて自身の体力を回復する。
- **E — 呪福の叫び：** 精神を集中して「血の狂乱」状態を解除し、エネルギーを溜めて凄まじい叫び声を上げ、敵にダメージとスロウ効果を与える。チャージ中はダメージ軽減効果を獲得し、最大体力の一定割合にあたる体力を回復する。最大までチャージすると、叫び声が敵をノックバックさせる。対象が壁に当たった場合、追加ダメージを与えてスタンさせる。
- **R — 迫りくる死：** 首枷に付けられた魔石ヘモリスを蹴り飛ばし、最初に命中したチャンピオンを獲物としてマークする。その後、獲物まで一直線に飛んでいき、到着時に周囲の他の敵にフィアー効果を与え、完全な渇血状態になる。この間は「血の狂乱」の効果を得て、物理防御、魔法防御、ライフスティール、移動速度が増加し、デスするまで獲物を追いかけ通常攻撃する。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Briar` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Briar.png)
