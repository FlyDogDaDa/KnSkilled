# Usage Guide

## Convert a single file

```bash
uv run scripts/convert.py --project-root <project-root> test-simplified-chinese.txt
```

## Convert a file with custom config

```bash
uv run scripts/convert.py --project-root <project-root> test-simplified-chinese.txt -c s2t
```

## Convert all matching files in a directory

```bash
uv run scripts/convert.py --project-root <project-root> <directory-path>
```

## Windows path example

```bash
uv run scripts/convert.py --project-root D:/KN_workspace/Echo-of-Though test-simplified-chinese_do-on-me.txt
```

## Config Differences

| Config   | Use case                          | Example: 软件 → |
|----------|-----------------------------------|----------|
| `s2t`    | Standard Traditional              | 軟體     |
| `s2tw`   | Taiwan Traditional                | 軟體     |
| `s2twp`  | Taiwan + common word preferences  | 軟體     |
| `s2hk`   | Hong Kong Traditional             | 軟件     |
| `t2s`    | Traditional → Simplified          | 软件     |

## Encoding

Files are read as UTF-8. If you encounter encoding issues, the converter
uses `latin-1` fallback internally.
