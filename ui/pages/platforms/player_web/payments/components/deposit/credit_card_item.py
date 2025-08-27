from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import CreditCardItemSelectors as Selectors


class CreditCardItem(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Credit Card Item", **kwargs)

    @locate(Button, selector=Selectors.button, component_name="Credit Card Item Button")
    def button(self) -> Button: pass
