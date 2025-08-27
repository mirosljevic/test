from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Toggle, Button
from ui.pages.locator import locate
from .__selectors__ import DoublePlaySelectors as Selectors


class DoublePlay(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Double Play Selection", **kwargs)

    @locate(Toggle, selector=Selectors.double_play_toggle, component_name="Double Play Toggle")
    def double_play(self):
        pass

    @locate(Button, selector=Selectors.continue_button, component_name="Continue Button")
    def continue_button(self):
        pass

    def set(self, double_play: bool):
        if double_play:
            self.double_play.turn_on()
        else:
            self.double_play.turn_off()
        self.continue_button.click()
        