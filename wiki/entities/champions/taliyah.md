---
title: "タリヤ"
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
  - role-mage
  - role-support
  - data-dragon
champion_id: "Taliyah"
champion_key: "163"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Taliyah.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Taliyah.png"
---

# タリヤ

![[raw/assets/champions/Taliyah.png|128]]

## 基本情報

- **英字ID：** `Taliyah`
- **キー：** `163`
- **称号：** ストーンウィーバー
- **データversion：** `16.18.1`

## 紹介

タリヤは少女の好奇心と大人の責任感の間で揺れ動く、シュリーマ出身の流浪のメイジだ。強大さを増す自身の力の本質を知るためヴァロラン全域の旅を続けていた彼女だが、最近になって部族を守るためにシュリーマに戻ってきた。彼女の心の優しさを弱さであると見誤る者は、そのはつらつとした振る舞いの下に潜む、山をも動かす強い意志、そして大地さえ揺るがす断固たる精神のもとに、手痛い代償を払うことになる。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 7 |
| `magic` | 8 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 550 |
| `hpperlevel` | 104 |
| `mp` | 470 |
| `mpperlevel` | 30 |
| `movespeed` | 330 |
| `armor` | 18 |
| `armorperlevel` | 4.7 |
| `spellblock` | 28 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.36 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — ロックサーフィン：** 壁の近くで移動速度が増加する。

- **Q — スレッドボレー：** 自由に移動しながら、指定された方向に石の欠片を連続して発射する。「スレッドボレー」を使用すると、自身の足元に「加工された地面」を作り出す。「加工された地面」上でこのスキルを使用するとその地面を消費して、敵にスロウ効果を与える大きな石を1発投げる。
- **W — サイズミックシャーブ：** 一定範囲の地面を隆起させ、範囲内の敵を指定した方向に飛ばす。
- **E — アンレイベルアース：** 一定範囲内に石をばら撒き、スロウ効果を付与する。この範囲内で敵がダッシュするかノックバックさせられると、石が爆発して対象をスタンさせる。
- **R — ウィーバーウォール：** 長い壁を作り、その上を移動する。

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
- **対象試合：** 73試合、全体勝率 41.1%
- **時間帯別勝率：** 〜20分 30.0%（n=20）、20〜25分 50.0%（n=6）、25〜30分 36.4%（n=11）、30〜35分 38.1%（n=21）、35分〜 60.0%（n=15）
- **最高帯：** 35分〜（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-163|タリヤの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（134試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-3116|リーライ クリスタル セプター]]（該当n=31、58.1% / 非該当39.8%、差+18.3pt）；[[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=55、50.9% / 非該当39.2%、差+11.7pt）
- **ステータス傾向：** 物理防御（該当n=55、52.7% / 非該当38.0%、差+14.8pt）
- **理論仮説：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3040|セラフ エンブレイス]]（n=3（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=2（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

### JUNGLE（39試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（未観測；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-3152|ヘクステック ロケットベルト]] + [[wiki/entities/items/item-4629|コズミック ドライブ]]（n=1（15未満）；共通stats: 魔力・体力／スキル相互作用は未検証）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-163|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=189）

- **高勝率コンボ候補：** [[wiki/entities/champions/ezreal|エズリアル（Ezreal）]] — 対象側勝率53.3%（8/15）、サンプル不足（n=15、十分性の目安30未満）。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

### JUNGLE（対象n=66）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Taliyah` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Taliyah.png)
