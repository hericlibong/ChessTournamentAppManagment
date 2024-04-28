
# util/data_manager.py

import json
import os
from datetime import datetime
from models.tournament import Tournament
from models.round import Round
from models.player import Player
from models.match import Match

from .config import TOURNAMENTS_FILE, PLAYERS_FILE


def my_datetime_handler(x):
    """
    Gère la sérialisation des objets datetime pour la conversion en JSON.
    
    Paramètres :
    - x (object) : L'objet à sérialiser.

    Retourne :
    - str : Représentation en chaîne de caractères de l'objet datetime, formatée selon '%Y-%m-%d %H:%M'.
    
    Lève :
    - TypeError : Si 'x' n'est pas une instance de datetime.datetime.
    """
    if isinstance(x, datetime):
        return x.strftime('%Y-%m-%d %H:%M')
    raise TypeError("Object of type 'datetime' is not JSON serializable")

def save_tournaments(tournaments, filename=TOURNAMENTS_FILE):
    """
    Sauvegarde une liste de tournois dans un fichier JSON.

    Paramètres :
    - tournaments (list) : Liste d'objets Tournament à sérialiser et sauvegarder.
    - filename (str) : Chemin vers le fichier où les tournois seront sauvegardés.

    Effets :
    - Crée le répertoire du fichier s'il n'existe pas.
    - Écrit les données des tournois dans un fichier JSON.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump([tournament.to_dict() for tournament in tournaments], file, ensure_ascii=False, indent=4, default=my_datetime_handler)

def load_tournaments(filename=TOURNAMENTS_FILE):
    """
    Charge les tournois à partir d'un fichier JSON.

    Paramètres :
    - filename (str) : Chemin vers le fichier JSON contenant les données des tournois.

    Retourne :
    - list : Liste des objets Tournament chargés, ou une liste vide en cas d'échec.

    Gère :
    - FileNotFoundError : Avertissement si le fichier n'est pas trouvé, retourne une liste vide.
    - JSONDecodeError : Erreur si le fichier JSON est mal formé.
    """
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        print("Warning: No tournament data found, returning empty list.")
        return []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            tournaments_data = json.load(file)
            return [build_tournament_from_data(data) for data in tournaments_data]
    except json.JSONDecodeError:
        print("Error decoding JSON from file.")
        return []





def build_tournament_from_data(data):
    registered_players = [Player(**player_data) for player_data in data.get('registered_players', [])]
    player_dict = {player.unique_id: player for player in registered_players}
    rounds = [build_round_from_data(round_data, player_dict) for round_data in data.get('rounds', [])]
    return Tournament(
        name=data['name'],
        location=data['location'],
        description=data['description'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        total_round=data['total_round'],
        t_id=data['t_id'],
        current_round=data['current_round'],
        rounds=rounds,
        registered_players=registered_players
    )

def build_round_from_data(round_data, player_dict):
    matches = [Match(players=(player_dict[match_data['players'][0]], player_dict[match_data['players'][1]]),
                     results=tuple(match_data['results'])) for match_data in round_data.get('matches', [])]
    return Round(
        name=round_data['name'],
        start_time=datetime.strptime(round_data['start_time'], '%Y-%m-%d %H:%M') if 'start_time' in round_data else None,
        end_time=datetime.strptime(round_data['end_time'], '%Y-%m-%d %H:%M') if 'end_time' in round_data and round_data['end_time'] else None,
        is_complete=round_data.get('is_complete', False),
        matches=matches
    )


def save_players(players, filename=PLAYERS_FILE):
    """
    Sauvegarde une liste de joueurs dans un fichier JSON.

    Paramètres :
    - players (list) : Liste d'objets Player à sérialiser et sauvegarder.
    - filename (str) : Chemin vers le fichier où les joueurs seront sauvegardés.

    Effets :
    - Crée le répertoire du fichier s'il n'existe pas.
    - Écrit les données des joueurs dans un fichier JSON.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump([player.to_dict() for player in players], file, ensure_ascii=False, indent=4)


def load_players(filename=PLAYERS_FILE):
    """
    Charge les joueurs à partir d'un fichier JSON.

    Paramètres :
    - filename (str) : Chemin vers le fichier JSON contenant les données des joueurs.

    Retourne :
    - list : Liste des objets Player chargés, ou une liste vide en cas d'échec.

    Gère :
    - FileNotFoundError : Avertissement si le fichier n'est pas trouvé, retourne une liste vide.
    - JSONDecodeError : Erreur si le fichier JSON est mal formé.
    - KeyError : Gestion des clés manquantes dans les données JSON.
    """
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        print("Warning: No player data found, returning empty list.")
        return []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            players_data = json.load(file)
            return [Player(**data) for data in players_data]
    except json.JSONDecodeError:
        print("Error decoding JSON from file.")
        return []
    except KeyError as e:
        print(f"Error: Missing expected data key in player data: {str(e)}")
        return []






























# def save_tournaments(tournaments, filename="data/tournaments.json"):
#     os.makedirs(os.path.dirname(filename), exist_ok=True)
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump([tournament.to_dict() for tournament in tournaments], file, ensure_ascii=False, indent=4, default=my_datetime_handler)


# def my_datetime_handler(x):
#     if isinstance(x, datetime):
#         return x.strftime('%Y-%m-%d %H:%M')
#     raise TypeError("Unknown type")        


# def load_tournaments(filename="data/tournaments.json"):
#     with open(filename, 'r', encoding='utf-8') as file:
#         tournaments_data = json.load(file)
#         tournaments = []
#         for data in tournaments_data:
#             registered_players = [Player(**player_data) for player_data in data.get('registered_players', [])]
#             player_dict = {player.unique_id: player for player in registered_players}
#             rounds = [Round(
#                 name=round_data['name'], 
#                 start_time=datetime.strptime(round_data['start_time'], '%Y-%m-%d %H:%M') if 'start_time' in round_data and round_data['start_time'] else None,
#                 end_time=datetime.strptime(round_data['end_time'], '%Y-%m-%d %H:%M') if 'end_time' in round_data and round_data['end_time'] else None,
#                 is_complete=round_data.get('is_complete', False),
#                 matches=[Match(players=(player_dict[match_data['players'][0]], player_dict[match_data['players'][1]]),
#                                results=tuple(match_data['results']))
#                          for match_data in round_data.get('matches', [])])
#                 for round_data in data.get('rounds', [])]
#             tournament = Tournament(
#                 name=data['name'],
#                 location=data['location'],
#                 description=data['description'],
#                 start_date=data['start_date'],
#                 end_date=data['end_date'],
#                 total_round=data['total_round'],
#                 t_id=data['t_id'],
#                 current_round=data['current_round'],
#                 rounds=rounds,
#                 registered_players=registered_players
#             )
#             tournaments.append(tournament)
#         return tournaments



# def load_players(filename="data/players.json"):
#     if not os.path.exists(filename) or os.stat(filename).st_size == 0:
#         return []  # Retourne une liste vide si le fichier n'existe pas ou est vide
#     with open(filename, 'r', encoding='utf-8') as file:
#         players_data = json.load(file)
#         return [Player(**data) for data in players_data]

# def save_players(players, filename="data/players.json"):
#     os.makedirs(os.path.dirname(filename), exist_ok=True)
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump([player.to_dict() for player in players], file, ensure_ascii=False, indent=4)

