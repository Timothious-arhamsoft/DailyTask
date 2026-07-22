from expense_tracker import add_expense, Expense

def test_add_expense():
    result = add_expense(10, "food")
    # print(result[0])
    assert len(result) == 1
    assert result[0].amount == 10
    assert result[0].category == "food"

