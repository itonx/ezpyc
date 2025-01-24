from os import getcwd

from ezpyc.ezpyc import ezpyc_command
from ezpyc.os_decorators import os_support, SupportedOS
from ezpyc.clipboard import to_clipboard_win

@ezpyc_command(__file__)
@os_support(allowed_os=[SupportedOS.WINDOWS])
def exec():
    """Get pwd and copy it to clipboard."""
    pwd = getcwd()
    to_clipboard_win(pwd)

if __name__ == '__main__':
    exec()