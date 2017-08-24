from app import db
from app.auth.models import *


def InitDB():
    print "Pre-populating DB"

    u1 = User(allergies='Cats', id_number='209499359', blood_type='A+', username=u'gNir', password=u'123456',
              email='admin@example.com')

    db.session.add(u1)
    db.session.commit()

    users = User.query.all()

    for u in users:
        print u


if __name__ == '__main__':
    for user in User.query.all():
        print user.blood_type