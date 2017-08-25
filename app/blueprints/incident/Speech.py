import os

import hebdepparser
import pydub
import requests
from flask import request, jsonify
from flask.ext.login import current_user
from flask.views import MethodView

from Categories import Category
from SpeechToText import convert_audio_file
from app import app, client
from app.auth.models import Incident, User
from consts import SPEECH_FOLDER, WORLD_GRID
from threading import Thread

class IncidentSpeechView(MethodView):
    def post(self):
        nearby_people_uuid = IncidentSpeechView.get_nearby_people()
        print '\nnearby ', nearby_people_uuid

        incident = create_incident()
        print 'Create incident {}'.format(incident)
        if nearby_people_uuid:
            with app.app_context():
                Thread(target=self.send_push_notification, args=[self, incident, nearby_people_uuid]).start()
                self.send_push_notification(incident, nearby_people_uuid)
                print 'sent push notification'

        return jsonify(incident_id=incident.id)

    def send_push_notification(self, incident, nearby_people_uuid):
        client.send(nearby_people_uuid, "Someone needs your help!",
                    title="{} Emergency!".format(incident.category),
                    extra={'incident': incident.to_json()})

    @staticmethod
    def get_nearby_people():
        data = {k: v for k, v in request.form.iteritems()}
        data["id"] = current_user.id
        data['lat'], data['long'] = float(data['lat']), float(data['long'])
        nearby_people = WORLD_GRID.get_nearby_people(data)
        nearby_people_uuid = [User.query.filter_by(id=person['id']).first().uuid for person in nearby_people]
        return nearby_people_uuid


def convert_to_wav(not_wav_file_path):
    filename = get_filename(not_wav_file_path)
    wav_filename = '{}.wav'.format(filename)
    print 'wav ', wav_filename
    print 'not ', not_wav_file_path
    not_wav_file = pydub.AudioSegment.from_file(not_wav_file_path)
    wav_file = not_wav_file.export(os.path.join(SPEECH_FOLDER, wav_filename), format='wav')
    os.remove(not_wav_file_path)
    wav_file.close()
    return wav_filename


def get_filename(not_wav_file_path):
    original_filename = filename = os.path.basename(not_wav_file_path.rsplit('.', 1)[0])
    files = os.listdir(SPEECH_FOLDER)
    while filename + '.wav' in files:
        filename = randomize_filename(original_filename)
    return filename


def randomize_filename(original_filename):
    import uuid
    hex = uuid.uuid4().hex
    return '{}---{}'.format(original_filename, hex)


def save_file():
    f = request.files.values()[0]
    only, ending = f.filename.rsplit('.', 1)
    local_speech_file_path = os.path.join(SPEECH_FOLDER, randomize_filename(only) + '.{}'.format(ending))
    f.save(local_speech_file_path)
    f.close()
    return local_speech_file_path


def create_incident():
    local_speech_file_path = save_file()
    print local_speech_file_path
    local_speech_file_path = convert_to_wav(local_speech_file_path)
    print '\nconverted to wav\n'
    data_text = convert_audio_file(os.path.join(SPEECH_FOLDER, local_speech_file_path))
    print '\nrecognized by google\n'

    try:
        parsed_data_text = hebdepparser.parse(data_text.encode('utf-8'), ip='192.168.0.102')
        print '\nparsed\n'
    except requests.packages.urllib3.exceptions.MaxRetryError:
        print 'did not parse because the parsing server is fucking dumb!'
        parsed_data_text = data_text.encode('utf-8').split()

    data = {k: v for k, v in request.form.iteritems()}

    category = Category.get(parsed_data_text)
    print '\nCATEGORY: {}\n'.format(category)
    return Incident(lat=float(data['lat']), long=float(data['long']), audio_file_path=local_speech_file_path,
                    description=data_text,
                    in_need_id=current_user.id, helpers=[], status="", category=category).save()
