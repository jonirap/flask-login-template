from flask import request
from flask.views import MethodView
from consts import WORLD_GRID
from app.auth.models import *
from app import app
import json
from flask_pushjack import FlaskAPNS


class NotificationsView(MethodView):
    def post(self):
        # todo: filter out people by last seen
        data = json.loads(request.data)
        nearby_people = WORLD_GRID.get_nearby_people(data)
        nearby_people_uuid = [person['uuid'] for person in nearby_people]
        client = FlaskAPNS()
        client.init_app(app)
        with app.app_context():
            to_rescue = User.query.filter_by(data['id'])
            client.send(nearby_people_uuid, "help! there is an emergency", title="emergency alert",
                                  extra={'to_rescue': to_rescue.to_json() + {'longitude': data['longitude'],
                                                                             'latitude': data['latitude']},
                                         'incident_id': 'id'})


