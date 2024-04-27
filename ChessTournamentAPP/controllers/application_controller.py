# application_controller.py

from datetime import datetime
from views.menu_view import MenuView
from views.tournament_views import TournamentView
from views.player_views import PlayerView
from views.round_views import RoundView
from models.tournament import Tournament
from models.round import Round
from models.player import Player
from util.data_manager import load_tournaments, save_tournaments, load_players, save_players




class ApplicationController:
    def __init__(self):
        self.tournaments = load_tournaments()
        self.players = load_players()  # Charge les joueurs existants

    def run(self):
        while True:
            choice = MenuView.display_main_menu()
            if choice == '1':
                self.manage_tournaments()
            elif choice == '2':
                self.manage_players()
            elif choice == '3':
                print("Quitter l'Application")
                self.save_data()  # Sauvegarde les données avant de quitter
                break
            else:
                print("Invalid choice, please try again.")

    def manage_tournaments(self):
        while True:
            choice = MenuView.display_tournament_menu()
            if choice == '1':
                self.create_tournament()
            elif choice == '2':
                self.update_tournament()
            elif choice == '3':
                self.load_tournament()
            elif choice == '4':
                self.start_tournament()
            elif choice == '5':
                self.display_tournaments()
            elif choice == '6':
                tournament = TournamentView.select_tournament(self.tournaments)
                if tournament:
                    self.manage_rounds(tournament)
                else :
                    print("Aucun tournoi sélectionné")
            elif choice == '7':  # Retour au menu principal
                break
            else:
    
                print("Invalid choice, please try again.")



   

    def start_tournament(self):
        tournament = TournamentView.select_tournament(self.tournaments)
        if tournament:
            tournament.start_tournament()  # La méthode start_tournament de Tournament gère toutes les vérifications
        else:
            print("Aucun tournoi sélectionné ou tournoi invalide.")




    def manage_rounds(self, tournament):
        while True:
            choice = MenuView.display_round_menu()
            if choice == '1':
                round_details = RoundView.create_round()
                tournament.add_round(*round_details)
            elif choice == '2':
                RoundView.start_round(tournament)
            elif choice == '3':
                RoundView.end_round(tournament)
                
                
            elif choice == '4':
                break  # Correctement placé dans une boucle, cela permet de retourner au menu précédent
            else:
                print("Choix invalide, veuillez réessayer.")


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

    

    
    
    def save_data(self):
        save_tournaments(self.tournaments) # Sauvegarde les tournois
        save_players(self.players)  # Sauvegarde les joueurs

    # Ici, ajoute les méthodes create_tournament, display_tournaments, add_player, display_players, etc.

    def create_tournament(self):
        """ Créer un tournoi  """
        tournament_details = TournamentView.create_tournament()
        new_tournament = Tournament(*tournament_details)
        self.tournaments.append(new_tournament)
        self.save_data()
        print(f"Tournament '{new_tournament.name}' has been successfully created.")


    def load_tournament(self):
        tournament = TournamentView.select_tournament(self.tournaments)
        if tournament:
            print(f"\nTournoi chargé : '{tournament.name}'")
            print(f"Lieu : {tournament.location}")
            print(f"Description : {tournament.description}")
            print(f"Date de début : {tournament.start_date.strftime('%d/%m/%Y')}")
            print(f"Date de fin : {tournament.end_date.strftime('%d/%m/%Y')}")
            print(f"Nombre total de rounds prévus : {tournament.total_round}")
            print(f"Rounds actuellement complétés : {len(tournament.rounds)}")
            print(f"Nombre de joueurs inscrits : {len(tournament.registered_players)}\n")
            if tournament.registered_players:
                    for player in tournament.registered_players:
                        print(f"- {player.firstname} {player.name} (ID: {player.unique_id})")
            else:
                    print("- En attente de joueurs.")
            # Ajouter ici d'autres informations si nécessaire
            # Ici, vous pouvez appeler d'autres méthodes pour gérer ce tournoi, comme éditer ses détails ou gérer ses rounds.
        else:
            print("Aucun tournoi sélectionné ou sélection invalide.")
    
    
    def display_tournaments(self):
        """ Afficher le tournois disponibles  """
        TournamentView.disp_tournaments(self.tournaments)

    def add_player(self):
        """ Ajouter un joueur"""
        existing_ids = {player.unique_id for player in self.players}
        player_details = PlayerView.create_player(existing_ids)
        new_player = Player(*player_details)
        self.players.append(new_player)
        self.save_data()
        print(f"Player '{new_player.name}' has been successfully added.")

    def display_players(self):
        """ Afficher les joueurs présents  """
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



    

    def update_tournament(self):
        """ Modifier les tournois"""
        tournament = RoundView.display_tournaments_for_selection(self.tournaments)  # Utilisez la méthode de sélection des tournois
        if tournament:
            print("Quel attribut voulez-vous modifier ?")
            print("1. Nom")
            print("2. Lieu")
            print("3. Date de début")
            print("4. Date de fin")
            print("5. Description")
            choice = input("Entrez votre choix : ")
            
            if choice == '1':
                new_value = input("Entrez le nouveau nom : ")
                tournament.name = new_value
            elif choice == '2':
                new_value = input("Entrez le nouveau lieu : ")
                tournament.location = new_value
            elif choice == '3':
                new_value = input("Entrez la nouvelle date de début (DD/MM/YYYY) : ")
                tournament.start_date = datetime.strptime(new_value, "%d/%m/%Y")
            elif choice == '4':
                new_value = input("Entrez la nouvelle date de fin (DD/MM/YYYY) : ")
                tournament.end_date = datetime.strptime(new_value, "%d/%m/%Y")
            elif choice == '5':
                new_value = input("Entrez la nouvelle description : ")
                tournament.description = new_value
            else:
                print("Choix non valide.")
                return
            
            self.save_data()
            print("Le tournoi a été mis à jour.")
        else:
            print("Tournoi non trouvé.")