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
        # Task 4: name mangling
        self.__balance = balance

        if self.__balance<0:
            raise ValueError("Balance cannot be negative!")
    def __repr__(self):
        return f"BankAccount(owner= {self.owner}, balance= {self.__balance})"
    
    def __eq__(self, other):
        return self.owner == other.owner and self.__balance == other.__balance
    #Task 3:  
    def withdraw(self,amount):
        if amount> self.__balance:
            raise InsufficientFundsError(self.__balance, amount)
        else:
            self.__balance -= amount
            return f"Your remaining balance is {self.__balance}"
    def show(self):
        return f"Current Balance is {self.__balance}"

class SpecialAccount(BankAccount):
    def __init__(self, owner, balance, bonus):
        super().__init__(owner, balance)
        self.__balance = balance + bonus 

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

# Task 4: Name Mangling
'''
Name mangling stops a subclass's __balance from silently overwriting the parent.
'''
s = SpecialAccount("Tim", 100, 10)
print(vars(s))

# Checking Equality
print(account2)
print(account1 == account2)

# Checking Withdraw
account1.withdraw(50)
print(account1.show())

try:
    account1.withdraw(1000)
except InsufficientFundsError as e:
    print(e)


