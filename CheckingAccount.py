from BankAccount import BankAccount


class CheckingAccount(BankAccount):
    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.transaction_fee = 1  # Fixed $1 transaction fee for every withdrawal

    def withdraw(self, amount):
        total_withdrawal = amount + self.transaction_fee
        super().withdraw(total_withdrawal)