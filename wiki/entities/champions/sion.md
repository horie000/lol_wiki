---
title: "サイオン"
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
  - role-tank
  - role-fighter
  - data-dragon
champion_id: "Sion"
champion_key: "14"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Sion.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sion.png"
---

# サイオン

![[raw/assets/champions/Sion.png|128]]

## 基本情報

- **英字ID：** `Sion`
- **キー：** `14`
- **称号：** 不死身の重戦車
- **データversion：** `16.18.1`

## 紹介

サイオンはデマーシア王を素手で絞殺したことでノクサス中で崇敬されていた過去の英雄だったが、死してなお帝国に奉仕させるために、死の淵から甦らされた。邪魔する者は敵も味方も見境なく虐殺する彼に、もはやかつての人間性は残っていない。腐った体にボルトで粗野な鎧を取り付け、強力な斧を振りかざして敵に向かって無謀な突撃を繰り返しながら、彼はなんとか自分の真の姿を思い出そうとしている。

## 分類

- **役割タグ：** `Tank`、`Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 9 |
| `magic` | 3 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 655 |
| `hpperlevel` | 87 |
| `mp` | 400 |
| `mpperlevel` | 52 |
| `movespeed` | 345 |
| `armor` | 36 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.3 |
| `attackspeed` | 0.679 |

## アビリティ

- **パッシブ — 名誉ある死：** サイオンは死亡後、体力が急速に減っていく状態で一時的に復活する。攻撃速度が飛躍的に上昇して通常攻撃で体力を回復するようになり、対象の最大体力に応じた追加ダメージを与える。

- **Q — 破滅の斧：** サイオンが斧を振り上げ、力を溜めてから前方に振り下ろして、範囲内の敵すべてにダメージを与える。十分に力を溜めた状態で振り下ろすと、ダメージに加えて命中した敵がノックアップし、その後スタン状態になる。
- **W — 魂の炉心：** サイオンがシールドを張り、時間が経過するか3秒たった後に再発動すると爆発して、周囲の敵に魔法ダメージを与える。また自動効果として、敵ユニットをキルするたびにサイオンの最大体力が増加する。
- **E — 殺意の雄叫び：** サイオンが短射程の衝撃波を発射し、最初に命中した敵にダメージとスロウ効果を与え、さらに物理防御を低下させる。ミニオンおよび中立モンスターに当たった場合は長い距離をノックバックし、接触した敵すべてにダメージとスロウ効果を与え、さらに物理防御を低下させる。
- **R — 猪突猛進：** サイオンが指定方向に突進し、時間とともに加速してゆく。突進中も、わずかに方向を制御できる。敵チャンピオンか壁に衝突すると停止し、敵チャンピオンの場合は突進距離に応じてダメージを与え、さらにノックアップする。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤、終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中10位（上位15%）。体力655、物理防御36、攻撃力68、移動速度345。
  - 敵ユニットをキルするたびに最大体力が増加する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 347試合、全体勝率 53.9%
- **時間帯別勝率：** 〜20分 46.5%（n=43）、20〜25分 50.0%（n=56）、25〜30分 54.7%（n=75）、30〜35分 59.1%（n=88）、35分〜 54.1%（n=85）
- **最高帯：** 30〜35分（判定差 12.6ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Sion` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sion.png)
