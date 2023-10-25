import random

class BankAccount:

      allAccounts = []

      @staticmethod
      def can_withdraw(balance,amount):
            if (balance - amount) < 0:
                  return False
            else:
                  return True



      @classmethod
      def printAllAccountData(cls):
            for account in cls.allAccounts:
                  print(f'FIRST NAME ON ACCOUNT: {account.first_name_on_account}')
                  print(f'LAST NAME ON ACCOUNT: {account.last_name_on_account}')
                  print(f'CURRENT BALANCE: {account.balance}')
                  print(f'INTEREST RATE: {account.int_rate}\n')


      def __init__ (self, first_name_on_account, last_name_on_account, balance, int_rate, accountNumber):
            self.first_name_on_account = first_name_on_account
            self.last_name_on_account = last_name_on_account
            self.int_rate = int_rate
            self.balance = balance
            self.accountNumber = accountNumber
            BankAccount.allAccounts.append(self)

      def __repr__(self):
            return f"{self.first_name_on_account} {self.last_name_on_account}'s account, Account # {self.accountNumber}\n"


      # def deposit(self, amount_to_deposit, accountIndex):
      #       selectedAccount = account_list[accountIndex]
      #       self.balance += amount_to_deposit
      #       return self

      # def withdraw(self, amount_to_withdraw, accountIndex):
      #       if BankAccount.can_withdraw(self.balance, amount_to_withdraw):
      #             self.balance -= amount_to_withdraw
      #             print(f"Your new balance after withdrawal is: {self.balance}\n")
      #             return self
      #       else:
      #             print("Insufficent Funds: Charging a $5 Fee")
      #             self.balance -= 5
      #             self.balance -= amount_to_withdraw
      #             return self

      def display_account_info(self):
            print(f'ACCOUNT NUMBER: {self.accountNumber}')
            print(f'FIRST NAME ON ACCOUNT: {self.first_name_on_account}')
            print(f'LAST NAME ON ACCOUNT: {self.last_name_on_account}')
            print(f'CURRENT BALANCE: {self.balance}')
            print(f'INTEREST RATE: {self.int_rate}\n')
            return self

      def yield_interest(self):
            self.balance *= self.int_rate
            return self


class User(BankAccount):

      def __init__(self, fName, lName, email):
            self.fName = fName
            self.lName = lName
            self.email = email
            self.account_list = []

      def create_account(self,fName, lName, int_rate, balance): ## THIS METHOD WILL ALLOW USERS TO CREATE BankAccounts // fName
            accountNumber = random.randint(10230203123,1000002043005045)  ## this random number will fufill the accountNumber attribue of the bankAccount class - it will be an identifier number
            new_account = BankAccount(fName, lName, balance, int_rate, accountNumber) ## remember the outline we made for creating a bankAccount, we need a//  first_name_on_account // last_name_on_account // int_rate // balance // accountNumber // this fufills the constructor functions parameters
            self.account_list.append(new_account) ## this append simply adds this new account to the Users account list
            return self

      def deposit(self, amount_to_deposit, accountIndex):
            selectedAccount = self.account_list[accountIndex]
            selectedAccount.balance += amount_to_deposit
            return selectedAccount.balance

      def withdraw(self, amount_to_withdraw, accountIndex):
            selectedAccount = self.account_list[accountIndex]
            if selectedAccount.can_withdraw(selectedAccount.balance, amount_to_withdraw):
                  selectedAccount.balance -= amount_to_withdraw
                  print(f"Your new balance after withdrawal is: {selectedAccount.balance}\n")
                  return selectedAccount
            else:
                  print("Insufficent Funds: Charging a $5 Fee")
                  selectedAccount.balance -= 5
                  selectedAccount.balance -= amount_to_withdraw
                  return selectedAccount

      def display_account_balance(self, accountIndex):
            selectedAccount = self.account_list[accountIndex]
            print(f'${selectedAccount.balance} is your current balance.\n')

      def display_account_info(self, accountIndex):
            selectedAccount = self.account_list[accountIndex]
            selectedAccount.display_account_info()

alanWake1 = User('Alan', 'Wake', 'alanistheman@yahoo.com')
alanWake1.create_account("Alan", "Wake", .02, 5000)
alanWake1.create_account("Alan", "Wake", .02, 3000)
# print(alanWake1.account_list[0])
# print(alanWake1.account_list[1])
# print(alanWake1.account_list)
alanWake1.account_list[0].display_account_info()
alanWake1.account_list[1].display_account_info()
# print(alanWake1.account_list[1].display_account_info())
alanWake1.deposit(523,0)
alanWake1.account_list[0].display_account_info()
alanWake1.withdraw(523,0)
alanWake1.account_list[0].display_account_info()
alanWake1.display_account_balance(0)
alanWake1.display_account_info(0)









# user_list = [
#       {
#             "first_name": "Alan",
#             "last_name": "Wake",
#             "Accounts": ["<account1>","<account2>" "<account3>"],
#       },
#             {
#             "first_name": "Bob",
#             "last_name": "Anders",
#             "Accounts": ["<account1>","<account2>" "<account3>"],
#       },
#             {
#             "first_name": "Conner",
#             "last_name": "Tillman",
#             "Accounts": ["<account1>","<account2>" "<account3>"],
#       },
# ]