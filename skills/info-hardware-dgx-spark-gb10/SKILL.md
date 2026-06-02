---
name: dgx-spark-gb10
description: 遠端連線與操作 NVIDIA DGX Spark GB10（Blackwell 架構, GB10 GPU, CUDA 13.0, aarch64）的硬體環境知識與開發注意事項
disable-model-invocation: true
---

## 硬體(遠端連接)
硬體與環境知識：
- CPU: Cortex-X925（大核, 4.0GHz） + Cortex-A725（小核, 2.86GHz），aarch64 架構
- GPU: NVIDIA GB10 ×1（Blackwell 架構），驅動版本 580.95.05，支持 NVFP4 硬體加速
- CUDA: CUDA 13.0.88（nvcc 版本），`nvidia-smi` 顯示 GPU 型號為 NVIDIA GB10
- 記憶體: 統一記憶體 128GB
- 儲存: NVMe SSD 3.7TB
- OS: Ubuntu 24.04.3 LTS，核心 6.14.0-1015-nvidia（NVIDIA 專用 kernel）
- Python: 內建 Python 3.14.2，但建議建立 venv 時用 `--python 3.12`（更穩定）
- 套件管理: 首選 `uv`（v0.10.0），**無需 pip**；虛擬環境內無 pip 模組也屬正常
- PyTorch 套件: 推薦 `torch==2.10.0+cu130`（+cu130 表示 CUDA 13.0 專用）
- 特殊規則:
  • `nvidia-smi --query-gpu=name,driver_version,...` 中 **`power.draw` 和 `temperature.gpu` 為無效選項**（DGX Spark BIOS 限制），改用 `nvidia-smi -q -d POWER,TEMPERATURE`
  • `nvcc --version` 顯示 `V13.0.88`，但 `/usr/local/cuda/version.txt` 不存在（CUDA toolkit 與 driver 捆綁安裝）
  • Python 虛擬環境（`.venv`）可用 `uv pip list` 查看套件，但不可用 `pip list`
  • 開發時應明確指定 `--extra-index-url https://download.pytorch.org/whl/cu130` 安裝 PyTorch
  • 若需驗證 NVFP4 支援，可查 `nvidia-smi -L` 是否含 "GB10"，或 `torch.backends.cudnn.version() >= 90000`（Blackwell 專用 cuDNN）
