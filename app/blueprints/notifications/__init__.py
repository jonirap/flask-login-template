from Notifications import NotificationsView

__author__ = 'Kieran'

from flask import Blueprint

notifications = Blueprint('notifications', __name__, template_folder='templates/notifications')
notifications.add_url_rule('/post_alert', view_func=NotificationsView.as_view('notifications'))

class View:
    def get_blueprint(self):
        return notifications