from flask import Blueprint
from Chat import ChatView

chat = Blueprint('chat', __name__, template_folder='templates/chat')
chat.add_url_rule('/chat', view_func=ChatView.as_view('chat'))


class View:
    def get_blueprint(self):
        return chat
