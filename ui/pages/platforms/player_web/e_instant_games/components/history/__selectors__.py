from ui.pages.locator import Selectors


class HistoryItemSelectors:
    container = Selectors(data_test_id="wc-transaction-history-history-item")
    view_button = Selectors(data_test_id="wc-transaction-history-view-button")


class PlaySummarySelectors:
    container = Selectors(data_test_id="wc-play-history-modal")
    play_text = Selectors(data_test_id="wc-play-history-amount-text")
    win_text = Selectors(data_test_id="wc-play-history-win-text")
    ticket_id_text = Selectors(data_test_id="wc-play-history-ticket-id-text")
    close_button = Selectors(default="button[aria-label='Close transaction details dialog']")
