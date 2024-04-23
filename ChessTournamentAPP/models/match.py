# models/match.py

from typing import Tuple
from .player import Player

class Match:
    """Représentation d'un match entre deux joueurs."""
    def __init__(self, players: Tuple[Player, Player], results: Tuple[float, float] = (0, 0)):
        self.players = players
        self.results = results  # Tuple de la forme (score_joueur_1, score_joueur_2)
        self.is_complete = False

    def to_dict(self):
        """Sérialise l'objet Match pour la sauvegarde en JSON."""
        return {
            'players': [player.unique_id for player in self.players],  # Stockage par unique_id pour cohérence avec les données enregistrées
            'results': self.results
        }

    def set_results(self, result):
        if self.is_complete:
            print("Le résultat ne peut pas être modifié; le match est déjà terminé.")
            return

        if isinstance(result, tuple) and len(result) == 2:
            try:
                score1, score2 = map(float, result)  # Assurez-vous que les scores sont des flottants
                if score1 >= 0 and score2 >= 0 and (score1 + score2) in [1, 0.5]:
                    self.results = (score1, score2)
                    self.is_complete = True
                else:
                    print("Format de résultat invalide.")
            except ValueError:
                print("Format de résultat invalide.")
        else:
            print("Format de résultat invalide ou inattendu.")

    
    
    
    def get_winner(self):
        """Retourne le joueur ayant le score le plus élevé ou None en cas de match nul."""
        if self.results[0] > self.results[1]:
            return self.players[0]
        elif self.results[1] > self.results[0]:
            return self.players[1]
        return None

    def reset_match(self):
        """Réinitialise les résultats du match."""
        self.results = (0, 0)
        self.is_complete = False
