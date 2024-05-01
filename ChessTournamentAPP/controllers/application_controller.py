# application_controller.py

from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

class ApplicationController:
    def __init__(self):
        # Initialisation des contrôleurs avec l'état correct (chargement des données)
        self.tournament_controller = TournamentController()
        self.player_controller = PlayerController()

    def run(self):
        while True:
            choice = MenuView.display_main_menu()
            if choice == '1':
                self.tournament_controller.manage_tournaments()  # Utilisez l'instance, pas la classe
            elif choice == '2':
                self.player_controller.manage_players()  # Utilisez l'instance, pas la classe
            elif choice == '3':
                print("Quitter l'Application")
                break
            else:
                print("Invalid choice, please try again.")
