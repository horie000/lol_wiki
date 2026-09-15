---
title: "アーリ"
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
  - role-mage
  - role-assassin
  - data-dragon
champion_id: "Ahri"
champion_key: "103"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Ahri.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ahri.png"
---

# アーリ

![[raw/assets/champions/Ahri.png|128]]

## 基本情報

- **英字ID：** `Ahri`
- **キー：** `103`
- **称号：** 九尾の狐
- **データversion：** `16.18.1`

## 紹介

生まれつき霊的領域の魔法との繋がりを持つアーリは、狐のような姿をしたヴァスタヤであり、獲物の感情を操ってその生気を自分に取り込む。その際、彼女は獲物の記憶や考えを垣間見ることができる。かつては強大な力を持つ気まぐれな捕食者だったが、今は祖先の足跡を探して世界中を旅しており、自らの記憶でこれまで奪ってきた記憶を置き換えようとしている。

## 分類

- **役割タグ：** `Mage`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 4 |
| `magic` | 8 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 590 |
| `hpperlevel` | 104 |
| `mp` | 418 |
| `mpperlevel` | 25 |
| `movespeed` | 330 |
| `armor` | 21 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 2.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 53 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.2 |
| `attackspeed` | 0.668 |

## アビリティ

- **パッシブ — 生気吸引：** ミニオンまたはモンスターを9体キルすると体力が回復する。 敵チャンピオンからキルまたはアシストを奪うと体力が大幅に回復する。

- **Q — 幻惑のオーブ：** 往復するオーブを放ち、命中した敵に魔法ダメージを与える。戻る時に与えるダメージは確定ダメージになる。
- **W — フォックスファイア：** 少しの間だけ移動速度が増加し、近くにいる敵を自動的に攻撃する、3つの狐火を放つ。
- **E — チャーム：** 投げキッスを放ち、最初に触れた敵にダメージとチャーム効果を与える。チャームされた敵は何もできなくなってアーリに引き寄せられ、発動中の移動スキルもただちに無効になる。
- **R — スピリットラッシュ：** ダッシュしてエネルギーを放ち、周囲にいる敵にダメージを与える。「スピリットラッシュ」はクールダウンに入るまでの間に、最大3回使用できる。敵チャンピオンからキルまたはアシストを奪うと、再発動可能な回数が増える。

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
- **対象試合：** 788試合、全体勝率 46.6%
- **時間帯別勝率：** 〜20分 42.7%（n=117）、20〜25分 43.8%（n=121）、25〜30分 49.7%（n=177）、30〜35分 46.6%（n=176）、35分〜 47.7%（n=197）
- **最高帯：** 25〜30分（判定差 7.0ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-103|アーリの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（1,346試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-3118|マリグナンス]]（該当n=46、82.6% / 非該当46.6%、差+36.0pt）；[[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=31、77.4% / 非該当47.1%、差+30.3pt）
- **ステータス傾向：** マナ（該当n=1313、48.1% / 非該当36.4%、差+11.8pt）；物理防御（該当n=600、54.3% / 非該当42.6%、差+11.7pt）
- **理論仮説：** [[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=6（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3118|マリグナンス]]（n=6（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-103|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=1,682）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/xin-zhao|シン・ジャオ（XinZhao）]] — 対象側勝率71.2%（37/52）、n=52（十分性の目安を満たす）。
  - [[wiki/entities/champions/xerath|ゼラス（Xerath）]] — 対象側勝率62.8%（27/43）、n=43（十分性の目安を満たす）。
  - [[wiki/entities/champions/braum|ブラウム（Braum）]] — 対象側勝率62.0%（44/71）、n=71（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/irelia|イレリア（Irelia）]] — 対象側勝率39.1%（18/46）、n=46（十分性の目安を満たす）。
  - [[wiki/entities/champions/veigar|ベイガー（Veigar）]] — 対象側勝率41.7%（30/72）、n=72（十分性の目安を満たす）。
  - [[wiki/entities/champions/akali|アカリ（Akali）]] — 対象側勝率42.2%（35/83）、n=83（十分性の目安を満たす）。

### TOP（対象n=18）

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

### MIDDLE（対象2,015試合、全体勝率48.8%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系覇道：電撃／血の味わい・グリスリー メメント・至極の賞金首狩り；副系魔道：マナフローバンド・至高；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 1,144/2,015 | 56.8% | 48.1% |
| 2 | 主系覇道：電撃／血の味わい・グリスリー メメント・至極の賞金首狩り；副系天啓：ビスケットデリバリー・宇宙の英知；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 108/2,015 | 5.4% | 42.6% |
| 3 | 主系覇道：電撃／血の味わい・グリスリー メメント・至極の賞金首狩り；副系魔道：マナフローバンド・至高；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 88/2,015 | 4.4% | 45.5% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Ahri` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ahri.png)
