from flask.views import MethodView
from flask import request, jsonify
import json
from app.auth.models import *
import datetime


class ChatView(MethodView):
    def get(self):
        data = json.loads(request.data)
        chat = Incident.query.filter_by(incident_id=data['incident_id'])
        chat.save()
        return jsonify(chat=chat.to_json())


def post(self):
    data = json.loads(request.data)
    message = Message(incident_id=data['incident_id'], ser_id=data['user_id'],
                      message=data['message'], insert_time=datetime.datetime.today())
    message.save()

