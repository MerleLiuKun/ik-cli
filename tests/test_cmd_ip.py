"""
    test for network commands.
"""

from click.testing import CliRunner

from ik_cli.commands.cmd_ip import cli


def test_ip_info():
    runner = CliRunner()
    result = runner.invoke(cli, ['8.8.8.8'])
    assert result.exit_code == 0
    assert '8.8.8.8' in result.output
