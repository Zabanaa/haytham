import sys
import click
from flask.cli import with_appcontext


@click.command('lint')
@with_appcontext
def lint():
    from subprocess import call
    exclude_dirs = [
        'ENV*/',
        '__pycache__/',
        'migrations/',
        'tests'
    ]
    click.echo("Linting project code ...")
    sys.exit(call(['flake8', '--exclude={}'.format(','.join(exclude_dirs))]))

