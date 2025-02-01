from os import listdir, path

from .output import OutputType, output

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

__all__ = ['copy_file', 'copy_files_by_ext']