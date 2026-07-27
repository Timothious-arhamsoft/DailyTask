from Task8 import BankAccount

def test_account_creation():
    acc = BankAccount("Tim", 50000)
    assert acc.owner == "Tim"
    assert acc.Balance == 50000

def test_deposit():
    acc = BankAccount("Tim", 5000)
    acc.deposit(1000)

    assert acc.balance == 6000