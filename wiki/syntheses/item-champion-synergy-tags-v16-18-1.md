---
title: アイテムのチャンピオン相性タグ分類 v16.18.1
type: synthesis
status: active
created: 2026-09-15
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
tags:
  - league-of-legends
  - item
  - champion
  - classification
  - synergy
  - empirical-analysis
---

# アイテムのチャンピオン相性タグ分類 v16.18.1

## 問い

868件のアイテムを、どのようなチャンピオン系統と相性がよいかで検索・絞り込みできるようにする。

## 結論

全アイテムページのフロントマターへ、`champion-synergy-*` 形式のタグを少なくとも1つ付与した。タグはData Dragon v16.18.1の日本語アイテムレコードにある原典タグ、数値ステータス、説明文の効果シグナルから、`scripts/item_synergy.py` が再現可能な規則で生成する。複数の系統に有効なアイテムには複数タグを付ける。

タグは「特定のチャンピオンが常に最適」というビルド断定ではない。原典にはチャンピオン別の購入率・勝率・ビルド順序がないため、チャンピオンの役割・戦闘特性に対応する候補系統を示す分類として扱う。

## 実試合データによる再評価

原典由来のタグが実戦の選択とどの程度対応するかを確認するため、収集済みMatch-v5データから `champion_id × 正規化ロール × item_id` を集計した。通常スロット `item0`〜`item5` の最終所持を参加者単位で重複排除し、同じチャンピオン・ロールでの「所持時勝率」と「非所持時勝率」の差を記録している。`item6`、消耗品、視界、トリンケット等は既定集計から除外した。

集計スクリプトは `scripts/riot_champion_item_synergy.py`、最新の全体スナップショットは `reports/riot-champion-item-synergy/run-20260915T060638Z/` に保存した。Data Dragon v16.18.1と `16.18` パッチを揃える以前の確認用スナップショットは `reports/riot-champion-item-synergy-patch-16-18/run-20260915T013049Z/` に残している。CSV/JSONの最小ゲーム数は15、Markdownの上位表は該当・非該当双方30ゲームを既定とする。

### 観測結果（最新スナップショット）

- 最新スナップショットは入力レコード13,736件からユニーク完全試合9,736件を得て、個別アイテム4,908行、ステータス群1,908行、完成アイテム中核5,988行、理論仮説候補25,426行を出力した。現在のData Dragonで名称・タグを解決できないアイテム所持観測は品質情報へ記録している。
- ステータス群では、クリティカル率（`FlatCritChanceMod`）を持つアイテムを1つ以上所持した場合、Jinx BOTTOMは1,354試合で勝率53.6%、非該当183試合で30.1%（差+23.6ポイント）、Ashe BOTTOMは1,560試合で50.3%対165試合で33.3%（差+17.0ポイント）、Yone MIDDLEは1,007試合で52.0%対180試合で36.7%（差+15.4ポイント）だった。これは「同じステータス群を持つアイテムをよく持つ」ことと勝率差を同時に見た例であり、クリティカル率の合計値やアイテム間の因果的シナジーを測ったものではない。
- ビルド中核の実測候補では、Akali MIDDLEの「メジャイ ソウルスティーラー + ヘクステック ガンブレード」が45試合で97.8%、非該当922試合で49.0%（差+48.8ポイント）だった。極端な差は候補抽出には有用だが、メジャイのスタック、勝勢での完成、生存者バイアスを含むため、推奨ビルドと断定しない。
- 以前のスナップショット同様、出場数が多い選択と勝率差は一致しない。例えば頻出するクリティカル率群でも MissFortune BOTTOM は1,549試合で51.8%、非該当205試合で45.9%（差+6.0ポイント）、Caitlyn BOTTOMは1,369試合で49.5%対65試合で50.8%（差-1.2ポイント）だった。採用頻度と相関差は分けて読む。
- マイナス差も同じように因果的な弱さとは読めない。たとえば最新スナップショットのYone MIDDLEのヴァンパイア セプターは66試合で所持時21.2%、非所持1,121試合で51.4%（差-30.2ポイント）だったが、不利な試合でそのアイテムを選ぶこと、パッチ差、構成差が混ざる。負の差を理由に個別ページのタグを削除しない。
- 現行Data Dragon v16.18.1で表示名・タグを解決できない過去アイテムIDは未知のまま保持し、推測で現行アイテムへ統合しない。厳密な相性確認はパッチごとの原典を揃えて行う。
- ステータス群とビルド中核は `maps["11"]` が真のアイテムに限定した。最新結果のビルド・理論候補でマップ11対象外だったアイテムIDは0件だった。

