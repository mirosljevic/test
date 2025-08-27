from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button, Input
from ui.pages.locator import locate
from .__selectors__ import AddCvvSelectors as Selectors


class AddCvv(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Add CVV dialog", **kwargs)

    @locate(Input, selector=Selectors.cvv_input, component_name="CVV Input")
    def cvv_input(self) -> Input: pass

    @locate(Button, selector=Selectors.confrim_button, component_name="Confirm Button")
    def confirm_button(self) -> Button: pass

    def confirm(self, cvv):
        self.cvv_input.enter(cvv)
        self.confirm_button.click()
