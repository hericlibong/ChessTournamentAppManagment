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
        if round_index < 0 or round_index >= len(tournament.rounds):
            print("Numéro de round invalide.")
            return
        selected_round = tournament.rounds[round_index]
        if selected_round.start_time is None:
            tournament.start_round(selected_round.name)
            print(f"Round '{selected_round.name}' a commencé.")
        else:
            print("Ce round a déjà été démarré.")

    @staticmethod
    def end_round(tournament):
        """Permet à l'utilisateur de terminer un round spécifié."""
        RoundView.display_rounds(tournament)
        round_index = int(input("Entrez le numéro du round à terminer : ")) - 1
        if round_index < 0 or round_index >= len(tournament.rounds):
            print("Numéro de round invalide.")
            return
        selected_round = tournament.rounds[round_index]
        if selected_round.start_time and not selected_round.is_complete:
            for match in selected_round.matches:
                print(f"Match entre {match.players[0].name} et {match.players[1].name}")
                result = input("Entrez le résultat (1-0, 0-1, 0.5-0.5) : ")
                match.set_results(tuple(map(float, result.split('-'))))
            tournament.end_round(selected_round.name)
            print(f"Round '{selected_round.name}' a été terminé.")
        else:
            print("Ce round ne peut pas être terminé (non commencé ou déjà terminé).")
    

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