

# Task 1: Recreate Bank Account

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def __repr__(self):
        return f"BankAccount(owner={self.owner}, balance= {self.__balance})"

    def __eq__(self, value):
        return self.owner == value.owner and self.__balance == value.__balance



