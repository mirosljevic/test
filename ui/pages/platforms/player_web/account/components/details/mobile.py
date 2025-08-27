from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button, Input, Text
from ui.pages.locator import locate
from .__selectors__ import MobileSelectors as Selectors


class MobileDetails(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Mobile Details", **kwargs)

    @locate(Text, selector=Selectors.mobile_value, name="Mobile Value")
    def mobile_value(self) -> Text: pass

    @locate(Button, selector=Selectors.edit_button, name="Edit Password Button")
    def edit_button(self) -> Button: pass

    @locate(Input, selector=Selectors.mobile_input, name="Mobile Input")
    def current_mobile_input(self) -> Input: pass

    @locate(Button, selector=Selectors.save_button, name="Save Mobile Button")
    def save_button(self) -> Button: pass

    def edit_mobile(self, current_mobile: str):
        self.edit_button().click()
        self.current_mobile_input().enter(current_mobile)
        self.save_button().click()
        return self

    def get_mobile(self):
        return self.mobile_value().get_text().replace("(", "").replace(")", "").replace(" ", "").replace("-", "")

