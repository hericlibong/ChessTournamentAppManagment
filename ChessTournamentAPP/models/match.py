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
        """
        Définit les résultats d'un match, avec validation pour s'assurer que les résultats sont dans un format correct.
        
        Paramètres:
        - results (tuple): Un tuple de deux flottants représentant les scores des deux joueurs.
        
        Lève:
        - ValueError: Si les résultats ne sont pas valides.
        """
        if self.is_complete:
            raise ValueError("Le résultat ne peut pas être modifié; le match est déjà terminé.")

        if not isinstance(result, tuple) or len(result) != 2:
            raise ValueError("Les résultats doivent être un tuple de deux éléments.")

        score1, score2 = result
        if not all(isinstance(score, (int, float)) for score in (score1, score2)):
            raise ValueError("Les scores doivent être des nombres.")

        if (score1 + score2) not in [1, 0.5]:
            raise ValueError("La somme des scores doit être 0, 0.5, ou 1.")

        self.results = (score1, score2)
        self.is_complete = True



    
    
    
    def get_winner(self):
        """
        Détermine le gagnant du match.
        
        Retourne:
        - Player: L'objet joueur qui a gagné le match.
        - None: Si le match est nul ou n'est pas encore complet.
        """
        if not self.is_complete:
            return None  # Le match n'est pas terminé, aucun gagnant
        
        score1, score2 = self.results
        if score1 > score2:
            return self.players[0]
        elif score2 > score1:
            return self.players[1]
        return None  # Match nul

    
    def reset_match(self):
        """
        Réinitialise les résultats du match, remettant les scores à (0, 0) et marquant le match comme non complet.
        Utile pour les tests ou les ajustements avant la finalisation d'un tournoi.
        """
        if not self.is_complete:
            raise RuntimeError("Le match n'est pas encore complété et ne nécessite pas de réinitialisation.")
        
        self.results = (0, 0)
        self.is_complete = False
        print("Match réinitialisé avec succès.")
