from ezpyc.os_decorators import os_support, SupportedOS
from ezpyc.ezpyc import ezpyc_group_command, ezpyc_group
from ezpyc.output import OutputType, output
from ezpyc.ezpyc import EzPyC

ezpyc = EzPyC()

@ezpyc_group()
def cli() -> None:
    """ezpyc command line."""
    pass

@ezpyc_group_command(cli, 'fix')
@os_support(allowed_os=[SupportedOS.WINDOWS])
def fix_ezpyc() -> None:
    """Fix ezpyc"""
    ezpyc.install(output_msg='Fixing ezpyc...')
    output(f'Ezpyc fixed. Create a new python script at {ezpyc.EZPYC_FULL_PATH_DIR} and try to run it. If you cannot execute it, restart your terminal or open a new one.', OutputType.HEADER)

@ezpyc_group_command(cli, 'uninstall')
@os_support(allowed_os=[SupportedOS.WINDOWS])
def uninstall() -> None:
    """Uninstall ezpyc"""
    ezpyc.uninstall()


cli.add_command(fix_ezpyc)
cli.add_command(uninstall)

if __name__ == '__main__':
    cli()