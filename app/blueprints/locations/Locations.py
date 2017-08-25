from flask import request, jsonify
from flask.ext.login import current_user
from flask.views import MethodView
import json
from app.auth.models import *


class LocationsView(MethodView):
    def post(self):
        # TODO: update last seen in DB
        data = json.loads(request.data)
        data['lat'] = float(data['lat'])
        data['long'] = float(data['long'])
        data['id'] = current_user.id
        WORLD_GRID.add_person(data)
        return jsonify(ok=True)


def change_id(id):
    return id.replace('<', '').replace('>', '').replace(' ', '')
