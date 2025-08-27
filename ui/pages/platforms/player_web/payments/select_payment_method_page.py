from playwright.sync_api import Page
from ui.pages import BasePage
from ui.pages.locator import locate
from ui.pages.components import Button
from .components.home.__selectors__ import SelectPaymentMethodPageSelectors as Selectors


class SelectPaymentMethodPage(BasePage):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, page_name="Select Payment Method Page", **kwargs)

    @locate(Button, selector=Selectors.payment_method_item, component_name="Credit Card Button", index=0)
    def credit_card_button(self) -> Button: pass

    @locate(Button, selector=Selectors.payment_method_item, component_name="Bank Transfer Button", index=1)
    def bank_transfer_button(self) -> Button: pass

    def select_credit_card(self):
        self.credit_card_button.click()

    def select_bank_transfer(self):
        self.bank_transfer_button.click()