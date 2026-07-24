

# Task 1: Recreate Bank Account

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def __repr__(self):
        return f"BankAccount(owner={self.owner}, balance= {self.__balance})"

    def __eq__(self, value):
        return self.owner == value.owner and self.__balance == value.__balance


class SavingsAccount(BankAccount):
    def __int__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate



def main():
    # Check Task1
    acc1 = BankAccount("Tim", 5000)
    acc2 = BankAccount("Tim", 5000)

    print(acc1)
    print(acc1 == acc2)

if __name__ == "__main__":
    main()