from os import path
from src.ezpyc.os_decorators import os_support, SupportedOS
from src.ezpyc.ezpyc import EzPyC
from src.ezpyc.folder import abspathjoin
from src.ezpyc.output import OutputType, output

def output_done() -> None:
    output('Setup done!', OutputType.HEADER)
    output('Try \'hworld\' or \'hworld -h\' command. If you cannot execute it, restart your terminal or open a new one.')

@os_support(allowed_os=[SupportedOS.WINDOWS])
def main():
    ezpyc = EzPyC()
    ezpyc.install()
    ezpyc.add_ezpyc_scripts(src_path_scripts=abspathjoin(__file__, 'src'), src_path_scripts_lib=abspathjoin(__file__, 'src', 'ezpyc'))
    output_done()

if(__name__ == '__main__'):
    main()