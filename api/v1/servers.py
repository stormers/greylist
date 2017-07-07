from flask import request
from flask import url_for
from ..models import mongo
from ..decorators import json
from ..auth import auth
from . import api


@api.route('/servers/', methods=['GET'])
def get_servers():
    servers, content = mongo.db.servers.find(), []
    for server in servers:
        content.append(server.get('name'))

    return "\n".join(content), 200


@api.route('/servers/<name>', methods=['GET'])
def get_server(name):
    server = mongo.db.servers.find_one_or_404({'name': name})
    return server


@api.route('/servers/', methods=['POST'])
# @auth.login_required
def new_server():
    server = {}
    for arg in request.form.keys():
        server[arg] = request.args[arg]

    servers = mongo.db.servers
    servers.insert_one(server)

    return 'ok', 201, {'Location': url_for('api.get_server',
                                           name=server.get('name'),
                                           _external=True)}


@api.route('/servers/<name>', methods=['PUT'])
# @auth.login_required
def edit_server(name):
    updated = {}
    for arg in request.args.keys():
        updated[arg] = request.args[arg]

    server = mongo.db.servers.find_one_and_update({'name': name},
                                                  {'$set': updated},
                                                  return_document=ReturnDocument.AFTER)
    return server, 200


@api.route('/servers/<name>', methods=['DELETE'])
# @auth.login_required
def delete_server(name):
    server = mongo.db.servers.delete_one({'name': name})
    return 'ok', 200
