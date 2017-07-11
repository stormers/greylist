import os
from flask import Flask
from pymongo import MongoClient
from .models import mongo
from .auth import auth
from .decorators import json
from .errors import not_found, not_allowed


def create_app(config_module=None):
    app = Flask(__name__)
    app.config.from_object(config_module or
                           os.environ.get('FLASK_CONFIG') or
                           'config')

    mongo.init_app(app)

    from api.v1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/v1')

    @app.route('/')
    # @auth.login_required
    @json
    def index():
        from api.v1 import get_catalog as v1_catalog
        return {'versions': {'v1': v1_catalog()}}

    @app.errorhandler(404)
    # @auth.login_required
    def not_found_error(e):
        return not_found('item not found')

    @app.errorhandler(405)
    def method_not_allowed_error(e):
        return not_allowed()

    return app
