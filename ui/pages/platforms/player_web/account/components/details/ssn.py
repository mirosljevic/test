from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Text
from ui.pages.locator import locate
from .__selectors__ import SsnSelectors as Selectors


class SsnDetails(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="SSN Details", **kwargs)

    @locate(Text, selector=Selectors.ssn_value, name="SSN Value")
    def ssn_value(self) -> Text: pass
