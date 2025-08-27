from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Toggle, Button
from ui.pages.locator import locate
from .__selectors__ import PowerPlaySelectors as Selectors


class PowerPlay(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Power Play Selection", **kwargs)

    @locate(Toggle, selector=Selectors.power_play_toggle, component_name="Power Play Toggle")
    def power_play(self): pass

    @locate(Button, selector=Selectors.continue_button, component_name="Continue Button")
    def continue_button(self): pass

    def set(self, power_play: bool):
        if power_play:
            self.power_play.turn_on()
        else:
            self.power_play.turn_off()
        self.continue_button.click()