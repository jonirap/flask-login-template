from Volunteer import VolunteerView
from Notifications import NotificationsView
from IncidentState import IncidentStateView

__author__ = 'Kieran'

from flask import Blueprint

notifications = Blueprint('notifications', __name__, template_folder='templates/notifications')
notifications.add_url_rule('/help', view_func=NotificationsView.as_view('notifications'))
notifications.add_url_rule('/i_want_to_help', view_func=VolunteerView.as_view('volunteer'))
notifications.add_url_rule('/incident_state', view_func=IncidentStateView.as_view('incident_state'))


class View:
    def get_blueprint(self):
        return notifications
