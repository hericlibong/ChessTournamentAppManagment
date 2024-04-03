""" 
Joueurs : Les joueurs sont des entités centrales de notre application. 
Chaque joueur doit avoir un nom, prénom, date de naissance, 
et un identifiant national d'échecs unique. 
Ces informations seront stockées dans des fichiers JSON.

"""


class Player:
    """Création de joueurs"""
    def __init__(self, name:str, firstname:str, birthdate:str, unique_id:int):
        """ Initialise le nom (name), le prénom (firstname), la date de naissance (birthdate), et l'id du joueur (unique_id) """
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.unique_id = unique_id


        
