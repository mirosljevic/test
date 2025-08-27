from requests import Session
from typing import Optional

from logger import log
from models import Player
from email_service import EmailClient

from api.endpoints.customer.customer_web import get_contracts, initiate_registration, register_player


class PlayerRegistrationApi:
    def __init__(self, session: Optional[Session] = None, player: Optional[Player] = None, email_client=None):
        self.session = session
        self.player = player
        self.email_client = email_client or EmailClient(username=player.username)

    def register(self) -> Player:
        try:
            self.player.email = self.email_client.create_account()
            log.debug(f"Registering player: {self.player}")

            self.session = Session()
            contract_id = get_contracts(session=self.session, validate_response=True).json().get('contractId')
            self.session.headers.update({"X-Csrftoken": self.session.cookies["csrftoken"]})
            initiate_registration(self.session, self.player.email)
            request_id, token, link = self.email_client.get_registration_auth_details()

            response = register_player(
                session=self.session,
                email=self.player.email,
                password=self.player.password,
                first_name=self.player.first_name,
                last_name=self.player.last_name,
                date_of_birth=self.player.date_of_birth.strftime('%Y-%m-%d'),
                identity_number_last_digits=self.player.ssn[-4:],
                mobile_phone=self.player.phone,
                address1=self.player.address,
                address2=None,
                city=self.player.city,
                zip_code=self.player.zip_code,
                state=self.player.state,
                country=self.player.country,
                personalised_offers=False,
                contract_id=contract_id,
                gender=self.player.gender.upper(),
                request_id=request_id,
                token=token,
                channel="WEB"
            )

            self.player.player_id = response.json().get('id')
            log.info(f"Player registered successfully with player id: {self.player.player_id}")
            return self.player
        except Exception as e:
            log.exception(f"Failed to register player: {self.player}. Error: {e}")
            raise e
