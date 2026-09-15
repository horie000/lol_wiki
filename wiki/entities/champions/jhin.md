---
title: "ジン"
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
  - role-marksman
  - role-mage
  - data-dragon
champion_id: "Jhin"
champion_key: "202"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Jhin.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jhin.png"
---

# ジン

![[raw/assets/champions/Jhin.png|128]]

## 基本情報

- **英字ID：** `Jhin`
- **キー：** `202`
- **称号：** 孤高の芸術家
- **データversion：** `16.18.1`

## 紹介

ジンは殺人を芸術であると信じてやまないサイコパスである。かつてアイオニアの牢獄に囚われていた緻密で周到な連続殺人犯は、同国の最高評議会の暗部により釈放され、彼らの陰謀を実行する暗殺者となった。ジンにとって、銃とは絵筆に他ならない。その筆先から生み出される作品は芸術的なまでに残酷であり、犠牲者とオーディエンスは身を震わせながら見ていることしかできない。身の毛もよだつ戯曲を上演することに歪んだ愉悦を覚える彼は、“恐怖”という強烈なメッセージを世に伝えるのに最適なアーティストなのだ。

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 10 |
| `defense` | 2 |
| `magic` | 6 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 655 |
| `hpperlevel` | 107 |
| `mp` | 300 |
| `mpperlevel` | 50 |
| `movespeed` | 330 |
| `armor` | 24 |
| `armorperlevel` | 4.7 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 0 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — この銃の名は｢囁き｣：** ジンの「囁き」は極めて精密に作られた銃である。弾倉は4発、一定の速度でしか発射できないが、最後の弾丸に黒魔術による特殊な効果が生まれ、クリティカル及び減少体力に応じた追加ダメージが発生する。また、クリティカルが発生すると自身の移動速度が増加する。

- **Q — ｢爆ぜ狂う果実｣：** 指定した敵ユニットに特殊なグレネードを放り投げる。グレネードは最大4体まで敵ユニットの上を跳ねながらダメージを与え、ユニットを倒すたびに与えるダメージが増加する。
- **W — ｢死者への狂奏曲｣：** 持っている杖から長射程の弾丸を1発発射する。この弾はミニオンおよびモンスターを貫通するが、敵チャンピオンは貫通しない。命中した対象がその前に味方チャンピオン、「女神の足跡」、またはジンからのダメージを受けていた場合、スネア効果を付与する。
- **E — ｢女神の抱擁｣：** 指定地点に、敵ユニットが上を通過すると花開く「女神の足跡」を設置する。「女神の足跡」は発動すると範囲内の敵ユニットをスロウ状態にし、その後爆発して魔法ダメージを与える。 「死とは、かくも美しい…」 - ジンが敵チャンピオンをキルすると、そのユニットの上で「女神の足跡」が発動し爆発する。
- **R — ｢終演 -フィナーレ-｣：** 詠唱とともに「囁き」と手に持った杖を合体させ、長銃へと変形させる。発射される4発の特殊な弾丸は非常に長い射程距離を持ち、ミニオンおよび中立モンスターを貫通して発射する事ができるが、敵チャンピオンを貫通しない。命中した敵に減少体力に応じたダメージを与え、スロウ効果を付与する。最高の技術で大胆かつ繊細に作り上げられた4発目は、より大きな威力を秘めており確実にクリティカルが発生する。

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
- **対象試合：** 661試合、全体勝率 54.3%
- **時間帯別勝率：** 〜20分 59.8%（n=107）、20〜25分 54.3%（n=92）、25〜30分 51.3%（n=154）、30〜35分 49.7%（n=151）、35分〜 58.0%（n=157）
- **最高帯：** 〜20分（判定差 10.1ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-202|ジンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（1,441試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3094|ラピッド ファイアキャノン]] + [[wiki/entities/items/item-3142|妖夢の霊剣]] + [[wiki/entities/items/item-3170|スイフトマーチ]]（該当n=32、81.2% / 非該当51.2%、差+30.1pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3170|スイフトマーチ]]（該当n=98、79.6% / 非該当49.8%、差+29.8pt）
- **ステータス傾向：** ライフスティール（該当n=74、64.9% / 非該当51.1%、差+13.7pt）；魔法防御（該当n=74、62.2% / 非該当51.3%、差+10.9pt）
- **理論仮説：** [[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-3094|ラピッド ファイアキャノン]]（n=3（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: クリティカル率・移動速度）；[[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-202|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=2,017）

- **高勝率コンボ候補：** [[wiki/entities/champions/zilean|ジリアン（Zilean）]] — 対象側勝率72.5%（29/40）、n=40（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/draven|ドレイヴン（Draven）]] — 対象側勝率32.3%（10/31）、n=31（十分性の目安を満たす）。

### MIDDLE（対象n=13）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Jhin` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jhin.png)
