class Jobs:
      def __init__(self,name,hp,mp,strength,agility,intelligence,stamina,luck,attack,accuracy,defense,evasion,magicDefense):
            self.name = name
            self.hp = hp
            self.strength = strength
            self.agility = agility
            self.intelligence = intelligence
            self.stamina = stamina
            self.luck = luck
            self.attack = attack
            self.accuracy = attack
            self.defense = defense
            self.evasion = evasion
            self.magicDefense = magicDefense

warrior = Jobs("Warrior", 100, 0, 15, 5, 2, 10, 3, 10, 10, 8, 8, 9)
print(f"Warriors Strength: {warrior.strength}")
print(warrior.hp)
print(warrior.strength)
print(warrior.agility)
print(warrior.intelligence)
print(warrior.stamina)
print(warrior.luck)
print(warrior.attack)
print(warrior.accuracy)
print(warrior.defense)
print(warrior.evasion)
print(warrior.magicDefense)