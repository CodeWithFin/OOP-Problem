def sort_scoreboard(scoreboard):
    """
    Sort the scoreboard by score in descending order,
    and then by name in alphabetical order in case of a tie.
    """
    scoreboard.sort(key=lambda x: (-x["score"], x["name"]))
    return scoreboard