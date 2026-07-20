import pytest

from Task2_for_test import withdraw, InsufficientFundsError

@pytest.fixture
def starting_balance():
    return 1000



def test_withdraw_success(starting_balance):
    balance = withdraw(starting_balance, 300)

    assert balance == 700


def test_withdraw_failure(starting_balance):

    with pytest.raises(InsufficientFundsError):
        withdraw(starting_balance, 5000)