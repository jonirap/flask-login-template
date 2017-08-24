from flask import request
from flask.views import MethodView
from config import WOURLD_GRID

from app import app
from flask_pushjack import FlaskAPNS



class NotificationsView(MethodView):
    def post(self):
        nearby_people = WOURLD_GRID.get_nearby_people(request.data)
        nearby_people_uuid = [person['uuid'] for person in nearby_people]
        client = FlaskAPNS()
        client.init_app(app)

        with app.app_context():
            results = client.send(nearby_people_uuid, "help")
