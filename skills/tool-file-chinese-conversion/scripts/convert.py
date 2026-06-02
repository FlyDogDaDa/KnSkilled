# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "opencc",
# ]
# ///
"""
簡體中文 → 繁體中文 轉換工具 (PEP 723 自包含腳本)

使用 OpenCC 進行詞彙級別的中間轉換，支援地區習慣用詞。
文件讀寫策略：
  - 讀取時先寫入暫存檔，避免檔案被佔用時讀取失敗
  - 轉換完成後寫入暫存檔
  - 最後以 shutil.move 原子替換原始檔案，解決「檔案已開啟」問題
"""

import argparse
import os
import shutil
import tempfile
from pathlib import Path

import opencc

# ──────────────────────────────────────────────
# 可選配置文件
# ──────────────────────────────────────────────
CONFIGS = {
    "s2t": "s2t.json",  # 簡體 → OpenCC 標準繁體
    "s2tw": "s2tw.json",  # 簡體 → 台灣正體
    "s2twp": "s2twp.json",  # 簡體 → 台灣正體（含台灣常用詞彙）← 預設
    "t2s": "t2s.json",  # 繁體 → 簡體
    "s2hk": "s2hk.json",  # 簡體 → 香港繁體
}

DEFAULT_CONFIG = "s2twp"


# ──────────────────────────────────────────────
# 核心轉換邏輯
# ──────────────────────────────────────────────
def convert_file(input_path: Path, config_name: str = DEFAULT_CONFIG) -> Path:
    """
    將 input_path 的簡體中文轉換為繁體中文，以 temp file 策略寫回。

    Args:
        input_path:   原始檔案路徑
        config_name:  配置名稱（s2t / s2tw / s2twp / t2s / s2hk）

    Returns:
        最終輸出檔案路徑（與 input_path 相同，因為會覆寫原始檔）

    Raises:
        FileNotFoundError:  輸入檔案不存在
        ValueError:         無效的配置名稱
    """
    if not input_path.is_file():
        raise FileNotFoundError(f"檔案不存在：{input_path}")

    if config_name not in CONFIGS:
        raise ValueError(
            f"不支援的配置名稱：{config_name}，可選：{list(CONFIGS.keys())}"
        )

    config_key = CONFIGS[config_name]

    # 1. 建立暫存目錄（與原始檔同目錄，確保在同一 partition，shutil.move 為原子操作）
    temp_dir = str(input_path.parent)

    # 2. 讀取原始內容
    with open(input_path, "r", encoding="utf-8") as f:
        original_content = f.read()

    # 3. 建立 converter
    converter = opencc.OpenCC(config_key)
    converted_content = converter.convert(original_content)

    # 4. 如果內容沒有變化，直接回傳
    if converted_content == original_content:
        print(f"⚠️  {input_path} 無簡體字，不需轉換")
        return input_path

    # 5. 寫入暫存檔案（而非直接覆寫）
    temp_fd, temp_path = tempfile.mkstemp(
        prefix=".s2t_convert_",
        suffix=".tmp",
        dir=temp_dir,
    )
    try:
        with os.fdopen(temp_fd, "w", encoding="utf-8") as temp_f:
            temp_f.write(converted_content)

        # 6. 以原子方式替換原始檔
        shutil.move(temp_path, str(input_path))
        print(f"✅ 已轉換：{input_path}  （配置：{config_name} / {config_key}）")
    except Exception:
        try:
            os.unlink(temp_path)
        except OSError:
            pass
        raise

    return input_path


def convert_files_batch(paths: list[Path], config_name: str = DEFAULT_CONFIG):
    """批次轉換多個檔案"""
    for p in paths:
        try:
            convert_file(p, config_name)
        except (FileNotFoundError, ValueError) as e:
            print(f"❌ 錯誤：{e}")


# ──────────────────────────────────────────────
# CLI 入口
# ──────────────────────────────────────────────
def _resolve_path(p: Path, project_root: Path) -> Path:
    """將路徑解析為絕對路徑。若為相對路徑則相對於 project_root 解析。"""
    if p.is_absolute():
        return p
    return project_root / p


def main():
    parser = argparse.ArgumentParser(
        description="簡體中文 → 繁體中文 轉換工具（使用 OpenCC）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "使用範例：\n"
            "  uv run scripts/convert.py file.txt                    # 轉換單檔\n"
            "  uv run scripts/convert.py dir/                        # 批次轉換目錄\n"
            "  uv run scripts/convert.py file.txt -c s2t             # 指定配置\n"
            "  uv run scripts/convert.py --project-root /proj path   # 相對路徑相對於 proj\n"
        ),
    )
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="輸入檔案或目錄路徑",
    )
    parser.add_argument(
        "-c",
        "--config",
        default=DEFAULT_CONFIG,
        choices=list(CONFIGS.keys()),
        help=f"轉換配置（預設：{DEFAULT_CONFIG}）",
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=None,
        help="專案根目錄：相對路徑將相對於此目錄解析。若未指定，則相對於當前工作目錄。",
    )

    args = parser.parse_args()

    # 解析專案根目錄：优先使用 --project-root，否則使用當前工作目錄
    project_root = args.project_root if args.project_root else Path.cwd()

    target_paths = []
    for p in args.paths:
        p = _resolve_path(p, project_root)
        if p.is_dir():
            for ext in (
                ".txt",
                ".md",
                ".json",
                ".py",
                ".yml",
                ".yaml",
                ".html",
                ".xml",
                ".cfg",
                ".ini",
            ):
                target_paths.extend(p.rglob(f"*{ext}"))
            print(
                f"📂 掃描目錄：{p} → 找到 {len(target_paths)} 個檔案"
            )
        elif p.is_file():
            target_paths.append(p)
        else:
            print(f"⚠️  路徑不存在，跳過：{p}（已解析為：{p}）")

    if not target_paths:
        print("⚠️  沒有找到需要轉換的檔案")
        return

    print(f"📁 專案根目錄：{project_root.resolve()}")
    convert_files_batch(target_paths, args.config)


if __name__ == "__main__":
    main()
