# menu_view.py

class MenuView:
    """Création du menu"""

    @staticmethod
    def display_main_menu():
        """Affiche les options du menu principal"""
        print("\n" + "-" * 30)
        print("MENU PRINCIPAL".center(30))
        print("-" * 30)
        print("[1] Gestion des tournois")
        print("[2] Gestion des joueurs")
        print("[3] Quitter l'application")
        print("-" * 30)
        choice = input("Entrez le choix [1-3]: ")
        return choice

    @staticmethod
    def display_tournament_menu():
        """Affiche le menu de gestion des tournois"""
        print("\n" + "-" * 30)
        print("GESTION DES TOURNOIS".center(30))
        print("-" * 30)
        print("[1] Créer un nouveau tournoi")
        print("[2] Editer un tournoi")
        print("[3] Charger un tournoi")
        print("[4] Démarrer un tournoi")
        print("[5] Voir la liste des tournois")
        print("[6] Gestion des rounds")
        print("[7] Retour au menu principal")
        print("-" * 30)
        choice = input("Entrez votre choix [1-7]: ")
        return choice

    @staticmethod
    def display_player_menu():
        print("\n" + "-" * 30)
        print("GESTION DES JOUEURS".center(30))
        print("-" * 30)
        print("[1] Ajouter un nouveau joueur")
        print("[2] Voir la liste des joueurs")
        print("[3] Inscrire un joueur à un tournoi")
        print("[4] Retour au menu principal")
        print("-" * 30)
        choice = input("Entrez votre choix [1-4]: ")
        return choice

    @staticmethod
    def display_round_menu():
        """Affiche le menu des options pour les rounds."""
        print("\n" + "-" * 30)
        print("GESTION DES ROUNDS".center(30))
        print("-" * 30)
        print("[1] Ajouter un Round")
        print("[2] Démarrer un Round")
        print("[3] Terminer un Round")
        print("[4] Retour")
        print("-" * 30)
        return input("Choisissez une option [1-4]: ")
