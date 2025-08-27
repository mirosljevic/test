from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import ShoppingCartDialogSelectors as Selectors


class ShoppingCart(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Shopping Cart Dialog", **kwargs)

    @locate(Button, selector=Selectors.checkout_button, component_name="Checkout Button")
    def checkout_button(self): pass

