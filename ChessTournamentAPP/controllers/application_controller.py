from views.menu_view import MenuView
from views.tournament_views import TournamentView 
from models.tournament import Tournament

class ApplicationController:
    def __init__(self):
        self.tournaments = [] # Liste pour stocker les tournois
    
    def run(self):
        while True:
            choice = MenuView.display_main_menu()
            if choice == '1':
                # Créer un nouveu tournoi
                tournament_details = TournamentView.create_tournament()
                new_tournament = Tournament(*tournament_details) 
                self.tournaments.append(new_tournament)
                print(f"Tournament '{new_tournament.name}' created successfully.")
            elif choice == '2':
                # Afficher les tournois existants
                TournamentView.display_tournaments(self.tournaments)
            elif choice =='3':
                # Charger un tournoi existant (fonctionnalité à développer)
                pass    
            elif choice == '4':
                print("Exit Application")
                break
            else :
                print("Invalid choice, please try again")

    
    