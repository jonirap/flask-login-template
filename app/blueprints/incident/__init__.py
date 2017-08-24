from flask import Blueprint
from Speech import IncidentSpeechView
from Text import IncidentTextView

incident = Blueprint('incident', __name__)
incident.add_url_rule('/speech', IncidentSpeechView.as_view('speech'))
incident.add_url_rule('/text', IncidentTextView.as_view('text'))


class View:
    def get_blueprint(self):
        return incident