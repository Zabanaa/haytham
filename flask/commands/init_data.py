from datetime import datetime as dt
import sys
import click
from flask.cli import with_appcontext
from app.database import db
from app.customers.model import Customer
from .reset_db import _reset_db

ALL_CUSTOMERS = [
    {
        'first_name': 'Karim',
        'last_name': 'Benzema',
        'email': 'rimk@gmail.com',
        'password': 'superkooks12345',
        'password_confirm': 'superkooks12345',
    },

    {
        'first_name': 'De',
        'last_name': 'Kooks',
        'email': 'kooks@gmail.com',
        'password': 'superkooks12345',
        'password_confirm': 'superkooks12345',
    },

    {
        'first_name': 'Arthur',
        'last_name': 'Lucchino',
        'email': 'lucchino@gmail.com',
        'password': 'superkooks12345',
        'password_confirm': 'superkooks12345',
    }
]


@click.command('init-data')
@with_appcontext
def init_data():
    _init_data()


def _init_data():
    click.echo("Resetting Database ...")
    _reset_db()
    click.echo("Done !")

    click.echo("Initializing data ...")
    click.echo("Creating Users ...")

    _create_customers()

    click.echo("Users created successfully !")


def _create_customers():

    for customer in ALL_CUSTOMERS:
        _customer = Customer(customer)
        _customer.stripe_customer_id = f'cus_{_customer.first_name}_{_customer.last_name}_{_customer.email}'
        _customer.subscription_info = {
            'trial_end': None,
            'start_date': None,
            'cancel_at': None,
            'canceled_at': None,
            'customer': _customer.stripe_customer_id,
            'id': f'plan_{_customer.public_id}',
            'plan': {'active': True},
        }
        db.session.add(_customer)

    try:
        db.session.commit()
    except Exception as e:
        sys.exit("ERROR: {}".format(str(e.__cause__).split('\n')[0]))


