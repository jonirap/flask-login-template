from flask import jsonify, session
from flask.ext.login import current_user, login_user
from flask.views import MethodView

from SignUpForm import SignUpForm
from app import db, app
from app.auth.models import User


class SignUpView(MethodView):
    def post(self):
        if current_user.is_authenticated():
            return jsonify(ok=True)
        form = SignUpForm()
        user = User.query.filter_by(id_number=form.id_number.data).first()
        if user is None:
            try:
                user = User(allergies=form.allergies.data,
                            id_number=form.id_number.data,
                            blood_type=form.blood_type.data,
                            username=form.fullname.data,
                            uuid=form.uuid.data,
                            can_help=form.can_help.data).save()
                client = FlaskAPNS()
                client.init_app(app)
                with app.app_context():
                    client.send(user.uuid, "help! there is an emergency", title="emergency alert",
                                extra={'to_rescue': user.to_json(), 'incident_id': "455454"})
                if login_user(user, remember=True):
                    session.permanent = True
            except Exception as e:
                print e.message
                return jsonify(ok=False, error='Error adding to DB')
            return jsonify(ok=True)
        return jsonify(ok=False, error='id number exists')
