class Parent:
      def __init__(self, name):
            def method_a(self):
                  print("invoking PARENT method_a!")

class Child(Parent):
            def method_a(self):
                  print("invoking CHILD method_a")

dad = Parent()
son = Child()

class Person:
      def pay_bill(self):
            raise NotImplementedError
# Millionaire inherits from person
class Millionarie(Person):
      def pay_bill(self):
            print("Here you go! Keep the Change!")
# Grad Student also inherits from the Person class
class GradStudent(Person):
      def pay_bill(self):
            print("can I owe you ten bucks or do the dishes?")