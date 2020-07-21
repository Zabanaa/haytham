import sys
import pytest
from app import create_app
from app.database import db as _db
from app.customers.model import User
from commands.init_data import _init_data
from .helpers import marshall_raw_data


@pytest.fixture(scope='module')
def app():
    app = create_app(config_obj='TestingConfig')
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture(scope='module')
def client(app):
    return app.test_client()


@pytest.fixture(scope='module')
def db(app):
    _init_data()
    yield _db
    _db.session.remove()
    _db.drop_all()


@pytest.fixture(scope='module')
def users(db):
    raw_users = list(db.session.execute('SELECT * FROM users;'))
    fields = ['id', 'first_name', 'last_name', 'public_id', 'email', 'password']
    dict_users = map(lambda user: marshall_raw_data(user, fields), raw_users)
    return list(dict_users)

