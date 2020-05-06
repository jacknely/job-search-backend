from flask import Flask

from app.views import api


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    with app.app_context():
        app.register_blueprint(api)

    return app


