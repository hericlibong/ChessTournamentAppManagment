# controllers/player_controller.py

from controllers.base_controller import BaseController
from views.player_views import PlayerView
from views.menu_view import MenuView
from models.player import Player


class PlayerController(BaseController):



    def manage_players(self):
        while True:
            choice = MenuView.display_player_menu()
            if choice == '1':
                self.add_player()
            elif choice == '2':
                self.display_players()
            elif choice == '3':
                self.associate_player_to_tournament()   
            elif choice == '4':  # Retour au menu principal
                break
            else:
                print("Choix invalide, veuillez réessayer.")
    
    
    def add_player(self):
        existing_ids = {player.unique_id for player in self.players}
        player_details = PlayerView.create_player(existing_ids)
        new_player = Player(*player_details)
        self.players.append(new_player)
        self.save_data()
        print(f"Player '{new_player.name}' has been successfully added.")

    def display_players(self):
        PlayerView.display_players(self.players)

    def associate_player_to_tournament(self):
        """ Associer un joueur à un tournoi"""
        # Filtrer seulement les tournois actifs
        #active_tournaments = [t for t in self.tournaments if t.is_active()]
        selected_tournament = PlayerView.display_tournaments_for_selection(self.tournaments)
        if selected_tournament:
            PlayerView.display_players(self.players)
            player_id = input("Entrez l'ID du joueur à inscrire : ")
            player_to_register = next((player for player in self.players if str(player.unique_id) == player_id), None)
            
            if player_to_register:
                selected_tournament.register_player(player_to_register)
                self.save_data()  # Sauvegarder après l'ajout du joueur
            else:
                print("Joueur non trouvé.")
        else:
            print("Aucune action effectuée.")