### ステータス群とチャンピオン別ファイル

`champions/champion-<champion_id>.md` に、データ上で対象になったチャンピオンごとの分析ファイルを生成した。各ファイルはロール別に、実測で最小ゲーム数と双方分母を満たす個別アイテム・ステータス群・完成アイテム中核を「推奨候補」として、実測不足または未観測で共通ステータスから機械的に導いた組み合わせを「理論仮説」として分離している。

Wikiでは173件の `wiki/entities/champions/` をチャンピオン情報の入口とし、各ページへ最大2ロール・各2候補の短い生成ブロックを同期した。ブロックは同一スナップショットの詳細レポートへ直接リンクする。同期は `scripts/riot_champion_build_wiki_sync.py` の `--dry-run`、`--write`、`--check` を明示的に使い、解析実行だけではentityを変更しない。

ステータス群の判定はData Dragon `item.json` の `stats` フィールドに限定した。クリティカル率は `FlatCritChanceMod`、攻撃力は `FlatPhysicalDamageMod` のように判定し、同一参加者が同群のアイテムを複数持っていても該当1回と数える。説明文の発動効果やチャンピオンのスキル相互作用は理論仮説へ自動的に加えていない。

理論仮説は「共有ステータスがあるため検証する価値がある」という候補生成であり、理論上強いと確定したビルドではない。チャンピオンのスキル係数、ダメージ計算、対面、防御値、パッチを含む別の検証が必要である。

### 見直しの判断

実試合データは、既存タグを置き換える根拠ではなく、タグから個別チャンピオンへ掘り下げる候補抽出層として追加する。現時点では、原典シグナルによる `champion-synergy-*` タグを検索用の広い分類として保持し、実試合の所持時・非所持時差は別レポートで確認する。パッチ、ロール、試合時間、対面、購入時点を揃えた追加分析なしに、個別アイテムのタグを勝率順へ書き換えない。

## タグの語彙

| タグ                          | 相性候補となるチャンピオン系統                     | 主な原典シグナル                                           |
| --------------------------- | ----------------------------------- | -------------------------------------------------- |
| `champion-synergy-marksman` | マークスマン、通常攻撃を主なダメージ源とする射撃型           | クリティカル、攻撃速度、通常攻撃時効果、ライフスティール                       |
| `champion-synergy-fighter`  | ファイター、近接の継続戦闘型・物理ブルーザー              | 攻撃力、体力、スキルヘイスト、通常攻撃時効果、物理防御貫通                      |
| `champion-synergy-assassin` | アサシン、短時間のバーストを狙う物理型                 | 脅威・物理防御貫通、ステルス、攻撃的な発動効果                            |
| `champion-synergy-mage`     | メイジ、魔力とスキルダメージを主軸とする型               | 魔力、魔法防御貫通、マナ、スキルヘイスト、スペルヴァンプ                       |
| `champion-synergy-tank`     | タンク、前衛・耐久を主軸とする型                    | 体力、物理防御、魔法防御、行動妨害耐性、被ダメージ軽減                        |
| `champion-synergy-support`  | サポート、味方への回復・シールド・視界・収入支援を担う型        | 味方効果、オーラ、ゴールド生成、視界、マナ自動回復                          |
| `champion-synergy-jungler`  | ジャングラー、原典でジャングル利用が明示された型            | Data Dragon の `Jungle` タグ                          |
| `champion-synergy-utility`  | 複数ポジションで使う汎用品、消耗品、トリンケット、特殊・内部用レコード | `Consumable`、`Trinket`、`Vision`、`Stealth`、判定不能なデータ |

