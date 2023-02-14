class SportsMan:
    def __init__(self, sport_id, sport_name):
        self.sport_id = sport_id
        self.sport_name = sport_name

    def printInfo(self):
        print(self.sport_id, self.sport_name)

    def set_type(self, sport_type):
        self.sport_type = sport_type

    def get_type(self):
        return self.sport_type

class TeamSport(SportsMan):
    def __init__(self, num_players, sport_id, sport_name):
        super(  ).__init__(sport_id, sport_name)
        self.num_players = num_players

    def printInfo(self):
        super().printInfo()
        print(self.num_players)

class Football(TeamSport):
    def __init__(self, num_players, sport_id, sport_name, team_name):
        super().__init__(num_players, sport_id, sport_name)
        self.team_name = team_name
    
    def printInfo(self):
        super().printInfo()
        print(self.team_name)

foot = Football(7, "football", 11, "Barca")
foot.printInfo()
foot.set_type("Outdoor")
print(foot.get_type())