---
title: "アフェリオス"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-marksman
champion_id: "Aphelios"
champion_key: "523"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Aphelios.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Aphelios.png"
---

# アフェリオス

![[raw/assets/champions/Aphelios.png|128]]

## 基本情報

- **英字ID：** `Aphelios`
- **キー：** `523`
- **称号：** 信ずる者の武器
- **データversion：** `16.18.1`

## 紹介

月明かりの陰から武器を構えて立ち現れるアフェリオスは、不気味なまでに音も無くルナリの敵の息の根を止める──その存在を示すのは、正確な狙いから放たれる銃声のみ。自らを突き動かす毒の力。アフェリオスは言葉を奪われながらも、その力によって妹のアルーンの導きを受ける。遠く離れた寺院の聖域から、彼女はムーンストーンの武器を兄の手に授けている。頭上に月が輝く限り、アフェリオスが孤独になることは決してない。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 2 |
| `magic` | 1 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 102 |
| `mp` | 348 |
| `mpperlevel` | 42 |
| `movespeed` | 325 |
| `armor` | 26 |
| `armorperlevel` | 4.2 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 3.25 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 6.5 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.1 |
| `attackspeed` | 0.665 |

## アビリティ

- **パッシブ — 殺す者と導く者：** アフェリオスは妹のアルーンが作った5種類のルナリ武器を使って戦う。一度に2種類の武器を保持でき、1つはメインハンド、もう1つはオフハンドに装備する。各武器にはそれぞれ独自の通常攻撃とスキルがある。通常攻撃とスキルは各武器の弾薬を消費する。弾薬が切れるとアフェリオスはその武器を捨て、5種類あるうちの次の武器をアルーンが召喚する。

- **Q — 武器ごとのスキル：** アフェリオスには、メインハンド武器に応じて変化する5種類の発動スキルがある: キャリブラム(ライフル): 長射程攻撃で対象をマークして再度長射程から攻撃する。 セヴェラム(鎌型ピストル): 素早く走りながら近くの敵を両方の武器で攻撃する。 グラヴィタム(キャノン): この武器のスロウ効果を受けているすべての敵にスネア効果を付与する。 インファーナム(火炎放射器): 扇状範囲内の敵に炎を浴びせ、対象をオフハンド武器で攻撃する。 クレッシェンダム(チャクラム): オフハンド武器を搭載したセントリーを設置する。
- **W — フェーズ：** メインハンド武器とオフハンド武器を切り替え、通常攻撃および発動スキルを変化させる。
- **E — 武器キューシステム：** アフェリオスには3つ目のスキルがない。このスロットにはアルーンから次に渡される武器が表示される。武器の登場順は固定だが、試合を進める過程で順番を入れ替えることはできる。弾が切れた武器は順番の最後に回される。
- **R — 月光の祈り：** 凝縮された月光のエネルギーを発射する。月光は敵チャンピオンに命中すると爆発する。メインハンド武器に応じて異なる効果を適用する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Aphelios` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Aphelios.png)
