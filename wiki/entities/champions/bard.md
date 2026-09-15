---
title: "バード"
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
  - role-support
  - role-mage
  - data-dragon
champion_id: "Bard"
champion_key: "432"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Bard.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Bard.png"
---

# バード

![[raw/assets/champions/Bard.png|128]]

## 基本情報

- **英字ID：** `Bard`
- **キー：** `432`
- **称号：** 流離いの庇護者
- **データversion：** `16.18.1`

## 紹介

星の向こうからやってきた旅人であるバードは幸運の使者であり、生命が混沌の無関心に耐えられる平衡を保つために戦っている。ルーンテラにはこの世のものとは思えない彼の不思議な性質を伝える歌が数多く残っているが、誰もがこの宇宙の放浪者は強力な魔法の力を宿す遺物を求めてやってきたのだと考えている。自身の手伝いをする陽気な精霊のミィプたちに囲まれたバードの行動には、悪意など一切感じられない。彼は大いなる善のために活動している…彼ならではの不思議なやり方で。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 4 |
| `magic` | 5 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 103 |
| `mp` | 350 |
| `mpperlevel` | 50 |
| `movespeed` | 335 |
| `armor` | 32 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 500 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 52 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 旅人の呼び声：** ミィプ: ミィプと呼ばれる精霊を呼び寄せて通常攻撃を支援させ、追加魔法ダメージを与える。一定数のチャイムを集めると、ミィプの攻撃が範囲攻撃になり、命中した敵にスロウ効果も与えるようになる。 いにしえの鐘: 古代のチャイムがランダムに出現し、回収するたびに経験値を獲得して、マナが回復するほか、非戦闘時の移動速度が増加する。

- **Q — 宇宙の法則：** 魔法のエネルギーを発射し、最初に命中した敵にスロウを与える。貫通したエネルギーが壁に当たった場合は最初の対象が、別の敵ユニットに当たった場合は両方の対象がスタン状態になる。
- **W — 回復の遺物：** 体力を回復する遺物を出現させる。遺物は短時間徐々に効果が増大し、最初に触れた味方の体力を回復して移動速度を増加させると消滅する。
- **E — 精霊の旅路：** 付近の地形に一方通行の魔法のトンネルを出現させる。敵も味方も同じようにトンネルを通り抜けられるが、レベルに応じて味方が通り抜ける速度は増加する。
- **R — 運命の調律：** 精霊の魔力を放つ。魔力は放物線を描いて飛んでいき、着弾と同時に範囲内のすべてのユニットとタワーをしばらく停止させる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 一定数のチャイムでミィプの通常攻撃が範囲攻撃・スロウへ強化される。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 判定保留（分母不足）
- **対象試合：** 54試合、全体勝率 50.0%
- **時間帯別勝率：** 〜20分 71.4%（n=7）、20〜25分 75.0%（n=8）、25〜30分 45.5%（n=11）、30〜35分 43.8%（n=16）、35分〜 33.3%（n=12）
- **最高帯：** 20〜25分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Bard` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Bard.png)
