from requests import Session
from typing import Optional
from functools import cached_property
from contextlib import contextmanager

from models import Player
from data_factory import create_player
from mongo import PlayerMongoClient

from .base import BaseAPIClient
from .features.registration import PlayerRegistrationApi
from .features.authentication import PlayerAuthenticationApi
from .features.bonus import PlayerBonusApi
from .features.documents import PlayerDocumentsApi
from .features.dgs import PlayerDrawsGamesApi
from .features.instants import PlayerInstantsApi
from .features.payments import PlayerPaymentsApi
from .features.claims import PlayerClaimsApi
from .features.rasponsible_gaming import PlayerRgApi
from .features.shopping_cart import PlayerShoppingCartApi


class PlayerApiClient(BaseAPIClient):
    def __init__(self, player: Optional[Player] = None, session: Optional[Session] = None, mongo=None):
        self.player = player
        self.session = session
        self.mongo = mongo

    @property
    def registration(self) -> PlayerRegistrationApi:
        return PlayerRegistrationApi(session=self.session, player=self.player)
    
    @property
    def authentication(self) -> PlayerAuthenticationApi:
        return PlayerAuthenticationApi(session=self.session, player=self.player)
    
    @property
    def bonus(self) -> PlayerBonusApi:
        return PlayerBonusApi(session=self.session, player=self.player)
    
    @property
    def documents(self) -> PlayerDocumentsApi:
        return PlayerDocumentsApi(session=self.session, player=self.player)
    
    @property
    def draws_games(self) -> PlayerDrawsGamesApi:
        return PlayerDrawsGamesApi(session=self.session, player=self.player)
    
    @property
    def instants(self) -> PlayerInstantsApi:
        return PlayerInstantsApi(session=self.session, player=self.player)
    
    @property
    def payments(self) -> PlayerPaymentsApi:
        return PlayerPaymentsApi(session=self.session, player=self.player)
    
    @property
    def claims(self) -> PlayerClaimsApi:
        return PlayerClaimsApi(session=self.session, player=self.player)
    
    @property
    def responsible_gaming(self) -> PlayerRgApi:
        return PlayerRgApi(session=self.session, player=self.player)
    
    @property
    def shopping_cart(self) -> PlayerShoppingCartApi:
        return PlayerShoppingCartApi(session=self.session, player=self.player)

    def authenticate(self):
        self.session = self.authentication.login()

    @staticmethod
    @contextmanager
    def new(authenticated: bool = True) -> "PlayerApiClient":
        player = create_player()
        player_api_client = PlayerApiClient(player=player)
        player_api_client.registration.register()
        player_api_client.mongo.insert()
        player_api_client.mongo.lock()
        if authenticated:
            player_api_client.authenticate()
        yield player_api_client
        player_api_client.mongo.set_available()

    
    