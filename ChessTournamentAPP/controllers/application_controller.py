# application_controller.py


from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController




class ApplicationController:
    def __init__(self):
        self.tournament_controller = TournamentController()
        self.player_controller = PlayerController() # Charge les joueurs existants

    def run(self):
        while True:
            choice = MenuView.display_main_menu()
            if choice == '1':
                self.tournament_controller.manage_tournaments()
            elif choice == '2':
                self.player_controller.manage_players()
            elif choice == '3':
                print("Quitter l'Application")
                #self.save_data()  # Sauvegarde les données avant de quitter
                break
            else:
                print("Invalid choice, please try again.")

    