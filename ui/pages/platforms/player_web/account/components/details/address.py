from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Text
from ui.pages.locator import locate
from .__selectors__ import AddressSelectors as Selectors


class AddressDetails(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Address Details", **kwargs)

    @locate(Text, selector=Selectors.address_value, name="Address Value")
    def address_value(self) -> Text: pass

    def get_address(self) -> dict:
        values = self.address_value.locator.inner_text().split("\n")
        state = values[2].strip().split(",")
        return {
            "address": values[0].strip(),
            "city": values[1].strip(),
            "zip_code": state[0].strip(),
            "state": state[1].strip(),
        }
