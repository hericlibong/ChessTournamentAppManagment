# menu_view.py

class MenuView:
    """Creation du menu"""
    
    
    @staticmethod
    def display_main_menu():
        """Affiche les options du menu principal """
        print("\nMenu principal :")
        print("1. Gérer les tournois")
        print("2. Gérer les joueurs")
        print("3. Quitter l'application")
        choice = input("Entrez le choix : ")
        return choice
    

    @staticmethod
    def display_tournament_menu():
        """ Affiche le menu de gestion des tournois """
        print("\nGestion des Tournois :")
        print("1. Créer un Nouveau Tournoi")
        print("2. Voir les Tournois existants")
        print("3. Charger un Tournoi existant")
        print("4. Modifier un Tournoi")
        print("5. Retour")
        choice = input("Entrez votre choix : ")
        return choice
    
    @staticmethod
    def display_player_menu():
        print("\nGestion des Joueurs :")
        print("1. Ajouter un Nouveau Joueur")
        print("2. Voir les Joueurs Existant")
        print("3. Modifier un Joueur")
        print("4. Retour")
        choice = input("Entrez votre choix : ")
        return choice