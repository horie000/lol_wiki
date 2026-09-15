---
title: "レネクトン"
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
  - role-tank
  - data-dragon
champion_id: "Renekton"
champion_key: "58"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "フューリー"
image_path: "raw/assets/champions/Renekton.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Renekton.png"
---

# レネクトン

![[raw/assets/champions/Renekton.png|128]]

## 基本情報

- **英字ID：** `Renekton`
- **キー：** `58`
- **称号：** 砂漠の解体屋
- **データversion：** `16.18.1`

## 紹介

威圧的な巨体に怒りをみなぎらせた超越者レネクトンは、灼熱のシュリーマに生まれ出でた。レネクトンはかつて、帝国随一と目されていた戦士であった。彼の率いる軍隊は、シュリーマを数限りない勝利に導いた。しかし、帝国は崩壊し、レネクトンは砂の下に幽閉される運命を辿る。時が流れ、世が変わりゆく間に、じわじわと彼は狂気に支配されていった。今や自由の身となったレネクトンは、兄ナサスを見つけ出し、葬り去ることに執念を燃やす。狂気の中、彼は数百年にも渡って自分を闇に封じ込めたのは、全てナサスの仕業だという妄想に憑りつかれ...

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** フューリー

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 2 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 660 |
| `hpperlevel` | 111 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 35 |
| `armorperlevel` | 5.2 |
| `spellblock` | 28 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 69 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.75 |
| `attackspeed` | 0.665 |

## アビリティ

- **パッシブ — 激情の支配：** 攻撃に「フューリー」を獲得する。自身の体力が低下していると「フューリー」の獲得量が増加する。「フューリー」を消費するとスキルに追加効果を付与できる。

- **Q — ミートカット：** 武器を振り回して周囲の敵に物理ダメージを与え、ダメージの数パーセントに相当する体力を回復する。「フューリー」が50以上たまっている場合は、ダメージと回復量が増える。
- **W — メッタ斬り：** 敵を2回斬りつけて物理ダメージを与え、0.75秒間スタン効果を付与する。「フューリー」が50以上たまっている場合は攻撃回数が3回に増え、対象のダメージシールドを消滅させてより多くのダメージを与える。また、スタン時間が1.5秒に延びる。
- **E — スライス・アンド・ダイス：** ダッシュ攻撃を繰り出し、進路上の敵にダメージを与える。強化時は与えるダメージが増え、2回目のダッシュ攻撃が命中した敵の物理防御を低下させる。
- **R — セベクの怒り：** 凶暴化して最大体力が増加し、周囲の敵にダメージを与える。凶暴化中は毎秒「フューリー」がたまっていく。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中7位（上位15%）。体力660、物理防御35、攻撃力69、移動速度345。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 320試合、全体勝率 49.1%
- **時間帯別勝率：** 〜20分 50.0%（n=56）、20〜25分 54.8%（n=42）、25〜30分 55.9%（n=68）、30〜35分 36.0%（n=75）、35分〜 51.9%（n=79）
- **最高帯：** 25〜30分（判定差 19.9ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Renekton` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Renekton.png)
