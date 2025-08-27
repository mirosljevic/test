from requests import Session
from typing import Optional

from logger import log
from models import Player
from api.endpoints.exponea.exponea import create_offer, achieve_bonus
from api.endpoints.bonus.bonus_cc import get_bonus_objects, create_bonus_object


class PlayerBonusApi:
    def __init__(self, session: Optional[Session] = None, player: Optional[Player] = None):
        self.session = session
        self.player = player

    def create_bonus_offer(self, campaign_id, bonus_id, **kwargs) -> None:
        log.debug(f"Creating bonus offer for player: {self.player.email}")
        create_offer(
            campaign_id=campaign_id,
            player_id=self.player.player_id,
            bonus_id=bonus_id
        )
        log.info(f"Bonus offer created for player: {self.player}")

    def achieve_bonus_offer(self, campaign_id, player_id, bonus_id) -> None:
        log.debug(f"Achieving bonus for player: {self.player.email}, Bonus")
        achieve_bonus(
            campaign_id=campaign_id,
            player_id=player_id,
            bonus_id=bonus_id
        )
        log.info(f"Bonus Achieved for Player: {self.player.email}")

    def get_bonuses(self) -> list:
        log.debug(f"Fetching bonuses for player: {self.player.email}")
        # TODO: Implement the logic to fetch bonuses
        log.info(f"Bonuses fetched for Player: {self.player.email}")
        return []


class OperatorBonusApi:
    def __init__(self, session: Optional[Session] = None, operator: Optional['Operator'] = None):
        self.session = session
        self.operator = operator

    def get_bonus_object(self, name, **kwargs):
        response = get_bonus_objects(self.session)
        bonus_objects = response.json().get("pageItems")

        filtered_objects = [x for x in bonus_objects if x['name'] == name]
        if filtered_objects:
            return filtered_objects[0]
        else:
            return None

    def create_free_rounds_object(self, games, cost_per_ticket, object_name, number_of_rounds, number_of_tickets):
        bonus_data = {
            "allowedGameDTOS": [{"gameId": game, "gameType": "PET", "version": "ALL"} for game in games],
            "amountType": "FIXED",
            "bonusType": "FREE_ROUNDS",
            "costPerTicket": cost_per_ticket,
            "name": object_name,
            "numberOfRounds": number_of_rounds,
            "numberOfTickets": number_of_tickets,
            "status": "ACTIVE",
            "totalAmount": cost_per_ticket * number_of_tickets * number_of_rounds,
        }
        response = create_bonus_object(self.session, bonus_data, validate_response=True)
        return response.json()