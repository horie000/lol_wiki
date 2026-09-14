---
title: アイテムのチャンピオン相性タグ分類 v16.18.1
type: synthesis
status: active
created: 2026-09-15
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
tags:
  - league-of-legends
  - item
  - champion
  - classification
  - synergy
---

# アイテムのチャンピオン相性タグ分類 v16.18.1

## 問い

868件のアイテムを、どのようなチャンピオン系統と相性がよいかで検索・絞り込みできるようにする。

## 結論

全アイテムページのフロントマターへ、`champion-synergy-*` 形式のタグを少なくとも1つ付与した。タグはData Dragon v16.18.1の日本語アイテムレコードにある原典タグ、数値ステータス、説明文の効果シグナルから、`scripts/item_synergy.py` が再現可能な規則で生成する。複数の系統に有効なアイテムには複数タグを付ける。

タグは「特定のチャンピオンが常に最適」というビルド断定ではない。原典にはチャンピオン別の購入率・勝率・ビルド順序がないため、チャンピオンの役割・戦闘特性に対応する候補系統を示す分類として扱う。

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
python3 scripts/lint.py
```

`scripts/lint.py` はゴールド効率、相性タグ、パワースパイクを順に検証する。`--check` は868件すべての `item_id` と期待タグが一致すること、`--write` は日付とフロントマターを同期することを確認する。

## 範囲と不確実性

- この分類はData Dragon v16.18.1のアイテム原典だけから作ったヒューリスティックであり、パッチごとの最適ビルド、対面相性、勝率、購入順を表さない。
- Data Dragon の汎用 `tags` は広い分類で、同じタグでも効果の目的が異なることがある。説明文に味方効果がある場合だけサポート点を追加し、自己オーラを自動的にサポート専用とは扱っていない。
- モード限定・内部用・名称空欄のレコードもID単位で保持している。これらは `utility` になる場合があり、通常のサモナーズリフト用ビルドと混同しない。
- 実際に相性のよい個別チャンピオンを確定するには、チャンピオンのスキル係数、パッシブ、対戦環境、ビルド統計を別の原典で追加する必要がある。

## 関連ページ

- [[wiki/concepts/game-data-catalog|ゲームデータ個別ページのカタログ]] — アイテム868件を含む個別ページの配置と原典範囲。
- [[wiki/syntheses/gold-efficiency-stat-values|アイテム金銭効率の基準単価]] — アイテムの基礎ステータスを比較する別軸の分類。
- [[wiki/syntheses/champion-power-spikes-v16-18-1|チャンピオンのパワースパイク分類 v16.18.1]] — チャンピオン側の時間帯シグナル。
- [[wiki/entities/items/item-3031|アイテム個別ページの例]] — タグ、効果、ステータス、ゴールド効率の統合表示。

## 未解決の問い

- 各アイテムタグから個別チャンピオンへの対応を、どのビルド統計・パッチ範囲で検証するか。
- アイテムの自動効果、発動効果、スタック、モード限定効果を役割別に比較する共通指標をどう定義するか。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]] — `data/ja_JP/item.json` のアイテムタグ、ステータス、説明。
- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|チャンピオンデータセット v16.18.1]] — チャンピオン役割タグの語彙。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
