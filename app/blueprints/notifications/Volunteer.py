from flask import request
from flask.views import MethodView

class VolunteerView(MethodView):
    def post(self):
        incident_id = request.data['incidentID']
        volunteer_id = request.data['id']
        # todo: add to DB helper