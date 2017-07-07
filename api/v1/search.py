import json

from flask import request
from ..models import mongo
from . import api


@api.route('/search/', methods=['GET'])
def search_servers():
    query = {}
    for arg in request.args.keys():
        query[arg] = request.args[arg]

    servers, content = mongo.db.find(query), []
    for server in servers:
        content.append(server.name)

    return "\n".join(content), 200