チャンピオンの原典役割語彙は[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|チャンピオンデータセット]]の `Mage`、`Fighter`、`Assassin`、`Tank`、`Support`、`Marksman` に対応させた。「ジャングラー」はチャンピオン固有の役割タグではなく、アイテム原典にある利用位置のシグナルである。

### タグを読むときのチャンピオン例

以下はタグの意味を具体化するための役割例であり、該当アイテムがそのチャンピオンの最適解だと断定するものではない。

- `marksman`：[[wiki/entities/champions/jinx|ジンクス]]、[[wiki/entities/champions/caitlyn|ケイトリン]]、[[wiki/entities/champions/vayne|ヴェイン]]。
- `fighter`：[[wiki/entities/champions/aatrox|エイトロックス]]、[[wiki/entities/champions/darius|ダリウス]]、[[wiki/entities/champions/camille|カミール]]。
- `assassin`：[[wiki/entities/champions/akali|アカリ]]、[[wiki/entities/champions/zed|ゼド]]、[[wiki/entities/champions/khazix|カ＝ジックス]]。
- `mage`：[[wiki/entities/champions/ahri|アーリ]]、[[wiki/entities/champions/syndra|シンドラ]]、[[wiki/entities/champions/viktor|ビクター]]。
- `tank`：[[wiki/entities/champions/ornn|オーン]]、[[wiki/entities/champions/malphite|マルファイト]]、[[wiki/entities/champions/sion|サイオン]]。
- `support`：[[wiki/entities/champions/janna|ジャンナ]]、[[wiki/entities/champions/thresh|スレッシュ]]、[[wiki/entities/champions/lulu|ルル]]。
- `jungler`：固定のチャンピオン役割タグではなく、原典の `Jungle` 指定を持つアイテムを、ジャングルを担当するチャンピオンが検討するという意味である。
- `utility`：チャンピオン固有の系統を限定せず、消耗品・視界・モード専用・内部用レコードとして扱うという意味である。

## 付与方法

1. `data/ja_JP/item.json` の `tags`、`stats`、説明文をアイテムIDごとに読み込む。
2. クリティカル・攻撃速度・通常攻撃時効果、攻撃力・体力・貫通、魔力・マナ、防御値、味方効果・視界などを役割別に加点する。
3. 最高点から1点以内で、かつ3点以上の役割を併記する。したがって、例えば物理クリティカル品はマークスマンとファイターの両方になり得る。
4. `Jungle` は他の役割スコアにかかわらず `champion-synergy-jungler` を残す。消耗品・視界品・トリンケットには `champion-synergy-utility` を併記する場合がある。
5. 説明・ステータスが空の内部用レコード、ランダム効果やプレースホルダーを含むレコードは、特定の役割へ推測で割り当てず `champion-synergy-utility` とする。

生成時の分類タグ件数（タグの重複を許す）は次のとおりである。

| タグ | 件数 |
| --- | ---: |
| `champion-synergy-marksman` | 160 |
| `champion-synergy-fighter` | 229 |
| `champion-synergy-assassin` | 42 |
| `champion-synergy-mage` | 201 |
| `champion-synergy-tank` | 162 |
| `champion-synergy-support` | 112 |
| `champion-synergy-jungler` | 26 |
| `champion-synergy-utility` | 196 |

## 個別ページの例

- [[wiki/entities/items/item-3031|インフィニティ エッジ]] — `champion-synergy-marksman` と `champion-synergy-fighter`。クリティカル率と攻撃力を持つ。
- [[wiki/entities/items/item-6655|ルーデン エコー]] — `champion-synergy-mage`。魔力・マナ・スキルヘイストとダメージ効果を持つ。
- [[wiki/entities/items/item-3109|騎士の誓い]] — `champion-synergy-tank` と `champion-synergy-support`。体力・防御力に加えて味方を守る効果がある。
- [[wiki/entities/items/item-1040|オブシディアン エッジ]] — `champion-synergy-jungler`。原典の `Jungle` タグを保持するジャングル用初期アイテムである。
- [[wiki/entities/items/item-2055|コントロール ワード]] — `champion-synergy-utility`。視界・消耗品として特定の戦闘役割を推測しない。
- [[wiki/entities/items/item-3179|アンブラル グレイブ]] — ファイター／アサシン向けの攻撃性能と、視界破壊による汎用性を併せ持つため、複数タグになる。

