# Usage Guide

## Convert a single file

```bash
uv run scripts/convert.py <file-path> --project-root <project-root>
```

## Convert a file with custom config

```bash
uv run scripts/convert.py <file-path> --project-root <project-root> -c s2t
```

## Convert all matching files in a directory

```bash
uv run scripts/convert.py <directory-path> --project-root <project-root>
```

## Windows path example

```bash
uv run scripts/convert.py "D:\KnSkilled\skills\explain-to-me\SKILL.md" --project-root "D:\KnSkilled"
```

## Config Differences

| Config   | Use case                          | Example: 軟體 → |
|----------|-----------------------------------|----------|
| `s2t`    | Standard Traditional              | 軟體     |
| `s2tw`   | Taiwan Traditional                | 軟體     |
| `s2twp`  | Taiwan + common word preferences  | 軟體     |
| `s2hk`   | Hong Kong Traditional             | 軟體     |
| `t2s`    | Traditional → Simplified          | 軟體     |

## Encoding

Files are read as UTF-8. If you encounter encoding issues, the converter
uses `latin-1` fallback internally.
