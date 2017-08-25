from flask import request
from flask.views import MethodView
from app.auth.models import *
from flask import jsonify
import json

class IncidentStateView(MethodView):
    def get(self):
        incident_id = request.args.get('incident_id')
        incident = Incident.query.filter_by(id=incident_id).first()
        return jsonify(incident=incident.to_json())



