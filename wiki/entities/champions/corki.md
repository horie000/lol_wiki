---
title: "コーキ"
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
  - role-mage
  - data-dragon
champion_id: "Corki"
champion_key: "42"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Corki.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Corki.png"
---

# コーキ

![[raw/assets/champions/Corki.png|128]]

## 基本情報

- **英字ID：** `Corki`
- **キー：** `42`
- **称号：** 豪気の爆撃手
- **データversion：** `16.18.1`

## 紹介

ヨードルのパイロットであるコーキが大好きなものは二つある──飛ぶこと、そして自分の立派な口ひげだ…ただし、この二つの順番は問わない。バンドルシティを離れてピルトーヴァーに移り住んだコーキは、そこで見つけた不思議な機械に夢中になった。彼は飛行装置の開発にすべてを捧げ、スクリーミング・イップスネーク飛行隊と呼ばれるベテランパイロットが集まる航空防衛隊のリーダーになった。銃撃を受けても冷静さを失わないコーキは新たな故郷となった街の空をパトロールしながら、無数のミサイルの雨を降らせれば解決できない問題はないと...

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 3 |
| `magic` | 6 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 100 |
| `mp` | 350 |
| `mpperlevel` | 40 |
| `movespeed` | 325 |
| `armor` | 27 |
| `armorperlevel` | 4.5 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7.4 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 52 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.8 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — ヘクステック榴散弾：** 通常攻撃ダメージの一定割合を追加確定ダメージとして与える。

- **Q — 閃光弾：** 爆弾を発射し、範囲内の敵に魔法ダメージを与える。 範囲内の敵は一定時間可視状態になる。
- **W — ワルキューレ機行：** 爆弾を落しながら短距離を飛行する。通過したエリアには一定時間火炎が残り、エリア内にいる敵にダメージを与える。
- **E — ガトリングガン：** ガトリングガンを高速連射し、前方の扇形範囲内にいる敵にダメージを与え、物理防御と魔法防御を低下させる。
- **R — 連発ミサイル：** 指定方向にミサイルを発射する。ミサイルは敵ユニットに命中すると爆発し、範囲内の敵ユニットにダメージを与える。ミサイルのストックは最大に達するまで一定時間ごとにチャージされる。 3発ごとに「ドデカミサイル」が発射され、通常より大きいダメージを与える。

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

- **観測分類：** 判定保留（分母不足）
- **対象試合：** 20試合、全体勝率 35.0%
- **時間帯別勝率：** 〜20分 50.0%（n=2）、20〜25分 50.0%（n=2）、25〜30分 50.0%（n=2）、30〜35分 40.0%（n=5）、35分〜 22.2%（n=9）
- **最高帯：** 〜20分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-42|コーキの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（77試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** マナムネ + ムラマナ（未観測；共通stats: 攻撃力・マナ／チャンピオン原典にも言及: 攻撃力・マナ）；インフィニティ エッジ + コレクター（n=12（15未満）；共通stats: 攻撃力・クリティカル率／チャンピオン原典にも言及: 攻撃力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Corki` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Corki.png)
