from pathlib import Path
from click import Command, Group, group
from os import path

from .env_variable import EnvVariableType, add_env_variable_value
from .folder import create_folder_if_needed

def ezpyc_command(__file: str) -> Command:
    return Group().command(name=Path(__file).stem, context_settings=dict(help_option_names=['-h', '--help'], show_default=True))

def ezpyc_group_command(group: Group, command_name: str) -> Command:
    return group.command(name=command_name)

def ezpyc_group() -> Group:
    return group(context_settings=dict(help_option_names=['-h', '--help'], show_default=True))

class EzPyC:
    def __init__(self) -> None:
        self.HOME_DIR = path.expanduser("~")
        self.EZPYC_FOLDER_NAME = ".ezpyc"
        self.EZPYC_FULL_PATH_DIR = path.join(self.HOME_DIR, self.EZPYC_FOLDER_NAME)
        self.PYTHON_EXTENSION = '.PY'
        self.PATHEXT = 'PATHEXT'
        self.PATH = 'PATH'

    def install(self) -> None:
        add_env_variable_value(self.PATHEXT, self.PYTHON_EXTENSION, EnvVariableType.SYSTEM)
        create_folder_if_needed(self.EZPYC_FULL_PATH_DIR)
        add_env_variable_value(self.PATH, self.EZPYC_FULL_PATH_DIR, EnvVariableType.CURRENT_USER)