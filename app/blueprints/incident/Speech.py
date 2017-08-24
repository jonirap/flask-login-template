import os

import pydub

from Categories import Category
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
        # import ipdb; ipdb.set_trace()
        f.close()
        if not filename.endswith('.wav'):
            wav_file = pydub.AudioSegment.from_file(local_speech_file_path).export(
                local_speech_file_path.rsplit('.', 1)[0] + '.wav', format='wav')
            os.remove(local_speech_file_path)
            local_speech_file_path = wav_file.name
            wav_file.close()
        data_text = convert_audio_file(local_speech_file_path).encode('utf-8')
        with open(local_text_file_path, 'wb') as text_file:
            text_file.write(data_text)

        category = Category.get(data_text)

        return jsonify(category=category)
