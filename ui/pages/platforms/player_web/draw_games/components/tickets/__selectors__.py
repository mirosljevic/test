from ui.pages.locator import Selectors


class MyTicketsPageSelectors:
    filter_tickets_button = Selectors(data_test_id="wc-ticket-history-filters")


class SearchTicketsSelectors:
    container = Selectors(data_test_id="wc-tickets-history-filters-modal")
    tab = Selectors(default="button")
    from_date_input = Selectors(default="//input[@data-test-id='wc-tickets-history-filters-modal-from-datepicker']")
    to_date_input = Selectors(default="//input[@data-test-id='wc-tickets-history-filters-modal-to-datepicker']")
    checkbox = Selectors(default=".cc-checkbox")
    view_tickets_button = Selectors(data_test_id="wc-tickets-history-filters-modal-view-button")