from typing import Optional
from requests import Session

from logger import log
from models import Player
from utils.session import get_session_state
from utils.soup import fetch
from environment import settings, geofencing, hosts
from api.endpoints.keycloak.keycloak_web import get_oidc_login, get_keycloak_player_login, authenticate_player
from api.endpoints.geofencing.mkodo import authenticate, get_mkodo_token, send_ping
from api.endpoints.keycloak.keycloak_cc import (get_oidc_login as get_oidc_login_cc, get_adfs_login_link,
                                                get_saml_post_binding, get_adfs_client_request, authenticate_operator,
                                                finalize_login)


class PlayerAuthenticationApi:
    def __init__(self, session: Optional[Session] = None, player: Optional[Player] = None):
        self.session = session
        self.player = player
        self.session_state = None

    def login(self, verify: bool = True) -> Session:
        log.debug(f"Attempting login for user: {self.player.email}")
        self.session = self.session or Session()
        try:
            response = get_oidc_login(session=self.session)
            self.session.headers.update({"SESSION": response.cookies['SESSION']})
            keycloak_response = get_keycloak_player_login(self.session, response.headers['Location'])
            self.session_state = get_session_state(keycloak_response)
            authenticate_player(
                session=self.session,
                action=fetch(keycloak_response).find('form', id='kc-form-login')['action'],
                email=self.player.email,
                password=self.player.password
            )

            self.session.headers.update({"X-Csrftoken": self.session.cookies["csrftoken"]})

            if settings.geofencing_enabled:
                self.make_ping()
            return self.session
        except Exception as e:
            if verify:
                log.exception(f"Failed to login player: {self.player.email}")
                log.exception(f"Error: {e}")
                raise
            log.warning(f"Login failed for player: {self.player.email}")
            return self.session

    def logout(self):
        log.info("Logging out user")
        pass

    def make_ping(self):
        try:
            response = authenticate()
            if geofencing.csrf_enabled:
                get_mkodo_token(session=self.session, client_id=response.headers['x-client-id'])

            response = send_ping(
                session=self.session,
                player_id=self.player.player_id,
                session_state=self.session_state,
                client_id=response.headers['x-client-id'],
                client_secret=response.headers['x-client-id-timestamp'],
                latitude=self.player.latitude if self.player.latitude else 39.048,
                longitude=self.player.longitude if self.player.longitude else -95.679,
            )
            log.info(f"Ping sent successfully: {response.status_code}")
        except Exception as e:
            log.error(f"Failed to send ping: {e}")
            raise


class OperatorAuthenticationApi:
    def __init__(self, session, operator):
        self.session = session
        self.operator = operator

    def login(self):
        log.debug(f"Logging in operator {self.operator} to Backoffice")
        try:
            session = Session()
            response = get_oidc_login_cc(session=session)
            response = get_adfs_login_link(
                session=session,
                location=response.headers["Location"]
            )

            if settings.adfs_enabled:
                response = get_saml_post_binding(
                    session=session,
                    link=f"{hosts.idp_admin}{fetch(response).find('a', id='social-ADFS')['href']}"
                )
                action = fetch(response).find('form', {"name": "saml-post-binding"})['action']
                response = get_adfs_client_request(
                    session=session,
                    action=action,
                    saml_request=fetch(response).find('input', {"name": "SAMLRequest"})['value'],
                    relay_state=fetch(response).find('input', {"name": "RelayState"})['value']
                )
                response = authenticate_operator(
                    session=session,
                    action=f"{action[:-8]}{fetch(response).find('form')['action']}",
                    username=self.operator.username,
                    password=self.operator.password
                )
                finalize_login(
                    session=session,
                    action=fetch(response).find('form')['action'],
                    saml_response=fetch(response).find('input', {"name": "SAMLResponse"})['value'],
                    relay_state=fetch(response).find('input', {"name": "RelayState"})['value']
                )

            else:
                authenticate_operator(
                    session=session,
                    action=f"{fetch(response).find('form')['action']}",
                    username=self.operator.username,
                    password=self.operator.password
                )

            session.headers.update({"X-Csrftoken": session.cookies["csrftoken"]})
            log.info(f"User {self.operator} operates in Backoffice")
            self.session = session
            return self.session
        except Exception as e:
            log.error(f"Error while logging in operator: {e}")
            raise
