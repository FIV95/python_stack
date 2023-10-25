players = [
      {
      "name": "Kevin Durant",
      "age": "34",
      "position": "small forward",
      "team": "Brookyln Nets"
      },
      {
      "name": "Jason Tatum",
      "age": "24",
      "position": "small forward",
      "team": "Boston Celtics"
      },
      {
            "name": "Kyrie Irving",
      "age": "32",
      "position": "Point Guard",
      "team": "Brookyln Nets"
      },
      {
            "name": "Damien Lillard",
      "age": "33",
      "position": "Point Guard",
      "team": "Portland Trailblazers"
      },
      {
            "name": "Joel Embiid",
      "age": "32",
      "position": "power forward",
      "team": "Philly 76ers"
      },
      {
            "name": "DeMar DeRozan",
      "age": "32",
      "position": "shooting guard",
      "team": "Chicago Bulls"
      }
]
class Player:

      @classmethod
      def printAllPlayerData(cls):
            for i in players:
                  print(i["name"])
                  print(i["age"])
                  print(i["position"])
                  print(i["team"])

      @classmethod
      def createInstances(cls):
                  playerInstanceList = []
                  for i in players:
                   newplayerinstance = Player((i["name"]), (i["age"]), (i["position"]), (i["team"]))
                   playerInstanceList.append(newplayerinstance)
                   print(playerInstanceList)



      def __init__(self, player_info):
            self.name = player_info["name"]
            self.age = player_info["age"]
            self.position = player_info["position"]
            self.team = player_info["team"]

Player.printAllPlayerData()