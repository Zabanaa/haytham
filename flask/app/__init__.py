import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS

crypt = Bcrypt()

def create_app(config_obj='Config'):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(f'app.config.{config_obj}')

    from app.database import db, migrate, ma

    # import blueprints
    from app.example_blueprint.routes import example_blueprint

    # this is where you would import cli commands if any
    from commands import init_data, reset_db, lint, test


    with app.app_context():
        CORS(app, resources={r"/*": {"origins": "*"}})

        db.init_app(app)
        ma.init_app(app)
        crypt.init_app(app)
        migrate.init_app(app, db)

        # register all blueprints
        app.register_blueprint(example_blueprint)

        # add cli commands
        app.cli.add_command(init_data)
        app.cli.add_command(reset_db)
        app.cli.add_command(lint)
        app.cli.add_command(test)

        # setup flask mail below

    return app
