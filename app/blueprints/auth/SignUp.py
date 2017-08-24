from flask import jsonify, session
from flask.ext.login import current_user, login_user
from flask.views import MethodView

from SignUpForm import SignUpForm
from app import db
from app.auth.models import User


class SignUpView(MethodView):
    def post(self):
        if current_user.is_authenticated():
            return jsonify(ok=True)
        form = SignUpForm()
        user = User.query.filter_by(id_number=form.id_number.data).first()
        if user is None:
            try:
                db.session.add(User(allergies=form.allergies.data,
                                    id_number=form.id_number.data,
                                    blood_type=form.blood_type.data,
                                    fullname=form.fullname.data,
                                    email=form.email.data,
                                    uuid=form.uuid.data))
                db.session.commit()
                if login_user(user, remember=True):
                    session.permanent = True
            except:
                return jsonify(ok=False, error='Error adding to DB')

        return jsonify(ok=True)
