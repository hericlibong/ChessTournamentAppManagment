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

    @staticmethod
    def display_tournament_details(tournament, width=80):
        """Affiche les détails d'un tournoi sélectionné"""
        separator = "-" * width
        title = "Détails du Tournoi Chargé".center(width)
        print(separator, title, separator, sep='\n')
        print(f"Nom du tournoi : {tournament.name}".upper().center(width))
        print(f"Lieu : {tournament.location}".center(width))
        print(f"Description : {tournament.description}".center(width))
        print(f"Date de début : {tournament.start_date.strftime('%d/%m/%Y')}".center(width))
        print(f"Date de fin : {tournament.end_date.strftime('%d/%m/%Y')}".center(width))
        print(f"Nombre total de rounds prévus : {tournament.total_round}".center(width))
        print(f"Rounds actuellement complétés : {len(tournament.rounds)}".center(width))
        print(f"Nombre de joueurs inscrits : {len(tournament.registered_players)}".center(width))
        print(separator, "\n", sep='\n')

    @staticmethod
    def display_players(tournament, width=80):
        """Affiche la liste des joueurs inscrits à un tournoi."""
        if tournament.registered_players:
            table = PrettyTable()
            table.field_names = ["ID", "Nom", "Prénom", "Date de naissance"]
            table.align = "l"  # Alignement des colonnes à gauche pour améliorer la lisibilité
            table.border = True
            for player in sorted(tournament.registered_players, key=lambda x: (x.name, x.firstname)):
                table.add_row([player.unique_id, player.name,
                               player.firstname, player.birthdate.strftime('%d/%m/%Y')])
            # Centraliser chaque ligne du tableau
            player_lines = table.get_string().splitlines()
            title = "Liste des joueurs inscrits au tournoi".center(width)
            print(title)
            for line in player_lines:
                print(line.center(width))
        else:
            print("Aucun joueur n'est inscrit dans le tournoi.".center(width))
        print()  # Ajouter une ligne vide pour une meilleure séparation

    @staticmethod
    def display_rounds(tournament, width=80):
        """Affiche la liste des rounds joués dans un tournoi"""
        if tournament.rounds:
            print("Liste des Rounds joués".center(width))
            for round in tournament.rounds:
                matches_table = PrettyTable()
                matches_table.field_names = ["Match #", "Joueur 1", "Score J-1", "vs.", "Joueur 2", "Score J-2"]
                for index, match in enumerate(round.matches, start=1):
                    player1_full_name = f"{match.players[0].firstname} {match.players[0].name}"
                    player2_full_name = f"{match.players[1].firstname} {match.players[1].name}"
                    matches_table.add_row([
                        index,
                        player1_full_name,
                        match.results[0],
                        "vs.",
                        player2_full_name,
                        match.results[1]
                    ])

                # Rendre le formatage compatible avec flake8
                start_time = round.start_time.strftime('%d/%m/%Y %H:%M') if round.start_time else 'N/A'
                end_time = round.end_time.strftime('%d/%m/%Y %H:%M') if round.end_time else 'N/A'
                round_details = f"{round.name} - Début : {start_time} - Fin : {end_time}"

                # Centraliser chaque ligne du tableau
                round_lines = matches_table.get_string(title=round_details).splitlines()
                for line in round_lines:
                    print(line.center(width))
            print()  # Ajouter une ligne vide pour une meilleure séparation
        else:
            print("Aucun round joué.".center(width))
            print()  # Ajouter une ligne vide pour une meilleure séparation

    @staticmethod
    def display_ranking(tournament, player_points, width=80):
        """Affiche le classement des joueurs d'un tournoi sélectionné"""
        ranking_table = PrettyTable()
        ranking_table.field_names = ["ID", "Nom", "Prénom", "Points"]
        ranking_table.align = "l"
        sorted_players = sorted(tournament.registered_players,
                                key=lambda player: player_points.get(player.unique_id, 0), reverse=True)
        for player in sorted_players:
            ranking_table.add_row([player.unique_id, player.name,
                                   player.firstname, player_points.get(player.unique_id, 0)])

        print("Classement des Joueurs".center(width))
        # Centraliser chaque ligne du tableau
        ranking_lines = ranking_table.get_string().splitlines()
        for line in ranking_lines:
            print(line.center(width))
