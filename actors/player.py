from functools import cached_property
from typing import Optional
from contextlib import contextmanager
from .base import BaseActor

from models import Player
from mongo import PlayerMongoClient
from api.clients.player_client import PlayerApiClient
from ui.facade.player import PlayerFacade


class PlayerActor(BaseActor):
    def __init__(self, player: Optional[Player] = None, browser=None, session=None, **kwargs):
        super().__init__(**kwargs)
        self.player = player
        self.browser = browser
        self.session = session

    @cached_property
    def api(self):
        return PlayerApiClient(player=self.player, session=self.session)

    @cached_property
    def ui(self):
        return PlayerFacade(player=self.player, browser=self.browser, session=self.session)

    @property
    def mongo(self):
        return PlayerMongoClient(player=self.player)

    def authenticate(self):
        self.session = self.api.authentication.login()
        self.api.session = self.session
        self.ui.session = self.session

    @staticmethod
    @contextmanager
    def get_available_player(browser=None, **kwargs):
        player_mongo = PlayerMongoClient.get_available_player(**kwargs)
        player_mongo.lock()
        yield PlayerActor(browser=browser, player=player_mongo.player, **kwargs)
        player_mongo.set_available()
