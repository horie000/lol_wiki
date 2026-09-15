---
title: "ルブラン"
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
  - role-assassin
  - role-mage
  - data-dragon
champion_id: "Leblanc"
champion_key: "7"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Leblanc.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Leblanc.png"
---

# ルブラン

![[raw/assets/champions/Leblanc.png|128]]

## 基本情報

- **英字ID：** `Leblanc`
- **キー：** `7`
- **称号：** 幻惑の奇術師
- **データversion：** `16.18.1`

## 紹介

黒薔薇団の他のメンバーにとっても謎に包まれた存在であるルブランだが、その名前ですら、ノクサス建国初期からあらゆる人々や出来事を操ってきた色白な女が持つ複数の名前のひとつにすぎない。自らの分身を発生させる魔法を使い、この魔術師はいつでもどこにでも姿を現すことが可能で、複数の場所に同時に存在することもできる。その正体と同じく、常に裏で画策を続けるルブランの真の動機は誰にもわからない。

## 分類

- **役割タグ：** `Assassin`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 4 |
| `magic` | 10 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 598 |
| `hpperlevel` | 108 |
| `mp` | 400 |
| `mpperlevel` | 25 |
| `movespeed` | 340 |
| `armor` | 22 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.5 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 鏡像：** 自身の体力が40%を下回ると1秒間インビジブル状態になり、「鏡像」を発生させる。「鏡像」はダメージを与えず、最大8秒間持続する。

- **Q — シジルマリス：** 刻印を飛ばし、対象にダメージを与えて3.5秒間マークする。マークした対象にスキルでダメージを与えると、刻印が爆発して追加ダメージを与える。どちらかのダメージで対象をキルした場合、マナコストが回復して、このスキルの残りクールダウンの一部が短縮される。
- **W — ディストーション：** 指定地点にすばやく移動し、周囲の敵にダメージを与える。4秒以内にこのスキルを再使用すると、最初の位置に戻ることができる。
- **E — エーテルチェイン：** 鎖の幻影を放ち、最初に当たった敵を鎖で繋ぐ。1.5秒間繋いだままにすると、追加ダメージとスネアを与える。
- **R — 再演：** 選択した通常スキルの偽バージョンを使用する。

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

- **観測分類：** 序盤寄り
- **対象試合：** 189試合、全体勝率 46.6%
- **時間帯別勝率：** 〜20分 56.8%（n=37）、20〜25分 44.1%（n=34）、25〜30分 42.5%（n=40）、30〜35分 48.8%（n=41）、35分〜 40.5%（n=37）
- **最高帯：** 〜20分（判定差 16.2ポイント）
- **判定根拠：** 〜20分が最高、長時間帯との差 16.2%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-7|ルブランの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（315試合）

- **実測ビルド候補：** メジャイ ソウルスティーラー + ルーデン エコー（該当n=41、63.4% / 非該当43.4%、差+20.0pt）；連呪使いのブーツ + シャドウフレイム + ルーデン エコー（該当n=103、56.3% / 非該当41.0%、差+15.3pt）
- **ステータス傾向：** 物理防御（該当n=80、48.8% / 非該当45.1%、差+3.6pt）
- **理論仮説：** コズミック ドライブ + ライアンドリーの仮面（n=1（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；メジャイ ソウルスティーラー + モレロノミコン（n=1（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

### UTILITY（50試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** マリグナンス + ルーデン エコー（n=1（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；メジャイ ソウルスティーラー + ヘクステック ロケットベルト（n=1（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Leblanc` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Leblanc.png)
