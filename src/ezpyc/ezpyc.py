from pathlib import Path
from click import Command, Group, group
from os import path

from .file import copy_files_ext
from .env_variable import EnvVariableType, add_env_variable_value
from .folder import create_folder_if_needed
from .output import output, OutputType

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
        self.EZPYC_LIB_FOLDER_NAME = "ezpyc"
        self.EZPYC_FULL_PATH_DIR = path.join(self.HOME_DIR, self.EZPYC_FOLDER_NAME)
        self.EZPYC_LIB_FULL_PATH_DIR = path.join(self.EZPYC_FULL_PATH_DIR, self.EZPYC_LIB_FOLDER_NAME)
        self.PYTHON_EXTENSION = '.PY'
        self.PATHEXT = 'PATHEXT'
        self.PATH = 'PATH'

    def install(self, output_msg = 'Installing ezpyc...') -> None:
        output(output_msg, OutputType.HEADER)
        add_env_variable_value(self.PATHEXT, self.PYTHON_EXTENSION, EnvVariableType.SYSTEM)
        create_folder_if_needed(self.EZPYC_FULL_PATH_DIR)
        add_env_variable_value(self.PATH, self.EZPYC_FULL_PATH_DIR, EnvVariableType.CURRENT_USER)
    
    def add_ezpyc_scripts(self, src_path_scripts, src_path_scripts_lib):
        output('Adding ezpyc scripts...', OutputType.HEADER)
        create_folder_if_needed(self.EZPYC_LIB_FULL_PATH_DIR)
        copy_files_ext(src_path_scripts_lib, self.EZPYC_LIB_FULL_PATH_DIR, '.py')
        copy_files_ext(src_path_scripts, self.EZPYC_FULL_PATH_DIR, '.py')