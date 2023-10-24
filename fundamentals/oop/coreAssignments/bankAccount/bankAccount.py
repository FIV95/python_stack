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


      def __init__ (self, first_name_on_account, last_name_on_account, balance, int_rate = .05):
            self.first_name_on_account = first_name_on_account
            self.last_name_on_account = last_name_on_account
            self.int_rate = int_rate
            self.balance = balance
            BankAccount.allAccounts.append(self)


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

account1 = BankAccount("Charles", "Martel", 4000)
account2 = BankAccount("El", "Cid", 500)
account1.deposit(500).deposit(500).deposit(500).withdraw(5499)
account2.deposit(150).deposit(100).withdraw(100).withdraw(150).withdraw(400).withdraw(50).yield_interest()

account1.printAllAccountData()
