from requests import Session
from typing import Optional

from logger import log
from models import Player


class PlayerShoppingCartApi:
    def __init__(self, session: Optional[Session] = None, player: Optional[Player] = None):
        self.session = session
        self.player = player