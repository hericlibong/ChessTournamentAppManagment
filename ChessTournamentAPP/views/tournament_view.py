class TournamentView:

    @staticmethod
    def create_tournament():
        """
        Vue statique qui permet à l'utilisateur de saisir les informations nécessaires 
        pour créer un nouveau tournoi, incluant le nom, le lieu, et les dates de début et de fin. 
        Elle collecte les entrées via la console et 
        retourne ces données pour une utilisation ultérieure dans l'application. 
        """
        name = input("Entrez le nom du tournoi : ")
        location = input("Entrez le lieu du tournoi : ")
        start_date = input("Entrez la date de début (YYYY-MM-DD) : ")
        end_date = input("Entrez la date de fin (YYYY-MM-DD) : ")
        # Valider et convertir les données si nécessaire
        return name, location, start_date, end_date
