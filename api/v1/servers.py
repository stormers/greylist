from flask import request
from ..models import db, Server
from ..decorators import json
from ..auth import auth
from . import api


@api.route('/servers/', methods=['GET'])
def get_servers():
    servers, content = Server.query.all(), []
    for server in servers:
        content.append(server.name)

    return "\n".join(content), 200


@api.route('/servers/<int:id>', methods=['GET'])
def get_server(id):
    return Server.query.get_or_404(id)


@api.route('/servers/', methods=['POST'])
@auth.login_required
def new_server():
    server = Server().import_data(request.get_json(force=True))
    db.session.add(server)
    db.session.commit()
    return 'ok', 201, {'Location': server.get_url()}


@api.route('/servers/<int:id>', methods=['PUT'])
@auth.login_required
def edit_server(id):
    server = Server.query.get_or_404(id)
    server.import_data(request.get_json(force=True))
    db.session.add(server)
    db.session.commit()
    return {}


@api.route('/servers/<int:id>', methods=['DELETE'])
@json
def delete_server(id):
    server = Server.query.get_or_404(id)
    db.session.delete(server)
    db.session.commit()
    return {}
