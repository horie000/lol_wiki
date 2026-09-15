---
title: "クレッド"
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
  - role-fighter
  - data-dragon
champion_id: "Kled"
champion_key: "240"
data_version: "16.18.1"
roles:
  - "Fighter"
resource_type: "勇気の護り"
image_path: "raw/assets/champions/Kled.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kled.png"
---

# クレッド

![[raw/assets/champions/Kled.png|128]]

## 基本情報

- **英字ID：** `Kled`
- **キー：** `240`
- **称号：** 狂乱の騎兵
- **データversion：** `16.18.1`

## 紹介

恐れ知らずで粗暴な武人であるヨードルのクレッドは、ノクサスの持つ激情的な無鉄砲さを体現しており、上官には信用されず、貴族には毛嫌いされているが、帝国の兵士たちには愛されている象徴的存在だ。多くの兵士たちが、クレッドは帝国の軍隊が戦ったあらゆる戦争に参加し、あらゆる階級称号を獲得し、そして、戦いにおいて一度たりとも退却したことがないと主張する。細かい部分の信憑性はかなり疑わしいが、クレッドの伝説には一つだけ否定できない事実がある。彼が信頼のおけない愛馬「スカール」に跨って戦場に向かう時、彼は自分のものは...

## 分類

- **役割タグ：** `Fighter`
- **リソース種別：** 勇気の護り

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 2 |
| `magic` | 2 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 410 |
| `hpperlevel` | 84 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 35 |
| `armorperlevel` | 5.2 |
| `spellblock` | 28 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 弱虫トカゲ「スカール」：** クレッドが彼の信頼する愛馬、スカールに騎乗している時は、クレッドの代わりにスカールがダメージを受けてくれる。スカールの体力がなくなるとクレッドはスカールから降ろされる。 非騎乗時はクレッドのスキルが変化して敵チャンピオンに与えるダメージが減少する。クレッドは敵と交戦することでスカールの「勇気」を回復できる。「勇気」が最大になると、クレッドは再び騎乗してスカールの体力を獲得する。

- **Q — トラバサミロープ：** ダメージを与えるトラバサミを投げて、敵チャンピオンに引っ掛ける。引っ掛かった状態を少しの間維持すると、対象に追加物理ダメージを与えて自身の方向に引き寄せる。 非騎乗時では、このスキルは「ポケットピストル」に変化する。これは銃を発砲する遠隔攻撃で、反動で自らを後方に飛ばし、「勇気」を回復する。
- **W — 狂暴の宴：** 次の4回の通常攻撃を繰り出す速度が大きく増加する。4回目の通常攻撃はダメージが増加する。
- **E — ジャウスト：** ダッシュして物理ダメージを与え、一時的に移動速度が増加する。スキルを再使用すると、最初に攻撃した対象にダッシュで戻り、初回と同量のダメージを与える。
- **R — チャァァァァァァァジ！！！：** クレッドとスカールが指定した位置に突撃してシールドを獲得し、通り道に移動速度を増加させる効果を残していく。スカールは最初に遭遇した敵チャンピオンにロックオンして体当たりする。

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
- **対象試合：** 33試合、全体勝率 54.5%
- **時間帯別勝率：** 〜20分 50.0%（n=8）、20〜25分 66.7%（n=6）、25〜30分 62.5%（n=8）、30〜35分 40.0%（n=5）、35分〜 50.0%（n=6）
- **最高帯：** 20〜25分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-240|クレッドの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（87試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-2501|覇王のブラッドメイル]] + [[wiki/entities/items/item-3748|タイタン ハイドラ]]（n=13（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-2501|覇王のブラッドメイル]] + [[wiki/entities/items/item-3181|ハルブレイカー]]（n=8（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-240|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=132）

- **高勝率コンボ候補：** [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率20.0%（3/15）、サンプル不足（n=15、十分性の目安30未満）。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

### MIDDLE（対象n=11）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kled` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kled.png)
