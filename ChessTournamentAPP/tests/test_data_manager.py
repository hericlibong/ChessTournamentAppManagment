import unittest
from util.data_manager import save_tournaments, load_tournaments
from models.tournament import Tournament
from util.config import TOURNAMENTS_FILE
import os
import json

class TestDataManager(unittest.TestCase):
    def test_error_handling_in_load_tournaments(self):
        # Écrire intentionnellement des données JSON invalides pour tester la gestion des erreurs
        with open(TOURNAMENTS_FILE, 'w') as f:
            f.write('Invalid JSON')
        
        # Appeler load_tournaments et attendre une liste vide en retour, indiquant que l'erreur a été gérée
        result = load_tournaments()
        self.assertEqual(result, [], "The function should return an empty list when JSON is invalid")

        # Nettoyer après le test
        os.remove(TOURNAMENTS_FILE)

    def test_load_tournaments_handles_corrupt_json_gracefully(self):
        with open(TOURNAMENTS_FILE, 'w') as f:
            f.write('Invalid JSON')  # Créer intentionnellement un fichier JSON corrompu
        result = load_tournaments()
        self.assertEqual(result, [], "Should return an empty list on JSON decode error")
        


if __name__ == '__main__':
    unittest.main()
