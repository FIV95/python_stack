players_data = [
    {
        "name": "Kevin Durant",
        "age": "34",
        "position": "small forward",
        "team": "Brookyln Nets",
    },
    {
        "name": "Jason Tatum",
        "age": "24",
        "position": "small forward",
        "team": "Boston Celtics",
    },
    {
        "name": "Kyrie Irving",
        "age": "32",
        "position": "Point Guard",
        "team": "Brookyln Nets",
    },
    {
        "name": "Damien Lillard",
        "age": "33",
        "position": "Point Guard",
        "team": "Portland Trailblazers",
    },
    {
        "name": "Joel Embiid",
        "age": "32",
        "position": "power forward",
        "team": "Philly 76ers",
    },
    {
        "name": "DeMar DeRozan",
        "age": "32",
        "position": "shooting guard",
        "team": "Chicago Bulls",
    },
]

new_team = []
# for data in players_data:
#     player = {}  # Create an empty dictionary for the player
#     player.update(data)  # Update the empty dictionary with the player's information
#     new_team.append(player)  # Add the updated dictionary to the players list


# KevinDurant = [0]
# JasonTatum = [1]
# KyrieIrving = [2]
# DamienLillard = [3]
# JoelEmbiid = [4]
# DemarDeRozan = [5]
# print(players)

kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets",
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics",
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets",
}

# print(kevin["name"])
# Create your Player instances here!
# player_jason = ???



class Player:

      @classmethod
      def teamCreator(cls):
            new_team = []
            for player_data in players_data:
                  player = Player(player_data)
                  new_team.append(player)
            print(f'The New Team list: {new_team}')

      def __init__(self, player_dict):
            self.name = player_dict["name"]
            self.age = player_dict["age"]
            self.position = player_dict["position"]
            self.team = player_dict["team"]

      def __repr__(self):
            return f"Player: {self.name}, Age: {self.age}, Position: {self.position}, Team: {self.team}"



player_kevin = Player(kevin)
player_kyrie = Player(kyrie)
player_jason = Player(jason)
print(player_kyrie)
print(player_kevin)
player_kevin.teamCreator()