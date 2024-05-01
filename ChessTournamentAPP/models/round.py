
from datetime import datetime
from typing import List, Tuple
from .match import Match
from .player import Player

class Round:
    def __init__(self, name: str, start_time: datetime = None,  end_time: datetime = None, is_complete:bool = False, matches=None):
        self.name = name
        self.is_complete = is_complete
        self.matches = matches if matches else []
        self.start_time = self.convert_str_to_datetime(start_time)
        self.end_time = self.convert_str_to_datetime(end_time) # Modification effectuée
        #self.end_time = None  
        


    def convert_str_to_datetime(self, date_str):
        if isinstance(date_str, datetime):
            return date_str
        elif isinstance(date_str, str):
            try:
                return datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            except ValueError:
                print(f"Invalid format for date: {date_str}. Expected 'YYYY-MM-DD HH:MM'.")
                return None
        return None


    def add_match(self, player1, player2, current_matches, results=(0, 0)):
        """Attempts to add a match to the round if it meets all conditions."""
        if self.can_add_match(player1, player2, current_matches):
            match = Match(players=(player1, player2), results=results)
            self.matches.append(match)
            self.update_match_tracking(current_matches, player1, player2)
            print(f"Match between {player1.firstname} {player1.name} and {player2.firstname} {player2.name} added to {self.name}.")
        else:
            print(f"Match not added to avoid duplicates or because the round is complete.")
    
    
    
    def can_add_match(self, player1, player2, current_matches):
        """Checks if a match can be added based on various conditions."""
        return (
            not self.is_complete and
            (player1, player2) not in current_matches and
            (player2, player1) not in current_matches and
            player2.unique_id not in player1.past_opponents
        )

    def update_match_tracking(self, current_matches, player1, player2):
        """Updates tracking of matches and opponents."""
        current_matches.add((player1, player2))
        current_matches.add((player2, player1))
        player1.add_past_opponent(player2.unique_id)
        player2.add_past_opponent(player1.unique_id)

    def to_dict(self):
        """ Converti l'objet Round en dictionnaire pour la sérialisation """
        return {
            'name': self.name,
            'is_complete': self.is_complete,
            'matches': [match.to_dict() for match in self.matches],
            'start_time': self.start_time.strftime('%Y-%m-%d %H:%M') if self.start_time else None,
            'end_time': self.end_time.strftime('%Y-%m-%d %H:%M') if self.end_time else None,
            
        }
    
    
    def end_round(self):
        self.end_time = datetime.now()
        self.is_complete = True
        print(f"Round '{self.name}' has ended at {self.end_time}.")
    

    def update_match_result(self, match_index, new_results):
        if self.is_complete:
            print(f"Cannot update match results. Round '{self.name}' is already complete.")
            return
        if match_index < 0 or match_index >= len(self.matches):
            print("Invalid match index. Please provide a correct index.")
            return
        self.matches[match_index].set_results(new_results)
        print(f"Results updated for match {match_index + 1} in round '{self.name}'.")

    
    
