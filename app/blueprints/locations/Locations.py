from flask import request
from flask.views import MethodView
import json
from config import WOURLD_GRID
from app.auth.models import *


class LocationsView(MethodView):
    def post(self):
        # todo: update last seen in DB
        data = json.dumps(request.data)
        WOURLD_GRID.add_people(data)
        return json.dumps({"status": "ok"})
