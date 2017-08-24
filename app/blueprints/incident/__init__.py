from flask import Blueprint
from Speech import IncidentSpeechView

incident = Blueprint('incident', __name__)
incident.add_url_rule('/help', view_func=IncidentSpeechView.as_view('speech'))


class View:
    def get_blueprint(self):
        return incident