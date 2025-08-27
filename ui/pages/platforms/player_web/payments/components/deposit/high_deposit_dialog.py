from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import HighDepositSelectors as Selectors


class HighDepositDialog(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="High Deposit Confirmation", **kwargs)

    @locate(Button, selector=Selectors.confirm_button, component_name="Confirm Button")
    def confirm_button(self) -> Button: pass
