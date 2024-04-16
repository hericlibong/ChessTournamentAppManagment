# player_views.py
import re
from datetime import datetime

class PlayerView:

    @staticmethod
    def create_player(existing_ids):
        """ 
        Vue statique pour créer des joueurs, collectant les informations nécessaires
        """
        while True:
            name = input("Entrez le nom du joueur : ")
            if not re.match(r'^[A-Za-z]{2,}$', name):
                print("Le nom doit contenir au moins 2 lettres et uniquement des caractères alphabétiques")
            else:
                break
        
        while True:

            firstname = input("Entrez le prénom du joueur : ")
            if not re.match(r'^[A-Za-z]{2,}$', firstname):
                print("Le prénom doit contenir au moins 2 lettres et uniquement des caractères alphabétiques")
            else:
                break 
        
        birthdate = input("Entrez la date de naissance du joueur (DD/MM/YYYY) : ")
        

        # Valider l'identifiant unique
        while True:
            u_id = input("Entrez l'identifiant unique (format XX00000) : ")
            if not re.match(r'^[A-Z]{2}\d{5}$', u_id):
                print("Format d'ID invalide. Veuillez respecter le format XX00000 (ex: AB12345).")
            elif u_id in existing_ids:
                print("Cet identifiant est déjà utilisé. Veuillez en entrer un nouveau")
            else : 
                break

        return name, firstname, birthdate, u_id
    


    @staticmethod
    def display_players(players):
        """Affiche les joueurs enregistrés triés par nom."""
        if not players:
            print("Aucun joueur n'est enregistré.")
        else:
            print("Liste des joueurs enregistrés :")
            sorted_players = sorted(players, key=lambda x: (x.name, x.firstname))
            for player in sorted_players:
                print(f"{player.name} {player.firstname}, {player.birthdate.strftime('%d/%m/%Y')} (ID: {player.unique_id})")




    @staticmethod
    def display_tournaments_for_selection(tournaments):
        """
        Affiche la liste de tournois disponibles pour permettre à l'utilisateur de sélectionner celui auquel il souhaite ajouter un joueur.


        """

        print("Sélectionnez un tournoi pour y ajouter un joueur :")
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
