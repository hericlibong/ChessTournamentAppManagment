# menu_view.py

class MenuView:
    """Creation du menu"""

    @staticmethod
    def display_main_menu():
        """Affiche les options du menu principal """
        print("\nMenu principal :")
        print("1. Gestion des tournois")
        print("2. Gestion des joueurs")
        print("3. Quitter l'application")
        choice = input("Entrez le choix : ")
        return choice

    @staticmethod
    def display_tournament_menu():
        """ Affiche le menu de gestion des tournois """
        print("\nGestion des Tournois :")
        print("1. Créer un Nouveau Tournoi")
        print("2. Editer un Tournoi")
        print("3. Charger un Tournoi")
        print("4. Démarrer un Tournoi")
        print("5. Voir la liste Tournois")
        print("6. Gestion des Rounds")
        print("7. Retour au menu principal")
        choice = input("Entrez votre choix : ")
        return choice

    @staticmethod
    def display_player_menu():
        print("\nGestion des Joueurs :")
        print("1. Ajouter un Nouveau Joueur")
        print("2. Voir la liste des Joueurs")
        print("3. inscrire un joueur à un tournoi")
        print("4. Retour au menu principal")
        choice = input("Entrez votre choix : ")

        print("--------------")
        return choice

    @staticmethod
    def display_round_menu():
        """Affiche le menu des options pour les rounds."""
        print("\nGestion des Rounds :")
        print("1. Ajouter un Round")
        print("2. Démarrer un Round")
        print("3. Terminer un Round")
        print("4. Retour")
        return input("Choisissez une option : ")
