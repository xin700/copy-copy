import os
import sys
import pyperclip
from .base_handler import BaseHandler

class TextHandler(BaseHandler):
    def can_handle(self, file_path: str) -> bool:
        try:
            # 尝试以文本模式打开文件
            with open(file_path, 'r'):
                return True
        except UnicodeDecodeError:
            return False

    def copy_to_clipboard(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                pyperclip.copy(content)
                print(f"Successfully copied text contents of '{file_path}' to clipboard!")
        except UnicodeDecodeError:
            print(f"Error: '{file_path}' appears to be a binary file and cannot be copied as text.",
                  file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)
            sys.exit(1)
