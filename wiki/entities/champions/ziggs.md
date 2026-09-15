---
title: "ジグス"
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
  - role-mage
  - data-dragon
champion_id: "Ziggs"
champion_key: "115"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Ziggs.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ziggs.png"
---

# ジグス

![[raw/assets/champions/Ziggs.png|128]]

## 基本情報

- **英字ID：** `Ziggs`
- **キー：** `115`
- **称号：** ヘクス爆薬のエキスパート
- **データversion：** `16.18.1`

## 紹介

爆弾を愛する気の短いヨードルのジグスは爆発的な性質の持ち主だ。ピルトーヴァーの発明家の助手として働いていた彼だが、先の見える人生にうんざりしていたところ、青い髪の狂気の爆弾魔であるジンクスと友達になった。夜の街での大暴れをきっかけに、ジグスは彼女の忠告に従ってゾウンに移り住み、ケミテック長者や一般市民を恐怖に陥れながら、以前よりも遥かに自由に、何かを吹き飛ばしたいという自身の願望の飽くなき探求を続けている。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 4 |
| `magic` | 9 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 606 |
| `hpperlevel` | 106 |
| `mp` | 480 |
| `mpperlevel` | 23.5 |
| `movespeed` | 325 |
| `armor` | 21 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.656 |

## アビリティ

- **パッシブ — ショートヒューズ：** 一定時間ごとに、次の通常攻撃に追加魔法ダメージがつく。スキルを使用するたびに、次の追加ダメージまでの時間が短くなる。

- **Q — バウンドボム：** 地面にバウンドする爆弾を投げ、魔法ダメージを与える。
- **W — エンジニアボム：** 発動から少し遅れて、またはスキルを再発動した時に起爆するヨードルグレネードを投げる。爆発は敵に魔法ダメージを与えて弾き飛ばす。ジグスも弾き飛ばされるがダメージは受けない。 体力が減った敵タワーをエンジニアボムで「ヘクスプロード」して破壊できる。
- **E — ヘクステックマイン：** 地面に地雷を複数設置する。敵が接触すると爆発し、魔法ダメージとスロウ効果を与える。同じ敵が地雷を起爆させた場合は与えるダメージが減少する。
- **R — メガインフェルノボム：** 究極の発明品「メガインフェルノボム」は射程距離が極めて長く、爆破範囲中央部にいる敵はさらに大ダメージを受ける。

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
- **対象試合：** 281試合、全体勝率 46.6%
- **時間帯別勝率：** 〜20分 60.0%（n=40）、20〜25分 62.2%（n=45）、25〜30分 44.8%（n=58）、30〜35分 42.6%（n=68）、35分〜 34.3%（n=70）
- **最高帯：** 20〜25分（判定差 27.9ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-115|ジグスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（457試合）

- **実測ビルド候補：** ホライゾン フォーカス + シャドウフレイム + ルーデン エコー（該当n=85、50.6% / 非該当47.8%、差+2.7pt）；ホライゾン フォーカス + シャドウフレイム（該当n=90、50.0% / 非該当48.0%、差+2.0pt）
- **ステータス傾向：** 体力（該当n=329、50.5% / 非該当43.0%、差+7.5pt）
- **理論仮説：** 黒炎のトーチ + セラフ エンブレイス（n=5（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；黒炎のトーチ + ルーデン エコー（n=3（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

### MIDDLE（55試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** セラフ エンブレイス + ルーデン エコー（n=5（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；黒炎のトーチ + ルーデン エコー（n=3（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Ziggs` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ziggs.png)
