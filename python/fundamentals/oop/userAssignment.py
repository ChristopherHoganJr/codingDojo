class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f'First name: {self.first_name}')
        print(f'Last name: {self.last_name}')
        print(f'Email: {self.email}')
        print(f'Is rewards member: {self.is_rewards_member}')
        print(f'Gold card points: {self.gold_card_points}')
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print('User is already a member.')
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self
        

    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("You don't have enough points")
        return self

chris = User('chris','hogan','ch@asdf.com', 32)
chris.display_info().enroll().spend_points(50).display_info()
batman = User('bruce','wayne','batman@dc.com', 48)
superman = User('clark','kent','superman@dc.com', 80)
batman.enroll().spend_points(80).display_info()
superman.display_info()