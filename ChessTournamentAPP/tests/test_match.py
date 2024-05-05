import unittest
from models.match import Match
from models.player import Player  # Assuming a simple Player class exists

class TestMatch(unittest.TestCase):
    def setUp(self):
        self.player1 = Player(name="Prince", firstname="Alice", birthdate= "24/03/1969", unique_id="RD56789")
        self.player2 = Player(name="Harry", firstname="Bob", birthdate="24/03/1969", unique_id="RE98765")
        self.match = Match((self.player1, self.player2))

    def test_initial_conditions(self):
        """Test initial state of a match."""
        self.assertEqual(self.match.results, (0, 0))
        self.assertFalse(self.match.is_complete)

    def test_set_results_valid(self):
        """Test setting valid results."""
        self.match.set_results((0.5, 0.5))
        self.assertEqual(self.match.results, (0.5, 0.5))
        self.assertTrue(self.match.is_complete)

    def test_set_results_invalid_type(self):
        """Test setting results with invalid types should raise ValueError."""
        with self.assertRaises(ValueError):
            self.match.set_results((0.5, "not a number"))

    def test_set_results_already_complete(self):
        """Test setting results when match is already complete should raise ValueError."""
        self.match.set_results((0.5, 0.5))
        with self.assertRaises(ValueError):
            self.match.set_results((1, 0))

    def test_reset_match(self):
        """Test resetting a match."""
        self.match.set_results((1, 0))
        self.match.reset_match()
        self.assertEqual(self.match.results, (0, 0))
        self.assertFalse(self.match.is_complete)

    def test_get_winner(self):
        """Test determining the winner of the match."""
        self.match.set_results((1, 0))
        self.assertEqual(self.match.get_winner(), self.player1)
        self.match.reset_match()  # Réinitialiser le match avant de définir de nouveaux résultats
        self.match.set_results((0, 1))
        self.assertEqual(self.match.get_winner(), self.player2)


    def test_get_winner_no_winner(self):
        """Test that no winner is returned if the match is a draw or not complete."""
        self.match.set_results((0.5, 0.5))
        self.assertIsNone(self.match.get_winner())
        self.match.reset_match()
        self.assertIsNone(self.match.get_winner())



    def test_get_winner_for_winner1(self):
        """Test determining the winner when player1 wins."""
        self.match.set_results((1, 0))
        self.assertEqual(self.match.get_winner(), self.player1)

    def test_get_winner_for_winner2(self):
        """Test determining the winner when player2 wins."""
        self.match.set_results((0, 1))
        self.assertEqual(self.match.get_winner(), self.player2)

    def test_get_winner_for_draw(self):
        """Test that no winner is returned if the match is a draw."""
        self.match.set_results((0.5, 0.5))
        self.assertIsNone(self.match.get_winner())


if __name__ == '__main__':
    unittest.main()
