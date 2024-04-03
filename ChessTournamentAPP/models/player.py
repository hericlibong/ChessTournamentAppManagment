""" 
Joueurs : Les joueurs sont des entités centrales de notre application. 
Chaque joueur doit avoir un nom, prénom, date de naissance, 
et un identifiant national d'échecs unique. 
Ces informations seront stockées dans des fichiers JSON.

"""
import re


class Player:
    """Création de joueurs"""
    def __init__(self, name:str, firstname:str, birthdate:str, unique_id:int):
        """ Initialise le nom (name), le prénom (firstname), la date de naissance (birthdate), et l'id du joueur (unique_id) """
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        # Validation de l'unique_id
        if not re.match(r'^[A-Z]{2}\d{5}$', unique_id):
            raise ValueError("L'unique_id doit suivre le format : deux lettres suivies de cinq chiffres.")
        self.unique_id = unique_id
        


        
