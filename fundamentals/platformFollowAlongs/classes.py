class User:
      # ! CONSTRUCTOR FUNCTION!!!  CREATES THE INSTANCE OF AN OBJECT
      def __init__(self, first_name, last_name, age):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age


      def greeting(self):
            print(f"Hello my name is {self.first_name}!")

      def conquest(self):
            print(f'I {self.first_name}, will conquer your lands!')
      def trueName(self):
            print(f'For those that have faced my blade in combat you know my true name! {self.last_name}')

achilles = User('Achilles', "Pitt", 0)
achilles.greeting()
brad_the_barbarian = User('Brad the Barbarian', "The Destroyer", 20)
brad_the_barbarian.conquest()
brad_the_barbarian.trueName()

class Shoe:
      def __init__(self, brand, shoe_type, price):
            self.brand = brand
            self.type = shoe_type
            self.price = price
            self.in_stock = True

      def priceReduction(self,percentOff):
            currentSalePercent = self.price * percentOff
            priceOnSale = self.price - currentSalePercent
            self.price =round(priceOnSale, 2)

      def couponApplication(self,couponPercent):
            currentCouponPercent = self.price *  couponPercent
            priceWithCoupon = self.price - currentCouponPercent
            self.price = round(priceWithCoupon, 2)

skater_shoe = Shoe('Vans', "Low-top Trainers", 40.55)
dress_shoe = Shoe("Jack and Jill Bootery", "Ballet Flats", 100.00)

print(skater_shoe.type)

print(dress_shoe.type + ' this is the attribute "type" of dress_shoes')

#the skater shoes gon on sale by 20% reduced price:
      # skater_shoe.priceReduction(0.20)
      # print(skater_shoe.price)
#the dress shoe goes on a sale by 10% reduced price:
dress_shoe.priceReduction(0.10)
print(dress_shoe.price)
#the skater shoes gets bought with a coupon for 10% on top of the existing 20%
skater_shoe.priceReduction(.20)
skater_shoe.couponApplication(.10)
print(skater_shoe.price)