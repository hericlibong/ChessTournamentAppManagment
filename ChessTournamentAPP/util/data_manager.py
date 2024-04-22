
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
    with open(filename, 'r', encoding='utf-8') as file:
        tournaments_data = json.load(file)
        tournaments = []
        for data in tournaments_data:
            registered_players = [Player(**player_data) for player_data in data.get('registered_players', [])]
            player_dict = {player.unique_id: player for player in registered_players}
            rounds = [Round(
                name=round_data['name'], 
                start_time=datetime.strptime(round_data['start_time'], '%Y-%m-%d %H:%M') if 'start_time' in round_data and round_data['start_time'] else None,
                end_time=datetime.strptime(round_data['end_time'], '%Y-%m-%d %H:%M') if 'end_time' in round_data and round_data['end_time'] else None,
                is_complete=round_data.get('is_complete', False),
                matches=[Match(players=(player_dict[match_data['players'][0]], player_dict[match_data['players'][1]]),
                               results=tuple(match_data['results']))
                         for match_data in round_data.get('matches', [])])
                for round_data in data.get('rounds', [])]
            tournament = Tournament(
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
            tournaments.append(tournament)
        return tournaments



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

