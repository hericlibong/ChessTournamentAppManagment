# # util/data_manager.py

# from models.tournament import Tournament
# from models.player import Player
# import json
# import os

# def save_tournaments(tournaments, filename="data/tournaments.json"):
#     """
#     Sauvegarde la liste des tournois dans un fichier JSON.
#     """
#     os.makedirs(os.path.dirname(filename), exist_ok=True)  # Assure que le dossier existe
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump([tournament.to_dict() for tournament in tournaments], file, ensure_ascii=False, indent=4)




# def load_tournaments(filename="data/tournaments.json"):
#     """
#     Charge les tournois depuis un fichier JSON et les retourne comme une liste d'instances de Tournament.
#     """
#     if not os.path.exists(filename) or os.stat(filename).st_size == 0:
#         return []  # Retourne une liste vide si le fichier n'existe pas ou est vide
    
#     with open(filename, 'r', encoding='utf-8') as file:
#         try:
#             tournaments_data = json.load(file)
#             tournaments = []
#             for data in tournaments_data:
#                 # Créez des instances de Player pour chaque joueur enregistré
#                 registered_players = [Player(**player_data) for player_data in data.get('registered_players', [])]
#                 # Remplacez la liste des dictionnaires par la liste des instances de Player
#                 data['registered_players'] = registered_players
#                 tournaments.append(Tournament(**data))
#             return tournaments
#         except json.decoder.JSONDecodeError:
#             return []  # Retourne une liste vide en cas d'erreur




# def load_players(filename="data/players.json"):
#     """
#     Charge les joueurs depuis un fichier JSON et les retourne comme une liste d'instances de Player.
#     """
#     if not os.path.exists(filename) or os.stat(filename).st_size == 0:
#         return []  # Retourne une liste vide si le fichier n'existe pas ou est vide
#     with open(filename, 'r', encoding='utf-8') as file:
#         players_data = json.load(file)
#         return [Player(**data) for data in players_data]

# def save_players(players, filename="data/players.json"):
#     """
#     Sauvegarde la liste des joueurs dans un fichier JSON.
#     """
#     os.makedirs(os.path.dirname(filename), exist_ok=True)  # Assure que le dossier existe
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump([player.to_dict() for player in players], file, ensure_ascii=False, indent=4)


# util/data_manager.py

import json
import os
from datetime import datetime
from models.tournament import Tournament
from models.round import Round
from models.player import Player
from models.match import Match

def save_tournaments(tournaments, filename="data/tournaments.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump([tournament.to_dict() for tournament in tournaments], file, ensure_ascii=False, indent=4)

def load_tournaments(filename="data/tournaments.json"):
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        return []  # Retourne une liste vide si le fichier n'existe pas ou est vide
    
    with open(filename, 'r', encoding='utf-8') as file:
        try:
            tournaments_data = json.load(file)
            tournaments = []
            for data in tournaments_data:
                registered_players = [Player(**player_data) for player_data in data.get('registered_players', [])]
                rounds = [Round(name=round_data['name'], 
                                start_time=datetime.strptime(round_data['start_time'], '%Y-%m-%d %H:%M') if round_data['start_time'] else None,
                                end_time=datetime.strptime(round_data['end_time'], '%Y-%m-%d %H:%M') if round_data['end_time'] else None,
                                is_complete=round_data['is_complete'],
                                matches=[Match(**match_data) for match_data in round_data['matches']])
                          for round_data in data.get('rounds', [])]
                data['registered_players'] = registered_players
                data['rounds'] = rounds
                tournaments.append(Tournament(**data))
            return tournaments
        except json.decoder.JSONDecodeError:
            return []  # Retourne une liste vide en cas d'erreur

def load_players(filename="data/players.json"):
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        return []  # Retourne une liste vide si le fichier n'existe pas ou est vide
    with open(filename, 'r', encoding='utf-8') as file:
        players_data = json.load(file)
        return [Player(**data) for data in players_data]

def save_players(players, filename="data/players.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump([player.to_dict() for player in players], file, ensure_ascii=False, indent=4)

