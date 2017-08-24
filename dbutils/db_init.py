from app import db
from app.auth.models import *


def InitDB():
    print "Pre-populating DB"

    u1 = User(allergies='Cats', id_number='209499359', blood_type='A+', username='gNir', uuid='12345678901234567890')
    u2 = User(allergies='Cats', id_number='204499359', blood_type='B+', username='joni', uuid='12345678901234567890')
    i1 = Incident(lat=10.5, long=12.2, audio_file_path="tmp/a.avi",
                  description="Joni gay", in_need_id=u1, helpers=[u2])
    db.session.add_all([u1, u2, i1])
    db.session.commit()

    users = User.query.all()

    for u in users:
        print u


if __name__ == '__main__':
    for user in User.query.all():
        print user
