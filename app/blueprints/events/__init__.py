from flask import Blueprint

from IncidentEnd import IncidentEndView
from IncidentState import IncidentStateView
from Volunteer import VolunteerView

events = Blueprint('event', __name__, template_folder='templates/events')
events.add_url_rule('/i_want_to_help', view_func=VolunteerView.as_view('volunteer'))
events.add_url_rule('/incident_state', view_func=IncidentStateView.as_view('incident_state'))
events.add_url_rule('/finished', view_func=IncidentEndView.as_view('finished'))


class View:
    def get_blueprint(self):
        return events
