from pytest import mark
from data_factory import create_bank_account

WITHDRAWAL_AMOUNT = 20


@mark.stability
@mark.withdrawals
def test_withdrawals_stability():
    pass
