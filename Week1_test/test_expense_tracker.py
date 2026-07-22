from Week1_test.expense_tracker.expense_tracker import add_expense

def test_add_expense():
    result = add_expense(10, "food")
    assert result