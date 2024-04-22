# models/tournament.py

from datetime import datetime
import uuid
from .round import Round
from .match import Match
import random

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
        # Conversion directe des chaînes de dates en objets datetime, sans validation avancé
        
        self.description = description
        self.current_round =  current_round  # Commence à zéro, indiquant qu'aucun round n'a encore été joué
        self.rounds = rounds if rounds is not None else []  # Liste de tours effectués pendant un tournoi
        self.registered_players = registered_players if registered_players is not None else []  # Initialise avec la valeur fournie ou une liste videe
        self.total_round = total_round  # 4 par défaut mais peut être ajusté
        self.current_matches = set()
        # Vérifie si start_date est une instance de datetime, sinon convertit de str
        if isinstance(start_date, datetime):
            self.start_date = start_date
        else:
            self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        
        # Vérifie si end_date est une instance de datetime, sinon convertit de str
        if isinstance(end_date, datetime):
            self.end_date = end_date
        else:
            self.end_date = datetime.strptime(end_date, "%d/%m/%Y")

    ## Sérialisation des données ##

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
    
    
    def is_active(self):
        """Vérifie si le tournoi est actif"""
        return self.current_round < self.total_round and self.end_date > datetime.now()



    def start_tournament(self):
        """Démarre le tournoi après avoir vérifié tous les prérequis."""
        if self.start_date > datetime.now():
            print("Le tournoi est prévu pour une date future et ne peut pas encore commencer.")
            return
        if len(self.registered_players) < 5:
            print("Pas assez de joueurs pour démarrer le tournoi (minimum 5 joueurs requis).")
            return
        print(f"Démarrage du tournoi '{self.name}' avec {len(self.registered_players)} joueurs.")
        self.shuffle_and_create_rounds()
        print(f"Le tournoi '{self.name}' a commencé avec succès.")



    def shuffle_and_create_rounds(self):
        """Mélange les joueurs et prépare les rounds basés sur le nombre de joueurs."""
        random.shuffle(self.registered_players)
        print("Joueurs mélangés pour le premier round.")
        # Générer les rounds et matches selon les règles définies
        self.generate_matches()

    def generate_matches(self):
        """Génère des matches pour chaque round en utilisant la classe Match."""
        # Assurez-vous que les joueurs sont mélangés et les matchs bien générés
        random.shuffle(self.registered_players)
        current_round = Round(name=f"Round {len(self.rounds) + 1}")
        for i in range(0, len(self.registered_players) - 1, 2):
            player1 = self.registered_players[i]
            player2 = self.registered_players[i + 1]
            match = Match(players=(player1, player2))
            current_round.matches.append(match)
        self.rounds.append(current_round)


    

    def update_scores(self, round_index, match_index, score1, score2):
        """Met à jour les scores pour un match spécifique dans un round donné."""
        match = self.rounds[round_index].matches[match_index]
        match.set_results((score1, score2))
        

    
    
    ### Gestion des joueurs ###

    def register_player(self, player):
        """ Ajoute un joueur au tournoi si le tournoi est actif"""
        if not self.is_active():
            print(f"Le tournoi '{self.name}' n'est pas actif ou est déjà terminé. ")
            return
        if player not in self.registered_players:
            self.registered_players.append(player)
            print(f"{player.firstname} {player.name} a été ajouté(e) au tournoi '{self.name}'.")
        else:
            print(f"{player.firstname} {player.name} est déjà inscrit(e) à ce tournoi.")
    
    
    
    ## Gestion des Rounds ##


    

    def add_round(self, round_name, start_time=None):
        """ Ajoute un nouveau round au tournoi si le tournoi est actif"""
        if not self.is_active():
            print("Le round ne peut pas être ajouté. Le Tournoi n'est pas actif.")
            return
        new_round = Round(name=round_name, start_time=start_time)
        self.rounds.append(new_round)
        #start_status = f"starting at {start_time}" if start_time else "not started"
        print(f"Le Round '{round_name}' a été ajouté au tournament '{self.name}'.")


    def start_round(self, round_name):
        """Démarre un round spécifié par son nom en définissant le start_time à maintenant si ce n'est pas déjà fait."""
        if not self.is_active():
            print(f"Impossible de démarrer un round. Le tournoi '{self.name}' n'est pas actif")
            return
        
        for round in self.rounds:
            if round.name == round_name and round.start_time is None:
                round.start_time = datetime.now()
                print(f"Round '{round_name}' has started.")
                break
        else:
            print(f"No round named '{round_name}' found or it's already started.")


    def end_round(self, round_name):
        """Termine un round spécifié par son nom en définissant le end_time à maintenant et en marquant le round comme complet."""
        if not self.is_active():
            print(f"Impossible de terminer le round. Le tournoi '{self.name}' n'est pas actif")
            return
        for round in self.rounds:
            if round.name == round_name and not round.is_complete:
                round.end_time = datetime.now()
                round.is_complete = True
                print(f"Round '{round_name}' has ended.")
                break
        else:
            print(f"No round named '{round_name}' found or it's already completed.")

