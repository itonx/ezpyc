from os import mkdir, path

from .output import OutputType, output

def create_folder_if_needed(base_dir: str, folder_name: str) -> None:
    full_path_dir = path.join(base_dir, folder_name)
    create_folder_if_needed(full_path_dir)

def create_folder_if_needed(full_path_dir: str) -> None:
    output('Validating folder', OutputType.HEADER)
    if(not path.exists(full_path_dir)):
        try:
            output('{0} not found'.format(full_path_dir))
            mkdir(full_path_dir)
            output('Creating {0}'.format(full_path_dir))
        except OSError:
            output('Error creating {0}'.format(full_path_dir))
            exit(1)
    else:
        output('{0} found'.format(full_path_dir))

def abspathjoin(file: str, *paths) -> str:
    return path.join(path.abspath(path.dirname(file)), *paths)

__all__ = ['create_folder_if_needed', 'abspathjoin']