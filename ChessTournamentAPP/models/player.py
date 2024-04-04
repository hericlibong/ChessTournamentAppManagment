
import re
from datetime import datetime


class Player:
    """Création de joueurs"""
    def __init__(self, name:str, firstname:str, birthdate:str, unique_id:int):
        """ Initialise le nom (name), le prénom (firstname), la date de naissance (birthdate), et l'id du joueur (unique_id) """
        self.name = name
        self.firstname = firstname
        self.birthdate = self.validate_birthdate(birthdate)
        self.unique_id = self.validate_unique_id(unique_id)
        
    
    def validate_birthdate(self, birthdate_str):
        try:
            birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Format de la date de naissance invalide.  Utilisez YYYY-MM-DD.")
        
        if birthdate >= datetime.now():
            raise ValueError("La date de naissance doit être dans la passé ")
        return birthdate

    def validate_unique_id(self, unique_id):
        if not re.match(r'^[A-Z]{2}\d{5}$', unique_id):
            raise ValueError("L'unique_id doit suivre le format: deux lettres suivies de cinq chiffres")
        return unique_id
    
    def __str__(self):
        # Représentation informelle, pour l'affichage à l'utilisateur
        return f"{self.firstname} {self.name} (ID: {self.unique_id})"

    def __repr__(self):
        # Représentation officielle de l'objet, plus détaillée et idéalement utile pour recréer l'objet
        return f"Player(name='{self.name}', firstname='{self.firstname}', birthdate='{self.birthdate.strftime('%Y-%m-%d')}', unique_id='{self.unique_id}')"


        

