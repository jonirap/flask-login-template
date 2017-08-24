import os
from config import TEXT_FOLDER
from flask import request
from flask.views import MethodView


class IncidentTextView(MethodView):
    def post(self):
        f = request.files['file']
        filename = f.filename
        local_text_file_path = os.path.join(TEXT_FOLDER, filename)
        f.save(local_text_file_path)
