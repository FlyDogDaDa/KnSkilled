---
name: daily-log-writing
description: Record daily development activities, decisions, and progress as time-stamped entries in the project's daily log. Use when completing a task, resolving a bug, making a design decision, or when the user asks to log progress.
---

# Daily Log Skill（SOP）

一次做一步：依 Step 1 → 4 順序執行，不要跳步。

所有寫入都直接寫到目標路徑；上層資料夾若不存在，先建立再寫入。

開始前，先看 `<project>/chat_with_my_agent/` 下有沒有今天的日誌資料夾 `{yyyy}_{mm}_{dd}/`，沒有就用今天日期建；同時看該資料夾內既有條目，決定下一個 `count`（`00`、`01`、…）。

## Step 1：有沒有程式要歸檔？

判斷這次產出的工作中有沒有程式碼或腳本檔案需要歸檔（實驗程式、ad-hoc 腳本、可重現樣本）。

- **有** → 讀 [實驗與腳本歸檔引導](references/scripts-archiving.md)，照它歸檔到
  `<project>/chat_with_my_agent/{yyyy}_{mm}_{dd}/scripts/{folder_name}/`
- **沒有** → 下一步

## Step 2：有沒有參考文件要歸檔？

判斷這次工作中有沒有參考材料或產出的檔案需要歸檔（外部資料、數據、報告產物）。

- **有** → 讀 [參考文件歸檔指引](references/assets-archiving.md)，照它歸檔到
  `<project>/chat_with_my_agent/{yyyy}_{mm}_{dd}/assets/{folder_name}/`
- **沒有** → 下一步

## Step 3：討論過程詳細匯出（必做）

這一步**必做**。將所有從頭到尾的過程 dump 到 details 檔：

```
<project>/chat_with_my_agent/{yyyy}_{mm}_{dd}/references/{count}_{agent|human}_{topic}.md
```

- **所有細節**都寫下來：討論、推理、考慮過的選項、選它的理由
- 可拆分成多份檔案，命名見 [naming convention](references/naming-convention.md)
- 討論過程歸檔後，Step 4 寫日誌與之後的回看都會更好做

## Step 4：執行日誌撰寫

主日誌寫入：

```
<project>/chat_with_my_agent/{yyyy}_{mm}_{dd}/{count}_{agent|human}_{topic}.md
```

- 用 [entry template](assets/entry-template.md)，命名見 [naming convention](references/naming-convention.md)
- 主日誌與討論 details 檔共用同一個 `count` 與 `topic`
- `References` 連結到 `references/` 的 details 檔與 `scripts/`、`assets/` 的歸檔
- **不要在日誌內嵌程式碼或大段材料**，一律連結到歸檔檔案
