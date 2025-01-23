import os
import sys
import pyperclip
from .base_handler import BaseHandler

class PathHandler(BaseHandler):
    def __init__(self, use_absolute_path: bool = True):
        self.use_absolute_path = use_absolute_path

    def can_handle(self, file_path: str) -> bool:
        return True  # 路径处理器可以处理任何文件

    def copy_to_clipboard(self, file_path: str) -> None:
        try:
            path_to_copy = os.path.abspath(file_path) if self.use_absolute_path else file_path
            pyperclip.copy(path_to_copy)
            path_type = "absolute" if self.use_absolute_path else "relative"
            print(f"Successfully copied {path_type} path '{path_to_copy}' to clipboard!")
        except Exception as e:
            print(f"Error copying path: {str(e)}", file=sys.stderr)
            sys.exit(1)
