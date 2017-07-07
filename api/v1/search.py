import json

from flask import request
from ..models import db, Server
from . import api


@api.route('/search/', methods=['GET'])
def search_servers():
    servers, content = Server.query.all(), []
    for server in servers:
        props = json.loads(server.properties)

        for arg in request.args.keys():
            import ipdb; ipdb.set_trace()

            if arg in props and props[arg] == request.args.get(arg):
                content.append(server.name)

    return "\n".join(content), 200
