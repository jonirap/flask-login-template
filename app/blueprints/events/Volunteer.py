from flask import request
from flask.ext.login import current_user
from flask.views import MethodView
from app.auth.models import *
from flask import jsonify
import json


class VolunteerView(MethodView):
    def post(self):
        data = json.loads(request.data)
        incident_id = data['incident_id']
        incident = Incident.query.filter_by(id=incident_id).first()
        incident.helpers.append(current_user)
        db.session.commit()
        return jsonify(ok=True)