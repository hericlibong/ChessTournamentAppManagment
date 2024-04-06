


import unittest
from models.player import Player
from models.tournament import Tournament


class TestPlayer(unittest.TestCase):
    
    def test_birthdate_validation(self):
        """Teste si la validation de la date de naissance fonctionne correctement."""
        with self.assertRaises(ValueError):
            Player(name="Doe", firstname="John", birthdate="2100-01-01", unique_id="AB12345")
    
    def test_unique_id_validation(self):
        """Teste si la validation de l'unique_id fonctionne correctement."""
        with self.assertRaises(ValueError):
            Player(name="Roe", firstname="Jane", birthdate="1992-02-02", unique_id="12345AB")


class TestDatesTournament(unittest.TestCase):
    
    def test_dates_valid(self):
        """Teste si les dates de début et de fin sont valides et bien formatées."""
        try:
            Tournament(name="Test", location="Test Location", description="A test tournament",
                       current_round=1, start_date="2023-01-01", end_date="2023-01-10", total_round=4)
        except ValueError as e:
            self.fail(f"La création d'un tournoi avec des dates valides a échoué: {e}")
    
    def test_end_date_before_start_date(self):
        """Teste si une ValueError est levée quand la date de fin est avant la date de début."""
        with self.assertRaises(ValueError):
            Tournament(name="Test", location="Test Location", description="A test tournament",
                       current_round=1, start_date="2023-01-10", end_date="2023-01-01", total_round=4)
    
    def test_invalid_date_format(self):
        """Teste si une ValueError est levée pour un format de date invalide."""
        with self.assertRaises(ValueError):
            Tournament(name="Test", location="Test Location", description="A test tournament",
                       current_round=1, start_date="01-01-2023", end_date="10-01-2023", total_round=4)


if __name__ == '__main__':
    unittest.main()