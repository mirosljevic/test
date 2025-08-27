from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import GameSectionSelectors as Selectors


class GameSection(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Game Section", **kwargs)

    @locate(Button, selector=Selectors.buy_now_button, component_name="Play Now Button")
    def play_now_button(self): pass

    @property
    def locator(self):
        locator = self.parent_locator.locator(self.selector)

        if self.index is not None:
            locator = locator.nth(self.index)
        if self.value is not None:
            locator = locator.filter(has=self.page.locator(f"[aria-label*='{self.value}']"))
        return locator
