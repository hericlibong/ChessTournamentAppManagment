


import unittest
from models.player import Player


class TestPlayer(unittest.TestCase):
    
    def test_birthdate_validation(self):
        """Teste si la validation de la date de naissance fonctionne correctement."""
        with self.assertRaises(ValueError):
            Player(name="Doe", firstname="John", birthdate="2100-01-01", unique_id="AB12345")
    
    def test_unique_id_validation(self):
        """Teste si la validation de l'unique_id fonctionne correctement."""
        with self.assertRaises(ValueError):
            Player(name="Roe", firstname="Jane", birthdate="1992-02-02", unique_id="12345AB")

if __name__ == '__main__':
    unittest.main()