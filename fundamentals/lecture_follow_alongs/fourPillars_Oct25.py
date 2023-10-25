#Encapsulation##################################################
class Computer:

      computer_list = []

      def __init__(self, cpu_speed ="2.8 Ghz", disk_space= "256 GB", price="300", ram="8 GB", motherboard="asus", os="Widnows", gpu="Potato"):
            self.cpu_speed = cpu_speed
            self.disk_space = disk_space
            self.price = price
            self.ram = ram
            self.motherboard = motherboard
            self.os = os
            self.gpu = gpu

      def print_stats(self):
            print(self.cpu_speed)
            print(self.disk_space)
            print(self.price)
            print(self.ram)
            print(self.motherboard)
            print(self.os)
            print(self.gpu)

      def boot(self):
            print(f'{self.os} boots!')

my_cpu = Computer("4.3 Ghz", "5 TB", 3000, "64GB", "ASUS", "Windows", "RTX4090")
default_cpu = Computer()
default_cpu.print_stats

my_cpu.print_stats()

##Inheritance ################################################
class Mac(Computer):
      def __init__(self, disk_space, price):
            super().__init__("3.6 Ghz", disk_space, price, "16 GB", "Apple", "Mac OS", "Integrated") ## gives Mac access to the parent class Computer

##POLYMORPHISM ################################################
      def boot(self): ### mac classs has boot that does something different than the Computer class
            print("Welcome to Mac, buy and Iphone and some airpods plz")

my_mac = Mac("512 GB", 3200)
my_mac.boot()
my_cpu.boot()
default_cpu = Mac


#EXTRA EXAMPLE
class Parent:
      def __init__(self):
            self.cool = True

      def say_hi(self):
            print("hi")
class Child(Parent):
      def __init__(self): ## the child doesnt know what cool is without Super // without it child does possess cool
            super().__init__()
            pass

p = Parent()
c = Child()

print(p.cool)
print(c.cool)

## ABTRACTION ################################################
# we need to keep our code inside of our classes /// Keep it all under the hood

