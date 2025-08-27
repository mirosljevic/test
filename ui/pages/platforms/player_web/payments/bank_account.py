from playwright.sync_api import Page
from ui.pages import BasePage
from ui.pages.locator import locate
from .components.withdrawal import BankAccountInfo, Withdrawal
from models import Player, BankAccount


class BankAccountPage(BasePage):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, page_name="Bank Account Page", **kwargs)

    @locate(BankAccountInfo)
    def bank_account_info(self) -> BankAccountInfo: pass

    @locate(Withdrawal)
    def withdrawal(self) -> Withdrawal: pass

    def add_bank_account(self, bank_account: BankAccount):
        self.bank_account_info.enter_bank_account_info(
            account_type=bank_account.account_type,
            account_number=bank_account.account_number,
            routing_number=bank_account.routing_number,
        )

    def withdraw(self, amount: int):
        self.withdrawal.submit_withdrawal(amount)