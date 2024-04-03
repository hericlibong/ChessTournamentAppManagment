from typing import Tuple
from player import Player

class Match:
    """Représentation d'un match entre deux joueurs."""
    def __init__(self, players: Tuple['Player', 'Player'], results: Tuple[float, float] = (0, 0)):
        self.players = players
        self.results = results  # Tuple de la forme (score_joueur_1, score_joueur_2)

    def set_results(self, results: Tuple[float, float]):
        """Définit les résultats du match."""
        self.results = results
