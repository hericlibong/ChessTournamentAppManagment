from datetime import datetime
from .match import Match


class Round:
    def __init__(
            self, name: str, start_time: datetime = None, end_time: datetime = None,
            is_complete: bool = False, matches=None):
        """Initialise un nouveau round avec des paramètres optionnels pour le début et la fin."""
        self.name = name
        self.is_complete = is_complete
        self.matches = matches if matches else []
        self.start_time = self.convert_str_to_datetime(start_time)
        self.end_time = self.convert_str_to_datetime(end_time)   # Modification effectuée

    def convert_str_to_datetime(self, date_str):
        """Convertit une chaîne de caractères en un objet datetime, gère les formats non valides."""
        if isinstance(date_str, datetime):
            return date_str
        elif isinstance(date_str, str):
            try:
                return datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            except ValueError:
                print(f"Format de date invalide : {date_str}. Attendu 'YYYY-MM-DD HH:MM'.")
                return None
        return None

    def add_match(self, player1, player2, current_matches, results=(0, 0)):
        """Tente d'ajouter un match au round si toutes les conditions sont remplies."""
        if self.can_add_match(player1, player2, current_matches):
            match = Match(players=(player1, player2), results=results)
            self.matches.append(match)
            self.update_match_tracking(current_matches, player1, player2)
            print(f"Match entre {player1.firstname} {player1.name} et"
                  f"{player2.firstname} {player2.name} ajouté à {self.name}.")
        else:
            print("Match not added to avoid duplicates or because the round is complete.")

    def can_add_match(self, player1, player2, current_matches):
        """Vérifie si un match peut être ajouté en évitant les doublons et les adversaires passés."""
        return (
            not self.is_complete and
            (player1, player2) not in current_matches and
            (player2, player1) not in current_matches and
            player2.unique_id not in player1.past_opponents
        )

    def update_match_tracking(self, current_matches, player1, player2):
        """Met à jour le suivi des matches joués et des adversaires rencontrés."""
        current_matches.add((player1, player2))
        current_matches.add((player2, player1))
        player1.add_past_opponent(player2.unique_id)
        player2.add_past_opponent(player1.unique_id)

    def to_dict(self):
        """Sérialise les informations du round en un dictionnaire pour la sauvegarde."""
        return {
            'name': self.name,
            'is_complete': self.is_complete,
            'matches': [match.to_dict() for match in self.matches],
            'start_time': self.start_time.strftime('%Y-%m-%d %H:%M') if self.start_time else None,
            'end_time': self.end_time.strftime('%Y-%m-%d %H:%M') if self.end_time else None,

        }

    def end_round(self):
        """Marque la fin du round et enregistre l'heure de fin."""
        self.end_time = datetime.now()
        self.is_complete = True
        print(f"Round '{self.name}' has ended at {self.end_time}.")

    def update_match_result(self, match_index, new_results):
        """Met à jour les résultats d'un match spécifié si le round n'est pas complet."""
        if self.is_complete:
            print(f"Cannot update match results. Round '{self.name}' is already complete.")
            return
        if match_index < 0 or match_index >= len(self.matches):
            print("Invalid match index. Please provide a correct index.")
            return
        self.matches[match_index].set_results(new_results)
        print(f"Results updated for match {match_index + 1} in round '{self.name}'.")
