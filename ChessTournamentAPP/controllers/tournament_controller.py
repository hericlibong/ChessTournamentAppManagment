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
        """Charge les tournois de l'application"""
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
                    table.add_row([player.unique_id, player.name, player.firstname,
                                   player.birthdate.strftime('%d/%m/%Y')])
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

            if tournament.rounds:
                for round in tournament.rounds:
                    matches_table = PrettyTable()
                    matches_table.field_names = ["Match #", "Nom P1", "Score P1", "vs.", "Nom P2", "Score P2"]

                    for index, match in enumerate(round.matches, start=1):
                        matches_table.add_row([
                            index,
                            match.players[0].name,
                            # Rank P1,  # Remplacez par l'attribut réel si disponible
                            match.results[0],
                            "vs.",
                            match.players[1].name,
                            # Rank P2,  # Remplacez par l'attribut réel si disponible
                            match.results[1]
                        ])

                    # Ajout de la date de début et de fin du round s'ils sont définis
                    round_details = f"Round {round.name}"
                    if hasattr(round, 'start_time') and round.start_time:
                        round_details += f" - Début : {round.start_time.strftime('%d/%m/%Y %H:%M')}"
                    if hasattr(round, 'end_time') and round.end_time:
                        round_details += f" - Fin : {round.end_time.strftime('%d/%m/%Y %H:%M')}"

                    print(matches_table.get_string(title=round_details))
            else:
                print("Aucun round joué")

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
