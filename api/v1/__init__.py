from flask import Blueprint, g, url_for
from ..errors import ValidationError, bad_request, not_found
from ..auth import auth
from ..decorators import json


api = Blueprint('api', __name__)


def get_catalog():
    return {'servers_url': url_for('api.get_servers', _external=True),}


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(str(e))


@api.errorhandler(400)
def bad_request_error(e):
    return bad_request('invalid request')


@api.before_request
@auth.login_required
def before_request():
    pass


@api.after_request
def after_request(response):
    if hasattr(g, 'headers'):
        response.headers.extend(g.headers)
    return response

# do this last to avoid circular dependencies
from . import servers
