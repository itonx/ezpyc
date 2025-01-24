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