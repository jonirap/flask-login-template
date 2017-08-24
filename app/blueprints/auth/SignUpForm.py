from flask.ext.wtf import Form, TextField, BooleanField, IntegerField, TextAreaField, SelectField, HiddenField
from flask.ext.wtf import Required


class SignUpForm(Form):
    id_number = IntegerField('ID number', validators=[Required('Enter your id number')])
    blood_type = SelectField('Select you blood type', choices=['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
    allergies = TextAreaField('Enter all your allergies')
    fullname = TextField('fullname', validators=[Required('Choose a username to be displayed when you need help')])
    can_help = BooleanField('can_help', default=False)
    uuid = HiddenField('uuid', validators=[Required()])
