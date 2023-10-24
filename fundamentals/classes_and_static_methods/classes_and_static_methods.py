# class User:
#       # ! Class Attribute
#       population = 0

#       @classmethod
#       def user_population(cls):
#             print(f'{cls.population} users in the program')

#       @staticmethod
#       def validate_age(age):
#             is_valid = True
#             if age < 18:
#                   is_valid = False
#             return is_valid

#       def __init__(self, first_name, last_name, age):
#             self.first_name = first_name
#             self.last_name = last_name
#             self.age = age
#             User.population += 1

#       def greeting(self):
#             print(f'Hello my name is {self.first_name}!')

# adrien = User("Adrien", "Dion", 39)
# Benny = User("Benny Bob", "Mcbob", 39)
# Shadow = User("Shadow", "McShadow", 5)
# adrien.greeting()

# User.user_population()

class BankAccount:
      #Delcaring a class attribute
      #This is shared among all bank Accounts
      bank_name = "First National Dojo"

      #new class attribute - a list of all the account!
      all_accounts = []

      #class method to change the name of the bank
      @classmethod
      def change_bank_name(cls,name):
            cls.bank_name = name

      #class method to get the balance of all accounts
      @classmethod
      def all_balances(cls):
            sum = 0
            for account in cls.all_accounts:
                  sum += account.balance
            return sum

      @staticmethod
      def can_withdraw(balance,amount):
            if (balance - amount) < 0:
                  return False
            else:
                  return True


      def __init__ (self, int_rate, balance):
            self.int_rate = int_rate
            self.balance = balance
            BankAccount.all_accounts.append(self)

      def with_draw(self,amount):
            #we can use the static method here to evaluate
            #if we can withrdaw the funds without going negative
            if BankAccount.can_withdraw(self.balance.amount):
                  self.balance -= amount
            else:
                  print('Insufficient Funds')
            return self


franksAccount = BankAccount(.05, 1000000)
nellysAccount = BankAccount(.1, 100000000)

print(franksAccount.bank_name)