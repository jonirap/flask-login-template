from flask import request
from flask.views import MethodView
import json
from config import WOURLD_GRID


class LocationsView(MethodView):
    def post(self):
        # id = request.data['id'] todo: update last seen in DB
        # longitude = request.data['longitude']
        # latitude = request.data['latitude']

        WOURLD_GRID.add_people(request.data)
        return json.dumps({"status": "ok"})
