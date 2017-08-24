from flask import request
from flask.ext.login import current_user
from flask.views import MethodView
from consts import WORLD_GRID
from app.auth.models import *
from app import app, client
import json
from flask_pushjack import FlaskAPNS


class NotificationsView(MethodView):
    def post(self):
        # todo: filter out people by last seen
        data = json.loads(request.data)
        data["id"] = current_user.id_number
        nearby_people = WORLD_GRID.get_nearby_people(data)
        nearby_people_uuid = [person['uuid'] for person in nearby_people]
        # todo: tals job
        incident_id = ''

        with app.app_context():
            client.send(nearby_people_uuid, "help! there is an emergency", title="emergency alert",
                                  extra={'to_rescue': current_user.to_json(), 'incident_id': incident_id})


