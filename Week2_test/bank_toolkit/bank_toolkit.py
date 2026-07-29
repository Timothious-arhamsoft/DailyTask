"""Week 2 Assessment — Bank Toolkit.

Implement every method/function below. Keep every signature exactly as given.
Use logging (not print) wherever a docstring says to log something.
"""
from __future__ import annotations

import asyncio
import json
import logging
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from typing import Callable

logger = logging.getLogger(__name__)


class InsufficientFundsError(Exception):
    """Raised when a withdrawal would exceed the account balance."""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        """Raise ValueError if balance is negative."""
        # Done
        if balance<0:
            raise ValueError("Balance must not be negative.")

        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Raise ValueError if amount is not positive (zero or negative).
        On success, increase the balance and log an INFO-level message.
        """
        # DONE
        if amount<=0:
            raise ValueError("Deposit must be positive.")
        
        self.balance+=amount
        logger.info(f"{self.owner} deposited {amount}")

    def withdraw(self, amount: float) -> None:
        """If amount exceeds the current balance: log a WARNING-level message
        that mentions the account has insufficient funds, then raise
        InsufficientFundsError. The balance must be unchanged when this
        happens. On success, decrease the balance and log an INFO-level
        message.
        """
        # DONE
        if amount> self.balance:
            logger.warning(f"Your requested amount {amount} is more than your current balance which is {self.balance}")
            raise InsufficientFundsError("Your Balance is Low")
            
        self.balance-=amount
        logger.info(f"Sucessfully withdrawl {amount}, now current balance is {self.balance}")

    def __repr__(self) -> str:
        """Must include the owner and the balance in the string."""
        # Done
        return f"BankAccount(owner={self.owner}, balance={self.balance})"

    def __eq__(self, other: object) -> bool:
        """Two BankAccounts are equal if owner and balance both match."""
        # Done
        return self.owner == other.owner and self.balance == other.balance


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.0) -> None:
        """Must call the parent's __init__ (via super()) rather than
        reimplementing balance validation — a negative starting balance must
        still be rejected the same way it is for a plain BankAccount.
        """
        # Done
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        """balance += balance * interest_rate."""
        # Done
        int_rate = self.balance * self.interest_rate
        self.balance+=int_rate

    def __repr__(self) -> str:
        """Must extend (not fully rewrite) the parent's __repr__ — start from
        super().__repr__() and add the interest rate to it.
        """
        # Done
        return super().__repr__() + \
               f", interest_rate={self.interest_rate}"


class Bank:
    def __init__(self) -> None:
        # Done
        self.accounts: list[BankAccount] = []

    def add_account(self, account: BankAccount) -> None:
        # Done
        self.accounts.append(account)

    def total_assets(self) -> float:
        """Sum of every held account's balance."""
        # Done
        return sum(account.balance for account in self.accounts)

    def summary_by_owner(self) -> dict[str, float]:
        """Map each owner name to their total balance across every account
        they hold — an owner may have more than one account.
        """
        # Done
        summary = defaultdict(float)
        for account in self.accounts:
            summary[account.owner]+=account.balance
        return dict(summary)

# Helping Function
def to_dict(account:BankAccount):
    data = {
        "type" : "SavingsAccount" if isinstance(account, SavingsAccount) else "BankAccount",
        "owner" : account.owner,
        "balance" : account.balance
    }
    if isinstance(account, SavingsAccount):
        data["interest_rate"] = account.interest_rate
    return data


def save_accounts(path: Path, accounts: list[BankAccount]) -> None:
    """Write accounts as JSON to path (create parent directories if needed).
    Each entry must carry enough information to reconstruct the correct
    class later — include a "type" field ("BankAccount" or "SavingsAccount")
    plus owner/balance/interest_rate as applicable.
    """
    base = Path(__file__).parent
    path = base / Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = [to_dict(account) for account in accounts]
    with path.open("w") as f:
        json.dump(data, f)


