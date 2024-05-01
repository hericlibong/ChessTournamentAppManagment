# controllers/base_controller.py

from util.data_manager import load_tournaments, save_tournaments, load_players, save_players

class BaseController:
    def __init__(self):
        self.tournaments = load_tournaments()  
        self.players = load_players()


    def save_data(self):
        save_tournaments(self.tournaments) # Sauvegarde les tournois
        save_players(self.players)  # Sauvegarde les joueurs
