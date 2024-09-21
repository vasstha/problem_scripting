from BankAccount import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.interest_rate = 0.02  # Fixed 2% interest rate

    def apply_interest(self):
        self.balance *= (1 + self.interest_rate)
        print(f"Interest applied. New balance: {self.balance}")
