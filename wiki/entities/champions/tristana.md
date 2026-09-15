---
title: "トリスターナ"
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
  - role-assassin
  - data-dragon
champion_id: "Tristana"
champion_key: "18"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Tristana.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Tristana.png"
---

# トリスターナ

![[raw/assets/champions/Tristana.png|128]]

## 基本情報

- **英字ID：** `Tristana`
- **キー：** `18`
- **称号：** ヨードルの主砲
- **データversion：** `16.18.1`

## 紹介

他のヨードルたちは自らのエネルギーを発見や発明、またはただのいたずらに注いでいるが、トリスターナはいつだって偉大な戦士の冒険に憧れていた。彼女はルーンテラの様々な派閥や戦争の話を聞き、自分たちヨードルだって、そこで価値のある伝説を残せるはずだと考えた。信頼する愛砲「ブーマー」とともに初めてこの世界に足を踏み入れた彼女は、断固たる勇気と楽観主義を胸に戦闘に飛び込んでいく。

## 分類

- **役割タグ：** `Marksman`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 3 |
| `magic` | 5 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 102 |
| `mp` | 300 |
| `mpperlevel` | 32 |
| `movespeed` | 325 |
| `armor` | 30 |
| `armorperlevel` | 4 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 4 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 7.2 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.5 |
| `attackspeed` | 0.656 |

## アビリティ

- **パッシブ — ドロー＆グロー：** レベルが上がるごとに射程が増加する。

- **Q — ラピッドファイア：** 高速で連射を行い、攻撃速度が数秒間増加する。
- **W — ロケットジャンプ：** 地面を砲撃した反動で指定地点へジャンプし、着地と同時に周辺のユニット全員にダメージを与え、短時間スロウ効果を付与する。
- **E — ヨードルグレネード：** 自動効果: ユニットを倒すと砲弾が炸裂して金属片が飛び散り、周辺の敵ユニットにダメージを与える。 発動効果: 対象にグレネードを付着させる。グレネードは数秒後に起爆し、対象と周囲のユニットにダメージを与える。
- **R — バスターショット：** 敵ユニット1体へ向けて巨大な砲弾を発射し、魔法ダメージを与えてノックバックさせる。対象に「ヨードルグレネード」が付着していた場合、爆発半径が2倍になる。

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
- **対象試合：** 292試合、全体勝率 47.6%
- **時間帯別勝率：** 〜20分 42.5%（n=40）、20〜25分 49.0%（n=49）、25〜30分 46.9%（n=64）、30〜35分 51.3%（n=76）、35分〜 46.0%（n=63）
- **最高帯：** 30〜35分（判定差 8.8ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-18|トリスターナの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（501試合）

- **実測ビルド候補：** インフィニティ エッジ + ガンメタル ブーツ（該当n=32、71.9% / 非該当46.7%、差+25.2pt）；ユン・タル ワイルドアロー + ドミニク リガード + ナヴォリ フリッカーブレード（該当n=32、71.9% / 非該当46.7%、差+25.2pt）
- **ステータス傾向：** 移動速度（該当n=426、50.9% / 非該当33.3%、差+17.6pt）；物理防御（該当n=65、58.5% / 非該当46.8%、差+11.7pt）
- **理論仮説：** ラピッド ファイアキャノン + ナヴォリ フリッカーブレード（n=3（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度）；ルナーン ハリケーン + ナヴォリ フリッカーブレード（n=2（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度）

### MIDDLE（41試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** ガンメタル ブーツ + クラーケン スレイヤー（n=4（15未満）；共通stats: 攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃速度）；クラーケン スレイヤー + ナヴォリ フリッカーブレード（n=3（15未満）；共通stats: 攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃速度）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Tristana` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Tristana.png)
