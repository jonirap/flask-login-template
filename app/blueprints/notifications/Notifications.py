from flask import request
from flask.views import MethodView
from consts import WORLD_GRID
from app import app
from flask_pushjack import FlaskAPNS


class NotificationsView(MethodView):
    def post(self):
        # todo: insert incident
        # todo: filter out people by last seen
        nearby_people = WORLD_GRID.get_nearby_people(request.data)
        nearby_people_uuid = [person['uuid'] for person in nearby_people]
        client = FlaskAPNS()
        client.init_app(app)
        with app.app_context():
            # todo: add extra from DB
            results = client.send(nearby_people_uuid, "help! there is an emergency", extra={'to_rescue': request.data, 'incidentID': 'id'})
