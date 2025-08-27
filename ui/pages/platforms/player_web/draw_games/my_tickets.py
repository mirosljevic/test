from playwright.sync_api import Page
from ui.pages import BasePage
from ui.pages.components import Button
from ui.pages.locator import locate
from .components.tickets import SearchTickets
from .components.tickets.__selectors__ import MyTicketsPageSelectors as Selectors


class MyTicketsPage(BasePage):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, page_name="My Tickets Page", **kwargs)

    @locate(Button, selector=Selectors.filter_tickets_button, component_name="Filter Tickets Button")
    def filter_tickets_button(self) -> Button: pass

    @locate(SearchTickets)
    def search_tickets(self) -> SearchTickets: pass

    def wait_for(self):
        pass
