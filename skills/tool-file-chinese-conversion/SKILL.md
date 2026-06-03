---
name: chinese-conversion-for-files
description: "簡體中文 ↔ 繁體中文 檔案轉換工具（基於 OpenCC，PEP 723 自包含腳本）。Trigger: user says 轉繁體, 轉簡體, 簡繁轉換, convert to traditional, convert to simplified, 繁化, 簡化。支援 s2t, s2tw, s2twp, s2hk, t2s 配置。"
---

## 快速開始

轉換單一檔案：

```
uv run scripts/convert.py <path>
```

批次轉換目錄：

```
uv run scripts/convert.py <directory-path>
```

指定轉換配置（預設 `s2twp`）：

```
uv run scripts/convert.py <path> -c <config>
```

指定專案根目錄（用於相對路徑）：

```
uv run scripts/convert.py --project-root <project-root> <path>
```

> **注意**：此腳本使用 PEP 723 格式，`uv run scripts/convert.py` 自動處理依賴，
> 不需要 `-p` 參數或虛擬環境。

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
