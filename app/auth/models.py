'''SQLAlchemy Models
    Models used in SQL
'''

from flask.ext.login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from consts import WORLD_GRID

from app import db

association_table = db.Table('association', db.Model.metadata,
                             db.Column('left_id', db.Integer, ForeignKey('user.id')),
                             db.Column('right_id', db.Integer, ForeignKey('incident.id'))
                             )


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_number = db.Column(db.Integer, unique=True, nullable=False)
    uuid = db.Column(db.String(20), nullable=False)
    blood_type = db.Column(db.String(3), nullable=False)
    allergies = db.Column(db.Text)
    username = db.Column(db.Text, nullable=False)
    can_help = db.Column(db.Boolean, nullable=False, default=False)
    can_help_medical = db.Column(db.Boolean, nullable=False, default=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    incidents_in_need = relationship('Incident')
    incidents_helped = relationship('Incident', secondary=association_table)

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<%s(%r, %r)>' % (self.__class__.__name__, self.id_number,
                                 self.username)

    def to_json(self):
        i, j = WORLD_GRID.people_locations[self.id]
        return {
            'id': self.id,
            'id_number': self.id_number,
            'uuid': self.uuid,
            'blood_type': self.blood_type,
            'allergies': self.allergies,
            'username': self.username,
            'can_help': self.can_help,
            'can_help_medical': self.can_help_medical,
            'active': self.active,
            'incidents_in_need': self.incidents_in_need,
            'incidents_helped': self.incidents_helped,
            'longitude': WORLD_GRID.world[i][j][self.id]['longitude'],
            'latitude': WORLD_GRID.world[i][j][self.id]['latitude']
        }


class Incident(db.Model):
    __tablename__ = 'incident'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)
    audio_file_path = db.Column(db.String(120), nullable=True)
    description = db.Column(db.Text, nullable=True)
    in_need_id = db.Column(db.Integer, ForeignKey('user.id'))
    helpers = relationship('User', secondary=association_table)
    status = db.Column(db.String(30), nullable=False)

    def get_id(self):
        return self.id

    def __eq__(self, other):
        '''
        Checks the equality of two `UserMixin` objects using `get_id`.
        '''
        if isinstance(other, Incident):
            return self.get_id() == other.get_id()
        return NotImplemented

    def __ne__(self, other):
        '''
        Checks the inequality of two `UserMixin` objects using `get_id`.
        '''
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented
        return not equal

    def __repr__(self):
        return '<%s(%r, %r)>' % (self.__class__.__name__, self.id_number,
                                 self.username)

    def to_json(self):
        return {
            'id': self.id,
            'latitude': self.lat,
            'longitude': self.long,
            'audio_file_path': self.audio_file_path,
            'description': self.description,
            'in_need_id': self.in_need_id,
            'num_of_helpers': len(self.helpers),
            'status': self.status
        }
