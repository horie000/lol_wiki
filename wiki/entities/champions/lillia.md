---
title: "リリア"
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
  - role-mage
  - data-dragon
champion_id: "Lillia"
champion_key: "876"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Lillia.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lillia.png"
---

# リリア

![[raw/assets/champions/Lillia.png|128]]

## 基本情報

- **英字ID：** `Lillia`
- **キー：** `876`
- **称号：** はにかみ屋の花
- **データversion：** `16.18.1`

## 紹介

極度の恥ずかしがり屋であるリリアは子鹿の妖精で、不安を胸に秘めつつもアイオニアの森の中を歩き回っている。彼女は定命の者たちの謎めいた性質に怯えながらも強い興味をいだいており、彼らの側に身を隠しながら、なぜ彼らの夢が古の「夢の木」に到達しなくなったのか理由を探ろうとしている。現在は魔法の枝を持ってアイオニアを旅しながら、人々のまだ見ぬ夢を探している。その夢を見つけて初めて、リリアは自ら花開き、他者の恐怖を取り除いてその内に眠る輝きを見つけてあげることができる。ひぃあ！

## 分類

- **役割タグ：** `Fighter`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 0 |
| `defense` | 2 |
| `magic` | 10 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 605 |
| `hpperlevel` | 105 |
| `mp` | 410 |
| `mpperlevel` | 50 |
| `movespeed` | 330 |
| `armor` | 22 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 1.55 |
| `attackrange` | 325 |
| `hpregen` | 2.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.95 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.7 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 夢を集める大枝：** スキルでチャンピオンかモンスターを攻撃すると、最大体力に応じた追加ダメージを継続的に与える。

- **Q — 花開く風：** 自動効果で、スキルが敵に命中するたびに増加移動速度のスタックを獲得する。発動効果で周囲の敵に魔法ダメージを与え、端にいる対象には追加確定ダメージを与える。
- **W — ひゃっ、あぶない！：** 周囲の敵にダメージを与える。中央にいた敵には、より大きなダメージを与える。
- **E — コロコロの種：** 落下時に当たった敵にダメージとスロウ効果を与える種を投げる。何にも当たらなかった場合は、壁か対象に当たるまで転がり続ける。
- **R — 夢見の子守唄：** 「夢のかけら」を受けているすべての敵に眠気を付与してから眠らせる。眠った敵は、強制的に目覚めさせられた際に追加ダメージを受ける。

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
- **対象試合：** 349試合、全体勝率 53.9%
- **時間帯別勝率：** 〜20分 59.3%（n=59）、20〜25分 64.9%（n=37）、25〜30分 52.3%（n=88）、30〜35分 50.0%（n=72）、35分〜 50.5%（n=93）
- **最高帯：** 20〜25分（判定差 14.9ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-876|リリアの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（719試合）

- **実測ビルド候補：** メジャイ ソウルスティーラー + ゾーニャの砂時計（該当n=43、81.4% / 非該当51.0%、差+30.4pt）；メジャイ ソウルスティーラー + ゾーニャの砂時計 + ライアンドリーの仮面（該当n=43、81.4% / 非該当51.0%、差+30.4pt）
- **ステータス傾向：** 物理防御（該当n=461、53.1% / 非該当52.3%、差+0.8pt）
- **理論仮説：** 自然の力 + コズミック ドライブ（n=1（15未満）；共通stats: 体力・移動速度／チャンピオン原典にも言及: 体力・移動速度）；メジャイ ソウルスティーラー + リーライ クリスタル セプター + リフトメーカー（n=14（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Lillia` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lillia.png)
