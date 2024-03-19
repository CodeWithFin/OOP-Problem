from data.participant_data import PARTICIPANTS
from utils.sorting import sort_scoreboard

def create_scoreboard(participants):
    scoreboard = [
        {
            "name": participant["name"],
            "score": calculate_score(
                participant["chickenwings"],
                participant["hamburgers"],
                participant["hotdogs"]
            )
        }
        for participant in participants
    ]
    return sort_scoreboard(scoreboard)

def calculate_score(chickenwings, hamburgers, hotdogs):
    chicken_wing_score = chickenwings * 5
    hamburger_score = hamburgers * 3
    hotdog_score = hotdogs * 2
    return chicken_wing_score + hamburger_score + hotdog_score