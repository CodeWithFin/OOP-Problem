from models.scoreboard import create_scoreboard
from data.participant_data import PARTICIPANTS

if __name__ == "__main__":
    scoreboard = create_scoreboard(PARTICIPANTS)
    print(scoreboard)