from pathlib import Path

import click

cmd_folder = Path(__file__).cwd() / 'commands'


class ComplexCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for path in list(cmd_folder.glob('cmd*.py')):
            rv.append(path.name[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, cmd_name):
        try:
            mod = __import__('ik_cli.commands.cmd_' + cmd_name, fromlist=['cli'])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ComplexCLI)
def cli():
    pass
