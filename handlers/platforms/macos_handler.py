import os
import sys
import subprocess
from ..base_handler import BaseHandler

class MacOSHandler(BaseHandler):
    def can_handle(self, file_path: str) -> bool:
        return True

    def copy_to_clipboard(self, file_path: str) -> None:
        try:
            abs_path = os.path.abspath(file_path)
            script = f'''
                tell application "Finder"
                    set sourceFile to (POSIX file "{abs_path}") as alias
                    set selectedFiles to {{sourceFile}}
                    set the clipboard to selectedFiles
                end tell
            '''
            
            process = subprocess.run(['osascript', '-e', script], 
                                   capture_output=True, 
                                   text=True,
                                   check=True)
            
            file_size = os.path.getsize(file_path)
            size_str = self._format_size(file_size)
            print(f"Successfully copied file '{file_path}' ({size_str}) to clipboard!")
            print("You can now paste the file using Cmd+V in Finder or other applications")
            
        except subprocess.CalledProcessError as e:
            print(f"Error copying file: {e.stderr}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error copying file: {str(e)}", file=sys.stderr)
            sys.exit(1)

    def _format_size(self, size: int) -> str:
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"
