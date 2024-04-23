
from datetime import datetime
from typing import List, Tuple
from .match import Match
from .player import Player

class Round:
    def __init__(self, name: str, start_time: datetime = None, end_time: datetime = None, is_complete:bool = False, matches=None):
        self.name = name
        if isinstance(start_time, datetime):
            self.start_time = start_time
        else:
            self.start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M") if start_time else None

        if isinstance(end_time, datetime):
            self.end_time = end_time
        else:
            self.end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M") if end_time else None
        self.is_complete = is_complete
        self.matches = matches if matches else []

    def to_dict(self):
        return {
            'name': self.name,
            'start_time': self.start_time.strftime('%Y-%m-%d %H:%M') if self.start_time else None,
            'end_time': self.end_time.strftime('%Y-%m-%d %H:%M') if self.end_time else None,
            'is_complete': self.is_complete,
            'matches': [match.to_dict() for match in self.matches]
        }
    


    def add_match(self, player1, player2, current_matches, results=(0, 0)):
        if not self.is_complete and (player1, player2) not in current_matches and (player2, player1) not in current_matches:
            if player2.unique_id not in player1.past_opponents:
                match = Match(players=(player1, player2), results=results)
                self.matches.append(match)
                current_matches.add((player1, player2))
                current_matches.add((player2, player1))
                # Mise à jour des adversaires passés
                player1.add_past_opponent(player2.unique_id)
                player2.add_past_opponent(player1.unique_id)
                print(f"Match entre {player1.firstname} {player1.name} et {player2.firstname} {player2.name} ajouté à {self.name}.")
            else:
                print(f"Match entre {player1.firstname} {player1.name} et {player2.firstname} {player2.name} non ajouté car ils ont déjà joué ensemble.")
        else:
            print("Match non ajouté pour éviter les répétitions ou car le round est complet.")

    # def add_match(self, player1, player2, current_matches, results=(0, 0)):
    #     if not self.is_complete and (player1, player2) not in current_matches and (player2, player1) not in current_matches:
    #         match = Match(players=(player1, player2), results=results)
    #         self.matches.append(match)
    #         current_matches.add((player1, player2))
    #         current_matches.add((player2, player1))
    #         print(f"Match entre {player1.firstname} {player1.name} et {player2.firstname} {player2.name} ajouté à {self.name}.")
    #     else:
    #         print("Match non ajouté pour éviter les répétitions ou car le round est complet.")

    def update_match_result(self, match_index, new_results):
        if self.is_complete:
            print(f"Cannot update match results. Round '{self.name}' is already complete.")
            return
        if match_index < 0 or match_index >= len(self.matches):
            print("Invalid match index. Please provide a correct index.")
            return
        self.matches[match_index].set_results(new_results)
        print(f"Results updated for match {match_index + 1} in round '{self.name}'.")

    
    
