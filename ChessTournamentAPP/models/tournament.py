# models/tournament.py

from datetime import datetime
import uuid

class Tournament:
    """Creation de tournois"""
    def __init__(self, name: str, location: str, description: str, start_date: str, end_date: str, 
                 total_round: int = 4, t_id:str = None, current_round: int = 0, rounds=None, registered_players=None):
        """ Initialise l'id, le nom (name), le lieu (location), la date de début (start_date), la date de fin (end_date), 
        la description, le tour actuel (current_round), le nombre total de tour (total round). Ainsi que la liste des joueurs enregistrés,
        et la liste des tours effectués 
        """
        
        self.t_id = t_id if t_id is not None else str(uuid.uuid4())[:8]
        # Génère un nouvel identifiant unique pour chaque tournoi si aucun n'est fourni et prend les 8 premiers caractères et un nouvel ID seulement 
        self.name = name 
        self.name = name
        self.location = location
        # Conversion directe des chaînes de dates en objets datetime, sans validation avancée
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.end_date = datetime.strptime(end_date, "%d/%m/%Y")
        self.description = description
        self.current_round =  current_round  # Commence à zéro, indiquant qu'aucun round n'a encore été joué
        self.rounds = rounds if rounds is not None else []  # Liste de tours effectués pendant un tournoi
        self.registered_players = registered_players if registered_players is not None else []  # Initialise avec la valeur fournie ou une liste videe
        self.total_round = total_round  # 4 par défaut mais peut être ajusté


    def to_dict(self):
        """Sérialise l'objet Tournament pour la sauvegarde en JSON."""
        return {
            "t_id": str(self.t_id),  # uuid est converti en string
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.strftime("%d/%m/%Y"),
            "end_date": self.end_date.strftime("%d/%m/%Y"),
            "description": self.description,
            "current_round": self.current_round,
            "rounds": [round.to_dict() for round in self.rounds],  # Supposant que Round a une méthode to_dict
            "registered_players": [player.to_dict() for player in self.registered_players],  # Supposant que Player a une méthode to_dict
            "total_round": self.total_round
        }
    


    # Méthodes créé pour tester le modèle
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