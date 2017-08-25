from flask import Blueprint
from Speech import IncidentSpeechView
from app.blueprints.incident.Audio import AudioView

incident = Blueprint('incident', __name__)
incident.add_url_rule('/help', view_func=IncidentSpeechView.as_view('help'))
incident.add_url_rule('/audio', view_func=AudioView.as_view('audio'))


class View:
    def get_blueprint(self):
        return incident