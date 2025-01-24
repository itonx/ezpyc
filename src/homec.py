from pathlib import Path

from ezpyc.os_decorators import os_support, SupportedOS
from ezpyc.clipboard import to_clipboard_win
from ezpyc.ezpyc import ezpyc_command

@ezpyc_command(__file__)
@os_support(allowed_os=[SupportedOS.WINDOWS])
def exec():
    """Get home path and copy it to clipboard."""
    home = str(Path.home())
    to_clipboard_win(home)

if __name__ == '__main__':
    exec()