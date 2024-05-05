# views/round_views.py
from datetime import datetime


class RoundView:
    @staticmethod
    def create_round_info():
        """Collecte les informations pour créer un nouveau round."""
        round_name = input("Entrez le nom du round : ")
        start_choice = input("Voulez-vous spécifier une heure de début ? (o/n) : ")
        start_time = None
        if start_choice.lower() == 'o':
            start_time_input = input("Entrez l'heure de début (format YYYY-MM-DD HH:MM) : ")
            try:
                start_time = datetime.strptime(start_time_input, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Format de date invalide.")
        return round_name, start_time

    @staticmethod
    def select_round_to_start(tournament):
        """Demande à l'utilisateur de sélectionner un round à démarrer."""
        RoundView.display_rounds(tournament)
        round_index = int(input("Entrez le numéro du round à démarrer : ")) - 1
        return round_index

    @staticmethod
    def select_round_to_end(tournament):
        """Demande à l'utilisateur de sélectionner un round à terminer."""
        RoundView.display_rounds(tournament)
        round_index = int(input("Entrez le numéro du round à terminer : ")) - 1
        return round_index

    @staticmethod
    def get_round_results(tournament):
        """Demande à l'utilisateur de sélectionner un round à terminer."""
        RoundView.display_rounds(tournament)
        round_index = int(input("Entrez le numéro du round à terminer : ")) - 1
        return round_index

    @staticmethod
    def display_rounds(tournament):
        """Affiche tous les rounds d'un tournoi avec leur état actuel."""
        print("\nListe des Rounds :")
        for index, rnd in enumerate(tournament.rounds):
            status = "Non commencé" if not rnd.start_time else "Terminé" if rnd.is_complete else "En cours"
            print(f"{index + 1}. Round: {rnd.name}, Statut: {status}")

    @staticmethod
    def get_match_results():
        result = input("Entrez le résultat (1-0, 0-1, 0.5-0.5) : ")
        try:
            results_tuple = tuple(map(float, result.split('-')))
            if len(results_tuple) != 2 or not all(isinstance(num, float) for num in results_tuple):
                raise ValueError
            return results_tuple
        except ValueError:
            print("Format invalide. Veuillez entrer les résultats sous la forme 'score1-score2'.")
            return None
