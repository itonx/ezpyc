from ezpyc.os_decorators import os_support, SupportedOS
from ezpyc.ezpyc import ezpyc_group_command, ezpyc_group
from ezpyc.output import OutputType, output
from ezpyc.ezpyc import EzPyC

ezpyc = EzPyC()

@ezpyc_group()
def cli() -> None:
    """ezpyc command line."""
    pass

@ezpyc_group_command(cli, 'fix-runner')
@os_support(allowed_os=[SupportedOS.WINDOWS])
def fix_ezpyc_runner() -> None:
    """Fix ezpyc runner"""
    ezpyc.install(output_msg='Fixing ezpyc runner...')
    output(f'Ezpyc runner fixed. Create a new python script at {ezpyc.EZPYC_FULL_PATH_DIR} and try to run it. If you cannot execute it, restart your terminal or open a new one.', OutputType.HEADER)

cli.add_command(fix_ezpyc_runner)

if __name__ == '__main__':
    cli()