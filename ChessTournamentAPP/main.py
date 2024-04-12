from models.player import Player
from models.round import Round
from models.match import Match
from datetime import datetime
from models.tournament import Tournament
from controllers.application_controller import ApplicationController
import random







def main():

    admin = ApplicationController()
    admin.run()
   
   
       

if __name__ == "__main__":
    main()
