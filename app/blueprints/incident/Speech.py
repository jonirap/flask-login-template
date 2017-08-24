import os
from consts import SPEECH_FOLDER, TEXT_FOLDER
from flask import request, jsonify
from flask.views import MethodView

from SpeechToText import convert_audio_file


class IncidentSpeechView(MethodView):
    def post(self):
        f = request.files.values()[0]
        filename = f.filename
        local_speech_file_path = os.path.join(SPEECH_FOLDER, filename)
        local_text_file_path = os.path.join(TEXT_FOLDER, filename)
        f.save(local_speech_file_path)
        data_text = convert_audio_file(local_speech_file_path)
        with open(local_text_file_path, 'wb') as text_file:
            text_file.write(data_text.encode('utf-8'))
        return jsonify(ok=True)
