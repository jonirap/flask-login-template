from flask import request
from flask.views import MethodView
from app.auth.models import *
from flask import jsonify
import json

class IncidentStateView(MethodView):
    def post(self):
        incident_id = json.loads(request.data)['incident_id']
        incident = Incident.query.filter_by(id=incident_id).first()
        print incident.helpers
        return jsonify(incident=incident.to_json())