## タグ別の代表アイテム（各5件）

以下は、各タグが付いたアイテムの中から、原典のステータス・効果がそのタグを直接示すものを5件ずつ選んだ例である。複数タグを持つアイテムは、ここでも複数の系統に登場し得る。個別ページの効果・価格・ゴールド効率は各リンク先で確認できる。

### `champion-synergy-marksman`

1. [[wiki/entities/items/item-3031|インフィニティ エッジ]] — 攻撃力とクリティカル率、クリティカルダメージを持つ。
2. [[wiki/entities/items/item-3006|バーサーカー ブーツ]] — 攻撃速度を大きく伸ばすブーツ。
3. [[wiki/entities/items/item-3046|ファントム ダンサー]] — クリティカル率・攻撃速度・移動速度を同時に持つ。
4. [[wiki/entities/items/item-3085|ルナーン ハリケーン]] — クリティカル・攻撃速度に加え、通常攻撃を追加対象へ拡散する。
5. [[wiki/entities/items/item-6672|クラーケン スレイヤー]] — 攻撃速度と通常攻撃3回ごとの追加物理ダメージを持つ。

### `champion-synergy-fighter`

1. [[wiki/entities/items/item-3071|ブラック クリーバー]] — 攻撃力・体力・スキルヘイストと、物理防御低下の継続戦闘効果を持つ。
2. [[wiki/entities/items/item-3078|トリニティ フォース]] — 攻撃力・攻撃速度・体力・スキルヘイストと、通常攻撃強化を併せ持つ。
3. [[wiki/entities/items/item-3053|ステラックの篭手]] — 体力・行動妨害耐性・増加攻撃力と、危険時のシールドを持つ。
4. [[wiki/entities/items/item-3074|ラヴァナス ハイドラ]] — 攻撃力・スキルヘイスト・ライフスティールと、範囲攻撃を持つ。
5. [[wiki/entities/items/item-6631|ストライドブレイカー]] — 攻撃力・攻撃速度・体力と、接近を補助するスロウを持つ。

### `champion-synergy-assassin`

1. [[wiki/entities/items/item-3142|妖夢の霊剣]] — 攻撃力・脅威・非戦闘時移動速度と、移動速度を得る発動効果を持つ。
2. [[wiki/entities/items/item-6697|ヒュブリス]] — 攻撃力・脅威・スキルヘイストに加え、キルで攻撃力が増加する。
3. [[wiki/entities/items/item-6698|プロフェイン ハイドラ]] — 攻撃力・脅威・スキルヘイストと、近距離範囲攻撃の発動効果を持つ。
4. [[wiki/entities/items/item-6696|アクシオム アーク]] — 攻撃力・脅威・スキルヘイストと、キル時のアルティメット短縮を持つ。
5. [[wiki/entities/items/item-6701|オポチュニティー]] — 攻撃力・脅威と、非戦闘時の脅威増加・キル時の移動速度を持つ。

### `champion-synergy-mage`

1. [[wiki/entities/items/item-6655|ルーデン エコー]] — 魔力・マナ・スキルヘイストと、スキル命中時の追加魔法ダメージを持つ。
2. [[wiki/entities/items/item-3089|ラバドン デスキャップ]] — 高い魔力と、合計魔力を割合で増幅する効果を持つ。
3. [[wiki/entities/items/item-3135|ヴォイド スタッフ]] — 魔力と割合魔法防御貫通を持つ。
4. [[wiki/entities/items/item-3003|アークエンジェル スタッフ]] — 魔力・マナ・スキルヘイストと、マナ蓄積・魔力変換を持つ。
5. [[wiki/entities/items/item-3157|ゾーニャの砂時計]] — 魔力・物理防御と、短時間の時停止を持つ。

