import os
import sys
import subprocess
from PIL import Image
import io
from .base_handler import BaseHandler

class ImageHandler(BaseHandler):
    def __init__(self):
        self.image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'}

    def can_handle(self, file_path: str) -> bool:
        return os.path.splitext(file_path)[1].lower() in self.image_extensions

    def copy_to_clipboard(self, file_path: str) -> None:
        try:
            image = Image.open(file_path)
            
            # 在macOS上，我们需要保持图片在内存中
            output = io.BytesIO()
            image.save(output, format=image.format)
            
            # 使用osascript来复制图片到剪贴板（macOS特定）
            clipboard_cmd = [
                'osascript',
                '-e',
                'set the clipboard to (read (POSIX file "' + file_path + '") as JPEG picture)'
            ]
            subprocess.run(clipboard_cmd, check=True)
            print(f"Successfully copied image '{file_path}' to clipboard!")
        except Exception as e:
            print(f"Error copying image: {str(e)}", file=sys.stderr)
            sys.exit(1)
