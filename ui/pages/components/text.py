from playwright.sync_api import Page
from logger import log
from .base import BaseComponent


class Text(BaseComponent):
    def __init__(self, page, **kwargs):
        super().__init__(page, **kwargs)

    def get_text(self):
        log.debug(f"Getting text from {self.full_name_with_selector}")
        text = self.locator.text_content()
        log.debug(f"Text content at {self.component_name}: {text}")
        return text.strip() if text else ""
