import os
from flask import Flask
from app.example_blueprint.routes import example_blueprint


def create_app(config_obj='Config'):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(f'app.config.{config_obj}')

    from app.database import db, migrate
    db.init_app(app)

    with app.app_context():
        try:
            db.create_all()
        except AttributeError as e:
            sys.exit("DB ERROR {}".format(e))

    migrate.init_app(app, db)
    app.register_blueprint(example_blueprint)

    @app.route('/')
    def index():
        return "Hello, thanks for using haytham"

    return app
