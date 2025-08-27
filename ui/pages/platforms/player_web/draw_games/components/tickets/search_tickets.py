from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button, Input, Checkbox
from ui.pages.locator import locate
from .__selectors__ import SearchTicketsSelectors as Selectors


class SearchTickets(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Search Tickets", **kwargs)

    @locate(Button, selector=Selectors.tab, component_name="Filter Tab")
    def tab(self) -> Button: pass

    @locate(Input, selector=Selectors.from_date_input, component_name="From Date Input")
    def from_date_input(self) -> Input: pass

    @locate(Input, selector=Selectors.to_date_input, component_name="To Date Input")
    def to_date_input(self) -> Input: pass

    @locate(Checkbox, selectors=Selectors.checkbox, component_name="Filter Checkbox")
    def filter_checkbox(self) -> Checkbox: pass

    @locate(Button, selector=Selectors.view_tickets_button, component_name="View Tickets Button")
    def view_tickets_button(self) -> Button: pass

    def submit(self, date_from=None, date_to=None, games=None, winning=None, kind=None):
        if kind == "purchase_date":
            self.tab("Purchase Date").click()
        if kind == "draw_date":
            self.tab("Draw Date").click()
        if date_from:
            self.from_date_input.enter(date_from, typing=True)
        if date_to:
            self.to_date_input.enter(date_to, typing=True)
        if games:
            for game in games:
                self.filter_checkbox(game).check()
        if winning is not None:
            self.filter_checkbox("Winnings").check()
        self.view_tickets_button.click()
