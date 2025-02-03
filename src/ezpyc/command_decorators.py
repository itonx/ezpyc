from pathlib import Path
from click import Command, Group, group

from .file import get_filename_without_extension

def ezpyc_command(__file_path: str) -> Command:
    """Create a simple command.
    
    Parameters
    ----------
    __file_path : str
        The file path where the command name is going to be taken
    """
    return Group().command(name=get_filename_without_extension(__file_path), context_settings=dict(help_option_names=['-h', '--help'], show_default=True))

def ezpyc_group_command(group: Group, command_name: str) -> Command:
    """Create a new command in the group.
    
    Parameters
    ----------
    group : Group
        The group created with click.group
    command_name : str
        The name for the command
    """
    return group.command(name=command_name)

def ezpyc_group() -> Group:
    """Create a new group command."""
    return group(context_settings=dict(help_option_names=['-h', '--help'], show_default=True))

__all__ = ['ezpyc_command', 'ezpyc_group_command', 'ezpyc_group']