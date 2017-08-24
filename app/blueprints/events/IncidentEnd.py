from flask import json
from flask import request, jsonify
from flask.views import MethodView

from app.auth.models import *
from app import db


class IncidentEndView(MethodView):
    def post(self):
        try:
            data = json.loads(request.data)
            incident_id = data['incidentID']
            incident = Incident.query.filter_by(id=incident_id).first()
            incident.status = "done1"
            db.session.commit()
            return jsonify(ok=True)
        except Exception as e:
            return jsonify(ok=False, error=e.message)
