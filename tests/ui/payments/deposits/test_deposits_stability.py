from pytest import mark
from data_factory import create_credit_card

INITIAL_BALANCE = 50
DEPOSIT_AMOUNT = 1000


@mark.stability
def test_deposits_stability(player):
    credit_card = create_credit_card(card_type="Visa")

    player.ui.open()
    player.ui.authentication.login()

    balance = player.ui.account.get_balance()
    player.ui.payments.add_credit_card(card=credit_card, amount=INITIAL_BALANCE)
    transaction = player.ui.payments.get_transaction(amount=INITIAL_BALANCE)

    assert transaction["amount"] == INITIAL_BALANCE
    assert player.ui.account.get_balance() == balance + INITIAL_BALANCE

    player.ui.payments.make_deposit(card=credit_card, amount=DEPOSIT_AMOUNT)
    transaction = player.ui.payments.get_transaction(amount=DEPOSIT_AMOUNT)

    assert player.ui.account.get_balance() == balance + INITIAL_BALANCE + DEPOSIT_AMOUNT
    assert transaction["amount"] == DEPOSIT_AMOUNT

