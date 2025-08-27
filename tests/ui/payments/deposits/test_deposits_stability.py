from pytest import mark
from data_factory import create_credit_card

INITIAL_BALANCE = 50
DEPOSIT_AMOUNT = 1000


@mark.stability
@mark.deposits
def test_deposits_stability():
    pass