### `champion-synergy-tank`

1. [[wiki/entities/items/item-3068|サンファイア イージス]] — 体力・物理防御・スキルヘイストと、周囲へ継続ダメージを与えるオーラを持つ。
2. [[wiki/entities/items/item-3075|ソーンメイル]] — 体力・物理防御と、通常攻撃への反射・負傷効果を持つ。
3. [[wiki/entities/items/item-3143|ランデュイン オーメン]] — 体力・物理防御、クリティカルダメージ軽減、範囲スロウを持つ。
4. [[wiki/entities/items/item-4401|自然の力]] — 体力・魔法防御・移動速度と、魔法ダメージを受けた後の耐久強化を持つ。
5. [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]] — 体力・物理防御・魔法防御と、戦闘中の防御力増加を持つ。

### `champion-synergy-support`

1. [[wiki/entities/items/item-3109|騎士の誓い]] — 味方の被ダメージを肩代わりし、味方のダメージに応じて回復する。
2. [[wiki/entities/items/item-2065|シュレリアの戦歌]] — 味方全体の移動速度を上げる発動効果を持つ。
3. [[wiki/entities/items/item-3190|ソラリのロケット]] — 周囲の味方へシールドを付与する。
4. [[wiki/entities/items/item-6617|ムーンストーンの再生]] — 味方への回復・シールドを別の味方へ連鎖させる。
5. [[wiki/entities/items/item-3107|リデンプション]] — 離れた味方を回復し、敵へ確定ダメージを与える発動効果を持つ。

### `champion-synergy-jungler`

1. [[wiki/entities/items/item-1035|残炎のナイフ]] — `Jungle` 指定があり、チャレンジ・スマイトへ進化する。
2. [[wiki/entities/items/item-1039|氷雨の刃]] — `Jungle` 指定があり、チル・スマイトへ進化する。
3. [[wiki/entities/items/item-1040|オブシディアン エッジ]] — `Jungle` 指定があり、アタックスマイトへ進化する。
4. [[wiki/entities/items/item-1101|スコーチクロウの幼体]] — ジャングルコンパニオンが攻撃を強化し、敵を炎上・スロウさせる。
5. [[wiki/entities/items/item-1102|ガストウォーカーの幼体]] — ジャングルコンパニオンの成長後、茂みでの移動速度を強化する。

### `champion-synergy-utility`

1. [[wiki/entities/items/item-2055|コントロール ワード]] — 敵のステルスワード・トラップ・カモフラージュを可視化する消耗品。
2. [[wiki/entities/items/item-3340|ステルス ワード]] — 一定時間の視界を提供するトリンケット。
3. [[wiki/entities/items/item-3364|オラクル レンズ]] — 敵のワードやトラップを検出するトリンケット。
4. [[wiki/entities/items/item-2031|詰め替えポーション]] — ショップで補充できる継続的なレーン回復手段。
5. [[wiki/entities/items/item-3158|アイオニア ブーツ]] — 特定の攻撃属性に限定されず、スキルの再使用間隔を短縮するブーツ。

個別ページでは、従来の `item`、`data-dragon` タグとこの分類タグを同じフロントマターで管理する。例えば、次のように検索できる。

```yaml
tags:
  - item
  - data-dragon
  - champion-synergy-marksman
  - champion-synergy-fighter
```

Obsidianの検索欄では、例えば `tag:#champion-synergy-marksman` や `tag:#champion-synergy-support` を指定して、該当するアイテムページだけを絞り込める。

## 再生成と検証

分類を更新するときは、原典を読み直して全ページを同期する。

