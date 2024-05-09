# models/tournament.py

from datetime import datetime
import uuid
from models.round import Round
from models.match import Match
import random


class Tournament:
    """ Gestion de tournois d'échecs. """
    def __init__(self, name: str, location: str, description: str, start_date: str, end_date: str,
                 total_round: int = 20, t_id: str = None,
                 current_round: int = 0, rounds=None, registered_players=None):
        self.t_id = t_id if t_id else str(uuid.uuid4())[:8]
        self.name = name
        self.location = location
        self.description = description
        self.current_round = current_round
        self.rounds = rounds if rounds else []
        self.registered_players = registered_players if registered_players else []
        self.total_round = total_round
        self.start_date = self.safe_strptime(start_date, "%d/%m/%Y")
        self.end_date = self.safe_strptime(end_date, "%d/%m/%Y")

    def to_dict(self):
        return {
            "t_id": self.t_id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.strftime("%d/%m/%Y") if self.start_date else "Invalid date",
            "end_date": self.end_date.strftime("%d/%m/%Y") if self.end_date else "Invalid date",
            "description": self.description,
            "current_round": self.current_round,
            "rounds": [round.to_dict() for round in self.rounds],
            "registered_players": [player.to_dict() for player in self.registered_players],
            "total_round": self.total_round
        }

    def safe_strptime(self, date_str, date_format="%Y-%m-%d"):
        """ Essaie de convertir une chaîne en datetime, renvoie None si échec. """
        try:
            return datetime.strptime(date_str, date_format)
        except ValueError:
            print(f"Erreur de format de date: {date_str}, attendu {date_format}")
            return None

    def initialize_rounds(self):
        num_players = len(self.registered_players)
        number_of_rounds = num_players - 1 if num_players % 2 == 0 else num_players
        self.rounds = [Round(name=f"Round {i + 1}") for i in range(number_of_rounds)]
        self.total_round = number_of_rounds

    def start_tournament(self):
        """Démarre un tournoi s'il n'est pas déjà terminé"""
        print("Démarrage du tournoi...".center(30))
        print("-" * 30)
        num_players = len(self.registered_players)
        if num_players < 2:
            print("Pas assez de joueurs pour commencer un tournoi.")
            print("Allez dans la section 'Gestion des joueurs' pour inscrire des participants.")
            print(" 7. Retour au menu principal --> Gestion des joueurs. ")
            return
        # Annuler le paramètre par défaut de total_round
        self.total_round = num_players - 1 if num_players % 2 == 0 else num_players
        self.initialize_rounds()
        self.generate_matches()
        if self.rounds:
            self.rounds[0].start_time = datetime.now()
            print(f"Le Tournoi '{self.name}' a commencé avec {len(self.registered_players)}"
                  f"joueurs et {self.total_round} rounds.")
        else:
            print("Failed to initialize rounds properly.")

    def generate_matches(self):
        """
        Génère et organise les matches pour chaque round du tournoi basé sur les joueurs inscrits.
        Les joueurs sont appariés de manière à éviter les répétitions avec des adversaires précédents.
        Cette méthode mélange les joueurs inscrits, les associe en paires pour les matches,
        et s'assure qu'aucun joueur ne rencontre un adversaire contre qui il a déjà joué,
        autant que possible. Les matches sont ajoutés aux rounds existants dans le tournoi.

        Les joueurs sans adversaires disponibles sont replacés dans la liste pour un nouvel essai,
        évitant ainsi de laisser un joueur sans match à la fin du processus de jumelage.
        """
        players = self.registered_players[:]  # Copie de la liste des joueurs pour manipulation
        random.shuffle(players)  # Mélange des joueurs pour l'aléatoire
        for round in self.rounds:  # Itérer sur chaque round du tournoi
            matches = []  # Liste pour stocker les matches de ce round
            while len(players) > 1:  # Tant qu'il y a au moins deux joueurs pour former un match
                player1 = players.pop(0)  # Sélection du premier joueur
                # Recherche d'un adversaire non rencontré précédemment
                player2 = next((p for p in players if p.unique_id not in player1.past_opponents), None)
                if player2:
                    matches.append(Match(players=(player1, player2)))  # Création du match
                    # Enregistrement de l'adversaire dans l'historique des deux joueurs
                    player1.past_opponents.add(player2.unique_id)
                    player2.past_opponents.add(player1.unique_id)
                    players.remove(player2)  # Retirer l'adversaire de la liste des joueurs disponibles
                else:
                    players.append(player1)  # Retour du joueur dans la liste pour une nouvelle tentative
            round.matches.extend(matches)  # Ajout des matches au round courant

    def update_scores(self, round_index, match_index, score1, score2):
        """Permet de mettre les score à jour"""
        match = self.rounds[round_index].matches[match_index]
        match.set_results((score1, score2))

    def register_player(self, player):
        """ Enregistre un joueur dans le tournoi si le tournoi est actif ou non terminé ou non commencé. """
        # Vérifie si le tournoi est terminé ou si le premier round a commencé
        if self.is_tournament_complete() or (self.rounds and self.rounds[0].start_time is not None):
            print(f"Le tournoi'{self.name}' est terminé ou en cours.")
            print("Inscription impossible.")
            return
        if not self.is_active():
            print(f" Le tournoi '{self.name}'n'est pas actif")
            return
        if player not in self.registered_players:
            player.past_opponents.clear()  # Efface l'historique du joueur
            self.registered_players.append(player)
            print(f"{player.firstname} {player.name} a été ajouté(e) au tournoi '{self.name}'.")
        else:
            print(f"{player.firstname} {player.name} est déjà inscrit(e) à ce tournoi.")

    def is_active(self):
        """ Vérifie si le tournoi est toujours en cours."""
        # Utilise datetime.now() pour obtenir le datetime actuel et le convertit pour obtenir minuit ce jour-là.
        today_midnight = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return self.current_round < self.total_round and self.end_date >= today_midnight

    def add_round(self, round_name, start_time=None):
        """Ajoute un nouveau round au tournoi si possible."""
        if not self.is_active():
            print("Le tournoi n'est pas actif.")
            return
        new_round = Round(name=round_name, start_time=start_time)
        self.rounds.append(new_round)
        print(f"Round '{round_name}' ajouté au tournoi '{self.name}'.")

    def start_round(self, round_index):
        """Démarre un round spécifié par son index."""
        try:
            round = self.rounds[round_index]
            if round.start_time is None:
                round.start_time = datetime.now()
                print(f"Round '{round.name}' démarré.")
            else:
                print(f"Round '{round.name}' a déjà été démarré.")
        except IndexError:
            print("Index de round invalide.")

    def is_tournament_complete(self):
        """Vérifie si tous les rounds du tournoi sont terminés"""
        if not self.rounds:  # Aucun round n'a été ajouté au tournoi
            return False
        return all(round.is_complete for round in self.rounds)

    def end_round(self, round_index, match_results):
        try:
            round = self.rounds[round_index]
            print(f"Attempting to end round: {round.name}, which started at: {round.start_time}")
            
            if round.start_time is None:
                print(f"Cannot end round {round.name} as it has not started.")
                return

            if not round.is_complete:
                print(f"Ending round: {round.name}")
                for match, result in zip(round.matches, match_results):
                    print(f"Updating match result: {result}")
                    match.set_results(result)
                round.end_time = datetime.now()
                round.is_complete = True
                print(f"Round '{round.name}' completed at {round.end_time}.")
                if all(r.is_complete for r in self.rounds):
                    print(f"All rounds completed. Tournament '{self.name}' is now finished.")
            else:
                print(f"Round '{round.name}' is already completed.")
        except IndexError:
<<<<<<< HEAD
            print("Invalid round index.")


    def calculate_player_points(self):
        player_points = {}
        for round in self.rounds:
            for match in round.matches:
                # Assurez-vous que chaque joueur est dans le dictionnaire
                if match.players[0].unique_id not in player_points:
                    player_points[match.players[0].unique_id] = 0
                if match.players[1].unique_id not in player_points:
                    player_points[match.players[1].unique_id] = 0

                # Ajouter les points pour chaque joueur selon les résultats
                player_points[match.players[0].unique_id] += match.results[0]
                player_points[match.players[1].unique_id] += match.results[1]

        return player_points
=======
            print("Index de round invalide")

>>>>>>> experimental-features
