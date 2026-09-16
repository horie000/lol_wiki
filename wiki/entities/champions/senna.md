---
title: "セナ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-16
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection]]"
tags:
  - champion
  - role-support
  - role-marksman
  - data-dragon
champion_id: "Senna"
champion_key: "235"
data_version: "16.18.1"
roles:
  - "Support"
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Senna.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Senna.png"
---

# セナ

![[raw/assets/champions/Senna.png|128]]

## 基本情報

- **英字ID：** `Senna`
- **キー：** `235`
- **称号：** 救済者
- **データversion：** `16.18.1`

## 紹介

幼い頃に呪いを受け、超自然現象である「黒き霧」に追われてきたセナは、「光の番人」として知られる聖なる騎士団に加わり、霧と激しく戦った──しかし、彼女は冷酷な亡霊スレッシュによって殺され、ランタンの中に囚われてしまった。それでも希望を捨てなかったセナは、ランタンの中で霧の力を掌握し、新たな命を得て復活を遂げた。光のみならず闇をも操るようになった彼女は、古の武器で放つ一撃ごとに霧の中で失われた魂を救済しながら、「黒き霧」を滅ぼそうとしている。

## 分類

- **役割タグ：** `Support`、`Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 2 |
| `magic` | 6 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 530 |
| `hpperlevel` | 89 |
| `mp` | 350 |
| `mpperlevel` | 45 |
| `movespeed` | 330 |
| `armor` | 25 |
| `armorperlevel` | 4 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 600 |
| `hpregen` | 3.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 50 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.6 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 魂の赦し：** セナの周囲でユニットが倒されると、一定時間ごとにその魂が「黒き霧」に囚われる。セナはこの魂を通常攻撃して解放することで、魂を死の世界に閉じ込めていた「霧」を吸収することができる。「霧」によって「レリックキャノン」が強化されて、攻撃力、射程距離、クリティカル率が増加する。 通常攻撃で「レリックキャノン」を発射するまでにかかる時間は長くなるが、追加ダメージを与えるようになり、さらに一時的に対象の移動速度の一部を獲得する。

- **Q — ピアシングダークネス：** 「レリックキャノン」のツインバレルから光と影が一体となったビームを発射して対象を撃ち抜き、味方は回復して敵にはダメージを与える。
- **W — 最期の抱擁：** 前方に「黒き霧」を放つ。霧は当たった敵に絡みつき、少ししてから対象と周囲のすべての敵ユニットにスネア効果を付与する。
- **E — 黒き霧の呪い：** 武器に取り込んだ「霧」を利用して周囲に嵐を引き起こし、闇を受け入れて亡霊に変化する。範囲内に入った味方はカモフラージュ状態になり、「霧」の作用によって亡霊の姿となる。亡霊の姿になると移動速度が増加し、対象指定不可になり、正体が隠される。
- **R — ドーニングシャドウ：** 亡くなった光の番人のレリックストーンに呼びかけ、「レリックキャノン」が聖なる影と光に分かれる。その後、超大射程のビームを発射して命中した味方にはシールドを展開し、ビームの中心にいた敵にはダメージを与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 「霧」の吸収で攻撃力・射程距離・クリティカル率が増加する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 明瞭な傾向なし
- **対象試合：** 366試合、全体勝率 48.9%
- **時間帯別勝率：** 〜20分 45.0%（n=60）、20〜25分 54.0%（n=50）、25〜30分 46.5%（n=86）、30〜35分 51.0%（n=96）、35分〜 48.6%（n=74）
- **最高帯：** 20〜25分（判定差 9.0ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-235|セナの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（438試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3071|ブラック クリーバー]]（該当n=31、64.5% / 非該当47.7%、差+16.9pt）；[[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3094|ラピッド ファイアキャノン]]（該当n=115、54.8% / 非該当46.7%、差+8.0pt）
- **ステータス傾向：** クリティカル率（該当n=242、52.5% / 非該当44.4%、差+8.1pt）；攻撃力（該当n=380、49.5% / 非該当44.8%、差+4.6pt）
- **理論仮説：** [[wiki/entities/items/item-3085|ルナーン ハリケーン]] + [[wiki/entities/items/item-3094|ラピッド ファイアキャノン]]（n=3（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: クリティカル率・移動速度）；[[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-3094|ラピッド ファイアキャノン]]（n=1（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: クリティカル率・移動速度）

### BOTTOM（345試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3094|ラピッド ファイアキャノン]]（該当n=36、66.7% / 非該当50.8%、差+15.9pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3087|スタティック シヴ]]（該当n=76、61.8% / 非該当49.8%、差+12.0pt）
- **ステータス傾向：** クリティカル率（該当n=238、55.9% / 非該当44.9%、差+11.0pt）；物理防御（該当n=145、53.8% / 非該当51.5%、差+2.3pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・移動速度）；[[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-3094|ラピッド ファイアキャノン]]（未観測；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: クリティカル率・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-235|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=602）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/smolder|スモルダー（Smolder）]] — 対象側勝率63.3%（19/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率56.4%（22/39）、n=39（十分性の目安を満たす）。
  - [[wiki/entities/champions/ezreal|エズリアル（Ezreal）]] — 対象側勝率51.1%（23/45）、n=45（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率39.4%（13/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/lux|ラックス（Lux）]] — 対象側勝率41.2%（14/34）、n=34（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率44.2%（19/43）、n=43（十分性の目安を満たす）。

### BOTTOM（対象n=495）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率67.7%（21/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率66.0%（33/50）、n=50（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率60.6%（20/33）、n=33（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率40.0%（12/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率41.9%（13/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率52.8%（28/53）、n=53（十分性の目安を満たす）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-16生成、キュー420、ユニーク試合10,000件、[[reports/riot-ranked-match-analysis/run-20260916T081004Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### BOTTOM（対象425試合、全体勝率49.4%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：死神の残り火／マナフローバンド・追い風・強まる嵐；副系天啓：なんでも屋・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5010)・UNKNOWN(5001) | 83/425 | 19.5% | 47.0% |
| 2 | 主系魔道：死神の残り火／マナフローバンド・追い風・強まる嵐；副系天啓：魔法の靴・なんでも屋；シャードUNKNOWN(5008)・UNKNOWN(5010)・UNKNOWN(5001) | 59/425 | 13.9% | 50.8% |
| 3 | 主系魔道：死神の残り火／マナフローバンド・追い風・強まる嵐；副系栄華：切り崩し・冷静沈着；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 41/425 | 9.6% | 48.8% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Senna` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Senna.png)
