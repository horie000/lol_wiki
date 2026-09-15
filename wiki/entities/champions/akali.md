---
title: "アカリ"
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
  - role-assassin
  - data-dragon
champion_id: "Akali"
champion_key: "84"
data_version: "16.18.1"
roles:
  - "Assassin"
resource_type: "気"
image_path: "raw/assets/champions/Akali.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Akali.png"
---

# アカリ

![[raw/assets/champions/Akali.png|128]]

## 基本情報

- **英字ID：** `Akali`
- **キー：** `84`
- **称号：** 主なき暗殺者
- **データversion：** `16.18.1`

## 紹介

「均衡の守人」であることをやめ、「影の拳」という立場も捨てたアカリは、自分こそ故郷の人々が必要としている武器になろうと決め、独り戦いに挑む。師であるシェンから授かった教えを忘れることなく、アイオニアを襲う敵をひとりずつ、確実に排除すると誓ったのである。アカリは音もなく襲い掛かるが、そのメッセージは誰の耳にも届くだろう──主なき暗殺者を恐れよ、と。

## 分類

- **役割タグ：** `Assassin`
- **リソース種別：** 気

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 3 |
| `magic` | 8 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 119 |
| `mp` | 200 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 23 |
| `armorperlevel` | 4.7 |
| `spellblock` | 37 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 50 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.2 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 刺客の刻印：** チャンピオンにスキルでダメージを与えると対象の周囲に気の輪が形成される。輪の外に出るとアカリの次の通常攻撃の射程とダメージが増加する。

- **Q — 五連苦無：** 5本のクナイを投げて自身の増加攻撃力と魔力に応じたダメージを与えてスロウ効果を与える。
- **W — 黄昏の帳：** 姿を隠すための煙幕を張り、少しの間だけ移動速度が増加する。「帳」の中ではインビジブル状態になり、敵のスキルや通常攻撃で対象指定されなくなる。通常攻撃を行うかスキルを使用すると一時的に可視化される。
- **E — 翻身手裏剣：** 後方に宙返りして前方に手裏剣を投げ、魔法ダメージを与える。最初に当たった敵または煙幕はマークされる。再発動するとマークされた対象までダッシュして追加でダメージを与える。
- **R — 完遂：** 指定方向に跳躍して攻撃した敵にダメージを与える。 再発動: 指定方向にダッシュして、攻撃したすべての敵に対象の減少体力に応じたダメージを与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - Qが増加攻撃力と魔力に応じたダメージを与える。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 477試合、全体勝率 52.4%
- **時間帯別勝率：** 〜20分 55.1%（n=89）、20〜25分 50.0%（n=70）、25〜30分 50.0%（n=104）、30〜35分 47.1%（n=102）、35分〜 58.9%（n=112）
- **最高帯：** 35分〜（判定差 11.9ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Akali` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Akali.png)
