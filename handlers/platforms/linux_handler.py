import os
import sys
import subprocess
from ..base_handler import BaseHandler

class LinuxHandler(BaseHandler):
    def can_handle(self, file_path: str) -> bool:
        return True

    def copy_to_clipboard(self, file_path: str) -> None:
        try:
            abs_path = os.path.abspath(file_path)
            
            # 检查是否存在 xclip
            if not self._check_xclip():
                print("Error: xclip is not installed. Please install it using your package manager:", file=sys.stderr)
                print("  Ubuntu/Debian: sudo apt-get install xclip", file=sys.stderr)
                print("  Fedora: sudo dnf install xclip", file=sys.stderr)
                print("  Arch Linux: sudo pacman -S xclip", file=sys.stderr)
                sys.exit(1)
            
            # 使用 xclip 复制文件 URI
            file_uri = f"file://{abs_path}"
            
            # 复制到 "CLIPBOARD" 和 "PRIMARY" 选择
            for selection in ['clipboard', 'primary']:
                process = subprocess.run(
                    ['xclip', '-selection', selection, '-t', 'text/uri-list'],
                    input=file_uri.encode(),
                    check=True
                )
            
            file_size = os.path.getsize(file_path)
            size_str = self._format_size(file_size)
            print(f"Successfully copied file '{file_path}' ({size_str}) to clipboard!")
            print("You can now paste the file using Ctrl+V in your file manager")
            
        except subprocess.CalledProcessError as e:
            print(f"Error copying file: {str(e)}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error copying file: {str(e)}", file=sys.stderr)
            sys.exit(1)

    def _check_xclip(self) -> bool:
        """检查系统是否安装了 xclip"""
        try:
            subprocess.run(['xclip', '-version'], 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE)
            return True
        except FileNotFoundError:
            return False

    def _format_size(self, size: int) -> str:
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"
