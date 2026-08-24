# 檔案命名規範

## 目錄結構

一天內的所有內容都放在日誌資料夾下：

```
<project>/chat_with_my_agent/{yyyy}_{mm}_{dd}/
├── {count}_{agent|human}_{topic}.md      # 主日誌
├── references/
│   └── {count}_{agent|human}_{topic}.md  # 討論細節（可拆多份）
├── scripts/
│   └── {folder_name}/                    # 程式／腳本歸檔
└── assets/
    └── {folder_name}/                    # 參考文件歸檔
```

日誌資料夾名就是 `{yyyy}_{mm}_{dd}`，不存在就先建。
所有寫入都直接寫到目標路徑；上層資料夾若不存在，先建立再寫入。

## 欄位定義

| 欄位 | 說明 | 範例 |
|------|------|------|
| `count` | 當日流水號，從 `00` 起 | `00`、`01`、`02` |
| `agent\|human` | 誰發起：`agent` 或 `human` | `agent`、`human` |
| `topic` | kebab-case（連字符分隔），全小寫 | `fix-database-connection` |
| `folder_name` | kebab-case，全小寫，依歸檔主題命名 | `dataset-scan`、`web-research` |

## 命名規則

- 檔名不再含日期（日期在日誌資料夾名中）
- `count` 當日每筆一條目遞增，從 `00` 起；主日誌與其討論 details 檔**共用同一個 `count`**
- 主日誌與 `references/` 內的 details 檔檔名相同，靠所在資料夾區分
- details 檔拆多份時：第一份 `{count}_{agent|human}_{topic}.md`，之後依序加 `-p2`、`-p3`…
  例如 `01_agent_design-review.md`、`01_agent_design-review-p2.md`
- 整個檔名全小寫；topic 用連字符，不用底線

## 範例

```
chat_with_my_agent/
└── 2026_08_24/
    ├── 00_agent_fix-database-connection.md
    ├── 01_human_design-review.md
    ├── references/
    │   ├── 01_human_design-review.md
    │   └── 01_human_design-review-p2.md
    ├── scripts/
    │   └── repro-scan/
    └── assets/
        └── spec-draft/
```
