"""  
Tournois : Les tournois sont des collections de tours et de matchs, 
avec des informations telles que le nom, lieu, dates, nombre de tours prévu, 
liste des joueurs inscrits, et une description générale. 
Les informations sur les tournois seront également stockées dans des fichiers JSON.

● nom ;
● lieu ;
● date de début et de fin ;
● nombre de tours – réglez la valeur par défaut sur 4 ;
● numéro correspondant au tour actuel ;
● une liste des tours ;
● une liste des joueurs enregistrés ;
● description pour les remarques générales du directeur du tournoi.


"""

from datetime import datetime

class Tournament:
    """Creation de tournois"""
    def __init__(self, t_id:int, name:str, location:str, description:str, current_round:int, start_date:datetime= None, end_date:datetime = None, total_round:int = 4):
        """ Initialise l'id, le nom (name), le lieu (location), la date de début (start_date), la date de fin (end_date), 
        la description, le tour actuel (current_round), le nombre total de tour (total round). Ainsi que la liste des joueurs enregistrés,
        et la liste des tours effectués 
        """
        self.t_id = t_id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.current_round = current_round
        self.rounds = [] # Liste de tours effectués pendant un tournoi
        self.register_player = [] # Liste de joueurs enregistrés dans le tournoi
        self.total_round = total_round

    

    def add_player(self, player):
        """Ajoute un joueur à la liste des joueurs inscrits au tournoi."""
        self.register_player.append(player)
        print(f"{player} a été ajouté au tournoi '{self.name}'.")
    

    def remove_player(self, player):
        """Retire un joueur de la liste des joueurs inscrits au tournoi, s'il y est."""
        if player in self.register_player:
            self.register_player.remove(player)
            print(f"{player} a été retiré du tournoi '{self.name}'.")
        else:
            print(f"{player} n'est pas inscrit au tournoi '{self.name}'.")