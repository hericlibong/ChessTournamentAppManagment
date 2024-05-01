# controllers/base_controller.py

from util.data_manager import load_tournaments, save_tournaments, load_players, save_players


class BaseController:
    tournaments = load_tournaments()  # Chargement statique des tournois
    players = load_players()          # Chargement statique des joueurs

    def save_data(self):
        save_tournaments(BaseController.tournaments)  # Sauvegarde des tournois
        save_players(BaseController.players)  
