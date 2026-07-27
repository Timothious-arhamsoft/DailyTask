# Task 2: Logging
import logging

# Task 4: Using DateTime
import datetime


class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance is Rs{balance}, attempted withdrawal is Rs{amount}.")


# Task 1: Type hints
class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.__balance = balance
    @property
    def balance(self) -> float:
        return self.__balance

    def __repr__(self) -> str:
        return f"BankAccount(owner = {self.owner}, balance = {self.__balance})"

    def __eq__(self, value) -> bool:
        return self.owner == value.owner and self.__balance == value.__balance

    def summary(self):
        return f"Current Account: {self.owner} has a {self.__balance}"

    def deposit(self,amount:str):
        self.__balance+=amount
        logging.info(f"{amount} deposited into {self.owner} account at {datetime.datetime.now()}.")
    def withdraw(self, amount: float):
        if amount> self.__balance:
            raise InsufficientFundsError(self.__balance, amount)

        self.__balance-= amount
        logging.info(f"{self.owner} has withdrawn {amount} at {datetime.datetime.now()}, now the balance is {self.__balance}.")


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float, interest_rate: float):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def __repr__(self) -> str:
         return super().__repr__() + \
               f", interest_rate={self.interest_rate}"

    def summary(self):
        return f"Total balance of {self.owner} Saving account is Rs{self.balance} and interest on it is {self.interest_rate}"

class Bank:
    def __int__(self):
        self.accounts: list[BankAccount] = []

    def add_account(self, account: BankAccount):
        self.accounts.append(account)

    def total_acc_balance(self):
        total:float = 0.0
        for acc in self.accounts:
            total+=acc.balance
        return f"Total Bank Balance is {total}."