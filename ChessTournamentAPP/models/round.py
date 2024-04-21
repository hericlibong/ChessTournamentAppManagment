# from datetime import datetime
# from typing import List, Tuple
# from .match import Match
# from .player import Player

# class Round:
#     """Représentation d'un tour dans un tournoi d'échecs."""
#     def __init__(self, name: str, start_time: datetime = None, end_time: datetime = None, is_complete:bool = False):
#         self.name = name
#         self.start_time = start_time if start_time else datetime.now()
#         self.end_time = end_time
#         self.matches = []
#         self.is_complete = is_complete

#     def to_dict(self):
#         return {
#             'name': self.name,
#             'start_time': self.start_time.strftime('%Y-%m-%d %H:%M') if self.start_time else None,
#             'end_time': self.end_time.strftime('%Y-%m-%d %H:%M') if self.end_time else None,
#             'is_complete': self.is_complete,
#             'matches': [match.to_dict() for match in self.matches]
#         }

#     def add_match(self, player1, player2):
#         """Adds a match to the round if not already present and the round is not complete."""
#         if self.is_complete:
#             print("Cannot add matches to a completed round.")
#             return

#         # Check for existing matches to prevent duplicates
#         player_pair = frozenset({player1, player2})
#         existing_pairs = {frozenset({match.players[0], match.players[1]}) for match in self.matches}

#         if player_pair not in existing_pairs:
#             match = Match(players=(player1, player2))
#             self.matches.append(match)
#             print(f"Match between {player1.name} and {player2.name} added to {self.name}.")
#         else:
#             print("Match not added to avoid duplication.")

#     def update_match_result(self, match_index, result):
#         """Updates the result of a specific match."""
#         if self.is_complete or match_index >= len(self.matches):
#             print("Cannot update match results for this round.")
#             return

#         self.matches[match_index].set_results(result)
#         print(f"Results updated for match {match_index + 1} in round '{self.name}'.")

# models/round.py

from datetime import datetime
from typing import List, Tuple
from .match import Match
from .player import Player

class Round:
    def __init__(self, name: str, start_time: datetime = None, end_time: datetime = None, is_complete:bool = False, matches=None):
        self.name = name
        self.start_time = start_time if start_time else datetime.now()
        self.end_time = end_time
        self.is_complete = is_complete
        self.matches = [Match(**match) for match in matches] if matches else []

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
            match = Match(players=(player1, player2), results=results)
            self.matches.append(match)
            current_matches.add((player1, player2))
            current_matches.add((player2, player1))
            print(f"Match entre {player1.firstname} {player1.name} et {player2.firstname} {player2.name} ajouté à {self.name}.")
        else:
            print("Match non ajouté pour éviter les répétitions ou car le round est complet.")

    def update_match_result(self, match_index, new_results):
        if self.is_complete:
            print(f"Cannot update match results. Round '{self.name}' is already complete.")
            return
        if match_index < 0 or match_index >= len(self.matches):
            print("Invalid match index. Please provide a correct index.")
            return
        self.matches[match_index].set_results(new_results)
        print(f"Results updated for match {match_index + 1} in round '{self.name}'.")

    
    
