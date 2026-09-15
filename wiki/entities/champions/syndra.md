---
title: "シンドラ"
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
champion_id: "Syndra"
champion_key: "134"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Syndra.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Syndra.png"
---

# シンドラ

![[raw/assets/champions/Syndra.png|128]]

## 基本情報

- **英字ID：** `Syndra`
- **キー：** `134`
- **称号：** 暗黒の女王
- **データversion：** `16.18.1`

## 紹介

シンドラは驚異的な力を操るアイオニアの恐るべきメイジである。幼いころには荒々しく制御のきかない魔法によって村の長たちを大いに悩ませていた。彼女は能力を制御する術を学ぶため遠い地へと送られたのだが、あるとき師であるはずの人物が自分の能力を弱体化させていたことを知ってしまった。裏切られ傷ついた心を黒いエネルギー球へと変換させるシンドラは、自分を操らんとする存在を残らず破滅させることを誓ったのだ。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 3 |
| `magic` | 9 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 583 |
| `hpperlevel` | 100 |
| `mp` | 480 |
| `mpperlevel` | 40 |
| `movespeed` | 330 |
| `armor` | 25 |
| `armorperlevel` | 4 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 54 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 絶大なる魔力：** チャンピオンレベルの上昇および敵へのダメージによって「怒りの破片」を集め、スキルをアップグレードできる。 ダークスフィア: チャージ数が1増加する ダークフォース: 追加確定ダメージを与える 闇の波導: 幅が増加し、すべての対象にスロウ効果を付与する 魔力の奔流: 体力が低下している対象にとどめを刺す

- **Q — ダークスフィア：** 闇のエネルギーの球体をつくりだし、敵に魔法ダメージを与える。 球体は一定時間消滅せず、他のスキルで操作することもできる。
- **W — ダークフォース：** 発生中の「ダークスフィア」または敵ミニオンや中立モンスター1体を持ち上げて投げ飛ばす。 投げ飛ばされた「ダークスフィア」およびミニオンや中立モンスターが命中した敵は魔法ダメージを受け、移動速度が低下する。
- **E — 闇の波導：** 敵ユニットおよび発生中の「ダークスフィア」をノックバックし、魔法ダメージを与える。 このスキルでノックバックした「ダークスフィア」が敵ユニットに命中した場合は、さらにスタン効果を付与する。
- **R — 魔力の奔流：** 発生中のすべての「ダークスフィア」で敵チャンピオン1体を集中攻撃する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - レベル上昇・敵へのダメージで「怒りの破片」を集め、スキルをアップグレードできる。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 中盤寄り
- **対象試合：** 222試合、全体勝率 46.8%
- **時間帯別勝率：** 〜20分 41.0%（n=39）、20〜25分 56.0%（n=25）、25〜30分 43.5%（n=46）、30〜35分 49.1%（n=53）、35分〜 47.5%（n=59）
- **最高帯：** 20〜25分（判定差 8.5ポイント）
- **判定根拠：** 中間帯が最高、端点との差 8.5%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-134|シンドラの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（386試合）

- **実測ビルド候補：** ラバドン デスキャップ + 連呪使いのブーツ（該当n=68、57.4% / 非該当42.1%、差+15.2pt）；ラバドン デスキャップ + ルーデン エコー（該当n=82、56.1% / 非該当41.8%、差+14.3pt）
- **ステータス傾向：** 体力（該当n=254、47.6% / 非該当39.4%、差+8.2pt）；物理防御（該当n=148、45.3% / 非該当44.5%、差+0.7pt）
- **理論仮説：** 黒炎のトーチ + ルーデン エコー（n=4（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）；セラフ エンブレイス + ルーデン エコー（n=3（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）

### BOTTOM（45試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** 黒炎のトーチ + ルーデン エコー（n=1（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）；ヘクステック ロケットベルト + コズミック ドライブ（未観測；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Syndra` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Syndra.png)
