# controllers/base_controller.py

from util.data_manager import load_tournaments, save_tournaments, load_players, save_players


class BaseController:
    """Base controller that manages data loading and saving operations."""

    tournaments = load_tournaments()  # Load static tournaments data
    players = load_players()          # Load static players data

    def save_data(self):
        """Save data to persistent storage."""
        save_tournaments(BaseController.tournaments)  # Save tournaments to the file system
        save_players(BaseController.players)          # Save players to the file system
