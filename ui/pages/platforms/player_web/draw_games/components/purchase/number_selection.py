from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import NumberSelectionSelectors as Selectors


class NumberSelection(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Number Selection", **kwargs)

    @locate(Button, selector=Selectors.number_button, component_name="Number Button", exact_value=True)
    def number_button(self): pass

    def select_numbers(self, *numbers):
        for number in numbers:
            self.number_button(str(number)).click()
