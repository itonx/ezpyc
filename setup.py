from os import path
from src.ezpyc.ezpyc import EzPyC
from src.ezpyc.file import copy_file
from src.ezpyc.output import OutputType, output

def add_helloworld(ezpyc: EzPyC) -> None:
    ezpychw_name = 'ezpychw.py'
    ezpychw_source_full_path_file = path.join(path.abspath(path.dirname(__file__)), 'examples', ezpychw_name)
    ezpychw_target_full_path_file = path.join(ezpyc.EZPYC_FULL_PATH_DIR, ezpychw_name)
    copy_file(ezpychw_source_full_path_file, ezpychw_target_full_path_file)

def output_done() -> None:
    output('Setup done!', OutputType.HEADER)
    output('Try \'ezpychw\' command. If you cannot execute it, restart your terminal or open a new one.')

if(__name__ == '__main__'):
    ezpyc = EzPyC()
    ezpyc.install()
    add_helloworld(ezpyc)
    output_done()