```bash
python3 scripts/item_synergy.py --write
python3 scripts/item_synergy.py --check
python3 scripts/riot_champion_item_synergy.py \
  --input raw/sources/riot-ranked-matches \
  --output reports/riot-champion-item-synergy
python3 scripts/riot_champion_build_wiki_sync.py \
  --analysis reports/riot-champion-item-synergy/run-YYYYMMDDTHHMMSSZ/analysis.json \
  --dry-run
python3 scripts/riot_champion_build_wiki_sync.py \
  --analysis reports/riot-champion-item-synergy/run-YYYYMMDDTHHMMSSZ/analysis.json \
  --write
python3 scripts/riot_champion_build_wiki_sync.py \
  --analysis reports/riot-champion-item-synergy/run-YYYYMMDDTHHMMSSZ/analysis.json \
  --check
python3 scripts/lint.py
```

`scripts/lint.py` はゴールド効率、相性タグ、パワースパイクを順に検証する。`--check` は868件すべての `item_id` と期待タグが一致すること、`--write` は日付とフロントマターを同期することを確認する。

## 範囲と不確実性

- この分類はData Dragon v16.18.1のアイテム原典だけから作ったヒューリスティックであり、パッチごとの最適ビルド、対面相性、勝率、購入順を表さない。
- 実試合レポートは最終アイテムの所持時・非所持時を比較する記述統計であり、試合時間、勝敗後まで生存したこと、プレイヤー、対面、構成、パッチ、逆因果を調整していない。勝率差から因果的なシナジーや弱さを推定しない。
- ステータス群はアイテムの合計ステータス、発動効果、固有効果、同時採用による非線形な閾値を表さない。完成アイテム中核は最終所持集合からの順不同組み合わせで、購入順・購入時刻・途中段階の強さを表さない。
- チャンピオン別の「推奨候補」は探索上の優先確認対象であり、理論仮説はData Dragonの共通ステータスだけから作った未検証候補である。実戦での最適ビルドを自動確定していない。
- 複数パッチの探索結果は、現在のData DragonでアイテムIDの表示名・タグを解決している。アイテム定義が変わったIDを厳密に比較する場合は、パッチと対応するData Dragonを揃える。
- Data Dragon の汎用 `tags` は広い分類で、同じタグでも効果の目的が異なることがある。説明文に味方効果がある場合だけサポート点を追加し、自己オーラを自動的にサポート専用とは扱っていない。
- モード限定・内部用・名称空欄のレコードもID単位で保持している。これらは `utility` になる場合があり、通常のサモナーズリフト用ビルドと混同しない。
- 実際に相性のよい個別チャンピオンを確定するには、チャンピオンのスキル係数、パッシブ、対戦環境、ビルド統計を別の原典で追加する必要がある。

## 関連ページ

- [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]] — 最新スナップショットの入力範囲、方法、品質、主要観測。
- [[wiki/concepts/game-data-catalog|ゲームデータ個別ページのカタログ]] — アイテム868件を含む個別ページの配置と原典範囲。
- [[wiki/syntheses/gold-efficiency-stat-values|アイテム金銭効率の基準単価]] — アイテムの基礎ステータスを比較する別軸の分類。
- [[wiki/syntheses/champion-power-spikes-v16-18-1|チャンピオンのパワースパイク分類 v16.18.1]] — チャンピオン側の時間帯シグナル。
- [[wiki/entities/items/item-3031|アイテム個別ページの例]] — タグ、効果、ステータス、ゴールド効率の統合表示。

## 未解決の問い

- 各アイテムタグから個別チャンピオンへの対応を、パッチ・ロール・試合時間・対面を揃えたどのビルド統計で検証するか。
- アイテムの自動効果、発動効果、スタック、モード限定効果を役割別に比較する共通指標をどう定義するか。
- Timelineまたは購入時刻を含むデータで、最終所持の生存者バイアスをどこまで分離できるか。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]] — `data/ja_JP/item.json` のアイテムタグ、ステータス、説明。
- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|チャンピオンデータセット v16.18.1]] — チャンピオン役割タグの語彙。
- [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]] — 実試合スナップショットの範囲、品質、記述統計。
- 実試合データ：`raw/sources/riot-ranked-matches/` — 収集時点の観測ランク帯を付与したMatch-v5 JSONLとキャッシュ。解析時点のスナップショットは各レポートの `quality.json` に記録。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
