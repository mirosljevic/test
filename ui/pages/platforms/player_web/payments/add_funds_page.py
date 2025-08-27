from playwright.sync_api import Page
from models import CreditCard
from ui.pages import BasePage
from ui.pages.locator import locate
from ui.pages.components import Button, Input
from .components.deposit import CreditCardItem, AddCvv, DepositConfirmation, HighDepositDialog
from .__selectors__ import AddFundsSelectors as Selectors


class AddFundsPage(BasePage):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, page_name="Add Funds Page", **kwargs)

    @locate(CreditCardItem)
    def credit_card_item(self) -> CreditCardItem: pass

    @locate(Button, selector=Selectors.pay_amount_button, component_name="Pay Amount Button")
    def pay_amount_button(self) -> Button:
        pass

    @locate(Input, selector=Selectors.amount_input, component_name="Amount Input")
    def amount_input(self) -> Input:
        pass

    @locate(Button, selector=Selectors.pay_add_button, component_name="Pay Add Button")
    def pay_add_button(self) -> Button:
        pass

    @locate(AddCvv)
    def add_cvv(self) -> AddCvv: pass

    @locate(DepositConfirmation)
    def deposit_confirmation(self) -> DepositConfirmation: pass

    @locate(HighDepositDialog)
    def high_deposit_dialog(self) -> HighDepositDialog: pass

    def add(self, card: CreditCard, amount: int, credit_card_index=0):
        self.credit_card_item(credit_card_index).button.click()
        if amount in [25, 40, 50]:
            self.pay_amount_button(str(amount)).click()
        elif amount is not None:
            self.amount_input(1).enter(str(amount))
        self.pay_add_button.click()

        if self.high_deposit_dialog.exists():
            self.high_deposit_dialog.confirm_button.click()

        if self.add_cvv.exists():
            self.add_cvv.confirm(cvv=card.cvv)

        self.deposit_confirmation.close_button.click()


