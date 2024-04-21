# views/round_views.py
from datetime import datetime

class RoundView:
    @staticmethod
    def create_round():
        """Permet à l'utilisateur de saisir les informations pour créer un nouveau round."""
        round_name = input("Entrez le nom du round : ")
        start_choice = input("Voulez-vous spécifier une heure de début ? (o/n) : ")
        start_time = None
        if start_choice.lower() == 'o':
            start_time_input = input("Entrez l'heure de début (format YYYY-MM-DD HH:MM) : ")
            try:
                start_time = datetime.strptime(start_time_input, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Format de date invalide, le round commencera immédiatement.") # Réfléchir sur cette option
        return round_name, start_time

    @staticmethod
    def start_round(tournament):
        """Permet à l'utilisateur de démarrer un round spécifié."""
        RoundView.display_rounds(tournament)
        round_index = int(input("Entrez le numéro du round à démarrer : ")) - 1
        try:
            selected_round = tournament.rounds[round_index]
            if not selected_round.start_time:
                tournament.start_round(selected_round.name)
                print(f"Round '{selected_round.name}' a commencé.")
            else:
                print("Ce round a déjà été démarré.")
        except IndexError:
            print("Numéro de round invalide.")

    @staticmethod
    def end_round(tournament):
        """Permet à l'utilisateur de terminer un round spécifié."""
        RoundView.display_rounds(tournament)
        round_index = int(input("Entrez le numéro du round à terminer : ")) - 1
        try:
            selected_round = tournament.rounds[round_index]
            if selected_round.start_time and not selected_round.is_complete:
                tournament.end_round(selected_round.name)
                print(f"Round '{selected_round.name}' a été terminé.")
            else:
                print("Ce round ne peut pas être terminé (non commencé ou déjà terminé).")
        except IndexError:
            print("Numéro de round invalide.")

    # @staticmethod
    # def display_rounds(tournament):
    #     """Affiche tous les rounds d'un tournoi avec leur état actuel."""
    #     print("\nListe des Rounds :")
    #     for index, round in enumerate(tournament.rounds):
    #         status = "Non commencé" if not round.start_time else "Terminé" if round.is_complete else "En cours"
    #         print(f"{index + 1}. Round: {round.name}, Statut: {status}")

    @staticmethod
    def display_rounds(tournament):
        print("\nListe des Rounds :")
        for index, rnd in enumerate(tournament.rounds):
            status = "Non commencé" if not rnd.start_time else "Terminé" if rnd.is_complete else "En cours"
            print(f"{index + 1}. Round: {rnd.name}, Statut: {status}")




    


    @staticmethod
    def display_tournaments_for_selection(tournaments):
        """
        Affiche la liste de tournois disponibles pour permettre à l'utilisateur de sélectionner celui auquel il souhaite ajouter un joueur.
        
        Cette méthode imprime chaque tournoi avec un numéro d'ordre pour faciliter la sélection par l'utilisateur.
        L'utilisateur est invité à entrer le numéro correspondant au tournoi de son choix.
        Si la sélection est valide (un numéro correspondant à un tournoi existant), le tournoi sélectionné est retourné.
        En cas de sélection invalide (un choix hors de la plage ou une entrée non numérique), l'utilisateur est informé de l'erreur et invité à réessayer.

        """

        print("Sélectionnez un tournoi pour y ajouter un round :")
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
