from expense_tracker import add_expense, iter_expenses, total_of

def test_add_expense():
    result = add_expense(10, "food")
    # print(result[0])
    assert len(result) == 1
    assert result[0].amount == 10
    assert result[0].category == "food"



def test_iter_expenses():
    expenses = []
    expenses = add_expense(40, "food", expenses)
    expenses = add_expense(60, "transport", expenses)

    total_expense = iter_expenses(expenses)

    assert next(total_expense).amount == 40
    assert next(total_expense).amount == 60


def test_total_of():
    expenses = []
    expenses= add_expense(10, "food", expenses)
    expenses = add_expense(50, "transport", expenses)
    expenses = add_expense(60, "electricity", expenses)

    total_expense = iter_expenses(expenses)
    result = total_of(total_expense)
    # print(expenses)
    # print(result)
    assert result == 120


