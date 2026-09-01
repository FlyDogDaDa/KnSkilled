# 人類思考方式／思考習慣 全面盤點 — 來源調查

> 整理日期：2026-08-25
> 目的：與 `../minerva-hcs/` 平行，搜尋其他「全面」的人類思考方式／思考習慣整理，供訂製自訂 agent 技能包使用。

## 關鍵結論

1. **沒有單一「完整清單」，但有四大互補系統**，各管一塊：
   - 思考習慣（disposition）：Costa & Kallick 16 Habits of Mind
   - 認知技能＋知識（skill/concept）：Minerva HCs（4×12，~109–115）
   - 思考模型／鏡片（mental models）：Munger latticework 系
   - 思考錯誤（biases/fallacies）：Wikipedia 認知偏誤清單（≈200+）
2. **Costa & Kallick 的「16 Habits of Mind」是教育界唯一的正式「思考習慣」清單**（ASCD 2000/2009），原作者明言「此清單不意圖完整，是起點」。線上偶見流傳的「33 habits of mind」查不到可靠出處，正式版本就是 16 個。
3. **Wikipedia `List of cognitive biases` 是目前最大的思考錯誤目錄**（≈200+ 條，CC-BY-SA 可引用），採 Dimara et al. (2020) 的分類：6 類認知任務 × 5 種偏差「風味」。
4. **Munger 的 latticework 是一手與二手混雜**：一手指的是 1994 年 USC 演講（*A Lesson on Elementary, Worldly Wisdom*）裡的 **25 種人類誤判心理傾向**；網路上的 80/99/100/129 模型集全是**二手編排**（品質參差，但可交叉比對）。
5. 這四套**互補而非互斥**：Minerva 管「要會做什麼」、Costa 管「什麼心態下持續做」、Munger 管「用什麼鏡片看」、偏誤清單管「哪裡會翻車」。技能包可以分層組裝（見文末建議）。

## 四大系統一覽

| 系統 | 代表來源 | 規模 | 性質 | 來源級別 |
|------|---------|------|------|---------|
| Habits of Mind（思考習慣／處置） | Costa & Kallick, ASCD | 16 | 正式、開放式（作者明言可擴展） | 第一手（全文免費可取得） |
| Habits of Cognition（認知技能＋概念） | Minerva University | 4×12，~109–115 | 官方、每年調整 | 見 `../minerva-hcs/` |
| Latticework of Mental Models（思考模型） | Munger 1994 演講；各資料庫 | 25（一手）＋80–129（二手） | 非正式、跨學科鏡片 | 25 項一手；模型集二手 |
| Cognitive Biases & Fallacies（思考錯誤） | Wikipedia（Dimara 2020 分類） | ≈200+ biases、≈100+ fallacies | 學術共識＋社群維護 | CC-BY-SA，可引用 |

## 來源分級

### 第一手（原作者／官方／學術）

| # | 來源 | 連結 | 狀態 |
|---|------|------|------|
| 1 | **Costa & Kallick, *Describing 16 Habits of Mind***（Systems Thinker 重印全文，含 16 habits 完整描述＋引語＋「13 Habits of a Systems Thinker」附錄） | https://thesystemsthinker.com/habits-of-mind-strategies-for-disciplined-choice-making/ | ✅ 已抓全文，素材存 `costa-kallick-16-habits.md` |
| 2 | 同文 PDF 版本（多校公開轉載，內容相同） | https://www.ccny.cuny.edu/sites/default/files/2025-11/HABITS%20OF%20MIND.pdf ／ https://projectacademy.org/resources/docs/Habits%20of%20Mind_mindfulness_05282014.pdf | 可交叉核對 |
| 3 | **Institute for Habits of Mind 官方站**（16 habits 官方介面） | https://habitsofmindinstitute.org/habits | ✅ 已確認官方就是 16 個 |
| 4 | **Wikipedia: List of cognitive biases**（Dimara et al. 2020 任務式分類：6 tasks × 5 flavors；CC-BY-SA） | https://en.wikipedia.org/wiki/List_of_cognitive_biases | ✅ 已抓全文結構；≈200+ 條，隨時可重抓 |
| 5 | **Wikipedia: List of fallacies**（formal + informal；informal 分 relevance/presumption/ambiguity 等） | https://en.wikipedia.org/wiki/List_of_fallacies | 已確認結構；未全量轉錄 |
| 6 | **Wikipedia: Outline of thought**（「思考」主題的 meta 索引：types of thought、reasoning、problem solving、decision making、erroneous thinking、thought tools…） | https://en.wikipedia.org/wiki/Outline_of_thought | ✅ 已抓；可當「還有什麼沒盤點到」的檢索表 |
| 7 | **Munger, *A Lesson on Elementary, Worldly Wisdom*（1994, USC）**：25 種人類誤判心理傾向（incentives、social proof、commitment & consistency、availability…） | 收錄於 *Poor Charlie's Almanack*；演講文字多處公開轉載 | ⏳ 未轉錄 25 項全表（待做） |
| 8 | **Waters Foundation, *13 Habits of a Systems Thinker***（Costa 原文自己推薦的附屬清單） | https://www.watersfoundation.org/ | 已知存在；未全量轉錄 |
| 9 | **Pólya, *How to Solve It*（1945）**：問題求解四步驟（理解問題→制訂計畫→執行→回顧） | 書（多處公開 PDF） | 經典一手；未轉錄 |
| 10 | 官方書籍：Costa & Kallick, *Learning and Leading with Habits of Mind*（ASCD, 2009） | https://www.ascd.org/ | 16 habits 的正式出處；免費全文已足夠，書可選配 |

