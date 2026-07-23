# Task 3:  Created the Custom the Exception

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance is Rs{balance}, attempted withdrawal is Rs{amount}.")

# Task 1: Created the Bankaccount

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        # Task 4: Task mangling
        self._balance = balance

        if self._balance<0:
            raise ValueError("Balance cannot be negative!")
    def __repr__(self):
        return f"BankAccount(owner= {self.owner}, balance= {self._balance})"
    
    def __eq__(self, other):
        return self.owner == other.owner and self._balance == other._balance
    #Task 3:  
    def withdraw(self,amount):
        if amount> self._balance:
            raise InsufficientFundsError(self._balance, amount)
        else:
            self._balance -= amount
            return f"Your reamining balance is {self._balance}"
    def show(self):
        return f"Current Balance is {self._balance}"



# Task 5: Data Class Comparison:
'''
from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    balance: int


-> As in data class we can't check the Exception Error
'''

account1 = BankAccount("Tim", 100)
account2 = BankAccount("Gill", 200)
# Task 2: Prove self is just a parameter
print(account1.show())
print(BankAccount.show(account1))

# Checking Equality
print(account2)
print(account1 == account2)


