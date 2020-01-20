from flask import Blueprint

example_blueprint = Blueprint(
    'example_blueprint',
    __name__,
    url_prefix='/blueprint'
)


@example_blueprint.route('/', methods=['GET'])
def index():
    return "Hello from the blueprint"


@example_blueprint.route('/goodbye', methods=['GET'])
def goodbye():
    return "Goodbye from the blueprint"
