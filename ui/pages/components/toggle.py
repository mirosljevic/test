from logger import log
from .base import BaseComponent


class Toggle(BaseComponent):
    def __init__(self, page, **kwargs):
        super().__init__(page, **kwargs)
        self.name = "Toggle"

    def turn_on(self):
        log.debug(f"Selecting Toggle: {self.full_name_with_selector}")
        try:
            self.locator.scroll_into_view_if_needed()
            if not self.is_turned_on():
                self.locator.click()
                log.debug(f"Toggle turned on successfully: {self.component_name}")
        except Exception as e:
            log.error(f"Failed to turn on toggle: {e}")

    def turn_off(self):
        log.debug(f"Deselecting Toggle: {self.full_name_with_selector}")
        try:
            self.locator.scroll_into_view_if_needed()
            if self.is_turned_on():
                self.locator.click()
                log.debug(f"Toggle turned off successfully: {self.component_name}")
        except Exception as e:
            log.error(f"Failed to turn off toggle: {e}")

    def is_turned_on(self):
        value = self.locator.get_attribute("aria-checked")
        if value.lower() == "true":
            return True
        else:
            return False
