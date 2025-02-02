from os import listdir, path
from pathlib import Path

from .output import OutputType, output
from .folder import abspathjoin

def copy_file(src: str, dest: str) -> None:
    output('Copying file', OutputType.HEADER)
    try:
        with open(src, 'r') as src_file:
            with open(dest, 'w') as dest_file:
                dest_file.write(src_file.read())
        output('{0} copied to {1}'.format(src, dest))
    except FileNotFoundError as e:
        output('Error copying file: {0}'.format(e))
        exit(1)

def copy_files_by_ext(source_dir: str, target_dir: str, ext: str) -> None:
    output(f'Copying {ext} files', OutputType.HEADER)
    try:
        files = listdir(source_dir)
        for file in files:
            if file.lower().endswith(ext):
                copy_file(path.join(source_dir, file), path.join(target_dir, file))
    except FileNotFoundError as e:
        output('Error copying files ext: {0}'.format(e))
        exit(1)

def get_filename(__file_path: str) -> str:
    return '{}{}'.format(Path(__file_path).stem, ''.join(Path(__file_path).suffixes))

def get_filename_without_extension(__file_path: str) -> str:
    return Path(__file_path).stem

def get_full_file_path(__file_path: str) -> str:
    return abspathjoin(__file_path, get_filename(__file_path))

def get_files_from_dir_by_ext(source_dir: str, extension: str, file_exceptions: list[str]) -> list[str]:
    return [path.join(source_dir, file) for file in listdir(source_dir) if str(file).lower().endswith(extension.lower()) and get_filename(str(file)) not in file_exceptions]

__all__ = ['copy_file', 'copy_files_by_ext', 'get_filename', 'get_filename_without_extension', 'get_full_file_path', 'get_files_from_dir_by_ext']