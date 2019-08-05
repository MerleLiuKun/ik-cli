"""
    test for time commands.
"""

from click.testing import CliRunner

from ik_cli.commands.cmd_time import cli


def test_time_str_to_timestamp():
    runner = CliRunner()
    result = runner.invoke(cli, ['1564876800'])
    assert result.exit_code == 0
    assert '2019-08-04' in result.output


def test_timestamp_to_time_str():
    runner = CliRunner()
    result = runner.invoke(cli, ["2019-08-05 12:25:13"])
    assert result.exit_code == 0
    assert '1565007913' in result.output
