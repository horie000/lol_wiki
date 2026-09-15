---
title: "ヘカリム"
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
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "Hecarim"
champion_key: "120"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Hecarim.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Hecarim.png"
---

# ヘカリム

![[raw/assets/champions/Hecarim.png|128]]

## 基本情報

- **英字ID：** `Hecarim`
- **キー：** `120`
- **称号：** 戦場の幻影
- **データversion：** `16.18.1`

## 紹介

生者の魂を永遠に狩るという呪いを受けたヘカリムは人間と獣が融合した亡霊だ。ブレスドアイルが影に飲まれた時、この誇り高き騎士は「破滅」の破壊的エネルギーに、騎士団と騎馬とともに消し去られてしまった。「黒き霧」がルーンテラに現れる時、彼は鎧をまとった蹄で敵を踏み砕き、虐殺に悦びを感じながら破滅的な突撃を指揮している。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 6 |
| `magic` | 4 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 625 |
| `hpperlevel` | 106 |
| `mp` | 280 |
| `mpperlevel` | 40 |
| `movespeed` | 345 |
| `armor` | 32 |
| `armorperlevel` | 5.45 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 66 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.67 |

## アビリティ

- **パッシブ — ウォーパス：** 増加移動速度の一定割合と同量だけ攻撃力が増加する。

- **Q — ランページ：** 周囲の敵を斬りつけて物理ダメージを与える。1体以上の敵にダメージを与えた場合、それ以降に行う「ランページ」のダメージが増加して、クールダウンが短縮される。
- **W — ソウルドレイン：** 物理防御と魔法防御を獲得する。また、周囲にいる敵に魔法ダメージを与えて、それらの敵が受けたあらゆるダメージの一定割合を体力として回復する。
- **E — チャージ：** 移動速度が短時間増加し、ユニットを通り抜けられるようになる。さらに次の通常攻撃に対象をノックバックする効果と、スキル発動後の移動距離に応じた追加物理ダメージが付与される。
- **R — スペクターズ・オンスロート：** 亡霊の騎士たちを召喚し、指定地点まで突撃して直線上の敵ユニットに魔法ダメージを与える。ヘカリムは到着と同時に衝撃波を放ち、付近の敵を恐怖に陥れて逃走させる。

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

- **観測分類：** 中盤寄り
- **対象試合：** 155試合、全体勝率 51.0%
- **時間帯別勝率：** 〜20分 50.0%（n=24）、20〜25分 61.9%（n=21）、25〜30分 47.5%（n=40）、30〜35分 56.8%（n=37）、35分〜 42.4%（n=33）
- **最高帯：** 20〜25分（判定差 11.9ポイント）
- **判定根拠：** 中間帯が最高、端点との差 11.9%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-120|ヘカリムの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（238試合）

- **実測ビルド候補：** 終わりなき飢え + ショウジンの矛（該当n=35、68.6% / 非該当45.3%、差+23.3pt）；ショウジンの矛 + デス ダンス + ヒュブリス（該当n=36、55.6% / 非該当47.5%、差+8.0pt）
- **ステータス傾向：** 物理防御（該当n=139、52.5% / 非該当43.4%、差+9.1pt）；魔法防御（該当n=52、55.8% / 非該当46.8%、差+9.0pt）
- **理論仮説：** ジーク コンバージェンス + 変幻自在のジャック＝ショー（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力・魔法防御）；トリニティ フォース + ストライドブレイカー（n=1（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Hecarim` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Hecarim.png)
