from ui.pages.locator import Selectors


class PaymentMethodsSelectors:
    add_payment_method_button = Selectors(data_test_id="wc-add-withdraw-method-button")
    add_withdraw_method_button = Selectors(data_test_id="wc-add-withdraw-method-button")
    empty_state_button = Selectors(data_test_id="wc-empty-state-button")


class AddFundsSelectors:
    container = Selectors(data_test_id="i-lottery-add-funds")
    pay_amount_button = Selectors(data_test_id="pay-amount-button")
    amount_input = Selectors(data_test_id="pay-amount-input")
    pay_add_button = Selectors(data_test_id="pay-add-button")


class TransactionHistorySelectors:
    filter_inputs = Selectors(default=".transaction-filters input")
