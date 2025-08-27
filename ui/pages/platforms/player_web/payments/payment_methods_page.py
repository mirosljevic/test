from playwright.sync_api import Page
from ui.pages import BasePage
from ui.pages.locator import locate
from ui.pages.components import Button
from .__selectors__ import PaymentMethodsSelectors as Selectors


class PaymentMethodsPage(BasePage):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, page_name="Payment Methods Page", **kwargs)

    @locate(Button, selector=Selectors.add_payment_method_button, component_name="Add Payment Method Button", index=0)
    def add_payment_method_button(self) -> Button: pass

    @locate(Button, selector=Selectors.add_withdraw_method_button, component_name="Add Withdraw Method Button", index=1)
    def add_withdraw_method_button(self) -> Button: pass

    @locate(Button, selector=Selectors.empty_state_button, component_name="Empty State Button")
    def empty_state_add_payment_button(self) -> Button: pass

    def select_new_payment_method(self):
        if self.add_payment_method_button.exists():
            self.add_payment_method_button.click()
        else:
            self.empty_state_add_payment_button.click()

    def select_new_withdraw_method(self):
        self.add_withdraw_method_button.click()