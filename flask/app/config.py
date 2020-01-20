import os

class Config(object):

    """Main configuration class"""

    SECRET_KEY = os.urandom(24)
    DB_USER = os.environ.get('POSTGRES_USER')
    DB_PASS = os.environ.get('POSTGRES_PASSWORD')
    DB_NAME = os.environ.get('POSTGRES_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f'postgres://{DB_USER}:{DB_PASS}@db/{DB_NAME}'


class TestingConfig(Config):

    """Main configuration class"""
    TESTING = True
