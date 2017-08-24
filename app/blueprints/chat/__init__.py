from flask import Blueprint
from Chat import ChatView

home = Blueprint('chat', __name__, template_folder='templates/chat')
home.add_url_rule('/', view_func=ChatView.as_view('chat'))


class View:
    def get_blueprint(self):
        return home
