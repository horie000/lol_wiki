---
title: "シンジド"
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
  - role-tank
  - role-mage
  - data-dragon
champion_id: "Singed"
champion_key: "27"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Singed.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Singed.png"
---

# シンジド

![[raw/assets/champions/Singed.png|128]]

## 基本情報

- **英字ID：** `Singed`
- **キー：** `27`
- **称号：** マッドケミスト
- **データversion：** `16.18.1`

## 紹介

シンジドは優れた錬金術師だが、倫理観が欠如した存在でもあり、その実験は極めて残忍な犯罪者ですら吐き気をもよおすほどだ。彼は最も高い報酬を提示した者にその技術を売り、自らの有害な調合物がいかに使用されようがろくに関心を払わず、それがもたらす混沌すらをも実験の一環として見ているふしがある。彼が生み出したものの中でも最も悪名高いのが「シマー」であり、これによってケミ長者たちはゾウンを彼らの遊び場へと変貌させることとなった。それでもシンジドは狂気に突き動かされ、常に新しいなにかに取り組んでいる。堕落の一途をた...

## 分類

- **役割タグ：** `Tank`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 8 |
| `magic` | 7 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 96 |
| `mp` | 330 |
| `mpperlevel` | 45 |
| `movespeed` | 345 |
| `armor` | 34 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.55 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.9 |
| `attackspeed` | 0.7 |

## アビリティ

- **パッシブ — スリップストリーム：** 周囲のチャンピオンを利用して空気抵抗を減らし、通り過ぎる際に一時的に移動速度が増加する。

- **Q — 毒の軌跡：** 背中から毒ガスをまき散らし、ガスに接触した敵にダメージを与える。
- **W — 強力粘着剤：** 強力な粘着剤の入ったビンを地面に投げ、接触した敵にスロウ効果を与えて釘付けにする。
- **E — すくい投げ：** 対象の敵ユニットにダメージを与え、シンジドの背後へ投げ飛ばす。 「強力粘着剤」の上に着地した場合は、スネア状態になる。
- **R — 狂人のポーション：** 強力な調合薬を飲んで戦闘能力が一時的に強化され、「毒の軌跡」が「重傷」を付与するようになる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中23位（上位15%）。体力650、物理防御34、攻撃力63、移動速度345。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 明瞭な傾向なし
- **対象試合：** 259試合、全体勝率 53.3%
- **時間帯別勝率：** 〜20分 54.3%（n=35）、20〜25分 58.5%（n=41）、25〜30分 51.7%（n=58）、30〜35分 50.0%（n=62）、35分〜 54.0%（n=63）
- **最高帯：** 20〜25分（判定差 8.5ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-27|シンジドの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（327試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2525|プロトプラズム ハーネス]] + [[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（該当n=37、67.6% / 非該当50.3%、差+17.2pt）；[[wiki/entities/items/item-2525|プロトプラズム ハーネス]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（該当n=39、64.1% / 非該当50.7%、差+13.4pt）
- **ステータス傾向：** 魔法防御（該当n=106、56.6% / 非該当50.2%、差+6.4pt）
- **理論仮説：** [[wiki/entities/items/item-3002|先人の道標]] + [[wiki/entities/items/item-3742|デッド マン プレート]]（未観測；共通stats: 物理防御・体力・移動速度／チャンピオン原典にも言及: 物理防御・体力・移動速度）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

### JUNGLE（38試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3143|ランデュイン オーメン]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（n=1（15未満）；共通stats: 物理防御・体力／チャンピオン原典にも言及: 物理防御・体力）；[[wiki/entities/items/item-3742|デッド マン プレート]] + [[wiki/entities/items/item-4629|コズミック ドライブ]]（未観測；共通stats: 体力・移動速度／チャンピオン原典にも言及: 体力・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-27|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=428）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率67.6%（23/34）、n=34（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率53.5%（23/43）、n=43（十分性の目安を満たす）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率53.1%（17/32）、n=32（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/yorick|ヨリック（Yorick）]] — 対象側勝率40.0%（8/20）、サンプル不足（n=20、十分性の目安30未満）。
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率45.5%（10/22）、サンプル不足（n=22、十分性の目安30未満）。
  - [[wiki/entities/champions/garen|ガレン（Garen）]] — 対象側勝率51.9%（14/27）、サンプル不足（n=27、十分性の目安30未満）。

### JUNGLE（対象n=43）

- **高勝率コンボ候補（最大3件）：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **低勝率カウンターピック候補（最大3件）：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-16生成、キュー420、ユニーク試合10,000件、[[reports/riot-ranked-match-analysis/run-20260916T081004Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### TOP（対象219試合、全体勝率54.8%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：死神の残り火／ニンバスクローク・追い風・追火；副系栄華：背水の陣・凱旋；シャードUNKNOWN(5008)・UNKNOWN(5010)・UNKNOWN(5001) | 63/219 | 28.8% | 65.1% |
| 2 | 主系魔道：死神の残り火／マナフローバンド・追い風・強まる嵐；副系栄華：凱旋・切り崩し；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5013) | 22/219 | 10.0% | 40.9% |
| 3 | 主系栄華：征服者／凱旋・レジェンド: 迅速・背水の陣；副系魔道：追い風・ニンバスクローク；シャードUNKNOWN(5008)・UNKNOWN(5010)・UNKNOWN(5001) | 14/219 | 6.4% | 42.9% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Singed` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Singed.png)
