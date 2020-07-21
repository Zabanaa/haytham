import click
import pytest
from flask.cli import with_appcontext


@click.command('test')
@with_appcontext
def test():
    pytest.main(["-vv", "-s", "tests/"])

