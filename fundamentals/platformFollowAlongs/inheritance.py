#WE WANT TO AVOID THIS - WE CAN AVOID THIS BY USING INHERITANCE


# class CheckingAccount:
#     def __init__(self, int_rate, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#     def deposit(self, amount):
#     	# code
#     def withdraw(self, amount):
#     	# code
#     def write_check(self, amount):
#     	# code
#     def display_account_info(self):
#     	# code

# class RetirementAccount:
#     def __init__(self, int_rate, is_roth, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#     	self.is_roth = is_roth
#     def deposit(self, amount):
#     	# code - assess tax if necessary
#     def withdraw(self, amount):
#     	# code - assess penalty if necessary
#     def display_account_info(self):
#     	# code


# class CheckingAccount(BankAccount)
#       pass
# class Retirement(BankAccount):
#       pass

class BankAccount:
      def __init__(self, int_rate, balance = 0):
            self.int_rate = int_rate
            self.balance = balance
      def withdraw(self, amount):
            if (self.balance - amount) > 0:
                  self.balance -= amount
            else:
                  print("INSUFFICIENT FUNDS")
            return self

class RetirementAccount(BankAccount):
      def __init__(self, int_rate, is_roth, balance=0 ):
            super().__init__(int_rate, balance)
            self.is_roth = is_roth
      def withdraw(self, amount, is_early):
            if is_early:
                  amount = amount * 1.10
            super().withdraw(amount)
            return self

