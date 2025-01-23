from abc import ABC, abstractmethod

class BaseHandler(ABC):
    @abstractmethod
    def can_handle(self, file_path: str) -> bool:
        """判断是否可以处理该文件"""
        pass

    @abstractmethod
    def copy_to_clipboard(self, file_path: str) -> None:
        """将文件内容复制到剪贴板"""
        pass
