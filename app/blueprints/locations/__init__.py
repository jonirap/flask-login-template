from Locations import LocationsView

__author__ = 'Kieran'

from flask import Blueprint

locations = Blueprint('notifications', __name__, template_folder='templates/notifications')
locations.add_url_rule('/location', view_func=LocationsView.as_view('notifications'))

class View:
    def get_blueprint(self):
        return locations