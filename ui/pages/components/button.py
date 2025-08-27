from logger import log
from .base import BaseComponent


class Button(BaseComponent):
    def __init__(self, page, **kwargs):
        super().__init__(page, **kwargs)
        
    def click(self):
        log.debug(f"Clicking button: {self.full_name_with_selector}")
        try:
            self.locator.scroll_into_view_if_needed()
            self.locator.click()
            log.debug(f"Button clicked successfully: {self.component_name}")
        except Exception as e:
            log.error(f"Failed to click button '{self.full_name_with_selector}': {e}")
            raise RuntimeError

