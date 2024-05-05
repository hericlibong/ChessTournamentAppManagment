import unittest
from datetime import datetime
from models.round import Round
from models.player import Player

class TestRound(unittest.TestCase):

    def setUp(self):
        # Assurez-vous d'inclure tous les paramètres requis pour créer un joueur
        self.player1 = Player(unique_id="AL76589", name="Alice", firstname="Land", birthdate="01/01/1990")
        self.player2 = Player(unique_id="BC89065", name="Bob", firstname="Denard", birthdate="02/02/1999")
        self.player1.past_opponents = set()  # S'assurer que les adversaires passés sont réinitialisés
        self.player2.past_opponents = set()

        # Création d'un round
        self.round = Round(name="Test Round")


    def test_end_time_serialization(self):
        """Teste que l'heure de fin est correctement sérialisée dans to_dict."""
        self.round.end_round()  # Définir l'heure de fin
        round_dict = self.round.to_dict()
        self.assertIsNotNone(round_dict['end_time'])  # S'assurer que l'heure de fin n'est pas None
        self.assertIsInstance(round_dict['end_time'], str)  # S'assurer que l'heure de fin est une chaîne
        # Vérifier le format de la date
        try:
            datetime.strptime(round_dict['end_time'], '%Y-%m-%d %H:%M')
            format_is_correct = True
        except ValueError:
            format_is_correct = False
        self.assertTrue(format_is_correct, "Le format de la date de fin doit être '%Y-%m-%d %H:%M'")

    def test_round_initialization(self):
        """Teste si un round est correctement initialisé."""
        self.assertEqual(self.round.name, "Test Round")
        self.assertIsNone(self.round.start_time)
        self.assertFalse(self.round.is_complete)
        self.assertEqual(len(self.round.matches), 0)

    def test_add_match(self):
        """Teste l'ajout d'un match au round."""
        self.round.add_match(self.player1, self.player2, set())
        self.assertEqual(len(self.round.matches), 1)  # Vérifie qu'un match a été ajouté

    def test_add_match_prevents_duplicates(self):
        """Teste que l'ajout de matchs en double est empêché."""
        current_matches = set()
        self.round.add_match(self.player1, self.player2, current_matches)
        self.round.add_match(self.player1, self.player2, current_matches)
        self.assertEqual(len(self.round.matches), 1)  # Seul un match doit être ajouté

    def test_end_round(self):
        """Teste que le round peut être terminé et que l'heure de fin est correctement enregistrée."""
        self.round.end_round()
        self.assertTrue(self.round.is_complete)
        self.assertIsNotNone(self.round.end_time)  # Vérifie que l'heure de fin est bien enregistrée
        self.assertIsInstance(self.round.end_time, datetime)  # Vérifie que end_time est bien un objet datetime


# Ceci permet d'exécuter les tests si ce script est exécuté directement
if __name__ == '__main__':
    unittest.main()

