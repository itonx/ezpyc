from enum import Enum
from subprocess import run, DEVNULL
from winreg import OpenKey, QueryValueEx, CloseKey, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE

from .output import OutputType, output

class EnvType(Enum):
    CURRENT_USER = 1
    SYSTEM = 2

def add_env_variable_value(env_variable_name: str, env_variable_value: str, env_variable_type: EnvType) -> None:
    output('Validating env variable', OutputType.HEADER)
    current_values = get_env_variable_value(env_variable_name, env_variable_type)
    if(len(current_values) > 1 and current_values[-1] != ';'):
        current_values += ';'
    is_value_in_variable_values = env_variable_value.upper() in current_values.upper()

    if(is_value_in_variable_values):
        output('{0} found in {1} values ({2})'.format(env_variable_value, env_variable_name, env_variable_type.name))
    else:
        output('{0} value not found in {1} values ({2}), trying to add the new value...'.format(env_variable_value, env_variable_name, env_variable_type.name))
        add_env_var_command = ['setx', env_variable_name, current_values + env_variable_value]
        if(env_variable_type == EnvType.SYSTEM):
            add_env_var_command.append('/m')
        process_result = run(add_env_var_command, stdout=DEVNULL, stderr=DEVNULL)
        if(process_result.returncode == 0): # All good
            output('{0} value added to {1} values ({2}).'.format(env_variable_value, env_variable_name, env_variable_type.name))
        else:
            admin_rights_text = env_variable_type == EnvType.SYSTEM and 'Execute the script as administrator.' or ''
            output('Error adding {0} value to {1} values ({2}). {3}'.format(env_variable_value, env_variable_name, env_variable_type.name, admin_rights_text))
            exit(1)

def remove_env_variable_value(env_variable_name: str, env_variable_value: str, env_variable_type: EnvType) -> None:
    output('Removing env variable', OutputType.HEADER)
    current_values = get_env_variable_value(env_variable_name, env_variable_type)
    is_value_in_variable_values = env_variable_value.upper() in current_values.upper()

    if(is_value_in_variable_values):
        output('{0} value found in {1} values ({2}), trying to remove the value...'.format(env_variable_value, env_variable_name, env_variable_type.name))
        remove_env_var_command = ['setx', env_variable_name, current_values.replace(f';{env_variable_value}', '').replace(env_variable_value, '').replace(';;', ';')]
        if(env_variable_type == EnvType.SYSTEM):
            remove_env_var_command.append('/m')
        process_result = run(remove_env_var_command, stdout=DEVNULL, stderr=DEVNULL)
        if(process_result.returncode == 0): # All good
            output('{0} value removed from {1} values ({2}).'.format(env_variable_value, env_variable_name, env_variable_type.name))
        else:
            admin_rights_text = env_variable_type == EnvType.SYSTEM and 'Execute the script as administrator.' or ''
            output('Error removing {0} value from {1} values ({2}). {3}'.format(env_variable_value, env_variable_name, env_variable_type.name, admin_rights_text))
            exit(1)
    else:
        output('{0} already removed from {1} values ({2})'.format(env_variable_value, env_variable_name, env_variable_type.name))

def get_env_variable_value(env_variable_name: str, env_var_type: EnvType) -> str:
    try:
        hKey = env_var_type == EnvType.CURRENT_USER and HKEY_CURRENT_USER or HKEY_LOCAL_MACHINE
        subKey = env_var_type == EnvType.CURRENT_USER and 'Environment' or 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
        key = OpenKey(hKey, subKey)
        value, _ = QueryValueEx(key, env_variable_name)
        CloseKey(key)
        return value
    except FileNotFoundError as e:
        return ''
    
__all__ = ['add_env_variable_value', 'remove_env_variable_value', 'get_env_variable_value', 'EnvType']