### 二手（資料庫／編排，交叉比對用）

| # | 來源 | 連結 | 規模／特點 |
|---|------|------|-----------|
| 11 | thoughts.money *Be Smarter with These Mental Models* | https://thoughts.money/mental-models/ | ≈90–100 模型，8 大類（core/physics/biology/systems/numeracy/microeconomics/military/human nature），Munger 語感 |
| 12 | ModelThinkers | https://www.modelthinkers.com/mental-model | 100+ 模型，按學科分，每個模型有獨立頁 |
| 13 | 99 Mental Models | https://www.99mentalmodels.com/ | 99 條，curated |
| 14 | Mental Models Database | https://mentalmodels.wiki/models | 資料庫型，math/physics/psych/econ/philosophy |
| 15 | *The Complete Latticework (129 Models by Theme)*（dataforcee）／sourcesofinsight 129 清單 | https://dataforcee.us/2025-11-27/the-complete-latticework-129-models-by-theme/ ／ https://sourcesofinsight.com/charlie-munger-mental-models/ | Munger 風格 129 項編排（純二手，數字無官方依據，僅供比對） |
| 16 | mnv-thinking-skill「76 個 HCs」 | （見 `../minerva-hcs/README.md`） | Minerva 二手整理，與官方數字對不上 |

## 認知偏誤的 Dimara 6×5 分類（偏誤層技能的骨架）

來源：Dimara et al. (2020) *A Task-Based Taxonomy of Cognitive Biases for Information Visualization*（IEEE TVCG），Wikipedia 採用。

- **6 類任務**：Estimation（估計）／Decision（決策）／Hypothesis assessment（假設評估）／Causal attribution（因果歸因）／Recall（回憶）／Opinion reporting（意見陳述）
- **5 種偏差「風味」**：Association（關聯）／Baseline（基準）／Inertia（慣性）／Outcome（結果導向）／Self-perspective（自我視角）

技能包若要收偏誤，建議按「6 任務」分組、每組挑高頻 5–10 條（如 estimation 抓 anchoring、planning fallacy、overconfidence；decision 抓 loss aversion、sunk cost、status quo bias；attribution 抓 fundamental attribution error、self-serving bias；recall 抓 hindsight bias、negativity bias），不必 200+ 全收。

## 其他清單速查（小而完整，可整併）

| 清單 | 出處 | 項數 |
|------|------|------|
| Habits of a Systems Thinker | Waters Foundation | 13 |
| Habits of Mind | Costa & Kallick | 16（本資料夾有全文） |
| Psychological tendencies of misjudgment | Munger 1994 | 25（待轉錄） |
| Leverage Points | Donella Meadows, *Leverage Points* (1999) | 12（系統槓桿點，從弱到強） |
| Six Thinking Hats | de Bono (1985) | 6（白紅黑黃綠藍） |
| Cognitive process dimension | Bloom's Taxonomy（revised, Anderson & Krathwohl 2001） | 6 層（remember→understand→apply→analyze→evaluate→create） |
| Dual process | Kahneman, *Thinking, Fast and Slow* (2011) | 2 系統（System 1/2，meta 框架，不是清單） |
| DSRP | Dewey, Schumann, Richey, Paul | 4 能力（describe, select, reason, pursue） |

## 對技能包的分層組裝建議

1. **Layer 0 — meta 分類**（決定何時啟動哪個層）：dual process（快/慢）＋ Bloom 六層（任務深度）。
2. **Layer 1 — 認知技能骨架**：Minerva HCs 官方 4×12（既有素材 `../minerva-hcs/`），每個 HC 套「定義＋應用例」格式。
3. **Layer 2 — 鏡片**：Munger 25 心理傾向（一手）＋ mental models 資料庫挑 20–30 條高頻（inversion、first principles、margin of safety、opportunity cost…）。
4. **Layer 3 — 除錯清單**：認知偏誤按 Dimara 6 任務挑 30–50 條高頻，做成 self-check。
5. **Layer 4 — 處置／心態**：Costa 16 habits（本資料夾 `costa-kallick-16-habits.md`），管「持續、靈活、問對問題、負責任地承擔風險」這類元行為。

## 未取得項目

- Munger 25 心理傾向逐條轉錄（一手文本需再抓 1994 演講 PDF）。
- Waters 13 habits、Meadows 12 leverage points 全文轉錄。
- `List of fallacies` 全量轉錄（若 Layer 3 需要邏輯謬誤，再抓）。
