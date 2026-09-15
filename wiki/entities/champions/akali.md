---
title: "アカリ"
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
  - role-assassin
  - data-dragon
champion_id: "Akali"
champion_key: "84"
data_version: "16.18.1"
roles:
  - "Assassin"
resource_type: "気"
image_path: "raw/assets/champions/Akali.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Akali.png"
---

# アカリ

![[raw/assets/champions/Akali.png|128]]

## 基本情報

- **英字ID：** `Akali`
- **キー：** `84`
- **称号：** 主なき暗殺者
- **データversion：** `16.18.1`

## 紹介

「均衡の守人」であることをやめ、「影の拳」という立場も捨てたアカリは、自分こそ故郷の人々が必要としている武器になろうと決め、独り戦いに挑む。師であるシェンから授かった教えを忘れることなく、アイオニアを襲う敵をひとりずつ、確実に排除すると誓ったのである。アカリは音もなく襲い掛かるが、そのメッセージは誰の耳にも届くだろう──主なき暗殺者を恐れよ、と。

## 分類

- **役割タグ：** `Assassin`
- **リソース種別：** 気

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 3 |
| `magic` | 8 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 119 |
| `mp` | 200 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 23 |
| `armorperlevel` | 4.7 |
| `spellblock` | 37 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 50 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.2 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 刺客の刻印：** チャンピオンにスキルでダメージを与えると対象の周囲に気の輪が形成される。輪の外に出るとアカリの次の通常攻撃の射程とダメージが増加する。

- **Q — 五連苦無：** 5本のクナイを投げて自身の増加攻撃力と魔力に応じたダメージを与えてスロウ効果を与える。
- **W — 黄昏の帳：** 姿を隠すための煙幕を張り、少しの間だけ移動速度が増加する。「帳」の中ではインビジブル状態になり、敵のスキルや通常攻撃で対象指定されなくなる。通常攻撃を行うかスキルを使用すると一時的に可視化される。
- **E — 翻身手裏剣：** 後方に宙返りして前方に手裏剣を投げ、魔法ダメージを与える。最初に当たった敵または煙幕はマークされる。再発動するとマークされた対象までダッシュして追加でダメージを与える。
- **R — 完遂：** 指定方向に跳躍して攻撃した敵にダメージを与える。 再発動: 指定方向にダッシュして、攻撃したすべての敵に対象の減少体力に応じたダメージを与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - Qが増加攻撃力と魔力に応じたダメージを与える。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 477試合、全体勝率 52.4%
- **時間帯別勝率：** 〜20分 55.1%（n=89）、20〜25分 50.0%（n=70）、25〜30分 50.0%（n=104）、30〜35分 47.1%（n=102）、35分〜 58.9%（n=112）
- **最高帯：** 35分〜（判定差 11.9ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-84|アカリの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（967試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-3146|ヘクステック ガンブレード]]（該当n=45、97.8% / 非該当49.0%、差+48.8pt）；[[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-3146|ヘクステック ガンブレード]] + [[wiki/entities/items/item-3175|連呪使いのブーツ]]（該当n=41、97.6% / 非該当49.2%、差+48.3pt）
- **ステータス傾向：** 魔力（該当n=930、52.3% / 非該当27.0%、差+25.2pt）；移動速度（該当n=926、51.8% / 非該当39.0%、差+12.8pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・移動速度）；[[wiki/entities/items/item-4633|リフトメーカー]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=12（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）

### TOP（130試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3157|ゾーニャの砂時計]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=32、65.6% / 非該当33.7%、差+32.0pt）
- **ステータス傾向：** 物理防御（該当n=59、50.8% / 非該当33.8%、差+17.0pt）；体力再生（該当n=31、41.9% / 非該当41.4%、差+0.5pt）
- **理論仮説：** [[wiki/entities/items/item-4633|リフトメーカー]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=9（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）；[[wiki/entities/items/item-4633|リフトメーカー]] + [[wiki/entities/items/item-8010|ブラッドレターの呪い]]（n=1（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-84|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=1,223）

- **高勝率コンボ候補：** [[wiki/entities/champions/master-yi|マスター・イー（MasterYi）]] — 対象側勝率74.2%（23/31）、n=31（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/veigar|ベイガー（Veigar）]] — 対象側勝率27.8%（10/36）、n=36（十分性の目安を満たす）。

### TOP（対象n=174）

- **高勝率コンボ候補：** [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率68.8%（11/16）、サンプル不足（n=16、十分性の目安30未満）。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Akali` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Akali.png)
