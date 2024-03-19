class Participant:
    def __init__(self, name, chickenwings, hamburgers, hotdogs):
        self.name = name
        self.chickenwings = chickenwings
        self.hamburgers = hamburgers
        self.hotdogs = hotdogs

    def calculate_score(self):
        chicken_wing_score = self.chickenwings * 5
        hamburger_score = self.hamburgers * 3
        hotdog_score = self.hotdogs * 2
        return chicken_wing_score + hamburger_score + hotdog_score