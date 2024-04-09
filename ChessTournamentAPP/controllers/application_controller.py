# application_controller.py

from datetime import datetime
from views.menu_view import MenuView
from views.tournament_views import TournamentView 
from views.player_views import PlayerView
from models.tournament import Tournament
from models.player import Player
from util.data_manager import load_tournaments, save_tournaments


class ApplicationController:
    def __init__(self):
        self.tournaments = load_tournaments()
    
    def run(self):
        while True:
            choice = MenuView.display_main_menu()
            if choice == '1':
                # Créer un nouveu tournoi
                tournament_details = TournamentView.create_tournament()
                new_tournament = Tournament(*tournament_details) 
                self.tournaments.append(new_tournament)
                self.save_data()  # Utilise la méthode sauvegarde centralisée
                print(f"Tournament '{new_tournament.name}' created successfully.")
            elif choice == '2':
                # Afficher les tournois existants
                TournamentView.display_tournaments(self.tournaments)
            elif choice =='3':
                # Charger un tournoi existant (fonctionnalité à développer)
                pass
            elif choice == '4':
                self.update_tournament()
            elif choice == '5':
                self.add_player()    
            
            elif choice == '6':
                print("Exit Application")
                break
            else :
                print("Invalid choice, please try again")

    
    def save_data(self):
        save_tournaments(self.tournaments)

    
    
    def update_tournament(self):
        TournamentView.display_tournaments(self.tournaments)
        t_id = input("Entrez l'ID du tournoi à modifier : ")
        tournament = next((t for t in self.tournaments if t.t_id == t_id), None)
        
        if tournament:
            print("Quel attribut voulez-vous modifier ?")
            print("1. Nom")
            print("2. Lieu")
            print("3. Date de début")
            print("4. Date de fin")
            print("5. Description")
            choice = input("Entrez votre choix : ")
            
            if choice == '1':
                new_value = input("Entrez le nouveau nom : ")
                tournament.name = new_value
            elif choice == '2':
                new_value = input("Entrez le nouveau lieu : ")
                tournament.location = new_value
            elif choice == '3':
                new_value = input("Entrez la nouvelle date de début (DD/MM/YYYY) : ")
                tournament.start_date = datetime.strptime(new_value, "%d/%m/%Y")
            elif choice == '4':
                new_value = input("Entrez la nouvelle date de fin (DD/MM/YYYY) : ")
                tournament.end_date = datetime.strptime(new_value, "%d/%m/%Y")
            elif choice == '5':
                new_value = input("Entrez la nouvelle description : ")
                tournament.description = new_value
            else:
                print("Choix non valide.")
                return
            
            self.save_data()
            print("Le tournoi a été mis à jour.")
        else:
            print("Tournoi non trouvé.")

    
    #### Gestion des joueurs ####

    def add_player(self):
        player_details = PlayerView.create_player()  # Supposer qu'une vue PlayerView existe
        new_player = Player(*player_details)
        # Ajouter ici la logique pour associer le joueur à un tournoi si nécessaire
        print(f"Player '{new_player.name}' added successfully.")


    
    
    