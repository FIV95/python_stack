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


      def __init__ (self, first_name_on_account='', last_name_on_account='', balance=0, int_rate = .05, account_name=None):
            self.first_name_on_account = first_name_on_account
            self.last_name_on_account = last_name_on_account
            self.int_rate = int_rate
            self.balance = balance
            self.account_name = account_name
            BankAccount.allAccounts.append(self)

      def __str__(self):
            return self.account_name

      def deposit(self, amount_to_deposit):
            self.balance += amount_to_deposit
            return self

      def withdraw(self, amount_to_withdraw):
            if BankAccount.can_withdraw(self.balance, amount_to_withdraw):
                  self.balance -= amount_to_withdraw
                  print(f"Your new balance after withdrawal is: {self.balance}\n")
                  return self
            else:
                  print("Insufficent Funds: Charging a $5 Fee")
                  self.balance -= 5
                  self.balance -= amount_to_withdraw
                  return self

      # def display_account_info(self):
      #       print(f'FIRST NAME ON ACCOUNT: {self.first_name_on_account}')
      #       print(f'LAST NAME ON ACCOUNT: {self.last_name_on_account}')
      #       print(f'CURRENT BALANCE: {self.balance}')
      #       print(f'INTEREST RATE: {self.int_rate}')
      #       return self

      def yield_interest(self):
            self.balance *= self.int_rate
            return self

account1 = BankAccount(first_name_on_account='Alan',balance=5000, int_rate=.02)
account2 = BankAccount(first_name_on_account='Alan',balance=500, int_rate=.02)
account3 = BankAccount()
account4 = BankAccount()
account1.deposit(500).deposit(500).deposit(500).withdraw(5499)
account2.deposit(150).deposit(100).withdraw(100).withdraw(150).withdraw(400).withdraw(50).yield_interest()

# account1.printAllAccountData()

class User:

      def __init__(self, name, email, account):
            self.name = name
            self.email = email
            self.account = account
            self.account_list = []

      def create_account(self, int_rate=.02, balance=0):
            new_account = BankAccount(int_rate=int_rate,balance=balance)
            self.account_list.append(new_account)
            return self

      def __repr__(account):
            return ('account')

      def make_deposit(self, amount):
            self.account.balance += amount

      def make_withdrawl(self, amount):
            self.account.balance -= amount

      def display_user_balance(self):
            print(self.account.balance)

alanWake1 = User('Alan', 'alanistheman@yahoo.com', account1)
alanWake1.create_account(account1)
alanWake1.create_account(account2)