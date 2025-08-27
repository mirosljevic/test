from ui.pages.locator import Selectors


class CreditCardInfoSelectors:
    container = Selectors(data_test_id="vc-desposit-card-form")
    name_input = Selectors(data_test_id="vc-cardholder-name-input")
    card_input = Selectors(data_test_id="vc-card-number-input")
    expiry_input = Selectors(data_test_id="vc-expiration-date-input")
    cvv_input = Selectors(data_test_id="vc-cvv-input")

    deposit_container = Selectors(data_test_id="pay-add-funds")
    pay_amount_button = Selectors(data_test_id="pay-amount-button")
    amount_input = Selectors(data_test_id="pay-amount-input")
    bonus_code_link = Selectors(data_test_id="pay-bonus-code-button")
    pay_add_button = Selectors(data_test_id="pay-add-button")


class ConfirmationSelectors:
    container = Selectors(data_test_id="wc-confirmation-dialog")
    close_button = Selectors(default="[aria-label='Close confirmation dialog']")


class CreditCardItemSelectors:
    container = Selectors(default="[data-test-id='wc-payment-method-items'] > [data-test-id='wc-payment-method-item']")
    button = Selectors(default=".cc-card")


class AddCvvSelectors:
    container = Selectors(data_test_id="wc-cvv-modal")
    cvv_input = Selectors(data_test_id="cvv-input")
    confrim_button = Selectors(data_test_id="cvv-confirm-button")


class HighDepositSelectors:
    container = Selectors(data_test_id="wc-high-deposit-modal")
    confirm_button = Selectors(data_test_id="wc-high-deposit-confirm-button")