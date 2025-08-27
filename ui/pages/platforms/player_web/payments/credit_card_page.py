from playwright.sync_api import Page
from ui.pages import BasePage
from ui.pages.locator import locate
from .components.deposit import CreditCardInfo, DepositConfirmation
from models import Player, CreditCard


class CreditCardPage(BasePage):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, page_name="Credit Card Page", **kwargs)

    @locate(CreditCardInfo)
    def credit_card_info(self) -> CreditCardInfo: pass

    @locate(DepositConfirmation)
    def confirmation(self) -> DepositConfirmation: pass

    def add_card(self, player: Player, card: CreditCard, amount=None):
        self.credit_card_info.submit_card_info(cardholder_name=player.full_name, card_number=card.number,
                                               expiry_date=card.expiry_short_year, cvv=card.cvv, amount=amount)
        self.confirmation.close_button.click()

