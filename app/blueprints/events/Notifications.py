from flask import request
from flask.views import MethodView
from consts import WORLD_GRID
from app import app
from flask_pushjack import FlaskAPNS


class NotificationsView(MethodView):
    def post(self):
        # todo: filter out people by last seen
        incident = request.data['incident_id']
        nearby_people = WORLD_GRID.get_nearby_people(request.data)
        nearby_people_uuid = [person['uuid'] for person in nearby_people]
        client = FlaskAPNS()
        client.init_app(app)
        with app.app_context():
            # todo: add extra from DB
            results = client.send(nearby_people_uuid, "help! there is an emergency", title="emergency alert",
                                  extra={'to_rescue': request.data, 'incident_id': 'id'})


