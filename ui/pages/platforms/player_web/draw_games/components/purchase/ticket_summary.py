from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import TicketSummarySelectors as Selectors


class TicketSummary(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Ticket Summary Dialog", **kwargs)

    @locate(Button, selector=Selectors.complete_button, component_name="Complete Button")
    def complete_button(self): pass
