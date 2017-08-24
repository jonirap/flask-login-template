import os
import hebdepparser
import pydub
import requests

from Categories import Category
from consts import SPEECH_FOLDER, WORLD_GRID
from flask import request, jsonify
from flask.views import MethodView
from app.auth.models import Incident, User
from flask.ext.login import current_user
import json
from app import app, client
from SpeechToText import convert_audio_file


class IncidentSpeechView(MethodView):
    def post(self):
        nearby_people_uuid = IncidentSpeechView.get_nearby_people()

        incident = create_incident()
        with app.app_context():
            client.send(nearby_people_uuid, "Someone needs your help!", title="{} Emergency!".format(incident.category),
                        extra={'to_rescue': current_user.to_json(), 'incident_id': incident.id})

        return jsonify(incident_id=incident.id)

    @staticmethod
    def get_nearby_people():
        data = json.loads(request.data)
        # data["id"] = current_user.id_number
        nearby_people = WORLD_GRID.get_nearby_people(data)
        nearby_people_uuid = [User.query.filter_by(id=person['id']).first().uuid for person in nearby_people]
        return nearby_people_uuid


def convert_to_wav(not_wav_file_path):
    wav_file = pydub.AudioSegment.from_file(not_wav_file_path).export(
        not_wav_file_path.rsplit('.', 1)[0] + '.wav', format='wav')
    os.remove(not_wav_file_path)
    local_speech_file_path = wav_file.name
    wav_file.close()
    return local_speech_file_path


def save_file(f):
    local_speech_file_path = os.path.join(SPEECH_FOLDER, f.filename)
    f.save(local_speech_file_path)
    f.close()
    return local_speech_file_path


def create_incident():
    f = request.files.values()[0]
    local_speech_file_path = save_file(f)

    if not f.filename.endswith('.wav'):
        local_speech_file_path = convert_to_wav(local_speech_file_path)
    data_text = convert_audio_file(local_speech_file_path)

    try:
        parsed_data_text = hebdepparser.parse(data_text.encode('utf-8'), ip='192.168.0.106')
    except requests.packages.urllib3.exceptions.MaxRetryError:
        print 'did not parse because the parsing server is fucking dumb!'
        parsed_data_text = data_text.encode('utf-8').split()

    category = Category.get(parsed_data_text)
    return Incident(lat=10.5, long=12.2, audio_file_path=local_speech_file_path, description=data_text,
                    in_need_id=current_user.id, helpers=[], status="", category=category).save()

