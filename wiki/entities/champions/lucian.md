---
title: "ルシアン"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
tags:
  - champion
  - role-marksman
  - role-assassin
  - data-dragon
champion_id: "Lucian"
champion_key: "236"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Lucian.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lucian.png"
---

# ルシアン

![[raw/assets/champions/Lucian.png|128]]

## 基本情報

- **英字ID：** `Lucian`
- **キー：** `236`
- **称号：** 不浄殲滅者
- **データversion：** `16.18.1`

## 紹介

光の番人であるルシアンは、二挺の古の拳銃を携え、亡者の魂を追い詰めて浄化するハンターだ。亡霊スレッシュに妻を殺されたルシアンは、復讐の道へと乗り出したが、彼女が蘇ってもその怒りが消えることはなかった。情け容赦なくひたむきなルシアンは、「黒き霧」に潜む古の亡霊の脅威から人々を護るためなら手段を選ばない。

## 分類

- **役割タグ：** `Marksman`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 641 |
| `hpperlevel` | 100 |
| `mp` | 320 |
| `mpperlevel` | 43 |
| `movespeed` | 335 |
| `armor` | 28 |
| `armorperlevel` | 4.2 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 500 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.638 |

## アビリティ

- **パッシブ — 二挺拳銃：** スキルを使用するたびに、次の通常攻撃が2連射になる。味方から体力回復効果またはシールドを付与されるか、自身の周囲で敵チャンピオンが移動不能効果を受けると、次の2回の通常攻撃が追加魔法ダメージを与える。

- **Q — ピアシングライト：** 指定した敵ユニットへ光線を発射する。光線はその軌道上にいるすべての敵ユニットにダメージを与える。
- **W — アーデントブレイズ：** 指定方向に星形に爆発するエネルギーを発射する。命中した敵ユニットには印が付与され、一時的に可視状態になる。印が付いた敵を攻撃するとルシアンの移動速度が増加する。
- **E — スライド：** 短距離を素早く移動する。「二挺拳銃」の通常攻撃が敵に命中するたびに、このスキルのクールダウンが短縮される。
- **R — 二挺掃射：** 二挺拳銃を構えて弾丸を高速で連射する。

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

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 185試合、全体勝率 44.9%
- **時間帯別勝率：** 〜20分 47.4%（n=38）、20〜25分 47.4%（n=19）、25〜30分 47.8%（n=46）、30〜35分 34.2%（n=38）、35分〜 47.7%（n=44）
- **最高帯：** 25〜30分（判定差 13.6ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Lucian` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lucian.png)
