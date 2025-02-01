from pathlib import Path
from os import system

def to_clipboard_win(text: str | Path) -> None:
    """Copy text to the clipboard.
    
    Parameters
    ----------
    text : str
        The text that will be set in the clipboard
    """
    value = text if isinstance(text, str) else str(text)
    command = f'echo {value}| clip'
    system(command)
    print(f'{value} (copied to clipboard)')

__all__ = ['to_clipboard_win']