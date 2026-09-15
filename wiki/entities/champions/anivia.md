---
title: "アニビア"
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
champion_id: "Anivia"
champion_key: "34"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Anivia.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Anivia.png"
---

# アニビア

![[raw/assets/champions/Anivia.png|128]]

## 基本情報

- **英字ID：** `Anivia`
- **キー：** `34`
- **称号：** 氷の不死鳥
- **データversion：** `16.18.1`

## 紹介

アニビアは翼を持った慈悲の守護者であり、無限に繰り返される生と死、そして再誕の繰り返しに耐えてフレヨルドを守っている。凍てつくような氷と激しい風の中から生まれた半神は、その元素の力を操って侵略者から自分の故郷を守り、過酷な環境の北部に住む部族たちを守り導いている。彼らにとってアニビアは希望の象徴であり、大いなる変化の前触れとして崇拝されている。彼女は自らの命が尽きるまで戦う。自身を犠牲にすることで彼女の記憶は留まり、新たな明日に向かって生まれ変われることを知っているからだ。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 4 |
| `magic` | 10 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 550 |
| `hpperlevel` | 92 |
| `mp` | 495 |
| `mpperlevel` | 45 |
| `movespeed` | 325 |
| `armor` | 19 |
| `armorperlevel` | 4.1 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 600 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 51 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.68 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 再誕：** アニビアは力尽きると、体力が最大の状態で卵に戻る。

- **Q — フラッシュフロスト：** 指定方向に両翼で力強く羽ばたいて、氷の塊を放つ。氷は触れた敵に魔法ダメージと「チルド」を与える。最大距離に達するかこのスキルを再使用すると氷の塊が炸裂して、範囲内の敵にダメージとスタンを与える。
- **W — アイスウォール：** 空気中の水分を凝縮して氷の壁をつくり、相手の移動を妨害する。壁は数秒後に溶けて消滅する。
- **E — フロストバイト：** 翼をはためかせて対象を凍てつく氷柱で攻撃し、ダメージを与える。直前に「フラッシュフロスト」が当たったか、最大範囲の「ブリザード」でダメージを受けた対象には、2倍のダメージを与える。
- **R — ブリザード：** 指定範囲に激しい吹雪を召喚する。吹雪は範囲内の敵に継続ダメージを与え「チルド」を付与する。

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
- **対象試合：** 202試合、全体勝率 55.4%
- **時間帯別勝率：** 〜20分 48.4%（n=31）、20〜25分 50.0%（n=22）、25〜30分 59.6%（n=47）、30〜35分 65.2%（n=46）、35分〜 50.0%（n=56）
- **最高帯：** 30〜35分（判定差 15.2ポイント）
- **判定根拠：** 中間帯が最高、端点との差 15.2%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-34|アニビアの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（280試合）

- **実測ビルド候補：** 連呪使いのブーツ + ライアンドリーの仮面（該当n=39、66.7% / 非該当55.2%、差+11.5pt）；セラフ エンブレイス + 連呪使いのブーツ + ライアンドリーの仮面（該当n=33、66.7% / 非該当55.5%、差+11.2pt）
- **ステータス傾向：** 物理防御（該当n=97、63.9% / 非該当53.0%、差+10.9pt）；魔法防御（該当n=51、64.7% / 非該当55.0%、差+9.7pt）
- **理論仮説：** フィンブルウィンター + ロッド オブ エイジス（n=1（15未満）；共通stats: 体力・マナ／チャンピオン原典にも言及: 体力・マナ）；セラフ エンブレイス + マリグナンス + ロッド オブ エイジス（n=13（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

### TOP（31試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** フィンブルウィンター + ロッド オブ エイジス（n=2（15未満）；共通stats: 体力・マナ／チャンピオン原典にも言及: 体力・マナ）；ライアンドリーの仮面 + ロッド オブ エイジス（n=14（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Anivia` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Anivia.png)
