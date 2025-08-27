from ui.pages.locator import Selectors


class BankAccountInfoSelectors:
    container = Selectors(default="form.cc-form")
    account_type_input = Selectors(default="#accountType")
    account_number_input = Selectors(data_test_id="vc-account-number-input")
    routing_number_input = Selectors(data_test_id="vc-routing-number-input")
    bank_transfer_button = Selectors(data_test_id="vc-bank-transfer-button")


class WithdrawalSelectors:
    container = Selectors(data_test_id="vc-withdraw")
    amount_input = Selectors(data_test_id="vc-withdraw-input")
    withdraw_button = Selectors(data_test_id="vc-withdraw-button")
    confirmation_dialog = Selectors(data_test_id="wc-withdraw-confirm-modal")
    close_confirmation_button = Selectors(data_test_id="confirm-button")
