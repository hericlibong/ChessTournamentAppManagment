import unittest
from datetime import datetime
from models.tournament import Tournament
from models.round import Round
from models.player import Player

class TestTournament(unittest.TestCase):
    def setUp(self):
        self.tournament = Tournament("Chess Championship", "New York", "International Tournament", "01/04/2024", "02/04/2024")

    def test_add_round(self):
        self.tournament.add_round("Round 1")
        self.assertEqual(len(self.tournament.rounds), 1)
        self.assertEqual(self.tournament.rounds[0].name, "Round 1")

    def test_start_round_not_found(self):
        with self.assertRaises(ValueError):
            self.tournament.start_round("Nonexistent Round")

    def test_end_round_not_started(self):
        self.tournament.add_round("Round 1")
        self.tournament.end_round("Round 1")
        self.assertTrue(self.tournament.rounds[0].is_complete)
        self.assertIsNotNone(self.tournament.rounds[0].end_time)

if __name__ == '__main__':
    unittest.main()
