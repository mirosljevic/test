from ui.pages.locator import Selectors


class TransactionItemSelectors:
    container = Selectors(data_test_id="wc-transaction-history-history-item")
    view_button = Selectors(data_test_id="wc-transaction-history-view-button")


class TransactionSummarySelectors:
    container = Selectors(data_test_id="wc-transaction-history-modal")
    item = Selectors(data_test_id="wc-list-item-name-text")
    close_button = Selectors(data_test_id="wc-transaction-history-modal-close-button")