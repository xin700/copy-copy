import os
import sys
import subprocess
from ..base_handler import BaseHandler

class WindowsHandler(BaseHandler):
    def __init__(self):
        # 延迟导入 Windows 特定的模块
        try:
            import win32clipboard
            import win32con
            self.win32clipboard = win32clipboard
            self.win32con = win32con
        except ImportError:
            self.win32clipboard = None
            self.win32con = None

    def can_handle(self, file_path: str) -> bool:
        return True

    def copy_to_clipboard(self, file_path: str) -> None:
        if not self.win32clipboard:
            print("Error: win32clipboard module is not available.", file=sys.stderr)
            print("This feature is only supported on Windows.", file=sys.stderr)
            sys.exit(1)

        try:
            abs_path = os.path.abspath(file_path)
            
            # 打开剪贴板
            self.win32clipboard.OpenClipboard()
            self.win32clipboard.EmptyClipboard()
            
            # 创建文件列表格式
            file_list = bytes(abs_path + '\0', 'utf-16-le') + b'\0\0'
            
            # 将文件路径复制到剪贴板
            self.win32clipboard.SetClipboardData(self.win32con.CF_HDROP, file_list)
            self.win32clipboard.CloseClipboard()
            
            file_size = os.path.getsize(file_path)
            size_str = self._format_size(file_size)
            print(f"Successfully copied file '{file_path}' ({size_str}) to clipboard!")
            print("You can now paste the file using Ctrl+V in File Explorer or other applications")
            
        except Exception as e:
            print(f"Error copying file: {str(e)}", file=sys.stderr)
            sys.exit(1)

    def _format_size(self, size: int) -> str:
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"
