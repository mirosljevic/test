from data_factory import create_credit_card, create_bank_account
from models import CreditCard

from ui.pages.platforms.player_web.home import HomePage
from ui.pages.platforms.player_web.account import MyAccountPage
from ui.pages.platforms.player_web.payments import (PaymentMethodsPage, SelectPaymentMethodPage, CreditCardPage,
                                                    BankAccountPage, AddFundsPage, TransactionHistoryPage)

from utils.datetime import today_mdy


class PlayerPaymentsUi:
    def __init__(self, page, player=None):
        self.page = page
        self.player = player

        self.home_page = HomePage(page)
        self.my_account_page = MyAccountPage(page)
        self.payment_methods_page = PaymentMethodsPage(page)
        self.select_payment_page = SelectPaymentMethodPage(page)
        self.credit_card_page = CreditCardPage(page)
        self.bank_account_page = BankAccountPage(page)
        self.add_funds_page = AddFundsPage(page)
        self.transaction_history_page = TransactionHistoryPage(page)

    def go_to_payment_methods(self):
        self.home_page.user_controls.user_menu.select("My Account")
        self.my_account_page.my_account_menu.select("Payment Methods")
        return self.payment_methods_page

    def go_to_add_funds(self):
        self.home_page.user_controls.user_menu.select("My Account")
        self.my_account_page.my_account_menu.select("Add Funds")
        return self.select_payment_page

    def go_to_transaction_history(self):
        self.home_page.user_controls.user_menu.select("My Account")
        self.my_account_page.my_account_menu.select("Transaction History")
        return self.transaction_history_page

    def add_credit_card(self, card: CreditCard = None, amount: int = None):
        if card is None:
            card = create_credit_card(card_type="Visa")

        self.go_to_payment_methods()
        self.payment_methods_page.select_new_payment_method()
        self.select_payment_page.select_credit_card()
        self.credit_card_page.add_card(self.player, card, amount)

    def add_bank_account(self, bank_account=None, withdraw_amount=10):
        if bank_account is None:
            bank_account = create_bank_account()

        self.go_to_payment_methods()
        self.payment_methods_page.select_new_withdraw_method()
        self.bank_account_page.add_bank_account(bank_account)
        self.bank_account_page.withdraw(amount=withdraw_amount)

    def make_deposit(self, card, amount):
        self.go_to_add_funds()
        self.add_funds_page.add(card=card, amount=amount)

    def get_transaction(self, transaction_type="Financial Transactions", amount=None):
        self.go_to_transaction_history()
        self.transaction_history_page.filter_transactions(date_from=today_mdy(), date_to=today_mdy(),
                                                          filter_by=transaction_type)
        return self.transaction_history_page.get_transaction(transaction_type=transaction_type,
                                                             amount=amount, index=0)

    def get_latest_transaction(self, transaction_type=None):
        self.go_to_transaction_history()
        self.transaction_history_page.filter_transactions(date_from=today_mdy(), date_to=today_mdy(),
                                                          filter_by=transaction_type)
        return self.transaction_history_page.get_transaction(index=0)

    def go_to_claims(self):
        pass

    def submit_reward_claim(self):
        pass

    def go_to_withdrawals(self):
        pass

    def submit_withdrawal_request(self, **kwargs):
        pass
