class BankAccount:

    bankAccountsInfo = 0

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.bankAccountsInfo += 1

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self

    def yield_interest(self):
        self.balance += self.int_rate * self.balance
        return self

    @classmethod
    def printBankAccounts(cls):
        print(cls.bankAccountsInfo)

# account01 = BankAccount(0.2, 30000)
# account02 = BankAccount(0.15, 100000)

# account01.deposit(15000).deposit(20000).deposit(10000).withdraw(30000).yield_interest().display_account_info()
# account02.deposit(2500).deposit(3000).withdraw(1000).withdraw(1000).withdraw(500).withdraw(600).yield_interest().display_account_info()

# BankAccount.printBankAccounts()
