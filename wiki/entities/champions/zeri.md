---
title: "ゼリ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
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

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 終盤寄り
- **対象試合：** 169試合、全体勝率 47.9%
- **時間帯別勝率：** 〜20分 50.0%（n=32）、20〜25分 34.6%（n=26）、25〜30分 48.9%（n=47）、30〜35分 42.9%（n=35）、35分〜 62.1%（n=29）
- **最高帯：** 35分〜（判定差 12.1ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 12.1%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-221|ゼリの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（338試合）

- **実測ビルド候補：** ユン・タル ワイルドアロー + ドミニク リガード（該当n=33、69.7% / 非該当46.2%、差+23.5pt）；インフィニティ エッジ + ユン・タル ワイルドアロー（該当n=108、62.0% / 非該当42.2%、差+19.9pt）
- **ステータス傾向：** ライフスティール（該当n=59、64.4% / 非該当45.2%、差+19.2pt）；クリティカル率（該当n=305、49.8% / 非該当36.4%、差+13.5pt）
- **理論仮説：** スタティック シヴ + クラーケン スレイヤー（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・移動速度）；スタティック シヴ + リッチ ベイン（未観測；共通stats: 魔力・移動速度／チャンピオン原典にも言及: 魔力・移動速度）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Zeri` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zeri.png)
