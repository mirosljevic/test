from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import DrawSelectionSelectors as Selectors


class DrawSelection(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Draw Selection", **kwargs)

    @locate(Button, selector=Selectors.draw_selector_button, component_name="Draw Selector Button")
    def draw_selector_button(self): pass

    @property
    def popper(self):
        return BaseComponent(self.page, selector=Selectors.draw_selector_popper,
                             instance=None, component_name="Draw Selection Popper")

    @property
    def item(self):
        return Button(self.page, selector=Selectors.draw_selector_item,
                      component_name="Draw Selection Item", instance=self.popper)

    def select(self, value: int):
        self.draw_selector_button(-1).click()
        if value == 1:
            self.item("Next draw only").click()
        elif value in [2, 3, 6, 9, 12, 15]:
            self.item(f"{value} draws").click()
        else:
            raise ValueError(f"Unsupported value for draw selection: {value}")
