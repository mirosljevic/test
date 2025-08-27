from ui.pages.locator import Selectors


class BonusTabSelectors:
    container = Selectors(data_test_id="wc-bonus-tabs")
    tab = Selectors(default="button")


class BonusCardSelectors:
    container = Selectors(data_test_id="wc-bonus-item")
    status = Selectors(data_test_id="wc-bonus-status-text")
    bonus_id = Selectors(data_test_id="wc-bonus-id-text")
    bonus_type = Selectors(data_test_id="wc-bonus-type-text")
    bonus_games = Selectors(data_test_id="wc-bonus-games-text")
    bonus_amount = Selectors(data_test_id="wc-bonus-amount-text")
