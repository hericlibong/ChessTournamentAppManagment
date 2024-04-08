from datetime import datetime
import uuid

class Tournament:
    """Creation de tournois"""
    def __init__(self, name: str, location: str, description: str, start_date: str, end_date: str, total_round: int = 4):
        """ Initialise l'id, le nom (name), le lieu (location), la date de début (start_date), la date de fin (end_date), 
        la description, le tour actuel (current_round), le nombre total de tour (total round). Ainsi que la liste des joueurs enregistrés,
        et la liste des tours effectués 
        """
        self.t_id = uuid.uuid4()  # Génère un identifiant unique pour chaque tournoi
        self.name = name
        self.location = location
        # Conversion directe des chaînes de dates en objets datetime, sans validation avancée
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.end_date = datetime.strptime(end_date, "%d/%m/%Y")
        self.description = description
        self.current_round = 0  # Commence à zéro, indiquant qu'aucun round n'a encore été joué
        self.rounds = []  # Liste de tours effectués pendant un tournoi
        self.registered_players = []  # Liste de joueurs enregistrés dans le tournoi
        self.total_round = total_round  # 4 par défaut mais peut être ajusté

    
    # def validate_date(self, date_str, date_type, start_date=None):
    #     """ Valide et convertit les dates de début et de fin."""
    #     if not date_str:
    #         raise ValueError(f"Aucune date fournie pour {date_type}.")
    #     try:
    #         date = datetime.strptime(date_str, "%Y-%m-%d")
    #         if date_type == "end" and start_date and date <= start_date:
    #             raise ValueError("La date de fin doit être après la date de début.")
    #         return date
    #     except ValueError as e:
    #         raise ValueError(f"Erreur de validation pour la date de {date_type}: {e}")








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