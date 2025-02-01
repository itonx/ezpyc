from enum import Enum
from platform import system as getos
from functools import wraps
from typing import Any

class OSType(Enum):
    WINDOWS = 'windows'
    LINUX = 'linux'
    MAC = 'darwin'

def os_support(allowed_os: list[OSType]) -> Any:
    """Decorator to restrict a command to specific OS."""
    supported_os = [supported_os.name.lower() for supported_os in allowed_os]
    supported_os_joined = ", ".join(supported_os).title()
    default_info = f'This command is only supported on: {supported_os_joined}'
    docstring = f'OS Support: {supported_os_joined}'

    def decorator(f):
        if f.__doc__:
            f.__doc__ += f" ({docstring})"
        else:
            f.__doc__ = f"{docstring}"
        @wraps(f)
        def wrapper(*args, **kwargs):
            current_os = getos().lower()
            if current_os not in supported_os:
                print(f"{default_info} (Detected: {current_os.title()})\n")
                exit(1)
            return f(*args, **kwargs)
        return wrapper
    
    return decorator

__all__ = ['os_support', 'OSType']