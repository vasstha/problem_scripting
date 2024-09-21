from BankAccount import BankAccount
from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

if __name__ == '__main__':
    """
    # through base class
    baseAccount = BankAccount("John Doe")
    depositAmount = 500
    baseAccount.deposit(depositAmount)
    print(f"{depositAmount} deposited.")

    firstWithDrawAmount = 200
    print(f"first with drawAmount: {firstWithDrawAmount} started.")
    baseAccount.withdraw(firstWithDrawAmount)

    print(baseAccount.account_info())
    
    
    #through saving account
    savingAccount = SavingsAccount("John Doe")
    depositAmountThroughSaving = 500
    savingAccount.deposit(depositAmountThroughSaving)
    print(f"{depositAmountThroughSaving} deposited.")

    savingAccount.apply_interest()
    """
    checkingAccount = CheckingAccount("John Doe")
    depositAmountThroughChecking = 1000
    checkingAccount.deposit(depositAmountThroughChecking)
    print(f"{depositAmountThroughChecking} deposited.")

    firstWithDrawAmountThroughChecking = 999
    print(f"first with drawAmount: {firstWithDrawAmountThroughChecking} started.")
    checkingAccount.withdraw(firstWithDrawAmountThroughChecking)