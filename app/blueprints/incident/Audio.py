import os

from flask import send_file, request
from flask.views import MethodView

from consts import SPEECH_FOLDER


class AudioView(MethodView):
    def get(self):
        filename = request.args.get('filename')
        return send_file(os.path.join(SPEECH_FOLDER, filename))
