<<<<<<< HEAD
from flask import Flask
from flask_socketio import SocketIO

SOCKETIO = SocketIO()
=======
import os
from grid_algorithm import WorldGrid
WORLD_GRID = WorldGrid()
SPEECH_FOLDER = os.path.join(__file__, '..', 'speech')
<<<<<<< HEAD
TEXT_FOLDER = os.path.join(__file__, '..', 'text')
>>>>>>> 57fc4980db77482c17ab40fa6511de87e2006bef
=======
TEXT_FOLDER = os.path.join(__file__, '..', 'text')
>>>>>>> 5f956e74388f91e55068c559be8572956b56b540
