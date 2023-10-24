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
            return self

      def enroll(self):
            # check if user is already rewards member
            if self._is_rewards_member == True:
                  print('User already a member\n')
                  return self

            else:
                  self.gold_card_points += 200
                  print(f'Thank you for being a member! Your current reward point total is {self.gold_card_points}\n')
                  self._is_rewards_member = True
                  return self

      def spend_points(self,decrease_amount):
            if self.gold_card_points > decrease_amount:
                  self.gold_card_points = self.gold_card_points - decrease_amount
                  return self
            else:
                  print('Insufficient Points to complete transacation.\n')
                  return self


user1 = User('Leon', 'Kennedy', 'leonK@rcpd.net', 27, False)
user1.user_info().enroll().spend_points(50).user_info().enroll()


user2 = User('Gordon', 'Freeman', 'freemanly@blkmesa.org', 40, False)
user2.enroll().spend_points(80).user_info()
user3 = User('Lara', 'Croft', 'croftManorrequests.net', 34, True)

user3.spend_points(30).user_info()


# Test step - we made her member status = True so she started with 200 points
# user3.user_info()