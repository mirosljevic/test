from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button, Text
from ui.pages.locator import locate
from logger import log
from .__selectors__ import PlaySelectionSelectors as Selectors


class PlaySelection(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Play Selection", **kwargs)

    @locate(Button, selector=Selectors.minus_button, component_name="Play Button")
    def minus_button(self): pass

    @locate(Button, selector=Selectors.plus_button, component_name="Play Button")
    def plus_button(self): pass

    @locate(Text, selector=Selectors.total_value, component_name="Total Plays")
    def total_plays(self): pass

    def select(self, value: int):
        current_value = int(self.total_plays(1).get_text())
        if current_value < value:
            for _ in range(value - current_value):
                self.plus_button.click()
        elif current_value > value:
            for _ in range(current_value - value):
                self.minus_button.click()
        else:
            log.debug(f"Already at the desired play count: {value}")