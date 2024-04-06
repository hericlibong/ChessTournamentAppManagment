from models.player import Player
from models.round import Round
from models.match import Match
from datetime import datetime
from models.tournament import Tournament
from controllers.application import ApplicationController
import random





def simulate_match_results(match, scores=None):
    if scores:
        match.set_results(scores)
    else :
        # Simule des résultats avec des scores aléatoires (1 = victoire, 0 = défaite, 0.5 = match nul)
        result = random.choice([(1, 0), (0, 1), (0.5, 0.5)])
        match.set_results(result)



def display_match_results(match):
    # Affichage formaté des résultats du match
    print(f"Match entre {match.players[0].firstname} et {match.players[1].firstname}: Résultats {match.results}")


def display_round_details(round):
    # Affichage du nom du round et des dates de début et de fin
    print(f"=== {round.name} ===")
    print(f"Date de début: {round.start_time}")
    if round.end_time:
        print(f"Date de fin: {round.end_time}")
    else:
        print("Le round n'est pas encore terminé.")
    
    # Affichage des détails de chaque match dans le round
    for match in round.matches:
        player1, player2 = match.players
        result = match.results
        print(f"Match: {player1.firstname} {player1.name} VS {player2.firstname} {player2.name}")
        print(f"Résultats: {result[0]} - {result[1]}")
        print("----------")


def main():

    admin = ApplicationController()
    admin.run()
    


    # tournament = Tournament(1,"Championnat International", "Paris", "Un tournoi très prestigieux", "2023-07-01", "2023-07-10")
    # # Création de joueurs
    # player1 = Player(name="Randal", firstname="Kolo", birthdate="1990-01-01", unique_id="AB12345")
    # player2 = Player(name="Mbappe", firstname="Kyllian", birthdate="1992-02-02", unique_id="CD67890")
    # player3 = Player(name="Rinner", firstname="Teddy", birthdate="1994-03-03", unique_id="EF12345")
    # player4 = Player(name="Perec", firstname="Marie José", birthdate="1996-04-04", unique_id="GH67890")


    
    # tournament.add_player(player1)
    # tournament.add_player(player2)
    # tournament.add_player(player3)
    # tournament.add_player(player4)

    # print("Joueurs inscrits: ")
    # for player in tournament.register_player:
    #     print(player)


    # tournament.remove_player(player3)

    # # Afficher les joueurs inscrits après le retrait
    # print("Joueurs inscrits après retrait :")
    # for player in tournament.register_player:
    #     print(player)
    

    # # Création d'un tour
    # round1 = Round(name="Round 1", start_time=datetime.now())
   

    # # Création et ajout de matchs au tour (association des joueurs dans les matchs)
    # match1 = Match(players=(player1, player2))
    # match2 = Match(players=(player3, player4))
    # match3 = Match(players=(player3, player2))
    # match4 = Match(players=(player4, player1))



    # round1.add_match(match1)
    # round1.add_match(match2)
    # round1.add_match(match3)
    # round1.add_match(match4)

    # # Simulation des résultats pour chaque match
    # simulate_match_results(match1, scores=(1, 0))
    # simulate_match_results(match2, scores=(0.5, 0.5))
    # simulate_match_results(match3, scores=(1, 0))
    # simulate_match_results(match4, scores=(0, 1))
    # Affichage des résultats
    # display_match_results(match1)
    # display_match_results(match2)
    #display_round_details(round1)


if __name__ == "__main__":
    main()
