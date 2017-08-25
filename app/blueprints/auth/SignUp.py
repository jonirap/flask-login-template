import json

from flask import jsonify, session, request
from flask.ext.login import current_user, login_user
from flask.views import MethodView

from SignUpForm import SignUpForm
from app import db, app
from app.auth.models import User


class SignUpView(MethodView):
    def post(self):
        data = json.loads(request.data)
        user = User.query.filter_by(id_number=data['id_number']).first()
        if user is None:
            try:
                user = User(allergies=data['allergies'],
                            id_number=data['id_number'],
                            blood_type=data['blood_type'],
                            username=data['fullname'],
                            uuid=change_id(data['uuid']),
                            can_help_medical=data['can_help_medical']).save()
                if login_user(user, remember=True):
                    session.permanent = True
            except Exception as e:
                return jsonify(ok=False, error='Error adding to DB'), 500
            return jsonify(ok=True)
        return jsonify(ok=False, error='id number exists'), 300


def change_id(id):
    return id.replace('<', '').replace('>', '').replace(' ', '')
