from os import path, remove

from .file import copy_files_by_ext, get_filename, get_full_file_path, get_files_from_dir_by_ext
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

    def link_scripts(self, paths: tuple[str, ...]) -> None:
        output('Attempting to link scripts...', OutputType.HEADER)
        for file_dir_path in paths:
            if(path.isfile(file_dir_path)):
                self._add_python_script_to_ezpyc(file_dir_path)
            elif(path.isdir(file_dir_path)):
                for full_file_path in get_files_from_dir_by_ext(file_dir_path, self.PYTHON_EXTENSION, ['__init__.py']):
                    self._add_python_script_to_ezpyc(full_file_path)

    def unlink_scripts(self, paths: tuple[str, ...]) -> None:
        output('Attempting to unlink scripts...', OutputType.HEADER)
        for file_dir_path in paths:
            if(path.isfile(file_dir_path)):
                self._remove_script_from_ezpyc(file_dir_path)
            elif(path.isdir(file_dir_path)):
                ezpyc_scripts = [get_filename(ezpyc_file) for ezpyc_file in get_files_from_dir_by_ext(self.EZPYC_FULL_PATH_DIR, self.PYTHON_EXTENSION, ['ezpyc.py'])]
                for full_file_path in get_files_from_dir_by_ext(file_dir_path, self.PYTHON_EXTENSION, ['__init__.py']):
                    if(get_filename(full_file_path) in ezpyc_scripts):
                        self._remove_script_from_ezpyc(full_file_path)
                    else:
                        output(f'{get_filename(full_file_path)} not found in ~\.ezpyc')

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
    
    def _add_python_script_to_ezpyc(self, file_path):
        filename = get_filename(file_path)
        full_file_path = get_full_file_path(file_path)
        with open(path.join(self.EZPYC_FULL_PATH_DIR, filename), 'w') as file_stream:
            file_stream.write(f'''from os import system
from sys import argv
script_path = '{full_file_path}'
system('{{0}} {{1}}'.format(script_path, ' '.join(argv[1:])))
            ''')
        output(f'Link for {full_file_path} created on {self.EZPYC_FULL_PATH_DIR}')

    def _remove_script_from_ezpyc(self, file_path):
        filename = get_filename(file_path)
        full_file_path = get_full_file_path(file_path)
        full_file_path_ezpyc = path.join(self.EZPYC_FULL_PATH_DIR, filename)
        file_found = None
        with open(full_file_path_ezpyc, 'r') as file_stream:
            for line in file_stream.readlines():
                tmp_line = line.strip()
                if(tmp_line.__contains__(full_file_path)):
                    file_found = full_file_path_ezpyc
                    output(f'{full_file_path} unlinked. [Deleted] {full_file_path_ezpyc}')
        remove(file_found) if file_found else output(f'[Failed] {file_path} not found in {full_file_path_ezpyc} content')

__all__ = ['EzpycInstaller']        