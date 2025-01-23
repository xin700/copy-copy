# Copy-Copy 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-macos%20%7C%20windows%20%7C%20linux-lightgrey)]()

[English](README.md) | [简体中文](README-ZH.md)

一个功能强大的跨平台命令行文件复制工具。支持复制文件内容、文件路径和整个文件，可在 macOS、Windows 和 Linux 上无缝运行。

## ✨ 特性

- 🔄 **跨平台支持**：支持 macOS、Windows 和 Linux
- 📋 **多种复制模式**：
  - 复制文件内容（文本和图片）
  - 复制文件路径
  - 复制整个文件（系统原生文件复制）
- 🎯 **原生集成**：使用平台特定的 API 以获得最佳兼容性
- 🚀 **易于使用**：简单的命令行界面
- 💪 **强大的错误处理**：清晰的错误消息和帮助提示

## 🚀 安装

1. 克隆仓库：
```bash
git clone https://github.com/xin700/copy-copy.git
cd copy-copy
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

### 平台特定要求

#### Linux
安装 xclip：
```bash
# Ubuntu/Debian
sudo apt-get install xclip

# Fedora
sudo dnf install xclip

# Arch Linux
sudo pacman -S xclip
```

## 🎯 使用方法

### 基本用法
```bash
python copy_to_clipboard.py [选项] 文件路径
```

### 选项
- `-c, --content`：复制文件内容（默认模式）
  - 文本文件：复制为文本
  - 图片文件：复制为图片
- `-p, --path`：复制文件路径
- `-f, --file`：复制文件本身（类似系统原生的文件复制）

### 示例
```bash
# 复制文件内容（默认）
python copy_to_clipboard.py document.txt

# 复制文件路径
python copy_to_clipboard.py -p document.txt

# 复制整个文件（可以在文件管理器中粘贴）
python copy_to_clipboard.py -f document.txt
```

## 💡 工作原理

Copy-Copy 使用平台特定的机制来确保原生兼容性：

- **macOS**：使用 AppleScript 进行文件操作和原生剪贴板处理
- **Windows**：通过 pywin32 使用 Win32 API
- **Linux**：使用 xclip 实现剪贴板操作

## 🤝 贡献

欢迎贡献！以下是参与方式：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m '添加一些很棒的特性'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启一个 Pull Request

## 📝 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- 感谢所有为项目做出贡献的人
- 灵感来自于对跨平台文件复制解决方案的需求

## 📞 支持

如果你遇到问题或有疑问：

1. 查看 [Issues](https://github.com/xin700/copy-copy/issues) 页面
2. 如果你的问题还没有被列出，创建一个新的 issue
3. 提供尽可能多的细节，包括你的操作系统和 Python 版本

---

由 [ XIN ] 用 ❤️ 制作