def load_accounts(path: Path) -> list[BankAccount]:
    """Read accounts back from JSON at path, reconstructing each as the
    correct class based on its "type" field. If the file doesn't exist, let
    FileNotFoundError propagate — do not swallow it.
    """
    # Done
    base = Path(__file__).parent
    path = base / Path(path)
    with path.open("r") as f:
        data = json.load(f)

    accounts: list[BankAccount] =  []
    for i in data:
        if i.get("type")=="SavingsAccount":
            accounts.append(
                SavingsAccount(
                    i["owner"],
                    i["balance"],
                    i.get("interest_rate", 0.0),
                )
            )
        else:
            accounts.append(BankAccount(i["owner"], i["balance"]))
    return accounts


def count_by_type(accounts: list[BankAccount]) -> Counter:
    """Counter mapping class name to how many accounts of that type are in
    the list.
    """
    # Done
    return Counter(type(account).__name__ for account in accounts)



def is_business_hours(dt: datetime) -> bool:
    """True if dt falls on a weekday (Monday-Friday) between 9:00 (inclusive)
    and 17:00 (exclusive) — hour 9 through hour 16 count, hour 17 does not.
    """
    # Done
    return dt.weekday() < 5 and 9<=dt.hour<17


def apply_interest_to_all(accounts: list[SavingsAccount]) -> None:
    """Apply interest to every account in the list, using a
    ThreadPoolExecutor to do it — the same tool this week's threading kata
    used, applied here for real.
    """
    # Done
    with ThreadPoolExecutor() as executor:
        list(executor.map(lambda account: account.apply_interest(), accounts))
  


def fetch_rates_concurrently(symbols: list[str], fetch_fn: Callable[[str], float]) -> dict[str, float]:
    """For each symbol, call fetch_fn(symbol) to get its rate. Use a
    ThreadPoolExecutor so the calls run concurrently rather than one at a
    time — fetch_fn stands in for a slow network call (this keeps the
    assessment from needing a real network request). If fetch_fn raises for
    a given symbol, log a warning and exclude that symbol from the result —
    one failure must not crash the whole batch.
    """
    # Done
    results = {}
    with ThreadPoolExecutor() as executor:
        future_to_symbol = {executor.submit(fetch_fn, symbol): symbol for symbol in symbols}
        for i in future_to_symbol:
            symbol = future_to_symbol[i]
            try:
                results[symbol] = i.result()
            except Exception as e:
                logger.warning("Failed to fetch rate for %s: %s", symbol, e)
    return results


async def apply_interest_async(accounts: list[SavingsAccount]) -> None:
    """For every account: await asyncio.sleep(0.05) to simulate a brief async
    confirmation step, then call apply_interest() on it. Run every account's
    confirmation concurrently using asyncio.gather — not a sequential loop.
    """
    # TODO
    raise NotImplementedError


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s"
    )


    file_name = Path("data/accounts.json")


    account = BankAccount("Tim", 1000)
    account.deposit(500)
    try:
        account.withdraw(300)
    except InsufficientFundsError as e:
        logger.warning(e)

    bank = Bank()
    bank.add_account(account)

    print("Bank Accounts:")
    print(bank.accounts)

    print("\nTotal Assets:")
    print(bank.total_assets())

    print("\nSummary by Owner:")
    print(bank.summary_by_owner())

    # Save 
    save_accounts(file_name, bank.accounts)
    print(f"\nAccounts saved to {file_name}")

    # Load 
    loaded_accounts = load_accounts(file_name)
    print("\nLoaded Accounts:")
    for acc in loaded_accounts:
        print(acc)

    # Count account types
    print("\nCount by Type:")
    print(count_by_type(loaded_accounts))

    sv_accounts = [
    SavingsAccount("Tim", 1000, 0.10),
    SavingsAccount("Alice", 2000, 0.05),
    SavingsAccount("Bob", 500, 0.20),
    ]

    print("Before:")
    for sv_acc in sv_accounts:
        print(sv_acc)
    apply_interest_to_all(sv_accounts)
    print("After:")
    for sv_acc in sv_accounts:
        print(sv_acc)

    

if __name__ == "__main__":
    main()