
from datetime import datetime
from typing import List
from match import Match

class Round:
    """Représentation d'un tour dans un tournoi d'échecs."""
    def __init__(self, name: str, start_time: datetime = None, end_time: datetime = None):
        """Initialise  le nom, la date de début et la date de fin d'un tour dans un tournoi """
        self.name = name
        self.start_time = start_time if start_time else datetime.now() # Un tour commence immédiatement par défaut si aucune heure de début n'est spécifiée
        self.end_time = end_time
        self.matches = []  # type: List[Match]

    def add_match(self, match):
        """Ajoute un match à la liste des matchs du tour."""
        self.matches.append(match)
