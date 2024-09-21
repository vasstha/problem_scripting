class BankAccount:

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Remaining amount: {self.balance}")
        else:
            print("Insufficient funds")

    def account_info(self):
        return f'Account holder: {self.account_holder}, Balance: ${self.balance:.2f}'
