import pytest

from Task2_for_test import withdraw, InsufficientFundsError


def test_withdraw_success():
    balance = withdraw(1000, 300)

    assert balance == 700


def test_withdraw_failure():

    with pytest.raises(InsufficientFundsError):
        withdraw(1000, 5000)