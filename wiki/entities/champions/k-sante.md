---
title: "カ・サンテ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]"
tags:
  - champion
  - role-tank
  - role-fighter
  - data-dragon
champion_id: "KSante"
champion_key: "897"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/KSante.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/KSante.png"
---

# カ・サンテ

![[raw/assets/champions/KSante.png|128]]

## 基本情報

- **英字ID：** `KSante`
- **キー：** `897`
- **称号：** ナズーマの誇り
- **データversion：** `16.18.1`

## 紹介

シュリーマの砂漠に位置する貴重なオアシス、ナズーマ。自らの故郷であるその地を守るため、尊大で勇敢なカ・サンテは巨大な獣や無慈悲な超越者と戦っている。だが、かつての相棒と仲たがいした彼は、民を率いるにふさわしい戦士となるには、成功を求めて身勝手になりがちな自己を抑えなければならないと悟る。それができて初めて、自らのうぬぼれに溺れることなく、民をおびやかす狂暴な怪物を倒すための知恵を見出せるのだ。

## 分類

- **役割タグ：** `Tank`、`Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 8 |
| `magic` | 7 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 625 |
| `hpperlevel` | 120 |
| `mp` | 320 |
| `mpperlevel` | 60 |
| `movespeed` | 330 |
| `armor` | 36 |
| `armorperlevel` | 5.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 2.1 |
| `attackrange` | 150 |
| `hpregen` | 9.5 |
| `hpregenperlevel` | 1 |
| `mpregen` | 7 |
| `mpregenperlevel` | 1 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.688 |

## アビリティ

- **パッシブ — 不屈の本能：** スキルが対象をマークする。マークされた対象への次の通常攻撃は、与えるダメージが増加する。 「オールアウト」中はあらゆる通常攻撃とスキルが与えるダメージが増加する。

- **Q — 破撃のエントーフォ：** 武器を叩きつけ、短い直線上にいた敵にダメージとスロウ効果を与える。 命中時に「破撃のエントーフォ」のスタックを獲得する。2スタックになると衝撃波を放って、敵を自身の方向に引き寄せる。 「オールアウト」中はクールダウンが短縮される。
- **W — 切り開く猛進：** 被ダメージを軽減させながらチャージし、その後ダッシュして敵をノックバックしてスタンさせる。 「オールアウト」中は与ダメージが増加するが、ノックバックとスタンを与えなくなる。
- **E — 辰砂の足取り：** ダッシュしてシールドを獲得する。味方を対象にした場合は距離が増加し、自身と味方の両方がシールドを獲得する。 「オールアウト」中はクールダウンが短縮され、速度が増加する。
- **R — オールアウト：** 敵をノックバックし、敵は通り道のあらゆる壁を通り抜けて弾き飛ばされる。その後、自身は「オールアウト」状態になり、その敵をダッシュして追いかけ、防御力が低下する代わりにダメージと体力回復量が大幅に増加し、スキルが変化する。

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
- **対象試合：** 173試合、全体勝率 46.2%
- **時間帯別勝率：** 〜20分 45.8%（n=24）、20〜25分 42.1%（n=19）、25〜30分 46.9%（n=49）、30〜35分 50.0%（n=44）、35分〜 43.2%（n=37）
- **最高帯：** 30〜35分（判定差 7.9ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-897|カ・サンテの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（501試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3143|ランデュイン オーメン]] + [[wiki/entities/items/item-6662|アイスボーン ガントレット]]（該当n=34、61.8% / 非該当50.1%、差+11.7pt）；[[wiki/entities/items/item-2502|終わりなき絶望]] + [[wiki/entities/items/item-2504|ケイニック ルーケルン]]（該当n=35、60.0% / 非該当50.2%、差+9.8pt）
- **ステータス傾向：** 魔法防御（該当n=407、51.8% / 非該当46.8%、差+5.0pt）
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（n=12（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]]（n=1（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）

### MIDDLE（45試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-2502|終わりなき絶望]] + [[wiki/entities/items/item-6662|アイスボーン ガントレット]]（n=10（15未満）；共通stats: 物理防御・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-3075|ソーンメイル]] + [[wiki/entities/items/item-6662|アイスボーン ガントレット]]（n=9（15未満）；共通stats: 物理防御・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-897|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=792）

- **高勝率コンボ候補：** [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率68.3%（28/41）、n=41（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/garen|ガレン（Garen）]] — 対象側勝率41.0%（16/39）、n=39（十分性の目安を満たす）。

### MIDDLE（対象n=75）

- **高勝率コンボ候補：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.KSante` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/KSante.png)
