# tournament_views.py

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
        # Optionnel: Demander le nombre total de rounds
        total_round = input("Entrez le nombre total de rounds (laissez vide pour la valeur par défaut de 4) : ") or 4
        total_round = int(total_round)  # Convertit la saisie en entier

        return  name, location, description, start_date, end_date, total_round
    


    

    
    @staticmethod
    def disp_tournaments(tournaments):
        """Affiche les tournois disponibles avec les joueurs inscrits."""
        if not tournaments:
            print("Aucun tournoi disponible.")
        else:
            for tournament in tournaments:
                print(f"Le Tournoi a {tournament.current_round}commencé(s)")
                print(f"Tournoi: {tournament.name} - Lieu: {tournament.location}")
                print(f"Dates: Du {tournament.start_date.strftime('%d/%m/%Y')} au {tournament.end_date.strftime('%d/%m/%Y')}")
                print(f"{len(tournament.registered_players)} Joueurs inscrits:")
                if tournament.registered_players:
                    for player in tournament.registered_players:
                        print(f"- {player.firstname} {player.name} (ID: {player.unique_id})")
                else:
                    print("- En attente de joueurs.")
                print("-" * 40)  # Pour séparer visuellement les tournois




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





