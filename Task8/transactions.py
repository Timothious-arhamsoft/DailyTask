# Task 3: PathLib

from pathlib import Path
import json

def save_transactions(path, transactions):
    base = Path(__file__).parent
    path = base / Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)  
    with path.open("w") as f:
        json.dump(transactions, f, indent=2)


def load_transactions(path):
    base = Path(__file__).parent
    path = base / Path(path)
    if not path.exists():
        return []
    return json.loads(path.read_text())

def main():
    print("\n-> Task 3: save/load transactions")
    sample = [
        {"category": "groceries", "amount": 45.5, "timestamp": "2026-07-27T10:15:00"},
        {"category": "rent", "amount": 1200.0, "timestamp": "2026-07-27T10:16:00"},
        {"category": "rent", "amount": 1200.0, "timestamp": "2026-07-27T10:16:00"},
        {"category": "rent", "amount": 1400.0, "timestamp": "2026-07-27T10:16:00"}
    ]
    save_transactions("data/transactions.json", sample)
    loaded = load_transactions("data/transactions.json")
    print(loaded)

if __name__ == "__main__":
    main()