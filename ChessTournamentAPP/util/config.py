# util/config.py

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
TOURNAMENTS_FILE = os.path.join(DATA_DIR, 'tournaments.json')
PLAYERS_FILE = os.path.join(DATA_DIR, 'players.json')