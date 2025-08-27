from requests import Session
from typing import Optional

from models import Player


class PlayerClaimsApi:
    def __init__(self, session: Optional[Session] = None, player: Optional[Player] = None):
        self.session = session
        self.player = player

    def request_claim(self):
        pass
