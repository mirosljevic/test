from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Input, Button
from ui.pages.locator import locate
from .__selectors__ import CreditCardInfoSelectors as Selectors


class CreditCardInfo(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Credit Card Info Form", **kwargs)
        self.in_frame = True
        self.frame_locator = "iframe.cc-border-none"

    @locate(Input, selector=Selectors.name_input, component_name="Cardholder Name Input")
    def cardholder_name_input(self) -> Input: pass

    @locate(Input, selector=Selectors.card_input, component_name="Card Number Input")
    def card_number_input(self) -> Input: pass

    @locate(Input, selector=Selectors.expiry_input, component_name="Expiry Date Input")
    def expiry_date_input(self) -> Input: pass

    @locate(Input, selector=Selectors.cvv_input, component_name="CVV Input")
    def cvv_input(self) -> Input: pass

    @locate(Button, selector=Selectors.pay_amount_button, component_name="Pay Amount Button")
    def pay_amount_button(self) -> Button: pass

    @locate(Input, selector=Selectors.amount_input, component_name="Amount Input")
    def amount_input(self) -> Input: pass

    @locate(Button, selector=Selectors.bonus_code_link, component_name="Bonus Code Link")
    def bonus_code_link(self) -> Button: pass

    @locate(Button, selector=Selectors.pay_add_button, component_name="Pay Add Button")
    def pay_add_button(self) -> Button: pass

    def submit_card_info(self, cardholder_name: str, card_number: str, expiry_date: str, cvv: str, amount: int):
        self.cardholder_name_input.enter(cardholder_name)
        self.card_number_input.enter(card_number)
        self.expiry_date_input.enter(expiry_date, typing=True)
        self.cvv_input.enter(cvv)

        if amount in [25, 40, 50]:
            self.pay_amount_button(str(amount)).click()
        elif amount is not None:
            self.amount_input.enter(str(amount))
        self.pay_add_button.click()