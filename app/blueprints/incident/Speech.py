import os

import pydub

from Categories import Category
from consts import SPEECH_FOLDER
from flask import request, jsonify
from flask.views import MethodView
from app.auth.models import Incident

from SpeechToText import convert_audio_file


class IncidentSpeechView(MethodView):
    def post(self):
        f = request.files.values()[0]
        filename = f.filename
        local_speech_file_path = os.path.join(SPEECH_FOLDER, filename)
        f.save(local_speech_file_path)
        f.close()
        if not filename.endswith('.wav'):
            local_speech_file_path = convert_to_wav(local_speech_file_path)
        data_text = convert_audio_file(local_speech_file_path).encode('utf-8')

        category = Category.get(data_text)
        incident = Incident(lat=10.5, long=12.2, audio_file_path=local_speech_file_path,
                            description=data_text, in_need_id=1, helpers=[], status="", category=category)


        return jsonify(incident_id=incident.id)


def convert_to_wav(not_wav_file_path):
    wav_file = pydub.AudioSegment.from_file(not_wav_file_path).export(
        not_wav_file_path.rsplit('.', 1)[0] + '.wav', format='wav')
    os.remove(not_wav_file_path)
    local_speech_file_path = wav_file.name
    wav_file.close()
    return local_speech_file_path
