from requests import Session
from typing import Optional

from logger import log
from models import Player, Operator


class PlayerAccountApi:
    def __init__(self, session: Optional[Session] = None, player: Optional[Player] = None):
        self.session = session
        self.player = player

    def get_account_info(self):
        pass

    def update_account(self, account_info: dict, verify: bool = True) -> None:
        log.debug(f"Updating account for player: {self.player.email}")
        # Implementation for updating account information goes here
        pass


class OperatorAccountApi:
    def __init__(self, session: Optional[Session] = None, operator: Optional[Operator] = None):
        self.session = session
        self.operator = operator

    def get_player_account(self, player: Player) -> None:
        pass

    def get_player_account_details(self):
        pass
