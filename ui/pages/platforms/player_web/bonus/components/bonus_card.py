from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Text
from ui.pages.locator import locate
from .__selectors__ import BonusCardSelectors as Selectors


class BonusCard(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Bonus Card", **kwargs)

    @locate(Text, selector=Selectors.status, component_name="Status")
    def status(self): pass

    @locate(Text, selector=Selectors.bonus_id, component_name="Bonus ID")
    def bonus_id(self): pass

    @locate(Text, selector=Selectors.bonus_type, component_name="Bonus Type")
    def bonus_type(self): pass

    @locate(Text, selector=Selectors.bonus_games, component_name="Bonus Games")
    def bonus_games(self): pass

    @locate(Text, selector=Selectors.bonus_amount, component_name="Bonus Amount")
    def bonus_amount(self): pass

    def get_details(self):
        return {
            "status": self.status.get_text(),
            "bonus_id": self.bonus_id.get_text(),
            "bonus_type": self.bonus_type.get_text(),
            "bonus_games": self.bonus_games.get_text(),
            "bonus_amount": self.bonus_amount.get_text(),
        }

