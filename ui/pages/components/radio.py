from logger import log
from .base import BaseComponent


class Radio(BaseComponent):
    def __init__(self, page, **kwargs):
        super().__init__(page, **kwargs)
        self.name = "Radio Button"

    def select(self):
        log.debug(f"Selecting radio button: {self.full_name_with_selector}")
        self.locator.click()
        log.debug(f"Radio button selected successfully: {self.component_name}")

    @property
    def locator(self):
        locator = self.parent_locator

        if self.in_frame:
            locator = locator.frame_locator(self.frame_locator)

        if self.selectors:
            locator = locator.locator(self.selector)

        if self.index is not None:
            locator = locator.nth(self.index)
        if self.value is not None:
            locator = locator.locator(f"[value='{self.value}']")
        return locator

