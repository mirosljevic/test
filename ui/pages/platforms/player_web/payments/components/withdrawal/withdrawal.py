from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Input, Button
from ui.pages.locator import locate
from .__selectors__ import WithdrawalSelectors as Selectors


class Withdrawal(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Withdrawal Form", **kwargs)
        self.in_frame = True
        self.frame_locator = "iframe.cc-border-none"

    @locate(Input, selector=Selectors.amount_input, component_name="Withdrawal Amount Input", index=1)
    def amount_input(self) -> Input: pass

    @locate(Button, selector=Selectors.withdraw_button, component_name="Submit Withdrawal Button")
    def withdraw_button(self) -> Input: pass

    @property
    def confirmation_dialog(self):
        return BaseComponent(self.page, selector=Selectors.confirmation_dialog,
                             component_name="Withdrawal Confirmation Dialog")

    @property
    def close_confirmation_button(self):
        return Button(self.page, selector=Selectors.close_confirmation_button,
                      component_name="Close Confirmation Button", instance=self.confirmation_dialog)

    def submit_withdrawal(self, amount: int):
        self.amount_input.enter(str(amount))
        self.withdraw_button.click()
        self.close_confirmation_button.click()
