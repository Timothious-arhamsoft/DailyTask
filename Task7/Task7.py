

# Task 1: Recreate Bank Account

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    # This decrator help to act as a getter
    def balance(self):
        return self.__balance
    def __repr__(self):
        return f"BankAccount(owner={self.owner}, balance= {self.__balance})"

    def __eq__(self, value):
        return self.owner == value.owner and self.__balance == value.__balance
    # Task 4: Polymorphism
    def summary(self):
        return f"Total balance of {self.owner} Curent account is Rs{self.__balance}"

# Task 2: Inheritance
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        
    # Task 3: Extending the __repr__() method 
    def __repr__(self):
        return super().__repr__() + f", interest_rate= {self.interest_rate}"
    # Task 4: Polymorphism
    def summary(self):
        return f"Total balance of {self.owner} Saving account is Rs{self.balance} and interest on it is {self.interest_rate}"

def main():
    # Check Task1
    acc1 = BankAccount("Tim", 5000)
    acc2 = BankAccount("Tim", 5000)

    print(acc1)
    print(acc1 == acc2)

    # Check Task2
    sav_acc = SavingsAccount("Tim", 10000, 5)
    print(sav_acc.owner)
    print(sav_acc.balance)
    print(sav_acc.interest_rate)

    # Check Task3
    print(sav_acc)

    # check Task 4: Polymorphism
    acc_list = []
    acc_list.append(acc1)
    acc_list.append(sav_acc)

    for i in acc_list:
        print(i.summary())

if __name__ == "__main__":
    main()