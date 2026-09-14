---
title: "ジン"
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
  - role-mage
  - data-dragon
champion_id: "Jhin"
champion_key: "202"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Jhin.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jhin.png"
---

# ジン

![[raw/assets/champions/Jhin.png|128]]

## 基本情報

- **英字ID：** `Jhin`
- **キー：** `202`
- **称号：** 孤高の芸術家
- **データversion：** `16.18.1`

## 紹介

ジンは殺人を芸術であると信じてやまないサイコパスである。かつてアイオニアの牢獄に囚われていた緻密で周到な連続殺人犯は、同国の最高評議会の暗部により釈放され、彼らの陰謀を実行する暗殺者となった。ジンにとって、銃とは絵筆に他ならない。その筆先から生み出される作品は芸術的なまでに残酷であり、犠牲者とオーディエンスは身を震わせながら見ていることしかできない。身の毛もよだつ戯曲を上演することに歪んだ愉悦を覚える彼は、“恐怖”という強烈なメッセージを世に伝えるのに最適なアーティストなのだ。

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 10 |
| `defense` | 2 |
| `magic` | 6 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 655 |
| `hpperlevel` | 107 |
| `mp` | 300 |
| `mpperlevel` | 50 |
| `movespeed` | 330 |
| `armor` | 24 |
| `armorperlevel` | 4.7 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 0 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — この銃の名は｢囁き｣：** ジンの「囁き」は極めて精密に作られた銃である。弾倉は4発、一定の速度でしか発射できないが、最後の弾丸に黒魔術による特殊な効果が生まれ、クリティカル及び減少体力に応じた追加ダメージが発生する。また、クリティカルが発生すると自身の移動速度が増加する。

- **Q — ｢爆ぜ狂う果実｣：** 指定した敵ユニットに特殊なグレネードを放り投げる。グレネードは最大4体まで敵ユニットの上を跳ねながらダメージを与え、ユニットを倒すたびに与えるダメージが増加する。
- **W — ｢死者への狂奏曲｣：** 持っている杖から長射程の弾丸を1発発射する。この弾はミニオンおよびモンスターを貫通するが、敵チャンピオンは貫通しない。命中した対象がその前に味方チャンピオン、「女神の足跡」、またはジンからのダメージを受けていた場合、スネア効果を付与する。
- **E — ｢女神の抱擁｣：** 指定地点に、敵ユニットが上を通過すると花開く「女神の足跡」を設置する。「女神の足跡」は発動すると範囲内の敵ユニットをスロウ状態にし、その後爆発して魔法ダメージを与える。 「死とは、かくも美しい…」 - ジンが敵チャンピオンをキルすると、そのユニットの上で「女神の足跡」が発動し爆発する。
- **R — ｢終演 -フィナーレ-｣：** 詠唱とともに「囁き」と手に持った杖を合体させ、長銃へと変形させる。発射される4発の特殊な弾丸は非常に長い射程距離を持ち、ミニオンおよび中立モンスターを貫通して発射する事ができるが、敵チャンピオンを貫通しない。命中した敵に減少体力に応じたダメージを与え、スロウ効果を付与する。最高の技術で大胆かつ繊細に作り上げられた4発目は、より大きな威力を秘めており確実にクリティカルが発生する。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Jhin` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jhin.png)
