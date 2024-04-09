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
    def display_tournaments(tournaments):
        """ Affiche les tournois existants"""
        if not tournaments:
            print("Aucun tournoi disponible.")
        else:
            print("Tournois disponibles :")
            for i, tournament in enumerate(tournaments, start=1):
                print(f"{i}. #ID : {tournament.t_id} | Name : {tournament.name} - Location : {tournament.location}, Dates : {tournament.start_date.strftime('%d/%m/%Y')} à {tournament.end_date.strftime('%d/%m/%Y')}")

    
