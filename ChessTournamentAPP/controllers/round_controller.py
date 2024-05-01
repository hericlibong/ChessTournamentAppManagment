
# controllers/round_controller.py

from controllers.base_controller import BaseController
from views.menu_view import MenuView
from views.round_views import RoundView

class RoundController(BaseController):

    def manage_rounds(self, tournament):
        while True:
            choice = MenuView.display_round_menu()
            if choice == '1':
                round_name = RoundView.create_round_info()
                tournament.add_round(round_name)
                self.save_data()
            elif choice == '2':
                round_index = RoundView.select_round_to_start(tournament)
                if round_index is not None:
                    tournament.start_round(round_index)
                    self.save_data()
            elif choice == '3':
                round_index = RoundView.select_round_to_end(tournament)
                if round_index is not None:
                    # Assumant que cette méthode gère correctement les modifications internes
                    for match in tournament.rounds[round_index].matches:
                        print(match.display_match())
                        match_results = RoundView.get_match_results()
                        match.set_results(match_results)
                    tournament.rounds[round_index].end_round()
                    self.save_data()
            elif choice == '4':
                break

