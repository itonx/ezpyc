from pathlib import Path
from click import Group, option

app = Group()

@app.command(name=Path(__file__).stem, context_settings=dict(help_option_names=['-h', '--help'], show_default=True))
@option('--name', '-n', default='dev', help='Your name.')
def exec(name: str) -> None:
    print(f'Hello {name}, ezpychw\'s working!')

if(__name__ == '__main__'):
    exec()