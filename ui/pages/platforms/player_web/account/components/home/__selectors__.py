from ui.pages.locator import Selectors


class WalletSelectors:
    container = Selectors(default="div[datatestid='wc-wallet-balance']")
    balance = Selectors(data_test_id="wc-wallet-balance-amount-text")
    funds_added = Selectors(data_test_id="wc-wallet-balance-amount-text")
    winnings = Selectors(data_test_id="wc-wallet-balance-amount-text")
    withdrawal_requests = Selectors(data_test_id="wc-wallet-balance-amount-text")


class PlayOnSelectors:
    container = Selectors(default=".MuiPaper-elevation3")
    points = Selectors(default=".MuiTypography-subtitle1")
    points_this_month = Selectors(default="p.MuiTypography-body2")
    draw_entries = Selectors(default="p.MuiTypography-body2")
    second_chance = Selectors(default="p.MuiTypography-body2")