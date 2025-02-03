from click import Path, argument

from ezpyc.os_decorators import os_support, OSType
from ezpyc.command_decorators import ezpyc_group_command, ezpyc_group
from ezpyc.installation_wizard import EzpycInstaller
from ezpyc.folder import abspathjoin

ezpyc_installer = EzpycInstaller()

@ezpyc_group()
def cli() -> None:
    """ezpyc command line."""
    pass

@ezpyc_group_command(cli, 'install')
@os_support(allowed_os=[OSType.WINDOWS])
def install() -> None:
    """Install ezpyc files and environment variables."""
    ezpyc_installer.install(abspathjoin(__file__))

@ezpyc_group_command(cli, 'fix')
@os_support(allowed_os=[OSType.WINDOWS])
def fix() -> None:
    """Fix ezpyc environment variables."""
    ezpyc_installer.install(abspathjoin(__file__))

@ezpyc_group_command(cli, 'uninstall')
@os_support(allowed_os=[OSType.WINDOWS])
def uninstall() -> None:
    """Uninstall ezpyc environment variables"""
    ezpyc_installer.uninstall()

@ezpyc_group_command(cli, 'link')
@argument('paths', nargs=-1, type=Path(exists=True), required=True)
@os_support(allowed_os=[OSType.WINDOWS])
def link(paths: tuple[str, ...]) -> None:
    """Create python script links in ~\.ezpyc for all python scripts found in 'paths'."""
    ezpyc_installer.link_scripts(paths)

@ezpyc_group_command(cli, 'unlink')
@argument('paths', nargs=-1, type=Path(exists=True), required=True)
@os_support(allowed_os=[OSType.WINDOWS])
def unlink(paths: tuple[str, ...]) -> None:
    """Delete python scripts from ~\.ezpyc for all python scripts found in 'paths'."""
    ezpyc_installer.unlink_scripts(paths)    

cli.add_command(install)
cli.add_command(fix)
cli.add_command(uninstall)
cli.add_command(link)
cli.add_command(unlink)

if __name__ == '__main__':
    cli()