from bankAccountAssignment import BankAccount

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.accounts = {}

    def create_new_account(self):
        counter = len(self.accounts) + 1
        globals()[f'Bank Account {counter}'] = BankAccount(1,100)
        self.accounts[f'Account {counter}'] = globals()[f'Bank Account {counter}']
        return self

    def make_deposit(self, amount):
        if len(self.accounts) < 1:
            print('You can not deposit money until you make an account.')
        else:
            print('There is no 0 index')
            accountAccess = input(f'You have {len(self.accounts)} accounts. Which index account would you like to access?: ')
            self.accounts[f'Account {accountAccess}'] = self.accounts[f'Account {accountAccess}'].deposit(amount)
        return self

    def make_withdrawal(self,amount):
        if len(self.accounts) < 1:
            print('You can not withdraw money until you make an account.')
        else:
            print('There is no 0 index')
            accountAccess = input(f'You have {len(self.accounts)} accounts. Which index account would you like to access?: ')
            self.accounts[f'Account {accountAccess}'] = self.accounts[f'Account {accountAccess}'].withdraw(amount)
        return self

    def display_user_balance(self):
        print('There is no 0 index')
        accountAccess = input(f'You have {len(self.accounts)} accounts. Which index account would you like to access?: ')
        print(self.accounts[f'Account {accountAccess}'].balance)

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

    def transfer_money(self, amount, other_user):
        print('There is no 0 index')
        selfAccess = input(f'You have {len(self.accounts)}. Which index account would you like to transfer money from?: ')
        otherAccess = input(f'{other_user.first_name} has {len(other_user.accounts)} accounts. Which index account would you like to transfer money into?: ')
        self.accounts[f'Account {selfAccess}'].withdraw(amount)
        other_user.accounts[f'Account {otherAccess}'].deposit(amount)

chris = User('chris','hogan','ch@asdf.com', 32)
batman = User('bruce','wayne','batman@dc.com',35)
chris.create_new_account().create_new_account().create_new_account().make_deposit(50).display_user_balance()
batman.create_new_account().create_new_account().create_new_account().make_deposit(50).display_user_balance()

chris.transfer_money(150,batman)

chris.display_user_balance()
batman.display_user_balance()
# chris.display_info().enroll().spend_points(50).display_info()
# batman = User('bruce','wayne','batman@dc.com', 48)
# superman = User('clark','kent','superman@dc.com', 80)
# batman.enroll().spend_points(80).display_info()
# superman.display_info()