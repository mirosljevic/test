from pytest import mark
from data_factory import create_bank_account

WITHDRAWAL_AMOUNT = 20


@mark.stability
def test_withdrawals_stability(player, risk_analyst):
    bank_account = create_bank_account()

    player.ui.open()
    player.ui.authentication.login()

    initial_balance = player.ui.account.get_balance()
    player.ui.payments.add_bank_account(bank_account=bank_account)

    player.ui.documents.upload(document_type="Financial Account Document")
    risk_analyst.api.workflows.approve_bank_account()

    player.ui.payments.make_withdrawal(bank_account=bank_account, amount=WITHDRAWAL_AMOUNT)
    transaction = player.ui.payments.get_transaction(amount=WITHDRAWAL_AMOUNT)

    balance = player.ui.account.get_balance()
    assert balance == initial_balance - WITHDRAWAL_AMOUNT
    assert transaction["amount"] == WITHDRAWAL_AMOUNT
