# controllers/tournament_controller.py

from controllers.base_controller import BaseController
from views.tournament_views import TournamentView
from views.menu_view import MenuView
from controllers.round_controller import RoundController
from models.tournament import Tournament
from datetime import datetime


class TournamentController(BaseController):
    def __init__(self):
        super().__init__()
        self.round_controller = RoundController()

    def manage_tournaments(self):
        """Gère le menu des tournois"""
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
                else:
                    print("Aucun tournoi sélectionné")
            elif choice == '7':  # Retour au menu principal
                break
            else:

                print("Invalid choice, please try again.")

    def create_tournament(self):
        """Crée un tournoi dans l'application"""
        tournament_details = TournamentView.create_tournament()
        new_tournament = Tournament(*tournament_details)
        self.tournaments.append(new_tournament)
        self.save_data()
        print(f"Tournament '{new_tournament.name}' has been successfully created.")

    def start_tournament(self):
        tournament = TournamentView.select_tournament(self.tournaments)
        if tournament:
            if tournament.is_tournament_complete():
                print(f"Le Tournoi '{tournament.name}' est déjà terminé.")
                return
            else:
                tournament.start_tournament()
        else:
            print("Aucun tournoi sélectionné ou tournoi invalide.")

    def load_tournament(self):
        """
        Charge un tournoi sélectionné et affiche ses informations détaillées,
        les joueurs inscrits, les rounds joués et le classement par points
        """
        tournament = TournamentView.select_tournament(self.tournaments)
        if tournament:
            TournamentView.display_tournament_details(tournament)
            TournamentView.display_players(tournament)
            TournamentView.display_rounds(tournament)
            player_points = tournament.calculate_player_points()
            TournamentView.display_ranking(tournament, player_points)
        else:
            print("Aucun tournoi sélectionné ou sélection invalide.")

    def display_tournaments(self):
        """ Afficher les tournois disponibles  """
        TournamentView.disp_tournaments(self.tournaments)

    def update_tournament(self):
        """ Modifier les tournois"""
        # tournament = RoundView.display_tournaments_for_selection(self.tournaments)
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
