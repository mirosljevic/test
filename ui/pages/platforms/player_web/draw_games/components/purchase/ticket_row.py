from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import TicketRowSelectors as Selectors


class TicketRow(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container,
                         component_name="Ticket Row", **kwargs)
        self.parent_locator = self.parent_locator.locator(Selectors.parent.get_selector(self.layout, self.tenant))

    @locate(Button, selector=Selectors.primary_number_button, component_name="Primary Number Button")
    def primary_number_button(self): pass

    @locate(Button, selector=Selectors.secondary_number_button, component_name="Secondary Number Button")
    def secondary_number_button(self): pass
