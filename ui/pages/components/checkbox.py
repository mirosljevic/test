from logger import log
from .base import BaseComponent


class Checkbox(BaseComponent):
    def __init__(self, page, **kwargs):
        super().__init__(page, **kwargs)
        self.name = "Checkbox"

    def check(self):
        log.debug(f"Checking checkbox: {self.full_name_with_selector}")
        try:
            self.locator.scroll_into_view_if_needed()
            if not self.locator.is_checked():
                self.locator.click()
                log.debug(f"Checkbox checked successfully: {self.component_name}")
            else:
                log.debug(f"Checkbox already checked: {self.component_name}")
        except Exception as e:
            log.error(f"Failed to check checkbox '{self.full_name_with_selector}': {e}")
            raise RuntimeError

    def uncheck(self):
        log.debug(f"Unchecking checkbox: {self.full_name_with_selector}")
        try:
            self.locator.scroll_into_view_if_needed()
            if self.locator.is_checked():
                self.locator.click()
                log.debug(f"Checkbox unchecked successfully: {self.component_name}")
            else:
                log.debug(f"Checkbox already unchecked: {self.component_name}")
        except Exception as e:
            log.error(f"Failed to uncheck checkbox '{self.full_name_with_selector}': {e}")
            raise RuntimeError
