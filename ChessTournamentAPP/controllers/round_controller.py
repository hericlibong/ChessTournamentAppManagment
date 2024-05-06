# controllers/round_controller.py

from controllers.base_controller import BaseController
from views.menu_view import MenuView
from views.round_views import RoundView


class RoundController(BaseController):
    def manage_rounds(self, tournament):
        """Manage et contrôle la gestion des rounds dans le tournoi"""
        while True:
            choice = MenuView.display_round_menu()
            if choice == '1':
                round_name, start_time = RoundView.create_round_info()
                tournament.add_round(round_name, start_time)
                self.save_data()
            elif choice == '2':
                round_index = RoundView.select_round_to_start(tournament)
                if round_index is not None:
                    tournament.start_round(round_index)
                    self.save_data()
            elif choice == '3':
                round_index = RoundView.select_round_to_end(tournament)
                if round_index is not None:
                    if tournament.rounds[round_index].start_time is None:
                        print(f"Erreur : Le round '{tournament.rounds[round_index].name}'"
                              f"n'a pas encore commencé et ne peut pas être terminé.")
                    else:
                        match_results = []
                        for match in tournament.rounds[round_index].matches:
                            print(match.display_match())
                            match_result = RoundView.get_match_results()
                            if match_result:
                                match_results.append(match_result)
                        if match_results:  # Ensure that results have been correctly collected
                            tournament.end_round(round_index, match_results)
                            self.save_data()
            elif choice == '4':
                break
