from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Text
from ui.pages.locator import locate
from .__selectors__ import WalletSelectors as Selectors


class Wallet(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Wallet", **kwargs)

    @locate(Text, selector=Selectors.balance, component_name="Balance", index=0)
    def balance(self) -> Text: pass

    @locate(Text, selector=Selectors.funds_added, component_name="Funds Added", index=1)
    def funds_added(self) -> Text: pass

    @locate(Text, selector=Selectors.winnings, component_name="Winnings", index=2)
    def winnings(self) -> Text: pass

    @locate(Text, selector=Selectors.withdrawal_requests, component_name="Withdrawal Requests", index=3)
    def withdrawal_requests(self) -> Text: pass

    def get_balance(self) -> float:
        return float(self.balance().get_text().replace("$", "").strip())

    def get_funds_added(self) -> float:
        return float(self.funds_added().get_text().replace("$", "").strip())

    def get_winnings(self) -> float:
        return float(self.winnings().get_text().replace("$", "").strip())

    def get_withdrawal_requests(self) -> float:
        return float(self.withdrawal_requests().get_text().replace("$", "").strip())
