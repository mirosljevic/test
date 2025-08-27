from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Text
from ui.pages.locator import locate
from .selectors import VerifyEmailSelectors as Selectors


class VerifyEmail(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Verify Email Dialog", **kwargs)

    @locate(Text, selector=Selectors.verify_email_text, component_name="Verify Email Text")
    def verify_email_text(self): pass
