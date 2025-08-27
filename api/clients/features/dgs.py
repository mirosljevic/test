from requests import Session
from typing import Optional

from logger import log
from models import Player, DrawGame


class PlayerDrawsGamesApi:
    def __init__(self, session: Optional[Session] = None, player: Optional[Player] = None):
        self.session = session
        self.player = player

    def get_available_games(self) -> None:
        log.debug(f"Fetching available draw games for player: {self.player.email}")
        # Implementation for fetching available games goes here
        pass

    def get_current_draw(self, game: DrawGame) -> None:
        log.debug(f"Fetching current draw for game: {game}")
        # Implementation for fetching the current draw goes here
        pass

    def purchase_ticket(self, game: DrawGame, verify: bool = True) -> None:
        log.debug(f"Purchasing ticket for game: {game}")
        # Implementation for purchasing a ticket goes here
        pass

    def get_tickets(self):
        log.debug(f"Fetching tickets for player: {self.player.email}")
        # Implementation for fetching tickets goes here
        pass
