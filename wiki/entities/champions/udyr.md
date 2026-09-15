---
title: "ウディア"
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
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "Udyr"
champion_key: "77"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Udyr.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Udyr.png"
---

# ウディア

![[raw/assets/champions/Udyr.png|128]]

## 基本情報

- **英字ID：** `Udyr`
- **キー：** `77`
- **称号：** 精霊と歩む者
- **データversion：** `16.18.1`

## 紹介

現存するスピリットウォーカーの中でも最大の力を持つウディアは、フレヨルドのあらゆる精霊と心を通わせることができる。彼らの欲求に共感して理解を示したり、その霊的なエネルギーを変換して、自身の原始的な戦闘法に取り入れることができるのだ。自らの心が周囲の心の声に埋もれてしまわないように、ウディアは内なる均衡を求めているが、外の世界についても均衡を欲している──フレヨルドの神秘的な風景は、対立と争いから生まれる成長によってのみ、繁栄することができるのだ。ウディアは、平和という停滞を避けるためには、犠牲を払うこ...

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 7 |
| `magic` | 4 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 664 |
| `hpperlevel` | 92 |
| `mp` | 271 |
| `mpperlevel` | 50 |
| `movespeed` | 350 |
| `armor` | 31 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.65 |

## アビリティ

- **パッシブ — 精霊の繋ぎ手：** 4つの通常スキルで「型」を切り替え、スキルを再発動すると「型」がリフレッシュされて究極の効果を得る。さらに、スキル使用後、次の2回の通常攻撃の攻撃速度が増加する。

- **Q — 野性の爪：** 攻撃速度が増加し、次の2回の通常攻撃が追加物理ダメージを与える。 再発動: 攻撃速度がさらに増加し、次の2回の通常攻撃が対象に電撃を放つようになる。
- **W — 鉄の外皮：** シールドを獲得し、次の2回の通常攻撃で自身の体力を回復する。 再発動: より耐久値の高いシールドを獲得し、数秒間かけて最大体力の一定割合を回復する。
- **E — 焔の猛進：** 移動速度が増加し、各対象への最初の通常攻撃が対象をスタンさせる。 再発動: 少しの間、移動速度がさらに増加し、移動不能効果を受けなくなる。
- **R — 氷翼の嵐：** 極寒の嵐に身を包み、周囲の敵にダメージとスロウ効果を与える。 再発動: 嵐を強化して解き放ち、敵を追跡させて追加ダメージを与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中15位（上位15%）。体力664、物理防御31、攻撃力62、移動速度350。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 判定保留（分母不足）
- **対象試合：** 95試合、全体勝率 55.8%
- **時間帯別勝率：** 〜20分 53.3%（n=15）、20〜25分 66.7%（n=12）、25〜30分 45.5%（n=22）、30〜35分 63.0%（n=27）、35分〜 52.6%（n=19）
- **最高帯：** 20〜25分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-77|ウディアの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（150試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 物理防御（該当n=104、48.1% / 非該当41.3%、差+6.8pt）；魔法防御（該当n=72、48.6% / 非該当43.6%、差+5.0pt）
- **理論仮説：** トリニティ フォース + ストライドブレイカー（n=3（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；実験的ヘクスプレート + トリニティ フォース（n=1（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）

### TOP（80試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 魔法防御（該当n=38、71.1% / 非該当50.0%、差+21.1pt）；マナ（該当n=47、66.0% / 非該当51.5%、差+14.4pt）
- **理論仮説：** トリニティ フォース + ストライドブレイカー（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；バンドルパイプ + 変幻自在のジャック＝ショー（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Udyr` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Udyr.png)
