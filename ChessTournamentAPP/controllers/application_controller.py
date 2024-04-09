# application_controller.py

from datetime import datetime
from views.menu_view import MenuView
from views.tournament_views import TournamentView 
from models.tournament import Tournament
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

    # def update_tournament_description(self):
    #     # Afficher les tournois avec leurs ID pour la sélection
    #     TournamentView.display_tournaments(self.tournaments)
    #     # Demander à l'utilisateur l'ID du tournoi à modifier
    #     t_id = input("Entrez l'ID du conyrol à modifier : ")
    #     # Trouver le tournoi correspondant
    #     tournament = next((t for t in self.tournaments if t.t_id == t_id), None)
    #     if tournament:
    #         # Demander la nouvelle description
    #         new_description = input("Entrez la nouvelle description : ")
    #         # Mettre à jour la description
    #         tournament.description = new_description
    #         # sauvegarder les modifications
    #         self.save_data()
    #         print("La description du tournoi a été mise à jour.")
    #     else:
    #         print("Tournoi non trouvé")

    
    