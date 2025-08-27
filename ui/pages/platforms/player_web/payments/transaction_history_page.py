from playwright.sync_api import Page
from ui.pages import BasePage
from ui.pages.locator import locate
from ui.pages.components import Input, DropDown
from utils.currency import string_to_float
from .components.transactions import TransactionItem, TransactionSummary
from .__selectors__ import TransactionHistorySelectors as Selectors


class TransactionHistoryPage(BasePage):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, page_name="Transaction History Page", **kwargs)

    @locate(Input, selector=Selectors.filter_inputs, component_name="From Date Input", index=0)
    def from_date_input(self) -> Input: pass

    @locate(Input, selector=Selectors.filter_inputs, component_name="To Date Input", index=1)
    def to_date_input(self) -> Input: pass

    @locate(Input, selector=Selectors.filter_inputs, component_name="Filter By Dropdown", index=2)
    def filter_by_dropdown(self) -> DropDown: pass

    @locate(TransactionItem)
    def transaction_item(self) -> TransactionItem: pass

    @locate(TransactionSummary)
    def transaction_summary(self) -> TransactionSummary: pass

    def filter_transactions(self, date_from, date_to, filter_by):
        self.from_date_input.enter(date_from, typing=True)
        self.to_date_input.enter(date_to, typing=True)
        if filter_by:
            self.filter_by_dropdown.enter(filter_by, typing=True, submit=True)
        self.page.wait_for_load_state("networkidle")

    def get_transaction(self, transaction_type=None, amount=None, index=0, **kwargs):
        self.transaction_item(index).view_button.click()
        transaction = {
            "amount": string_to_float(self.transaction_summary.get_item_value("Amount"))
        }
        self.transaction_summary.close_button.click()
        return transaction
