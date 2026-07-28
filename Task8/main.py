import logging

from logger_config import setup_logging

from Task8 import (BankAccount, SavingsAccount, Bank, InsufficientFundsError)

from transactions import (Transaction, save_transactions, load_transactions, transactions_today, tally_by_category, group_amounts_by_category)


setup_logging()

logger = logging.getLogger(__name__)

# Task 6
def main():

    logger.info("Bank application started")

    account = BankAccount("Tim", 5000)

    account.deposit(200)

    try:
        account.withdraw(1000000)

    except InsufficientFundsError as e:
        logger.error("Withdrawal failed: %s",e)

    try:
        account.deposit("fifty")
    except TypeError as e:
        logger.error(e)


    bank = Bank()

    bank.add_account(account)

    bank.add_account(SavingsAccount("Tim2", 10000, 5))

    logger.info("Total bank balance: %s", bank.total_acc_balance())

    transactions = [Transaction("food", 50), Transaction("rent", 1200)]

    save_transactions("data/transactions.json", transactions)

    loaded = load_transactions("data/transactions.json")

    print(loaded)

    print(transactions_today(loaded))

    print(tally_by_category(loaded))

    print(dict(group_amounts_by_category(loaded)))


if __name__ == "__main__":
    main()
