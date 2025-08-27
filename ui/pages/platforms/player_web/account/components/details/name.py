from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Text
from ui.pages.locator import locate
from .__selectors__ import NameSelectors as Selectors


class NameDetails(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Name Details", **kwargs)

    @locate(Text, selector=Selectors.name_value, name="Name Value")
    def name_value(self) -> Text: pass
