---
title: "グレイブス"
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
champion_id: "Graves"
champion_key: "104"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Graves.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Graves.png"
---

# グレイブス

![[raw/assets/champions/Graves.png|128]]

## 基本情報

- **英字ID：** `Graves`
- **キー：** `104`
- **称号：** 無法者
- **データversion：** `16.18.1`

## 紹介

マルコム・グレイブスは傭兵、ギャンブラー、泥棒としてその名を知られた存在で、訪れたあらゆる街や帝国で指名手配されている。激しい気性ながら犯罪者としての名誉を維持することを重視し、逆らう者にはダブルバレルショットガン「デスティニー」の銃口でそれを思い知らせる。ここ数年は問題を抱えていた相棒のツイステッド・フェイトと和解し、混沌としたビルジウォーターの闇社会で協力して再び成功を手にしている。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 625 |
| `hpperlevel` | 106 |
| `mp` | 325 |
| `mpperlevel` | 40 |
| `movespeed` | 340 |
| `armor` | 33 |
| `armorperlevel` | 4.6 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 425 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 66 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.475 |

## アビリティ

- **パッシブ — ニュー・デスティニー：** ショットガンには独特の特性がある。弾を撃ち尽くしたらリロードが必要となる。通常攻撃は弾丸を4発発射する。弾丸はユニットを貫通しない。チャンピオン以外のユニットは、複数の弾丸が命中するとノックバックする。

- **Q — エンドライン：** 爆薬の詰まった弾を発射する。弾は発射してから1秒後、あるいは地形に当たると爆発する。
- **W — スモークスクリーン：** 指定地点に発煙弾を発射し、煙幕を発生させて範囲内の敵の視界を低下させる。着弾時の爆発に巻き込まれた敵は魔法ダメージを受け、一時的に移動速度が低下する。
- **E — クイックドロー：** グレイブスが前方にダッシュして物理防御と魔法防御が数秒間増加する。敵チャンピオンに向かってダッシュすると、代わりに「確固たる信念」を2スタック獲得する。敵ユニットに通常攻撃を行うと、このスキルのクールダウンが短縮され、防御力増加時間が更新される。
- **R — コラテラルダメージ：** 強力な炸裂弾を発射して、最初に命中した敵チャンピオンに大ダメージを与える。弾は敵チャンピオンに命中するか、最大射程に達すると炸裂し、扇状の範囲内にいる敵にダメージを与える。

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
- **対象試合：** 162試合、全体勝率 46.9%
- **時間帯別勝率：** 〜20分 57.1%（n=28）、20〜25分 57.9%（n=19）、25〜30分 52.5%（n=40）、30〜35分 31.1%（n=45）、35分〜 46.7%（n=30）
- **最高帯：** 20〜25分（判定差 26.8ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-104|グレイブスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（407試合）

- **実測ビルド候補：** イモータル シールドボウ + コレクター + ヒュブリス（該当n=32、68.8% / 非該当46.9%、差+21.8pt）；イモータル シールドボウ + ヒュブリス（該当n=32、68.8% / 非該当46.9%、差+21.8pt）
- **ステータス傾向：** クリティカル率（該当n=351、49.9% / 非該当41.1%、差+8.8pt）
- **理論仮説：** ガーディアン エンジェル + デス ダンス（未観測；共通stats: 物理防御・攻撃力／チャンピオン原典にも言及: 物理防御・攻撃力）；マーキュリアル シミター + マルモティウスの胃袋（未観測；共通stats: 攻撃力・魔法防御／チャンピオン原典にも言及: 攻撃力・魔法防御）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Graves` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Graves.png)
