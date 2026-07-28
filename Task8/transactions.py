# Task 3: PathLib
# Task 4: DateTime

from pathlib import Path
import datetime
import json

# Task 5
import collections


class Transaction:
    def __init__(self, category: str, amount: float, timestamp: datetime.datetime = None):
        self.category = category
        self.amount = amount
        self.timestamp = timestamp or datetime.datetime.now()

    def __repr__(self) -> str:
        return f"Transaction(category={self.category}, amount={self.amount}, timestamp={self.timestamp})"

    def to_dict(self) -> dict:
        return {
            "category": self.category,
            "amount": self.amount,
            "timestamp": self.timestamp.isoformat(),  
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Transaction":
        return cls(
            category=data["category"],
            amount=data["amount"],
            timestamp=datetime.datetime.fromisoformat(data["timestamp"]), 
        )


def save_transactions(path, transactions: list[Transaction]) -> None:
    base = Path(__file__).parent
    path = base / Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        json.dump([t.to_dict() for t in transactions], f, indent=2)


def load_transactions(path) -> list[Transaction]:
    base = Path(__file__).parent
    path = base / Path(path)
    if not path.exists():
        return []
    data = json.loads(path.read_text())
    return [Transaction.from_dict(item) for item in data]


def transactions_today(transactions: list[Transaction]) -> list[Transaction]:
    today = datetime.datetime.now().date()
    return [t for t in transactions if t.timestamp.date() == today]

def tally_by_category(transactions: list[Transaction]) -> collections.Counter:
    return collections.Counter(t.category for t in transactions)


def group_amounts_by_category(transactions: list[Transaction]) -> collections.defaultdict:
    grouped: collections.defaultdict[str, list] = collections.defaultdict(list)
    for t in transactions:
        grouped[t.category].append(t.amount)
    return grouped


def main():
    print("\n-> Task 3/4: save/load transactions with real datetime objects")
    sample = [
        Transaction("groceries", 45.5),
        Transaction("rent", 1200.0),
        Transaction("rent", 1200.0),
        Transaction("rent", 1400.0),
    ]
    save_transactions("data/transactions.json", sample)
    loaded = load_transactions("data/transactions.json")
    print(loaded)

    print("\n-> Task 4: transactions_today")
    print(transactions_today(loaded))

    print("\n-> Task 5: Counter and defaultdict")
    print(tally_by_category(loaded))
    print(dict(group_amounts_by_category(loaded)))


if __name__ == "__main__":
    main()