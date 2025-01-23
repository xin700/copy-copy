# Copy-Copy 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-macos%20%7C%20windows%20%7C%20linux-lightgrey)]()

[English](README.md) | [简体中文](README-ZH.md)

A powerful and cross-platform command-line tool for copying files to clipboard. It supports copying file contents, file paths, and entire files, working seamlessly across macOS, Windows, and Linux.

## ✨ Features

- 🔄 **Cross-Platform Support**: Works on macOS, Windows, and Linux
- 📋 **Multiple Copy Modes**:
  - Copy file contents (text and images)
  - Copy file paths
  - Copy entire files (system-native file copying)
- 🎯 **Native Integration**: Uses platform-specific APIs for best compatibility
- 🚀 **Easy to Use**: Simple command-line interface
- 💪 **Robust Error Handling**: Clear error messages and helpful suggestions

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/xin700/copy-copy.git
cd copy-copy
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Platform-Specific Requirements

#### Linux
Install xclip:
```bash
# Ubuntu/Debian
sudo apt-get install xclip

# Fedora
sudo dnf install xclip

# Arch Linux
sudo pacman -S xclip
```

## 🎯 Usage

### Basic Usage
```bash
python copy_to_clipboard.py [options] file_path
```

### Options
- `-c, --content`: Copy file contents (default mode)
  - Text files: copies as text
  - Image files: copies as image
- `-p, --path`: Copy file path
- `-f, --file`: Copy file itself (like system's native file copy)

### Examples
```bash
# Copy file contents (default)
python copy_to_clipboard.py document.txt

# Copy file path
python copy_to_clipboard.py -p document.txt

# Copy the entire file (can be pasted in file manager)
python copy_to_clipboard.py -f document.txt
```

## 💡 How It Works

Copy-Copy uses platform-specific mechanisms to ensure native compatibility:

- **macOS**: Uses AppleScript for file operations and native clipboard handling
- **Windows**: Utilizes Win32 API through pywin32
- **Linux**: Implements xclip for clipboard operations

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all the contributors who have helped with the project
- Inspired by the need for a cross-platform file copying solution

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/xin700/copy-copy/issues) page
2. Create a new issue if your problem isn't already listed
3. Provide as much detail as possible, including your OS and Python version

---

Made with ❤️ by [ XIN ]
