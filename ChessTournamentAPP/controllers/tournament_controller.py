# controllers/tournament_controller.py

from controllers.base_controller import BaseController
from views.tournament_views import TournamentView
from views.menu_view import MenuView
from controllers.round_controller import RoundController
from models.tournament import Tournament
from prettytable import PrettyTable
from datetime import datetime

class TournamentController(BaseController):
    def __init__(self):
        super().__init__()
        self.round_controller = RoundController()

    def manage_tournaments(self):
        while True:
            choice = MenuView.display_tournament_menu()
            if choice == '1':
                self.create_tournament()
            elif choice == '2':
                self.update_tournament()
            elif choice == '3':
                self.load_tournament()
            elif choice == '4':
                self.start_tournament()
            elif choice == '5':
                self.display_tournaments()
            elif choice == '6':
                tournament = TournamentView.select_tournament(self.tournaments)
                if tournament:
                    self.round_controller.manage_rounds(tournament)
                else :
                    print("Aucun tournoi sélectionné")
            elif choice == '7':  # Retour au menu principal
                break
            else:
    
                print("Invalid choice, please try again.")
    
    
    
    
    def create_tournament(self):
        tournament_details = TournamentView.create_tournament()
        new_tournament = Tournament(*tournament_details)
        self.tournaments.append(new_tournament)
        self.save_data()
        print(f"Tournament '{new_tournament.name}' has been successfully created.")

    
    def start_tournament(self):
        tournament = TournamentView.select_tournament(self.tournaments)
        if tournament:
            tournament.start_tournament()  # La méthode start_tournament de Tournament gère toutes les vérifications
        else:
            print("Aucun tournoi sélectionné ou tournoi invalide.")

    def load_tournament(self):
        tournament = TournamentView.select_tournament(self.tournaments)
        if tournament:
            # Affichage des détails du tournoi
            print("\nDétails du tournoi chargé :")
            print(f"Nom du tournoi : {tournament.name}".upper())
            print(f"Lieu : {tournament.location}")
            print(f"Description : {tournament.description}")
            print(f"Date de début : {tournament.start_date.strftime('%d/%m/%Y')}")
            print(f"Date de fin : {tournament.end_date.strftime('%d/%m/%Y')}")
            print(f"Nombre total de rounds prévus : {tournament.total_round}")
            print(f"Rounds actuellement complétés : {len(tournament.rounds)}")
            print(f"Nombre de joueurs inscrits : {len(tournament.registered_players)}\n")

            # Préparation du tableau pour les joueurs inscrits
            if tournament.registered_players:
                table = PrettyTable()
                table.field_names = ["ID", "Nom", "Prénom", "Date de naissance"]
                table.align = "l"  # Alignement des colonnes à gauche
                table.border = True
                table.header = True

                for player in sorted(tournament.registered_players, key=lambda x: (x.name, x.firstname)):
                    table.add_row([player.unique_id, player.name, player.firstname, player.birthdate.strftime('%d/%m/%Y')])
                table_string = table.get_string()
                table_width = len(table_string.splitlines()[0])
                title = "liste des joueurs inscrits"
                centered_title = title.center(table_width).upper()
                line = "-" * 40
                center_line = line.center(table_width)
                print(centered_title)
                print(center_line)
                print(table)
            else:
                print("Aucun joueur n'est inscrit dans le tournoi.")
        else:
            print("Aucun tournoi sélectionné ou sélection invalide.")

    
    
    def display_tournaments(self):
        """ Afficher le tournois disponibles  """
        TournamentView.disp_tournaments(self.tournaments)

    def update_tournament(self):
        """ Modifier les tournois"""
        #tournament = RoundView.display_tournaments_for_selection(self.tournaments)  # Utilisez la méthode de sélection des tournois
        tournament = TournamentView.select_tournament(self.tournaments)
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






    
   