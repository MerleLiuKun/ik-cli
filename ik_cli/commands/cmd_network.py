import click
import requests
from requests.exceptions import Timeout

from . import constant
from .models.network import IpInfo


@click.command('get_ip', short_help='get ip info')
@click.argument('ip', nargs=1)
@click.option('-m', '--mode', type=str, default='net')
def cli(ip, mode):
    if not ip:
        ip = ''
    if mode == 'net':
        session = requests.session()
        try:
            uri = constant.NETWORK_IP_SB_URI + ip
            resp = session.get(uri)
            if resp.ok:
                ip_info = IpInfo.build_info(resp.json())
                click.echo(ip_info)
                click.echo(ip_info.as_json())
        except Timeout as e:
            click.echo('Ops. Maybe your internet not work.', color='red')
