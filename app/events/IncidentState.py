from flask import request
from flask.views import MethodView

class IncidentStateView(MethodView):
    def get(self):
        incident_id = request.data['incidentID']
        # todo: return helpers count, message...