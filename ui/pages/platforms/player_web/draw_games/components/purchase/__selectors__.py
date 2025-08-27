from ui.pages.locator import Selectors


class QuickPickSelectors:
    container = Selectors(default="dialog[aria-label*='game dialog']")
    quick_pick_button = Selectors(data_test_id="gcl-game-action-button")


class TicketSelectionSelectors:
    container = Selectors(default="dialog[aria-label*='game dialog']")
    footer_price = Selectors(data_test_id="gcl-game-footer-price-text")
    continue_button = Selectors(data_test_id="gcl-game-footer-button")


class NumberSelectionSelectors:
    container = Selectors(data_test_id="gcl-nr-selector")
    number_button = Selectors(data_test_id="gcl-number-button")


class DrawSelectionSelectors:
    parent = Selectors(".ticket-section > .gcl-hidden")
    container = Selectors(data_test_id="gcl-draw-selector")
    draw_selector_button = Selectors(data_test_id="gcl-draw-selector-button")
    draw_selector_popper = Selectors(default=".popper")
    draw_selector_item = Selectors(data_test_id="gcl-draw-selector-button")


class PlaySelectionSelectors:
    parent = Selectors(".ticket-section > .gcl-hidden")
    container = Selectors(data_test_id="gcl-ticket-increment")
    minus_button = Selectors(data_test_id="gcl-ticket-increment-remove-button")
    plus_button = Selectors(data_test_id="gcl-ticket-increment-add-button")
    total_value = Selectors(default=".gcl-font-bold")


class TicketRowSelectors:
    parent = Selectors(".ticket-section > .gcl-hidden")
    container = Selectors(data_test_id="gcl-ticket")
    primary_number_button = Selectors(data_test_id="gcl-ticket-primary-number-button")
    secondary_number_button = Selectors(data_test_id="gcl-ticket-secondary-number-button")


class PowerPlaySelectors:
    container = Selectors(default="dialog[aria-label*='game dialog']")
    power_play_toggle = Selectors(data_test_id="gcl-power-play-toggle")
    continue_button = Selectors(data_test_id="gcl-game-footer-button")


class DoublePlaySelectors:
    container = Selectors(default="dialog[aria-label*='game dialog']")
    double_play_toggle = Selectors("[aria-labelledBy='maximizeChancesToggle']")
    continue_button = Selectors(data_test_id="gcl-game-footer-button")


class ShoppingCartDialogSelectors:
    container = Selectors(default="dialog[aria-label*='Shopping cart dialog']")
    total_items_count = Selectors(data_test_id="wc-shopping-cart-ticket-count-text")
    checkout_button = Selectors(data_test_id="wc-shopping-cart-checkout-footer-button")


class TicketSummarySelectors:
    container = Selectors(default="dialog[aria-label*='Summary of your purchase dialog']")
    complete_button = Selectors(data_test_id="wc-checkout-complete-button")


class PurchaseSuccessSelectors:
    container = Selectors(default=".wc-shoppingcart-receipt")
    close_button = Selectors(default="button.cc-modal-close-button")