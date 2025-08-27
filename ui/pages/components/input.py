from playwright.sync_api import Page
from logger import log
from .base import BaseComponent


class Input(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, **kwargs)

    def enter(self, text: str, typing=False, delay=50, submit=False):
        log.debug(f"Entering text into {self.full_name_with_selector}: '{text}'")
        try:
            self.locator.scroll_into_view_if_needed()
            if not typing:
                self.locator.fill(text)
            else:
                self.locator.press_sequentially(text, delay=delay)
            if submit:
                self.page.keyboard.press("Enter")
            log.debug(f"Text '{text}' entered successfully into {self.component_name}")
        except Exception as e:
            log.error(f"Failed to enter text '{text}' into input '{self.full_name_with_selector}': {e}")
            raise RuntimeError
