from IncidentEnd import IncidentEndView
from IncidentState import IncidentStateView
from Volunteer import VolunteerView
from flask import Blueprint

from app.events.Notifications import NotificationsView

notifications = Blueprint('event', __name__, template_folder='templates/events')
notifications.add_url_rule('/help', view_func=NotificationsView.as_view('notifications'))
notifications.add_url_rule('/i_want_to_help', view_func=VolunteerView.as_view('volunteer'))
notifications.add_url_rule('/incident_state', view_func=IncidentStateView.as_view('incident_state'))
notifications.add_url_rule('/finished', view_func=IncidentEndView.as_view('finished'))


class View:
    def get_blueprint(self):
        return notifications
