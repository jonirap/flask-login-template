from app.auth.models import *


def InitDB():

    print "Pre-populating DB"

    u1 = User(allergies='Cats', id_number='209499359', blood_type='A+', username='gNir', uuid='12345678901234567890')
    u3 = User(allergies='Cats', id_number='209499659', blood_type='A+', username='gNir', uuid='12645678901234567890')

    i1 = Incident(lat=10.5, long=12.2, audio_file_path="tmp/a.avi",
                  description="Joni gay", in_need_id=u1.get_id(), helpers=[], status="running", category='')
    u2 = User(incidents_helped=[], incidents_in_need=[i1], allergies='Cats', id_number='204499359',
              blood_type='B+', username='joni', uuid='12345678901234567890')
    db.session.add_all([u1, u2, i1])
    db.session.commit()

    WORLD_GRID.add_person({'id': u1.id, 'longitude': 40.123, 'latitude': 40.222})
    WORLD_GRID.add_person({'id': u3.id, 'longitude': 41.123, 'latitude': 41.222})
    WORLD_GRID.add_person({'id': u2.id, 'longitude': 30.123, 'latitude': 15.222})

    users = User.query.all()
    for u in users:
        print u

if __name__ == '__main__':
    for user in User.query.all():
        print user
