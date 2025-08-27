from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import ConfirmationSelectors as Selectors


class DepositConfirmation(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Credit Card Info Form", **kwargs)

    @locate(Button, selector=Selectors.close_button, component_name="Close Button")
    def close_button(self) -> Button: pass
