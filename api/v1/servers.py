from flask import request
from ..models import db, Server
from ..decorators import json
from . import api


@api.route('/servers/', methods=['GET'])
@json
def get_servers():
    return Server.query


@api.route('/servers/<int:id>', methods=['GET'])
@json
def get_server(id):
    return Server.query.get_or_404(id)


@api.route('/servers/', methods=['POST'])
@json
def new_server():
    server = Server().import_data(request.get_json(force=True))
    db.session.add(server)
    db.session.commit()
    return {}, 201, {'Location': server.get_url()}


@api.route('/servers/<int:id>', methods=['PUT'])
@json
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
