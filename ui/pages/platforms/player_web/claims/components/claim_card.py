from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Text, Button
from ui.pages.locator import locate
from .__selectors__ import ClaimCardSelectors as Selectors


class ClaimCard(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Claim Card", **kwargs)

    @locate(Text, selector=Selectors.status, component_name="Status")
    def status(self): pass

    @locate(Text, selector=Selectors.item, component_name="Item Name")
    def item(self): pass

    @locate(Button, selector=Selectors.claim_button, component_name="Claim Button")
    def claim_button(self): pass

    def get_details(self):
        return {
            "status": self.status.get_text(),
        }
