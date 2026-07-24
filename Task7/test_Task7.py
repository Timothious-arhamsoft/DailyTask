
from Task7 import BankAccount, SavingsAccount, Bank


def test_BankAccout():
    acc = BankAccount("Tim", 500) 
    assert acc.owner == 'Tim' and acc.balance == 500


def test_SavingsAccount():
    sav_acc= SavingsAccount("Tim_Gill", 500, 10)
    assert sav_acc.owner == "Tim_Gill" and sav_acc.balance == 500 and sav_acc.interest_rate == 10

def test_Bank_total():
    bank_accounts = Bank()
    bank_accounts.add_account(BankAccount("Tim", 500))
    bank_accounts.add_account(SavingsAccount("Tim_Gill", 500, 10))

    assert bank_accounts.total_assets() == 1000
    