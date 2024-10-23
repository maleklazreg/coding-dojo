from python1 import PLayers

class Player:
    def init(self, player_member):
        self.name = player_member["name"]
        self.age = player_member["age"]
        self.position = player_member["position"]
        self.team = player_member["team"]

    def repr(self):
        display = f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}"
        return display

kevin_data = {
    "name": "Kevin Durant", 
    "age": 34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason_data = {
    "name": "Jason Tatum", 
    "age": 24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie_data = { 
    "name": "Kyrie Irving", 
    "age": 32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}


player_kevin = Player(kevin_data)
player_jason = Player(jason_data)
player_kyrie = Player(kyrie_data)


new_team = []
for player in PLayers:
    player = Player(player)
    new_team.append(player)

print(new_team)