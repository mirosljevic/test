from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Text
from ui.pages.locator import locate
from .__selectors__ import EmailSelectors as Selectors


class EmailDetails(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Email Details", **kwargs)

    @locate(Text, selector=Selectors.email_value, name="Email Value")
    def email_value(self) -> Text: pass
