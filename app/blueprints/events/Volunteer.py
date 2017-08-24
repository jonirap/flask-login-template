from flask import request
from flask.views import MethodView
from app.auth.models import *
from flask import jsonify


class VolunteerView(MethodView):
    def post(self):
        incident_id = request.data['incident_id']
        volunteer_id = request.data['id']
        incident = Incident.query.filter_by(id=incident_id).first()
