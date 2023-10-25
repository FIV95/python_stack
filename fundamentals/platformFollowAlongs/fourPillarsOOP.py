### Encasulation
# we use classes to define what our objects are and how they behave

class CoffeeM:
      def __init__(self,name):
            self.name = name
            self.water_temp = 200
      def brew_now(self,beans):
            print(f'Using {beans}!')
            print("Brew now brown cow!")
      def clean(self):
            print("Cleaning!")


### Inheritance
## is the idea that we pass along attributes and methods from one class into a "sub-class" //
## Parent class gets key word = 'super'

class CappucinoM( CoffeeM ):
      def __init__(self,name):
            super().__init__(name)
            self.milk = "whole"
      def make_cappucino(self,beans): ### Polymorphism refers to the idea that a child class can have
            super().brew_now(beans) ###   different versions of the same method as the parent class
            print("Frothy!!!")      ###   Depending on the class, the clean method will do different things
      def clean(self):
            print("Cleaning the Froth!")


### Abstraction is extension of encapsulation. We hide attibutes or methods. The abstraction still has the functionality but it hides the code?

class Barist:
      def __init__(self,name):
            self.name = name
            self.cafe = CoffeeM("Cafe")
      def make_coffee(self,beans):
            self.cafe.brew_now(beans)

