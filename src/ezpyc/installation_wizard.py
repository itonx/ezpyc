from os import path

from .file import copy_files_by_ext
from .env_variable import EnvType, add_env_variable_value, remove_env_variable_value
from .folder import create_folder_if_needed, abspathjoin
from .output import output, OutputType

class EzpycInstaller:
    """
    ezpyc installer class
    """
    def __init__(self) -> None:
        self.HOME_DIR = path.expanduser("~")
        self.EZPYC_FOLDER_NAME = ".ezpyc"
        self.EZPYC_LIB_FOLDER_NAME = "ezpyc"
        self.EZPYC_FULL_PATH_DIR = path.join(self.HOME_DIR, self.EZPYC_FOLDER_NAME)
        self.EZPYC_LIB_FULL_PATH_DIR = path.join(self.EZPYC_FULL_PATH_DIR, self.EZPYC_LIB_FOLDER_NAME)
        self.PYTHON_EXTENSION = '.PY'
        self.PATHEXT = 'PATHEXT'
        self.PATH = 'PATH'
        self._SCRIPT_PATHS_KEY = 'script_paths'

    def install(self, commands_path: str) -> None:
        """Install ezpyc files and environment variables.
        
        Parameters
        ----------
        commands_path : str
            The path where all python scripts command-like are
        """
        self._add_win_configuration('ezpyc installation wizard...')
        self._add_scripts(commands_path)
        output(f'Setup done. Create a new python script at {self.EZPYC_FULL_PATH_DIR} and try to run it. If you cannot execute it, restart your terminal or open a new one.', OutputType.HEADER)

    def uninstall(self) -> None:
        """Uninstall ezpyc environment variables"""
        output('Uninstalling ezpyc...', OutputType.HEADER)
        remove_env_variable_value(self.PATHEXT, self.PYTHON_EXTENSION, EnvType.SYSTEM)
        remove_env_variable_value(self.PATH, self.EZPYC_FULL_PATH_DIR, EnvType.CURRENT_USER)
        output(f'ezpyc\'s been uninstalled. {self.EZPYC_FULL_PATH_DIR} needs to be deleted manually, don\'t forget to backup your scripts.', OutputType.HEADER)

    def _add_scripts(self, commands_path):
        if(commands_path == self.EZPYC_FULL_PATH_DIR):
            output('Warning: ezpyc files detected. Skiping files...')
            return
        output('Adding ezpyc scripts...', OutputType.HEADER)
        create_folder_if_needed(self.EZPYC_LIB_FULL_PATH_DIR)
        copy_files_by_ext(abspathjoin(__file__), self.EZPYC_LIB_FULL_PATH_DIR, '.py')
        copy_files_by_ext(commands_path, self.EZPYC_FULL_PATH_DIR, '.py')

    def _add_win_configuration(self, output_msg):
        output(output_msg, OutputType.HEADER)
        add_env_variable_value(self.PATHEXT, self.PYTHON_EXTENSION, EnvType.SYSTEM)
        create_folder_if_needed(self.EZPYC_FULL_PATH_DIR)
        add_env_variable_value(self.PATH, self.EZPYC_FULL_PATH_DIR, EnvType.CURRENT_USER)

__all__ = ['EzpycInstaller']        