# player_views.py

class PlayerView:

    @staticmethod
    def create_player():
        """ 
        Vue statique pour créer des joueurs, collectant les informations nécessaires
        """
        name = input("Entrez le nom du joueur : ")
        firstname = input("Entrez le prénom du joueur : ")
        birthdate = input("Entrez la date de naissance du joueur (DD/MM/YYYY) : ")
        # Le unique_id peut être généré automatiquement? Voir les spécifités techniques
        u_id = input("Entrez l'identifiant unique : ")

        return name, firstname, birthdate, u_id
    

    @staticmethod
    def display_players(players):
        """Affiche les joueurs enregistrés"""
        if not players:
            print("Aucun joueur n'est enregistré.")
        else:
            print("Liste des joueurs enregistrés :")
            for player in players:
                print(f"ID: {player.unique_id}, Nom: {player.name}, Prénom: {player.firstname}, Date de naissance: {player.birthdate.strftime('%d/%m/%Y')}")

