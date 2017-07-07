from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
# from .models import User
from .errors import unauthorized

auth = HTTPBasicAuth()


# @auth.verify_password
# def verify_password(username_or_token, password):
#     # username/password authentication
#     g.user = User.query.filter_by(username=username_or_token).first()
#     return g.user is not None and g.user.verify_password(password)


@auth.error_handler
def unauthorized_error():
    return unauthorized()
