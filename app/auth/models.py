'''SQLAlchemy Models
    Models used in SQL
'''

from flask.ext.login import UserMixin

from app import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id_number = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(20), nullable=False)
    blood_type = db.Column(db.String(3), nullable=False)
    allergies = db.Column(db.Text)
    fullname = db.Column(db.Text, nullable=False)
    can_help = db.Column(db.Boolean, nullable=False, default=False)
    active = db.Column(db.Boolean, nullable=False, default=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id_number

    def __repr__(self):
        return '<%s(%r, %r)>' % (self.__class__.__name__, self.id_number,
                                 self.username)
