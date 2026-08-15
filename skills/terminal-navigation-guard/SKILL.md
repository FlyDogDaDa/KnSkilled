---
name: terminal-navigation-guard
description: >-
  The `terminal-navigation-guard` skill: mandatory pre-flight check and error recovery
  for all terminal operations.
  
  Load before:
  (a) Calling the `terminal` tool directly
  (b) Spawning a sub-agent that may call `terminal` (instruct it to load this skill first)
  
  Fix when:
  (c) Terminal tool call failed
  (d) `was not in any of the project's worktrees` error
---

# Terminal Navigation Guard

## 絕對規則（`cd` 引數）

| 規則 | ✅ 正確 | ❌ 錯誤 | 原因 |
|------|---------|---------|------|
| **Only root directory** | `cd="ProjectName"` | `cd="ProjectName/skills"` | System rejects subdirectories |
| **No absolute paths** | `cd="ProjectName"` | `cd="C:\ProjectName"` | Rejected by system |
| **No redundancy** | `cd="ProjectName"` | `cd="ProjectName/ProjectName"` | Duplicate root |

## Subdirectory Operations

```
cd="<根目錄>" command="<子路徑>/<指令>"
```

| 目標 | ✅ 正確 | ❌ 錯誤 |
|------|---------|---------|
| 執行 `uv run script.py` | `cd="ProjectName" command="uv run script.py"` | `cd="ProjectName/scripts" command="uv run script.py"` |

## 執行前檢查清單

在呼叫 `terminal` 之前，**每一項**都必須是 YES：

```
[ ] cd 引數 = 只有根目錄名稱（不含子目錄）
[ ] command 引數 = 包含完整子路徑（如有）
[ ] cd 引數 = 沒有絕對路徑
[ ] cd 引數 = 沒有路徑冗餘
```

有任何 NO → 修正後再呼叫。

## 常見錯誤碼對照

| 錯誤訊息片段 | 根因 | 解法 |
|-------------|------|------|
| `was not in any of the project's worktrees` | `cd` 包含子目錄 | 改為根目錄名稱 |
| Fail silently / 無輸出 | `cd` 格式錯誤 | 檢查是否為絕對路徑或冗餘 |
| 重複失敗 | 未載入本技能就直接重試 | 載入技能 → 修正引數 |