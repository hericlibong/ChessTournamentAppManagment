# util/data_manager.py

from models.tournament import Tournament
from models.player import Player
import json
import os

def save_tournaments(tournaments, filename="data/tournaments.json"):
    """
    Sauvegarde la liste des tournois dans un fichier JSON.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # Assure que le dossier existe
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump([tournament.to_dict() for tournament in tournaments], file, ensure_ascii=False, indent=4)

def load_tournaments(filename="data/tournaments.json"):
    """
    Charge les tournois depuis un fichier JSON et les retourne comme une liste d'instances de Tournament.
    """
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        return []  # Retourne une liste vide si le fichier n'existe pas ou est vide
    with open(filename, 'r', encoding='utf-8') as file:
        try:
            tournaments_data = json.load(file)
            return [Tournament(**data) for data in tournaments_data]
        except json.decoder.JSONDecodeError:
            return []  # Retourne une liste vide en cas d'erreur

def load_players(filename="data/players.json"):
    """
    Charge les joueurs depuis un fichier JSON et les retourne comme une liste d'instances de Player.
    """
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        return []  # Retourne une liste vide si le fichier n'existe pas ou est vide
    with open(filename, 'r', encoding='utf-8') as file:
        players_data = json.load(file)
        return [Player(**data) for data in players_data]

def save_players(players, filename="data/players.json"):
    """
    Sauvegarde la liste des joueurs dans un fichier JSON.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # Assure que le dossier existe
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump([player.to_dict() for player in players], file, ensure_ascii=False, indent=4)
