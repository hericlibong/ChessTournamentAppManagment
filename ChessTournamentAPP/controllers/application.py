from views.menu_view import MenuView
from views.tournament_view import TournamentView
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
                new_tournament = Tournament(*tournament_details) # quid de t_id
                self.tournaments.append(new_tournament)
                print(f"Tournament '{new_tournament.name}' created successfully.")
            elif choice == '2':
                # Afficher les tournois existants
                self.display_tournaments()
            elif choice =='3':
                # Charger un tournoi existant (fonctionnalité à développer)
                pass    
            elif choice == '4':
                print("Exit Application")
                break
            else :
                print("Invalid choice, please try again")

    
    def display_tournaments(self):
        if not self.tournaments:
            print("No tournaments have been created yet.")
        else:
            print("Existing tournaments:")
            for i, tournament in enumerate(self.tournaments, 1):
                print(f"{i}. {tournament.name} - Location: {tournament.location}")