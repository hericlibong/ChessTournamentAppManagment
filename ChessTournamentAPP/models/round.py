#models/round.py

from datetime import datetime
from typing import List, Tuple
from .match import Match
from .player import Player

class Round:
    """Représentation d'un tour dans un tournoi d'échecs."""
    def __init__(self, name: str, start_time: datetime = None, end_time: datetime = None, is_complete:bool = False):
        """Initialise  le nom, la date de début et la date de fin d'un tour dans un tournoi """
        self.name = name
        self.start_time = start_time if start_time else datetime.now() # Un tour commence immédiatement par défaut si aucune heure de début n'est spécifiée
        self.end_time = end_time
        self.matches = []  # type: List[Match]
        self.is_complete = is_complete  # Attribut ajouté en guise de test



    def add_match(self, player1:Player, player2:Player, results: Tuple[float, float] = (0, 0)):
        """Ajoute un match au round avec les joueurs et les résultats spécifiés si le round n'est pas complet"""
        if self.is_complete:
            print("Le round est complet. On ne peut pas ajouter ce match.")
            return
        new_match = Match(players=(player1, player2), results=results)
        self.matches.append(new_match)
        print(f"Le match entre {player1.firstname} {player1.name} and {player2.firstname} {player2.name} a été ajouté au round '{self.name}")
        

    def update_match_result(self, match_index, new_results):
        """Mise à jour des résultats d'un match spécifique dans le round."""
        if self.is_complete:
            print(f"Cannot update match results. Round '{self.name}' is already complete.")
            return

        if match_index < 0 or match_index >= len(self.matches):
            print("Invalid match index. Please provide a correct index.")
            return

        # Mise à jour des résultats du match
        self.matches[match_index].set_results(new_results)
        print(f"Results updated for match {match_index + 1} in round '{self.name}'.")

    
    
