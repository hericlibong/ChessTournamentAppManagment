

class MenuView:
    """Creation du menu"""
    @staticmethod
    def display_main_menu():
        """Affiche le menu principal """
        print("1. Start a new tournament")
        print("2. See the existing tournaments")
        print("3. Load a tournament")
        print("4. Quit")
        choice = input("Enter your choice : ")
        return choice