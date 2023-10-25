class Robot:

      all_robots = []

      @staticmethod
      def validate():
            if data(['color'] == 'orange'):

            print('Orange robots are not allowed!')

      @classmethod
      def evil_mode(cls):
            for robot in cls.all_robots:
                  print(f'{robot} turning evil...')
                  robot.dangerous = True
                  robot.ammo = 100
                  robot.add_equipment

      my_attribute = "Yup Its Here"

      def __init__(self, data):

            # print("Beep Boop! Hello World")
            self.energy = 100
            self.ammo = 0
            self.wifi = True

            self.name = data["name"]
            self.color = data["color"]
            self.dangerous = data["dangerous"]
            self.beer_tolerance = data["beer_tolerance"]
            self.equipment = data["equipment"]


            Robot.all_robots.append(self)

      def __repr__(self):
            return f'{self.color} robot: {self.name}'

      def print_stats(self):
            print(f"========{self.name}========")
            print(f'{self.color} robot')
            print(f'{self.dangerous}')



Robot.validate()
Robot.evil_mode()

bobr_data = {
      "name" : "R.O.B.O.B",
      "color": "Orange",
      "Dangerous": ""
}