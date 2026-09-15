---
title: "ジェイス"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
tags:
  - champion
  - role-fighter
  - role-marksman
  - data-dragon
champion_id: "Jayce"
champion_key: "126"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Jayce.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jayce.png"
---

# ジェイス

![[raw/assets/champions/Jayce.png|128]]

## 基本情報

- **英字ID：** `Jayce`
- **キー：** `126`
- **称号：** 未来への希望
- **データversion：** `16.18.1`

## 紹介

ジェイス・タリスは天才的な発明家であり、友人のビクターと共にヘクステックの秘密を初めて大きく解き明かした人物でもある。ピルトーヴァー全域で称賛された彼は、「進歩の男」という呼び名に相応しい存在たるべく努めてはいるものの、その期待からくる重圧に苦しむことも多い。そんな中、自身の発明がピルトーヴァーとゾウンの分断を助長していることに気づき始めた彼は、未来を守るべくヘクステックハンマーを手に戦うことを決意した。

## 分類

- **役割タグ：** `Fighter`、`Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 4 |
| `magic` | 3 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 590 |
| `hpperlevel` | 109 |
| `mp` | 375 |
| `mpperlevel` | 45 |
| `movespeed` | 335 |
| `armor` | 22 |
| `armorperlevel` | 5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 125 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — ヘクステック・コンデンサー：** 武器を切り替えると少しの間移動速度が増加する。

- **Q — スカイバスター/ショックブラスト：** ハンマーモード: 敵に飛びかかって物理ダメージとスロウ効果を与える。 キャノンモード: 電流の玉を発射し、敵に命中するか最大射程に達すると爆発して、範囲内の敵ユニットに物理ダメージを与える。
- **W — ライトニング/ハイパーチャージ：** ハンマーモード: 自動効果: 攻撃のたびにマナが回復する。 発動効果: 雷のフィールドを発生させ、周囲の敵に数秒間ダメージを与える。 キャノンモード: 爆発的なエネルギーを得て、次の数回の攻撃速度が最大まで増加する。
- **E — サンダーブロー/アクセルゲート：** ハンマーモード: 敵に魔法ダメージを与え、わずかに突き飛ばす。 キャノンモード: そこを通過したすべての味方チャンピオンの移動速度が増加する「アクセルゲート」を配備する。「ショックブラスト」が「アクセルゲート」を通過すると、弾速、射程、ダメージが増加する。
- **R — マーキュリーキャノン/マーキュリーハンマー：** ハンマーモード: 「マーキュリーハンマー」が「マーキュリーキャノン」に切り替わり、スキルが変化すると同時に射程距離が広がる。モード変更後の最初の一撃には、対象の物理防御と魔法防御を低下させる効果がつく。 キャノンモード: 「マーキュリーキャノン」が「マーキュリーハンマー」に切り替わり、変化と同時に物理防御と魔法防御が増加する。モード変更後の最初の一撃には魔法ダメージが追加される。

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
- **対象試合：** 116試合、全体勝率 45.7%
- **時間帯別勝率：** 〜20分 42.1%（n=19）、20〜25分 47.6%（n=21）、25〜30分 41.7%（n=24）、30〜35分 50.0%（n=22）、35分〜 46.7%（n=30）
- **最高帯：** 30〜35分（判定差 8.3ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Jayce` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jayce.png)
