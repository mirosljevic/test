from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import TransactionItemSelectors as Selectors


class TransactionItem(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Transaction Item", **kwargs)

    @locate(Button, selector=Selectors.view_button, component_name="Transaction View Button")
    def view_button(self) -> Button: pass
