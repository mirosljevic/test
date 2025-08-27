from models import Player, Operator
from logger import log

from .base_client import BaseMongoClient
from .player_client import PlayerMongoClient
from .operator_client import OperatorMongoClient
from .config import Status, PLAYERS_COLLECTION, OPERATORS_COLLECTION


class MongoClient(BaseMongoClient):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.players_collection = self.db.get_collection(PLAYERS_COLLECTION)
        self.operators_collection = self.db.get_collection(OPERATORS_COLLECTION)

    def get_player(self, **kwargs) -> 'PlayerMongoClient':
        player_doc = self.players_collection.find_one(kwargs)

        if not player_doc:
            log.error(f"No player found with filters: {kwargs}")
            raise ValueError

        geolocation = player_doc.get("geolocation")
        if geolocation and isinstance(geolocation, list) and len(geolocation) == 2:
            geolocation = tuple(geolocation)

        player = Player(
            first_name=player_doc.get("first_name", ""),
            last_name=player_doc.get("last_name", ""),
            email=player_doc.get("email"),
            password=player_doc.get("password"),
            player_id=str(player_doc.get("player_id")),
            date_of_birth=player_doc.get("date_of_birth"),
            address=player_doc.get("address"),
            city=player_doc.get("city"),
            state=player_doc.get("state"),
            country=player_doc.get("country"),
            phone=player_doc.get("phone"),
            gender=player_doc.get("gender"),
            geolocation=geolocation
        )

        return PlayerMongoClient(player=player, **kwargs)

    def get_available_player(self, **kwargs) -> 'PlayerMongoClient':
        return self.get_player(status=Status.AVAILABLE, **kwargs)

    def get_operator(self, **kwargs) -> 'OperatorMongoClient':
        operator_doc = self.operators_collection.find_one(kwargs)

        if not operator_doc:
            log.error(f"No operator found with filters: {kwargs}")
            raise ValueError

        operator = Operator(
            username=operator_doc.get("username"),
            password=operator_doc.get("password"),
            role=operator_doc.get("role")
        )

        operator_client = OperatorMongoClient(operator, **kwargs)
        return operator_client

    def get_available_operator(self, **kwargs) -> 'OperatorMongoClient':
        return self.get_operator(status=Status.AVAILABLE, **kwargs)



