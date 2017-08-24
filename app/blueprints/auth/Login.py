from flask import render_template, flash, redirect, request, session, jsonify
from flask.views import MethodView

from app.auth.models import *

from flask.ext.login import login_user, current_user
from LoginForm import LoginForm


class LoginView(MethodView):
    def post(self):
        if current_user.is_authenticated():
            return jsonify(ok=True)
        form = LoginForm()
        user = User.query.filter_by(id_number=form.id_number.data).first()
        if user is not None:
            if login_user(user, remember=True):
                session.permanent = True
                return jsonify(ok=True)
        return jsonify(ok=False)
