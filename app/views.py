from flask import Blueprint


api = Blueprint('example_blueprint', __name__)


@api.route('/')
def index():
    return "test by Jack v2"
