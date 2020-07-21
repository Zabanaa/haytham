import click
from flask.cli import with_appcontext
from app.database import db


@click.command('reset-db')
@with_appcontext
def reset_db():
    _reset_db()


def _reset_db():
    from flask_migrate import upgrade, stamp

    db.drop_all()
    db.engine.execute('DROP TABLE IF EXISTS alembic_version;')
    db.create_all()
    stamp()
    upgrade()


