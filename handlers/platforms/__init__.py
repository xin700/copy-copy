import sys
import platform

def get_platform_handler():
    """根据当前操作系统返回合适的处理器"""
    system = platform.system().lower()
    
    if system == 'darwin':
        from .macos_handler import MacOSHandler
        return MacOSHandler()
    elif system == 'windows':
        from .windows_handler import WindowsHandler
        return WindowsHandler()
    elif system == 'linux':
        from .linux_handler import LinuxHandler
        return LinuxHandler()
    else:
        raise NotImplementedError(
            f"Platform '{platform.system()}' is not supported. "
            f"This tool currently supports: macOS, Windows, and Linux."
        )
