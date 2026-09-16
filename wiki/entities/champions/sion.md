---
title: "サイオン"
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
  - role-fighter
  - data-dragon
champion_id: "Sion"
champion_key: "14"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Sion.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sion.png"
---

# サイオン

![[raw/assets/champions/Sion.png|128]]

## 基本情報

- **英字ID：** `Sion`
- **キー：** `14`
- **称号：** 不死身の重戦車
- **データversion：** `16.18.1`

## 紹介

サイオンはデマーシア王を素手で絞殺したことでノクサス中で崇敬されていた過去の英雄だったが、死してなお帝国に奉仕させるために、死の淵から甦らされた。邪魔する者は敵も味方も見境なく虐殺する彼に、もはやかつての人間性は残っていない。腐った体にボルトで粗野な鎧を取り付け、強力な斧を振りかざして敵に向かって無謀な突撃を繰り返しながら、彼はなんとか自分の真の姿を思い出そうとしている。

## 分類

- **役割タグ：** `Tank`、`Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 9 |
| `magic` | 3 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 655 |
| `hpperlevel` | 87 |
| `mp` | 400 |
| `mpperlevel` | 52 |
| `movespeed` | 345 |
| `armor` | 36 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.3 |
| `attackspeed` | 0.679 |

## アビリティ

- **パッシブ — 名誉ある死：** サイオンは死亡後、体力が急速に減っていく状態で一時的に復活する。攻撃速度が飛躍的に上昇して通常攻撃で体力を回復するようになり、対象の最大体力に応じた追加ダメージを与える。

- **Q — 破滅の斧：** サイオンが斧を振り上げ、力を溜めてから前方に振り下ろして、範囲内の敵すべてにダメージを与える。十分に力を溜めた状態で振り下ろすと、ダメージに加えて命中した敵がノックアップし、その後スタン状態になる。
- **W — 魂の炉心：** サイオンがシールドを張り、時間が経過するか3秒たった後に再発動すると爆発して、周囲の敵に魔法ダメージを与える。また自動効果として、敵ユニットをキルするたびにサイオンの最大体力が増加する。
- **E — 殺意の雄叫び：** サイオンが短射程の衝撃波を発射し、最初に命中した敵にダメージとスロウ効果を与え、さらに物理防御を低下させる。ミニオンおよび中立モンスターに当たった場合は長い距離をノックバックし、接触した敵すべてにダメージとスロウ効果を与え、さらに物理防御を低下させる。
- **R — 猪突猛進：** サイオンが指定方向に突進し、時間とともに加速してゆく。突進中も、わずかに方向を制御できる。敵チャンピオンか壁に衝突すると停止し、敵チャンピオンの場合は突進距離に応じてダメージを与え、さらにノックアップする。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤、終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中10位（上位15%）。体力655、物理防御36、攻撃力68、移動速度345。
  - 敵ユニットをキルするたびに最大体力が増加する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 明瞭な傾向なし
- **対象試合：** 347試合、全体勝率 53.9%
- **時間帯別勝率：** 〜20分 46.5%（n=43）、20〜25分 50.0%（n=56）、25〜30分 54.7%（n=75）、30〜35分 59.1%（n=88）、35分〜 54.1%（n=85）
- **最高帯：** 30〜35分（判定差 12.6ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-14|サイオンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（605試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3084|心の鋼]] + [[wiki/entities/items/item-6664|ホロウ レディアンス]]（該当n=41、65.9% / 非該当49.6%、差+16.2pt）；[[wiki/entities/items/item-3748|タイタン ハイドラ]] + [[wiki/entities/items/item-6664|ホロウ レディアンス]]（該当n=40、65.0% / 非該当49.7%、差+15.3pt）
- **ステータス傾向：** 魔法防御（該当n=391、52.9% / 非該当46.7%、差+6.2pt）；攻撃力（該当n=204、54.4% / 非該当48.9%、差+5.5pt）
- **理論仮説：** [[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）

### MIDDLE（210試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2502|終わりなき絶望]] + [[wiki/entities/items/item-3174|装甲強化の進撃]]（該当n=43、67.4% / 非該当50.3%、差+17.1pt）；[[wiki/entities/items/item-3748|タイタン ハイドラ]] + [[wiki/entities/items/item-6664|ホロウ レディアンス]]（該当n=32、65.6% / 非該当51.7%、差+13.9pt）
- **ステータス傾向：** 魔法防御（該当n=167、55.7% / 非該当46.5%、差+9.2pt）；体力再生（該当n=62、59.7% / 非該当51.4%、差+8.3pt）
- **理論仮説：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-14|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=806）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/sivir|シヴィア（Sivir）]] — 対象側勝率66.7%（26/39）、n=39（十分性の目安を満たす）。
  - [[wiki/entities/champions/morgana|モルガナ（Morgana）]] — 対象側勝率65.8%（25/38）、n=38（十分性の目安を満たす）。
  - [[wiki/entities/champions/veigar|ベイガー（Veigar）]] — 対象側勝率63.6%（21/33）、n=33（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/yorick|ヨリック（Yorick）]] — 対象側勝率40.4%（19/47）、n=47（十分性の目安を満たす）。
  - [[wiki/entities/champions/darius|ダリウス（Darius）]] — 対象側勝率45.9%（17/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率50.0%（22/44）、n=44（十分性の目安を満たす）。

### MIDDLE（対象n=288）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/lux|ラックス（Lux）]] — 対象側勝率75.0%（12/16）、サンプル不足（n=16、十分性の目安30未満）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率73.1%（19/26）、サンプル不足（n=26、十分性の目安30未満）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率66.7%（12/18）、サンプル不足（n=18、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率55.6%（10/18）、サンプル不足（n=18、十分性の目安30未満）。
  - [[wiki/entities/champions/malzahar|マルザハール（Malzahar）]] — 対象側勝率72.0%（18/25）、サンプル不足（n=25、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-16生成、キュー420、ユニーク試合10,000件、[[reports/riot-ranked-match-analysis/run-20260916T081004Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### TOP（対象496試合、全体勝率52.8%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系不滅：不死者の握撃／打ちこわし・心身調整・超成長；副系天啓：疾駆・キャッシュバック；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 176/496 | 35.5% | 50.0% |
| 2 | 主系不滅：不死者の握撃／打ちこわし・心身調整・超成長；副系栄華：レジェンド: ヘイスト・凱旋；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 52/496 | 10.5% | 59.6% |
| 3 | 主系不滅：不死者の握撃／打ちこわし・心身調整・超成長；副系天啓：キャッシュバック・疾駆；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 34/496 | 6.9% | 35.3% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Sion` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sion.png)
