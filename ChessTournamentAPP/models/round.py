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
        """Ajoute un match au round avec les joueurs et les résultats spécifiés"""
        match = Match(players=(player1, player2), results=results)
        if not self.is_complete:
            self.matches.append(match)
            print(f"Le match entre {player1.firstname} {player1.name} and {player2.firstname} {player2.name} a été ajouté au round '{self.name}")
        else:
            print("Cannot add match to a completed round")

    

    # def add_match(self, match):
    #     """Ajoute un match à la liste des matchs du tour."""
    #     if not self.is_complete:
    #         self.matches.append(match)
    #     else:
    #         print("Impossible d'ajouter un match à un tour complet")


    # # Ajouté en guise de test
    # def complete_round(self):
    #     self.is_complete = True
    #     self.end_time = datetime.now()

    
