---
title: "ルシアン"
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
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection]]"
tags:
  - champion
  - role-marksman
  - role-assassin
  - data-dragon
champion_id: "Lucian"
champion_key: "236"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Lucian.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lucian.png"
---

# ルシアン

![[raw/assets/champions/Lucian.png|128]]

## 基本情報

- **英字ID：** `Lucian`
- **キー：** `236`
- **称号：** 不浄殲滅者
- **データversion：** `16.18.1`

## 紹介

光の番人であるルシアンは、二挺の古の拳銃を携え、亡者の魂を追い詰めて浄化するハンターだ。亡霊スレッシュに妻を殺されたルシアンは、復讐の道へと乗り出したが、彼女が蘇ってもその怒りが消えることはなかった。情け容赦なくひたむきなルシアンは、「黒き霧」に潜む古の亡霊の脅威から人々を護るためなら手段を選ばない。

## 分類

- **役割タグ：** `Marksman`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 641 |
| `hpperlevel` | 100 |
| `mp` | 320 |
| `mpperlevel` | 43 |
| `movespeed` | 335 |
| `armor` | 28 |
| `armorperlevel` | 4.2 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 500 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.638 |

## アビリティ

- **パッシブ — 二挺拳銃：** スキルを使用するたびに、次の通常攻撃が2連射になる。味方から体力回復効果またはシールドを付与されるか、自身の周囲で敵チャンピオンが移動不能効果を受けると、次の2回の通常攻撃が追加魔法ダメージを与える。

- **Q — ピアシングライト：** 指定した敵ユニットへ光線を発射する。光線はその軌道上にいるすべての敵ユニットにダメージを与える。
- **W — アーデントブレイズ：** 指定方向に星形に爆発するエネルギーを発射する。命中した敵ユニットには印が付与され、一時的に可視状態になる。印が付いた敵を攻撃するとルシアンの移動速度が増加する。
- **E — スライド：** 短距離を素早く移動する。「二挺拳銃」の通常攻撃が敵に命中するたびに、このスキルのクールダウンが短縮される。
- **R — 二挺掃射：** 二挺拳銃を構えて弾丸を高速で連射する。

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
- **対象試合：** 185試合、全体勝率 44.9%
- **時間帯別勝率：** 〜20分 47.4%（n=38）、20〜25分 47.4%（n=19）、25〜30分 47.8%（n=46）、30〜35分 34.2%（n=38）、35分〜 47.7%（n=44）
- **最高帯：** 25〜30分（判定差 13.6ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-236|ルシアンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（532試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-6676|コレクター]]（該当n=31、71.0% / 非該当46.7%、差+24.3pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3036|ドミニク リガード]] + [[wiki/entities/items/item-3508|エッセンス リーバー]]（該当n=100、61.0% / 非該当45.1%、差+15.9pt）
- **ステータス傾向：** クリティカル率（該当n=500、48.8% / 非該当37.5%、差+11.3pt）；攻撃速度（該当n=463、49.5% / 非該当39.1%、差+10.3pt）
- **理論仮説：** [[wiki/entities/items/item-3814|ナイト エッジ]] + [[wiki/entities/items/item-6609|ケミパンク チェーンソード]]（未観測；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-6609|ケミパンク チェーンソード]]（未観測；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-236|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=796）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率67.6%（23/34）、n=34（十分性の目安を満たす）。
  - [[wiki/entities/champions/darius|ダリウス（Darius）]] — 対象側勝率58.1%（18/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/milio|ミリオ（Milio）]] — 対象側勝率54.1%（33/61）、n=61（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率36.2%（17/47）、n=47（十分性の目安を満たす）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率39.1%（18/46）、n=46（十分性の目安を満たす）。
  - [[wiki/entities/champions/sivir|シヴィア（Sivir）]] — 対象側勝率40.6%（13/32）、n=32（十分性の目安を満たす）。

### MIDDLE（対象n=17）

- **高勝率コンボ候補（最大3件）：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **低勝率カウンターピック候補（最大3件）：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合20,010件、[[reports/riot-ranked-match-analysis/run-20260915T103154Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### BOTTOM（対象1,324試合、全体勝率48.3%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：プレスアタック／冷静沈着・レジェンド: 血脈・最期の慈悲；副系天啓：ビスケットデリバリー・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 300/1,324 | 22.7% | 47.0% |
| 2 | 主系栄華：プレスアタック／冷静沈着・レジェンド: 血脈・切り崩し；副系天啓：キャッシュバック・トリプル トニック；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 98/1,324 | 7.4% | 54.1% |
| 3 | 主系栄華：プレスアタック／冷静沈着・レジェンド: 血脈・最期の慈悲；副系天啓：魔法の靴・ビスケットデリバリー；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 89/1,324 | 6.7% | 55.1% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Lucian` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lucian.png)
