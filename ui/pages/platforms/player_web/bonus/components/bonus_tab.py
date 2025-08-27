from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button, DropDown
from ui.pages.locator import locate
from .__selectors__ import BonusTabSelectors as Selectors


class BonusTabs(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Bonus Tab", **kwargs)

    @locate(Button, selector=Selectors.tab, name="Bonus Tab")
    def bonus_tab(self): pass

    def select(self, item):
        self.bonus_tab(item).click()

