---
title: "ゼリ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-marksman
  - data-dragon
champion_id: "Zeri"
champion_key: "221"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Zeri.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zeri.png"
---

# ゼリ

![[raw/assets/champions/Zeri.png|128]]

## 基本情報

- **英字ID：** `Zeri`
- **キー：** `221`
- **称号：** ゾウンの火花
- **データversion：** `16.18.1`

## 紹介

ゾウンの労働階級に生まれたゼリは、頑固で活発な若者だ。彼女は電気の魔力を操り、自らと特製のライフルに電力を注ぎこんでいる。ゼリの不安定な力は彼女の感情を反映しており、飛び散る火花は命を救うために電光石火で飛び回る彼女のアプローチそのものだ。他者に対して深い思いやりを持つゼリは、いつも家族と故郷への愛を胸に、戦いに臨む。助けようとする熱意が裏目に出ることもあるが、ゼリは一つの真実を確信している。仲間のために立ち上がれば、彼らも共に立ち上がってくれるということを。

## 分類

- **役割タグ：** `Marksman`
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
| `hp` | 600 |
| `hpperlevel` | 110 |
| `mp` | 250 |
| `mpperlevel` | 45 |
| `movespeed` | 330 |
| `armor` | 24 |
| `armorperlevel` | 4.2 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 3.25 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 56 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 生体バッテリー：** ゼリの通常攻撃は魔法ダメージを与え、スキルとして扱われる。移動および「バーストファイア」の使用により、「スパークパック」にエネルギーが蓄積される。最大までチャージされると、次の通常攻撃が追加ダメージを与える。

- **Q — バーストファイア：** 「バーストファイア」は7発の弾をバースト射撃し、最初に命中した敵に攻撃力ダメージを与える。このスキルは通常攻撃として扱われる。
- **W — ウルトラショックレーザー：** 電磁パルスを発射して、最初に命中した敵にスロウ効果とダメージを与える。パルスが壁に当たると、当たった位置から幅が広く、射程の長いレーザーを発射する。
- **E — スパークサージ：** 短い距離をダッシュし、「バーストファイア」が強化されて敵を貫通するようになる。地形に触れた場合は、地形を飛び越えるか地形に沿って滑る。
- **R — ライトニングクラッシュ：** 大量の電力を放出して自身をオーバーチャージし、ダメージと移動速度が増加する。この増加移動速度はスタック可能で、敵チャンピオンに攻撃が命中するたび、リフレッシュされて強化される。オーバーチャージ中は「バーストファイア」が素早い3連射になり、他の敵へと連鎖する電撃が放たれるようになる。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Zeri` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zeri.png)
