from playwright.sync_api import Page
from ui.pages.base import BasePage
from ui.pages.locator import locate
from .components.home import Wallet, PlayOn
from .components.menu import MyAccountMenu


class MyAccountPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, page_name="My Account Page")

    @locate(MyAccountMenu)
    def my_account_menu(self) -> MyAccountMenu: pass

    @locate(Wallet)
    def wallet(self) -> Wallet: pass

    @locate(PlayOn)
    def play_on(self) -> PlayOn: pass

    def wait_for(self):
        self.wallet().wait_for()
        self.play_on().wait_for()
        return self

    def get_details(self):
        return {
            "wallet": {
                "balance": self.wallet.get_balance(),
                "funds_added": self.wallet.get_funds_added(),
                "winnings": self.wallet.get_winnings(),
                "withdrawal_requests": self.wallet.get_withdrawal_requests()
            },
            "play_on": {
                "points": self.play_on.get_points(),
                "points_expiring_this_month": self.play_on.get_points_this_month(),
                "draw_entries": self.play_on.get_draw_entries(),
                "second_chance": self.play_on.get_second_chance()
            }
        }
