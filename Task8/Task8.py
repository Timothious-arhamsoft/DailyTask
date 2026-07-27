# Task 2: Logging
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


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
        if not isinstance(value, BankAccount):
            return NotImplemented
        return self.owner == value.owner and self.__balance == value.__balance

    def summary(self):
        return f"Current Account: {self.owner} has a {self.__balance}"

    def deposit(self,amount:float):
        self.__balance+=amount
        logger.info("%s deposited into %s account now balance is %s.", amount, self.owner, self.__balance)

    def withdraw(self, amount: float):
        if amount> self.__balance:
            logger.warning("Withdrawl of %s rejected as balance is %s", amount, self.__balance)
            raise InsufficientFundsError(self.__balance, amount)

        self.__balance-= amount
        logger.info("%s has withdrawn %s, now the balance is %s.", self.owner, amount, self.__balance)


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
    def __init__(self):
        self.accounts: list[BankAccount] = []

    def add_account(self, account: BankAccount):
        self.accounts.append(account)

    def total_acc_balance(self):
        total:float = 0.0
        for acc in self.accounts:
            total+=acc.balance
        return f"Total Bank Balance is {total}."

def main():
    print("-> Deposit (should log INFO)")
    acc = BankAccount("Tim", 5000)
    acc.deposit(200)
 
    print("\n-> Withdraw too much (should log WARNING, then raise)")
    try:
        acc.withdraw(999999)
    except InsufficientFundsError as e:
        logger.error("Withdrawal failed and was caught in main: %s", e)
 
    print("\n-> Successful withdraw (should log INFO)")
    acc.withdraw(100)
 
    print("\n-> Bank total")
    bank = Bank()
    bank.add_account(acc)
    sav = SavingsAccount("Asha", 10000, 5)
    bank.add_account(sav)
    print(bank.total_acc_balance())
 
    print("\n-> repr / eq / summary checks")
    print(acc)
    print(sav)
    print(acc == BankAccount("Tim", acc.balance))  
    # print(acc == "Tim") 
    print(acc.summary())
    print(sav.summary())

if __name__ == "__main__":
    main()