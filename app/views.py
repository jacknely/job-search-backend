from flask import Blueprint, jsonify, current_app


api = Blueprint('example_blueprint', __name__)


@api.route('/')
def index():
    config = current_app.config['LOCATION']
    return "this is a test by Jack Nelson"
