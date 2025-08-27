from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import QuickPickSelectors as Selectors


class QuickPick(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Quick Pick", **kwargs)

    @locate(Button, selector=Selectors.quick_pick_button, component_name="Quick Pick Button")
    def quick_pick_button(self): pass
