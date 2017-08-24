from flask import request, jsonify
from flask.views import MethodView

from app import Incident, db

class IncidentEndView(MethodView):
    def post(self):
        incident_id = request.data['incidentID']
        incident = Incident.query.filter_by(id=incident_id).first()
        incident.status = "done"
        db.session.commit()
        return jsonify(ok=True)

