import functools
from flask import jsonify


def json(f):
    """This decorator generates a JSON response from a Python dictionary or
    a SQLAlchemy model."""
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        rv = f(*args, **kwargs)
        status_or_headers = None
        headers = None
        if isinstance(rv, tuple):
            rv, status_or_headers, headers = rv + (None,) * (3 - len(rv))
        if isinstance(status_or_headers, (dict, list)):
            headers, status_or_headers = status_or_headers, None
        if not isinstance(rv, dict):
            # assume it is a model, call its export_data() method
            rv = rv.export_data()

        rv = jsonify(rv)
        if status_or_headers is not None:
            rv.status_code = status_or_headers
        if headers is not None:
            rv.headers.extend(headers)
        return rv
    return wrapped
