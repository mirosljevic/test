from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import MyAccountMenuSelectors as Selectors


class MyAccountMenu(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="My Account Menu", **kwargs)

    @locate(Button, selector=Selectors.menu_item, component_name="Menu Item")
    def menu_item(self) -> Button: pass

    def select(self, item: str):
        self.menu_item(item).click()
        return self
