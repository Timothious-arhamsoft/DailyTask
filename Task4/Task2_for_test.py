class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance is Rs{balance}, attempted withdrawal is Rs{amount}.")

def withdraw(balance, amount):
    if amount> balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount