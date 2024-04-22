# models/match.py


from typing import Tuple
from .player import Player

class Match:
    """Représentation d'un match entre deux joueurs."""
    def __init__(self, players: Tuple['Player', 'Player'], results: Tuple[float, float] = (0, 0)):
        self.players = players
        self.results = results  # Tuple de la forme (score_joueur_1, score_joueur_2)
        self.is_complete = False


    def set_results(self, result: str):
        """Définit les résultats du match en fonction d'un code de résultat."""
        if not self.is_complete:
            if result == '1':
                self.results = (1, 0)  # Victoire pour le joueur 1
            elif result == '2':
                self.results = (0, 1)  # Victoire pour le joueur 2
            elif result == '0':
                self.results = (0.5, 0.5)  # Match nul
            self.is_complete = True
        else:
            print("Le résultat ne peut pas être modifié; le match est déjà terminé.")



    def to_dict(self):
        """Sérialise l'objet Match pour la sauvegarde en JSON."""
        return {
            'players': [player.unique_id for player in self.players],
            'results': self.results
        }
    

    def set_results(self, results: Tuple[float, float]):
        """Définit les résultats du match."""
        if not self.is_complete:
            self.results = results
            self.is_complete = True
        else:
            print("Le résultat ne peut pas être modifié; le match est déjà terminé.")

    
    def get_winner(self):
        """Retourne le joueur ayant le score le plus élevé ou None en cas de match nul"""
        if self.results[0] > self.results[1]:
            return self.players[0]
        elif self.results[1] > self.results[0]:
            return self.players[1]
        return None
    

    def reset_match(self):
        """Réinitialise les résultats du match."""
        self.results = (0, 0)
        self.is_complete = False