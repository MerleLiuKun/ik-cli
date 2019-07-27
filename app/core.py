import click
import requests


@click.command()
def ik_ip():
    session = requests.session()
    resp = session.get('https://api.ip.sb/ip')
    click.echo(resp.content)


if __name__ == '__main__':
    ik_ip()
