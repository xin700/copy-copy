import os
from .base_handler import BaseHandler
from .platforms import get_platform_handler

class BinaryHandler(BaseHandler):
    def __init__(self):
        self.platform_handler = get_platform_handler()

    def can_handle(self, file_path: str) -> bool:
        return self.platform_handler.can_handle(file_path)

    def copy_to_clipboard(self, file_path: str) -> None:
        self.platform_handler.copy_to_clipboard(file_path)
