from flask.views import MethodView
from flask import jsonify, request
import json
from app.auth.models import *
import datetime


class ChatView(MethodView):
    def get(self):
        incident = Incident.query.filter_by(id=request.args.get('incident_id')).first()
        return jsonify(incident=incident.to_json()['messages'])

    def post(self):
        data = json.loads(request.data)
        message = Message(incident_id=data['incident_id'], ser_id=data['user_id'],
                          message=data['message'], insert_time=datetime.datetime.today())
        message.save()

