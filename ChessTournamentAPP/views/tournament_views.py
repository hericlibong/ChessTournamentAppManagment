# views/tournament_views.py

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
        total_round = input("Entrez le nombre total de rounds (laissez vide pour la valeur par défaut de 20) : ") or 20
        total_round = int(total_round)  # Convertit la saisie en entier
        return name, location, description, start_date, end_date, total_round

    @staticmethod
    def disp_tournaments(tournaments):
        """Affiche la liste de tournois de l'application"""
        table = PrettyTable()
        table.field_names = ["ID", "Nom", "Lieu", "Description", "Date de début", "Date de fin"]
        table.align = "l"
        table.align["ID"] = "l"

        # Vérifie qu'il y a des tournois
        if not tournaments:
            print("Aucun tournoi disponible.")
        else:
            for tournament in tournaments:
                table.add_row([tournament.t_id, tournament.name, tournament.location,
                               tournament.description, tournament.start_date.strftime('%d/%m/%Y'),
                               tournament.end_date.strftime('%d/%m/%Y')])
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
        Affiche la liste de tournois disponibles pour permettre à l'utilisateur de sélectionner
        celui auquel il souhaite ajouter un joueur.
        """
        print("Charger un tournoi :")
        for index, tournament in enumerate(tournaments, start=1):
            dates = f"{tournament.start_date.strftime('%d/%m/%Y')} à {tournament.end_date.strftime('%d/%m/%Y')}"
            print(f"{index}. {tournament.name} - Lieu : {tournament.location}, Dates : {dates}")
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
