from os import path
from src.ezpyc.os_decorators import os_support, SupportedOS
from src.ezpyc.ezpyc import EzPyC, ezpyc_group, ezpyc_group_command
from src.ezpyc.folder import abspathjoin
from src.ezpyc.output import OutputType, output

ezpyc = EzPyC()

@ezpyc_group()
def cli() -> None:
    """ezpyc command line."""
    pass

def output_done() -> None:
    output('Setup done!', OutputType.HEADER)
    output('Try \'hworld\' or \'hworld -h\' command. If you cannot execute it, restart your terminal or open a new one.')

@ezpyc_group_command(cli, 'install')
@os_support(allowed_os=[SupportedOS.WINDOWS])
def install() -> None:
    """Install ezpyc"""
    ezpyc.install()
    ezpyc.add_ezpyc_scripts(src_path_scripts=abspathjoin(__file__, 'src'), src_path_scripts_lib=abspathjoin(__file__, 'src', 'ezpyc'))
    output_done()

@ezpyc_group_command(cli, 'uninstall')
@os_support(allowed_os=[SupportedOS.WINDOWS])
def uninstall() -> None:
    """Uninstall ezpyc"""
    ezpyc.uninstall()

cli.add_command(install)
cli.add_command(uninstall)

if(__name__ == '__main__'):
    cli()