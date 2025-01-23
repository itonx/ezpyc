import winreg
import os
import subprocess
from enum import Enum

class EnvVariableType(Enum):
    CURRENT_USER = 1
    SYSTEM = 2

class PrintType(Enum):
    SECTION = 1
    SECTION_DESCRIPTION = 2

HOME_DIR = os.path.expanduser("~")
EZPYC_FOLDER_NAME = ".ezpyc"
EZPYC_FULL_PATH_DIR = os.path.join(HOME_DIR, EZPYC_FOLDER_NAME)
PYTHON_EXTENSION = '.PY'
PATHEXT = 'PATHEXT'
PATH = 'PATH'
EZPYCHW_NAME = 'ezpychw.py'
EZPYCHW_SOURCE_FULL_PATH_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'examples', EZPYCHW_NAME)
EZPYCHW_TARGET_FULL_PATH_FILE = os.path.join(EZPYC_FULL_PATH_DIR, EZPYCHW_NAME)

def print_info(text: str, print_type: PrintType = PrintType.SECTION_DESCRIPTION) -> None:
    if(print_type == PrintType.SECTION):
        print('▒ {0}'.format(text))
    else:
        print('└─ {0}'.format(text))

def create_folder_if_needed(base_dir: str, folder_name: str) -> None:
    full_path_dir = os.path.join(base_dir, folder_name)
    create_folder_if_needed(full_path_dir)

def create_folder_if_needed(full_path_dir: str) -> None:
    print_info('Validating folder', PrintType.SECTION)
    if(not os.path.exists(full_path_dir)):
        try:
            print_info('{0} not found'.format(full_path_dir))
            os.mkdir(full_path_dir)
            print_info('Creating {0}'.format(full_path_dir))
        except OSError:
            print_info('Error creating {0}'.format(full_path_dir))
            exit(1)
    else:
        print_info('{0} found'.format(full_path_dir))

def add_env_variable_value(env_variable_name: str, env_variable_value: str, env_variable_type: EnvVariableType) -> None:
    print_info('Validating env variable', PrintType.SECTION)
    current_values = get_env_variable_value(env_variable_name, env_variable_type)
    if(len(current_values) > 1 and current_values[-1] != ';'):
        current_values += ';'
    is_value_in_variable_values = env_variable_value.upper() in current_values.upper()

    if(is_value_in_variable_values):
        print_info('{0} found in {1} values ({2})'.format(env_variable_value, env_variable_name, env_variable_type.name))
    else:
        print_info('{0} value not found in {1} values ({2}), trying to add the new value...'.format(env_variable_value, env_variable_name, env_variable_type.name))
        add_env_var_command = ['setx', env_variable_name, current_values + env_variable_value]
        if(env_variable_type == EnvVariableType.SYSTEM):
            add_env_var_command.append('/m')
        process_result = subprocess.run(add_env_var_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if(process_result.returncode == 0): # All good
            print_info('{0} value added to {1} values ({2}).'.format(env_variable_value, env_variable_name, env_variable_type.name))
        else:
            admin_rights_text = env_variable_type == EnvVariableType.SYSTEM and 'Execute the script as administrator.' or ''
            print_info('Error adding {0} value to {1} values ({2}). {3}'.format(env_variable_value, env_variable_name, env_variable_type.name, admin_rights_text))
            exit(1)

def get_env_variable_value(env_variable_name: str, env_var_type: EnvVariableType) -> str:
    try:
        hKey = env_var_type == EnvVariableType.CURRENT_USER and winreg.HKEY_CURRENT_USER or winreg.HKEY_LOCAL_MACHINE
        subKey = env_var_type == EnvVariableType.CURRENT_USER and 'Environment' or 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
        key = winreg.OpenKey(hKey, subKey)
        value, _ = winreg.QueryValueEx(key, env_variable_name)
        winreg.CloseKey(key)
        return value
    except FileNotFoundError as e:
        return ''
    
def copy_file(src: str, dest: str) -> None:
    print_info('Copying file', PrintType.SECTION)
    try:
        with open(src, 'r') as src_file:
            with open(dest, 'w') as dest_file:
                dest_file.write(src_file.read())
        print_info('{0} copied to {1}'.format(src, dest))
    except FileNotFoundError as e:
        print_info('Error copying file: {0}'.format(e))
        exit(1)
    

if(__name__ == '__main__'):
    add_env_variable_value(PATHEXT, PYTHON_EXTENSION, EnvVariableType.SYSTEM)
    create_folder_if_needed(EZPYC_FULL_PATH_DIR)
    add_env_variable_value(PATH, EZPYC_FULL_PATH_DIR, EnvVariableType.CURRENT_USER)
    copy_file(EZPYCHW_SOURCE_FULL_PATH_FILE, EZPYCHW_TARGET_FULL_PATH_FILE)
    print_info('Setup done!', PrintType.SECTION)
    print_info('Try \'ezpychw\' command. If you cannot execute it, restart your terminal or open a new one.')