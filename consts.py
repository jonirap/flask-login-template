import os
from grid_algorithm import WorldGrid
WORLD_GRID = WorldGrid()

WORLD_GRID.add_person({'id': 1, 'long': 40.120003, 'lat': 40.220002})
WORLD_GRID.add_person({'id': 2, 'long': 40.120004, 'lat': 40.220002})
WORLD_GRID.add_person({'id': 3, 'long': 30.123, 'lat': 15.222})

SPEECH_FOLDER = os.path.join(__file__, '..', 'speech')
TEXT_FOLDER = os.path.join(__file__, '..', 'text')
