# tournament_views.py

from .player_views import PlayerView
from models.tournament import Tournament
from prettytable import PrettyTable

class TournamentView:

    @staticmethod
    def create_tournament():
        """
        Vue statique pour créer un nouveau tournoi, collectant toutes les informations nécessaires.
        """
        
        name = input("Entrez le nom du tournoi : ")
        location = input("Entrez le lieu du tournoi : ")
        description = input("Entrez une description : ")
        start_date = input("Entrez la date de début (DD/MM/YYYY) : ")
        end_date = input("Entrez la date de fin (DD/MM/YYYY) : ")
        # # Optionnel: Demander le nombre total de rounds
        total_round = input("Entrez le nombre total de rounds (laissez vide pour la valeur par défaut de 4) : ") or 20
        total_round = int(total_round)  # Convertit la saisie en entier

        return  name, location, description, start_date, end_date, total_round



    @staticmethod
    def disp_tournaments(tournaments):
        """Affiche la liste de tournois de l'application"""
        table = PrettyTable()
        table.field_names = ["ID", "Nom", "Lieu", "Description", "Date de début", "Date de fin" ]
        table.align = "l"
        table.align["ID"] = "l"

        # Vérifie qu'il y a des tournois
        if not tournaments:
            print("Aucun tournoi disponible.")
        else:
            for tournament in tournaments:
                table.add_row([tournament.t_id, tournament.name, tournament.location, 
                               tournament.description, tournament.start_date.strftime('%d/%m/%Y'), tournament.end_date.strftime('%d/%m/%Y')])

        table_string = table.get_string()
        table_width = len(table_string.splitlines()[0])
        title = "liste des tournois enregistrés"
        centered_title = title.center(table_width).upper()
        line = "-" * 40
        center_line = line.center(table_width)
        print(centered_title)
        print(center_line)
        print(table)

   
   
    @staticmethod
    def select_tournament(tournaments):
        """
        Affiche la liste de tournois disponibles pour permettre à l'utilisateur de sélectionner celui auquel il souhaite ajouter un joueur.


        """

        print("Charger un tournoi :")
        for index, tournament in enumerate(tournaments, start=1):
            print(f"{index}. {tournament.name} - Lieu : {tournament.location}, Dates : {tournament.start_date.strftime('%d/%m/%Y')} à {tournament.end_date.strftime('%d/%m/%Y')}")
        choice = input("Entrez le numéro du tournoi : ")
        try:
            selected_index = int(choice) - 1
            if 0 <= selected_index < len(tournaments):
                return tournaments[selected_index]
            else:
                print("Sélection invalide. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        return None
    

   
    @staticmethod
    def display_all_tournament_details(tournament):
        


        # En-tête du tournoi
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

        # Tableau pour afficher les rounds et les matches
        if tournament.rounds:
            for round in tournament.rounds:
                matches_table = PrettyTable()

                # Il faudrait pouvoir afficher le round concerné
                matches_table.field_names = ["Match #", "Nom P1", "Rang P1", "Score P1", "vs.", "Nom P2", "Rang P2", "Score P2"]
                for index, match in enumerate(round.matches, start=1):
                    matches_table.add_row([
                        index,
                        match.players[0].name,  # Assurez-vous que ces attributs existent
                        "Rank P1",  # Remplacez par l'attribut réel si disponible
                        match.results[0],
                        "vs.",
                        match.players[1].name,
                        "Rank P2",  # Remplacez par l'attribut réel si disponible
                        match.results[1]
                    ])
                print(matches_table.get_string(title=f"Round {round.name}"))







    





