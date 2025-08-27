from requests import Session
from typing import Optional

from logger import log
from models import Player, Operator


class PlayerRgApi:
    def __init__(self, session: Optional[Session] = None, player: Optional[Player] = None):
        self.session = session
        self.player = player

    def set_funding_limit(self):
        pass

    def take_break(self, verify: bool = True) -> None:
        log.debug(f"Taking break for player: {self.player.email} with operator: {operator.name}")
        # Implementation for taking a break
        pass

    def set_time_limit(self):
        pass

    def self_exclude(self, verify: bool = True) -> None:
        log.debug(f"Self-excluding player: {self.player.email} with operator: {operator.name}")
        # Implementation for self-exclusion
        pass