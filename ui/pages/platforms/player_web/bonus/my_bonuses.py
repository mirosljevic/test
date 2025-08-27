from playwright.sync_api import Page
from ui.pages.base import BasePage
from ui.pages.locator import locate
from .components import BonusTabs, BonusCard


class MyBonusesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @locate(BonusTabs)
    def bonus_tabs(self): pass

    @locate(BonusCard)
    def bonus_card(self): pass

    def wait_for(self):
        pass

    def select_tab(self, item):
        self.bonus_tabs.select(item)
        return self
