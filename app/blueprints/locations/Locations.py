from flask import request
from flask.views import MethodView
import json

class LocationsView(MethodView):
    def post(self):
        uuid = request.data['uuid']
        longitude = request.data['longitude']
        latitude = request.data['latitude']
        return json.dumps({"status": "ok"})
    
