from flask import request
from flask.views import MethodView


class IncidentEndView(MethodView):
    def post(self):
        incident_id = request.data['incidentID']
        # todo: update DB