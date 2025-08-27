from requests import Session
from typing import Optional
from random import randint
from time import sleep

from data_factory import create_credit_card
from logger import log
from models import Player, Operator
from api.endpoints.payment_processor.payment_processor_web import init_new_payment_method, new_payment
from api.endpoints.payment_method_vault.pmv_web import add_payment_method, update_payment_method
from api.endpoints.wallet.wallet_web import get_payment_methods
from api.endpoints.customer.customer_web import get_player_levels


class PlayerPaymentsApi:
    def __init__(self, session: Optional[Session] = None, player: Optional[Player] = None):
        self.session = session
        self.player = player

    def add_credit_card(self, credit_card):
        self.wait_for_player_level(level="TEMPORARY_ACCOUNT")
        credit_card = credit_card or create_credit_card(card_type="visa")
        response_init = init_new_payment_method(self.session, "CARD", validate_response=True)
        token = response_init.json().get('payload')

        account_data = {
            "card": {
                "accountNumber": credit_card.number,
                "cardHolderName": self.player.full_name,
                "expiryYear": credit_card.expiry_year,
                "expiryMonth": credit_card.expiry_month,
                "cvv": credit_card.cvv,
                "amount": 40
            }
        }
        response = add_payment_method(self.session, token, account_data, validate_response=True)
        account_data["card"]["paymentId"] = response.json()["paymentId"]
        return account_data

    def get_card(self):
        response = get_payment_methods(self.session, direction="IN")
        return response.json()[0].get('paymentMethodId')

    def make_deposit(self, credit_card, amount: float, verify: bool = True) -> None:
        self.wait_for_player_level(level="VERIFIED_ACCOUNT")
        method_id = self.get_card()
        first_step = new_payment(self.session, method_id, amount, validate_response=True)
        second_step = update_payment_method(self.session, first_step.json()["payload"],
                              {"card": {"cvv": credit_card.cvv}}, validate_response=True)
        return second_step.json()

    def wait_for_player_level(self, level, retries=20, timeout=2) -> bool:
        log.debug(f"Waiting for player {self.player.email} to reach level: {level}")
        for _ in range(retries):
            if get_player_levels(self.session).json().get("playerLevel") == level:
                log.debug(f"Player {self.player.email} has reached level: {level}")
                return True
            log.warning(f"Player {self.player.email} not at level {level}. Retrying...")
            sleep(timeout)
        log.error(f"Player {self.player.email} did not reach level: {level} after {retries} retries")
        return False

    def add_bank_account(self):
        pass

    def withdraw_funds(self, amount: float, verify: bool = True) -> None:
        log.debug(f"Withdrawing funds for player: {self.player.email} with amount: {amount}")
        # Implementation for withdrawing funds
        pass