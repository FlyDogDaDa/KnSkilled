---
name: chinese-conversion-for-files
description: >-
  Simplified ↔ Traditional Chinese file conversion tool.
  Use to convert Simplified Chinese to Traditional Chinese,
  or ensure file content is in Traditional Chinese.
  Use after writing code to verify all comments are in Traditional Chinese.
---

## 快速開始

預設 dry-run 模式（只顯示轉換結果，不寫入檔案）：

```
uv run scripts/convert.py <path>
```

實際寫入（--apply）：

```
uv run scripts/convert.py <path> --apply
```

指定轉換配置（預設 `s2twp`）：

```
uv run scripts/convert.py <path> -c <config>
```

指定專案根目錄（用於相對路徑）：

```
uv run scripts/convert.py --project-root <project-root> <path> --apply
```

> **注意**：預設 dry-run 模式，只顯示預覽結果，不實際寫入檔案。加入 `--apply` 才真正轉換。

## 支援的配置

| Config | 方向 | 說明 |
|--------|------|------|
| `s2twp` | 簡體 → 繁體 (台灣) | **預設**，含台灣常用詞彙 |
| `s2t` | 簡體 → 繁體 (標準) | 通用繁體轉換 |
| `s2tw` | 簡體 → 繁體 (台灣) | 不含常用詞 |
| `s2hk` | 簡體 → 繁體 (香港) | 香港習慣用詞 |
| `t2s` | 繁體 → 簡體 | 繁體轉簡體 |

## 支援的副檔名

`.txt`, `.md`, `.json`, `.py`, `.yml`, `.yaml`, `.html`, `.xml`, `.cfg`, `.ini`

## 使用範例

詳細範例請見 [references/usage-guide.md](references/usage-guide.md)。

## 注意事項

- 檔案以 UTF-8 編碼讀取，寫入時以 atomic move 替換原始檔。
- 轉換完成後請確認專業術語——OpenCC 使用的是通用詞彙庫。
- 若檔案內容無簡體字，會輸出警告但不修改檔案。
- **預設 dry-run 模式**：執行後只顯示轉換結果，不寫入檔案。確認無誤後加 `--apply` 實際轉換。
