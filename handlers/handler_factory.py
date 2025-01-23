from typing import List
from enum import Enum
from .base_handler import BaseHandler
from .text_handler import TextHandler
from .image_handler import ImageHandler
from .path_handler import PathHandler
from .binary_handler import BinaryHandler

class CopyMode(Enum):
    CONTENT = 'content'  # 复制文件内容
    PATH = 'path'        # 复制文件路径
    FILE = 'file'        # 复制文件本体（作为系统文件）

class HandlerFactory:
    def __init__(self, mode: CopyMode = CopyMode.CONTENT):
        self.mode = mode
        
        if mode == CopyMode.PATH:
            self.handlers: List[BaseHandler] = [PathHandler()]
        elif mode == CopyMode.CONTENT:
            self.handlers: List[BaseHandler] = [
                ImageHandler(),  # 先检查是否为图片
                TextHandler(),   # 后检查是否为文本
            ]
        elif mode == CopyMode.FILE:
            self.handlers: List[BaseHandler] = [BinaryHandler()]  # 直接使用系统的文件复制机制
        else:
            raise ValueError(f"Unsupported copy mode: {mode}")

    def get_handler(self, file_path: str) -> BaseHandler:
        for handler in self.handlers:
            if handler.can_handle(file_path):
                return handler
        raise ValueError(f"No suitable handler found for file: {file_path} in mode: {self.mode.value}")
