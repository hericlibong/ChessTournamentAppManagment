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






    


    # @staticmethod
    # def display_tournaments_with_players(tournaments):
    #     """Affiche les tournois et leurs joueurs inscrits."""
    #     for tournament in tournaments:
    #         print(f"\nTournoi: {tournament.name} - Lieu: {tournament.location}")
    #         if tournament.registered_players:
    #             print("Joueurs inscrits :")
    #             for player in tournament.registered_players:
    #                 print(f"- {player.name} {player.firstname}")
    #         else:
    #             print("Aucun joueur inscrit pour le moment.")

