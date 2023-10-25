class Ninja:

      def __init__(self, first_name, last_name, treats, pet_food, pet):
            self.first_name = first_name
            self.last_name = last_name
            self.treats = treats
            self.pet_food = pet_food

      def walk(self, pet):
            print(f'{self.first_name} beings to walk their {self.pet}')

      def feed(self, pet):
            print(f'{self.first_name} begins to feed their {self.pet}')

      def bath(self,pet):
            print(f'{self.first_name} begins to bathe their {self.pet}')

class Pet:

      def __init__(self, name, kind, tricks, health, energy):
            self.name = name
            self.kind = kind
            self.tricks = []
            self.health = health
            self.energy = energy