from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import ConfirmClaimSelectors as Selectors


class ConfirmClaimDialog(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Confirm Claim Dialog", **kwargs)

    @locate(Button, selector=Selectors.submit_button, component_name="Submit Button")
    def submit_button(self): pass
