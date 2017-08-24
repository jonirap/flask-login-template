from flask.ext.wtf import Form, IntegerField, TextField
from flask.ext.wtf import Required


class LoginForm(Form):
    id_number = IntegerField('id_number', validators=[Required()])
    uuid = TextField('uuid', validators=[Required()])
