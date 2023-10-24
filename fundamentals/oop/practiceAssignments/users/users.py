class User:
      def __init__(self, first_name, last_name, email, age, _is_rewards_member, gold_card_points = 0):
            # These are my attributes for User
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.age = age
            self._is_rewards_member = False
            self.gold_card_points = gold_card_points
            if _is_rewards_member :
                  self.enroll()
            # These are my methods for User
      def user_info(self):
            print(f"First Name: {self.first_name}")
            print(f"Last Name: {self.last_name}")
            print(f"Email: {self.email}")
            print(f"Age: {self.age}")
            print(f"Reward Member: {self._is_rewards_member}")
            print(f"Gold Card Points: {self.gold_card_points}\n")

      def enroll(self):
            # check if user is already rewards member
            if self._is_rewards_member == True:
                  print('User already a member\n')

            else:
                  self.gold_card_points += 200
                  print(f'Thank you for being a member! Your current reward point total is {self.gold_card_points}\n')
                  self._is_rewards_member = True

      def spend_points(self,decrease_amount):
            if self.gold_card_points > decrease_amount:
                  self.gold_card_points = self.gold_card_points - decrease_amount
            else:
                  print('Insufficient Points to complete transacation.\n')


user1 = User('Leon', 'Kennedy', 'leonK@rcpd.net', 27, False)
user1.user_info()
user1.enroll()

user2 = User('Gordon', 'Freeman', 'freemanly@blkmesa.org', 40, False)
user2.enroll()
user3 = User('Lara', 'Croft', 'croftManorrequests.net', 34, True)

user1.spend_points(50)
user1.user_info()
user2.spend_points(80)
user2.user_info()

# bonus step:
user1.enroll()
user3.spend_points(30)


# Test step
user3.user_info()