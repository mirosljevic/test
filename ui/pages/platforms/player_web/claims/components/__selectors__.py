from ui.pages.locator import Selectors


class ClaimCardSelectors:
    container = Selectors(data_test_id="wc-claim-prize-card")
    status = Selectors(data_test_id="wc-claim-prize-card-status-text")
    item = Selectors(data_test_id="wc-list-item-name-text")
    claim_button = Selectors(data_test_id="wc-claim-prize-button")


class ConfirmClaimSelectors:
    container = Selectors(data_test_id="wc-game-modal")
    submit_button = Selectors(default="text=Submit")


class ClaimInfoSelectors:
    container = Selectors(default="[aria-label='Claim prize dialog']")
    close_button = Selectors(default="button[aria-label='Close claim prize dialog']")