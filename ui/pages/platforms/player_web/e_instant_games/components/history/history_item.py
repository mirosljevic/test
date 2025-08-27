from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import HistoryItemSelectors as Selectors


class HistoryItem(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Play History Item", **kwargs)

    @locate(Button, selector=Selectors.view_button, component_name="View Button")
    def view_button(self): pass
