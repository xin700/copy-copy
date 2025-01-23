#!/usr/bin/env python3
import argparse
import sys
import os
from handlers import HandlerFactory
from handlers.handler_factory import CopyMode

def copy_file_to_clipboard(file_path: str, mode: CopyMode) -> None:
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")

        handler_factory = HandlerFactory(mode)
        handler = handler_factory.get_handler(file_path)
        handler.copy_to_clipboard(file_path)

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='Copy file to clipboard in different modes',
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # 创建互斥的参数组
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument('-c', '--content', action='store_true',
                           help='Copy file contents (default mode)\n'
                                '- Text files: copies as text\n'
                                '- Image files: copies as image')
    mode_group.add_argument('-p', '--path', action='store_true',
                           help='Copy file path')
    mode_group.add_argument('-f', '--file', action='store_true',
                           help='Copy file itself (like Finder\'s copy)\n'
                                'The file can be pasted in Finder or other apps\n'
                                'This behaves the same as copying a file in Finder')
    
    parser.add_argument('file_path', help='Path to the file to be copied')
    
    args = parser.parse_args()
    
    # 确定使用哪种模式
    if args.path:
        mode = CopyMode.PATH
    elif args.file:
        mode = CopyMode.FILE
    else:  # 默认使用 content 模式
        mode = CopyMode.CONTENT
    
    copy_file_to_clipboard(args.file_path, mode)

if __name__ == '__main__':
    main()
