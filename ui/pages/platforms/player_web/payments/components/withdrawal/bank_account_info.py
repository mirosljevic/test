from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Input, Button
from ui.pages.locator import locate
from .__selectors__ import BankAccountInfoSelectors as Selectors


class BankAccountInfo(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Bank Account Info Form", **kwargs)
        self.in_frame = True
        self.frame_locator = "iframe.cc-border-none"

    @locate(Input, selector=Selectors.account_type_input, component_name="Account Type Input")
    def account_type_input(self) -> Input: pass

    @locate(Input, selector=Selectors.account_number_input, component_name="Account Number Input")
    def account_number_input(self) -> Input: pass

    @locate(Input, selector=Selectors.routing_number_input, component_name="Routing Number Input")
    def routing_number_input(self) -> Input: pass

    @locate(Button, selector=Selectors.bank_transfer_button, component_name="Bank Transfer Button")
    def bank_transfer_button(self) -> Button: pass

    def enter_bank_account_info(self, account_type: str, account_number: str, routing_number: str):
        self.account_type_input.enter(account_type, submit=True)
        self.account_number_input.enter(account_number)
        self.routing_number_input.enter(routing_number)
        self.bank_transfer_button.click()