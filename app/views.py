from flask import Blueprint, jsonify


api = Blueprint('example_blueprint', __name__)


@api.route('/')
def index():
    return "this is a test by Jack Nelson"
